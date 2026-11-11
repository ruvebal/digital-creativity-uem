import { Layout, Context } from "rive/host";
import { Renderer } from "rive/renderer";
import { Paint, PaintStyle } from "rive/paint";
import { Path } from "rive/path";
import { Vector } from "rive/vector";
import { Color } from "rive/color";
import { Mat4 } from "rive/mat4";

/**
 * P4 Space-box (Raumkasten) — true Mat4 perspective.
 * Room + floor orthogonals + interior cloth volume share one MVP.
 * Floor lines are 3D edges on y = floor; they converge because of projection,
 * not because we faked 2D midpoints.
 */
export class Main extends Layout {
    edge: Paint = new Paint();
    floor: Paint = new Paint();
    cloth: Paint = new Paint();
    fold: Paint = new Paint();
    accent: Paint = new Paint();
    w: f32 = 1600; h: f32 = 900; t: f32 = 0;
    path: Path = new Path();
    clip: StaticArray<f32> = new StaticArray<f32>(4);
    mvp: Mat4 = Mat4.identity();
    tmp: Mat4 = Mat4.identity();

    override init(context: Context): bool {
        this.edge.color = Color.rgb(255, 255, 255);
        this.floor.color = Color.rgb(240, 124, 99);
        this.cloth.color = Color.rgb(155, 226, 209);
        this.fold.color = Color.rgb(232, 197, 108);
        this.accent.color = Color.rgb(240, 124, 99);
        this.edge.thickness = 2.5; this.floor.thickness = 2.8;
        this.cloth.thickness = 2.5; this.fold.thickness = 2; this.accent.thickness = 2;
        this.edge.style = PaintStyle.stroke;
        this.floor.style = PaintStyle.stroke;
        this.cloth.style = PaintStyle.stroke;
        this.fold.style = PaintStyle.stroke;
        this.accent.style = PaintStyle.stroke;
        return true;
    }

    override resize(width: f64, height: f64, scale: f64): void {
        this.w = <f32>width; this.h = <f32>height;
    }

    override advance(seconds: f64): bool { this.t += <f32>seconds; return true; }

    /** Project world (x,y,z) through current mvp → screen pixels. */
    private project(x: f32, y: f32, z: f32): Vector {
        this.mvp.transformVec4(this.clip, x, y, z, 1);
        let ww = this.clip[3];
        if (Mathf.abs(ww) < 1e-5) ww = 1;
        let ndcX = this.clip[0] / ww;
        let ndcY = this.clip[1] / ww;
        return Vector.xy((ndcX * 0.5 + 0.5) * this.w, (1.0 - (ndcY * 0.5 + 0.5)) * this.h);
    }

    private line3(renderer: Renderer, paint: Paint, ax: f32, ay: f32, az: f32, bx: f32, by: f32, bz: f32): void {
        let a = this.project(ax, ay, az);
        let b = this.project(bx, by, bz);
        this.path.reset();
        this.path.moveTo(a);
        this.path.lineTo(b);
        renderer.drawPath(this.path, paint);
    }

    private rebuildMvp(yawBias: f32): void {
        let aspect = this.w / Mathf.max(<f32>1, this.h);
        let proj = Mat4.perspective(Mathf.PI / <f32>3.2, aspect, <f32>0.1, <f32>40);
        // Eye orbits slightly so the Raumkasten reads as volume, not a flat trapezoid.
        let eyeX = Mathf.sin(this.t * <f32>0.35 + yawBias) * <f32>1.2;
        let eyeY = <f32>1.55 + Mathf.sin(this.t * <f32>0.22) * <f32>0.08;
        let eyeZ = <f32>5.4;
        let view = Mat4.lookAt(eyeX, eyeY, eyeZ, <f32>0, <f32>0.9, <f32>0, <f32>0, <f32>1, <f32>0);
        Mat4.multiply(this.tmp, proj, view);
        this.mvp = this.tmp;
    }

    override draw(renderer: Renderer): void {
        this.rebuildMvp(0);
        const s = Mathf.min(1, this.t * 0.45);
        // Room extents (world units): floor at y=0, ceiling y=2.2, depth z∈[-2.2, 2.2]
        const xL: f32 = -2.0; const xR: f32 = 2.0;
        const y0: f32 = 0; const yC: f32 = 2.2;
        const zN: f32 = -2.2; const zF: f32 = 2.2;

        // Ceiling rectangle
        if (s > 0.05) {
            this.line3(renderer, this.edge, xL, yC, zN, xR, yC, zN);
            this.line3(renderer, this.edge, xR, yC, zN, xR, yC, zF);
            this.line3(renderer, this.edge, xR, yC, zF, xL, yC, zF);
            this.line3(renderer, this.edge, xL, yC, zF, xL, yC, zN);
        }
        // Floor rectangle
        if (s > 0.15) {
            this.line3(renderer, this.floor, xL, y0, zN, xR, y0, zN);
            this.line3(renderer, this.floor, xR, y0, zN, xR, y0, zF);
            this.line3(renderer, this.floor, xR, y0, zF, xL, y0, zF);
            this.line3(renderer, this.floor, xL, y0, zF, xL, y0, zN);
        }
        // Verticals
        if (s > 0.25) this.line3(renderer, this.edge, xL, y0, zN, xL, yC, zN);
        if (s > 0.35) this.line3(renderer, this.edge, xR, y0, zN, xR, yC, zN);
        if (s > 0.45) this.line3(renderer, this.edge, xR, y0, zF, xR, yC, zF);
        if (s > 0.55) this.line3(renderer, this.edge, xL, y0, zF, xL, yC, zF);

        // Floor orthogonals: lines of constant x on the floor plane → true depth rays
        if (s > 0.65) {
            for (let i = 1; i < 5; i++) {
                let u = <f32>i / 5.0;
                let x = xL + (xR - xL) * u;
                this.line3(renderer, this.fold, x, y0, zN, x, y0, zF);
            }
            // transversals (constant z) so the grid reads as a plane
            for (let i = 1; i < 4; i++) {
                let u = <f32>i / 4.0;
                let z = zN + (zF - zN) * u;
                this.line3(renderer, this.fold, xL, y0, z, xR, y0, z);
            }
        }

        // Interior cloth volume: unit box at room centre, yawed in world space then projected
        if (s > 0.75) {
            let yaw = this.t * 0.85;
            let cy: f32 = 0.95;
            let hw: f32 = 0.45; let hh: f32 = 0.7; let hd: f32 = 0.35;
            let drape = Mathf.sin(this.t * 1.15) * 0.08;
            let c = Mathf.cos(yaw); let sn = Mathf.sin(yaw);
            // local corners → yaw about Y → translate to (0, cy, 0)
            let lx = [-hw,  hw,  hw, -hw, -hw,  hw,  hw, -hw];
            let ly = [-hh + drape, -hh, hh, hh + drape * 0.4, -hh + drape, -hh, hh, hh + drape * 0.4];
            let lz = [-hd, -hd, -hd, -hd,  hd,  hd,  hd,  hd];
            let pts = new Array<Vector>(8);
            for (let i = 0; i < 8; i++) {
                let wx = lx[i] * c + lz[i] * sn;
                let wz = -lx[i] * sn + lz[i] * c;
                pts[i] = this.project(wx, cy + ly[i], wz);
            }
            // back face
            this.path.reset();
            this.path.moveTo(pts[4]); this.path.lineTo(pts[5]); this.path.lineTo(pts[6]); this.path.lineTo(pts[7]); this.path.close();
            renderer.drawPath(this.path, this.accent);
            // front face
            this.path.reset();
            this.path.moveTo(pts[0]); this.path.lineTo(pts[1]); this.path.lineTo(pts[2]); this.path.lineTo(pts[3]); this.path.close();
            renderer.drawPath(this.path, this.cloth);
            // depth edges
            this.lineThrough(renderer, this.fold, pts[0], pts[4]);
            this.lineThrough(renderer, this.fold, pts[1], pts[5]);
            this.lineThrough(renderer, this.fold, pts[2], pts[6]);
            this.lineThrough(renderer, this.fold, pts[3], pts[7]);
        }
    }

    private lineThrough(renderer: Renderer, paint: Paint, a: Vector, b: Vector): void {
        this.path.reset(); this.path.moveTo(a); this.path.lineTo(b); renderer.drawPath(this.path, paint);
    }
}

import { Layout, Context } from "rive/host";
import { Renderer } from "rive/renderer";
import { Paint, PaintStyle } from "rive/paint";
import { Path } from "rive/path";
import { Vector } from "rive/vector";
import { Color } from "rive/color";
import { Mat4 } from "rive/mat4";

/**
 * P5 Central vanishing point — Mat4 one-point corridor.
 * Orthogonals are world-space lines of constant (x,y) running in z;
 * after perspective they meet at the projected VP of the view axis.
 */
export class Main extends Layout {
    line: Paint = new Paint();
    hot: Paint = new Paint();
    plane: Paint = new Paint();
    w: f32 = 1600; h: f32 = 900; t: f32 = 0;
    path: Path = new Path();
    clip: StaticArray<f32> = new StaticArray<f32>(4);
    mvp: Mat4 = Mat4.identity();
    tmp: Mat4 = Mat4.identity();

    override init(context: Context): bool {
        this.line.color = Color.rgb(255, 255, 255);
        this.hot.color = Color.rgb(232, 197, 108);
        this.plane.color = Color.rgb(240, 124, 99);
        this.line.thickness = 1.6; this.hot.thickness = 2.5; this.plane.thickness = 2.8;
        this.line.style = PaintStyle.stroke;
        this.hot.style = PaintStyle.stroke;
        this.plane.style = PaintStyle.stroke;
        return true;
    }

    override resize(width: f64, height: f64, scale: f64): void {
        this.w = <f32>width; this.h = <f32>height;
    }

    override advance(seconds: f64): bool { this.t += <f32>seconds; return true; }

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
        this.path.reset(); this.path.moveTo(a); this.path.lineTo(b);
        renderer.drawPath(this.path, paint);
    }

    private rebuildMvp(): void {
        let aspect = this.w / Mathf.max(<f32>1, this.h);
        let fov = Mathf.PI / <f32>3.0 + Mathf.sin(this.t * <f32>0.5) * <f32>0.04;
        let proj = Mat4.perspective(fov, aspect, <f32>0.05, <f32>50);
        let eyeZ = <f32>0.01; // near picture plane
        let view = Mat4.lookAt(<f32>0, <f32>1.2, eyeZ, <f32>0, <f32>1.2, <f32>-8, <f32>0, <f32>1, <f32>0);
        Mat4.multiply(this.tmp, proj, view);
        this.mvp = this.tmp;
    }

    override draw(renderer: Renderer): void {
        this.rebuildMvp();
        // Picture-plane frame (near z)
        this.line3(renderer, this.hot, -3.2, 2.6, -0.2, 3.2, 2.6, -0.2);
        this.line3(renderer, this.hot, -3.2, 0.0, -0.2, 3.2, 0.0, -0.2);

        // Horizon = eye height projected (y = 1.2, far)
        let hl = this.project(-4, 1.2, -18);
        let hr = this.project(4, 1.2, -18);
        this.path.reset(); this.path.moveTo(hl); this.path.lineTo(hr);
        renderer.drawPath(this.path, this.hot);

        // Orthogonals on the ground plane (y=0): constant-x rays into depth
        const xs: f32[] = [-2.8, -2.0, -1.2, -0.5, 0.5, 1.2, 2.0, 2.8];
        for (let i = 0; i < xs.length; i++) {
            this.line3(renderer, this.line, xs[i], 0, -0.3, xs[i], 0, -16);
        }
        // Ceiling orthogonals
        for (let i = 0; i < xs.length; i++) {
            this.line3(renderer, this.line, xs[i], 2.4, -0.3, xs[i], 2.4, -16);
        }

        // Foreshortened ground diamond (breathing span via FOV already)
        let breath = 1.6 + 0.25 * Mathf.sin(this.t);
        let a = this.project(-breath, 0, -1.2);
        let b = this.project(0, 0, -10);
        let c = this.project(breath, 0, -1.2);
        this.path.reset(); this.path.moveTo(a); this.path.lineTo(b); this.path.lineTo(c); this.path.close();
        renderer.drawPath(this.path, this.plane);

        // VP mark: project a point far on the view axis
        let vp = this.project(0, 1.2, -40);
        let r: f32 = 6 + Mathf.sin(this.t * 2) * 2;
        this.path.reset(); this.path.moveTo(Vector.xy(vp.x - r, vp.y)); this.path.lineTo(Vector.xy(vp.x + r, vp.y));
        renderer.drawPath(this.path, this.hot);
        this.path.reset(); this.path.moveTo(Vector.xy(vp.x, vp.y - r)); this.path.lineTo(Vector.xy(vp.x, vp.y + r));
        renderer.drawPath(this.path, this.hot);
    }
}

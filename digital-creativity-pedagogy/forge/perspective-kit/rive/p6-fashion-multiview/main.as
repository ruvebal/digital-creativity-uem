import { Layout, Context } from "rive/host";
import { Renderer } from "rive/renderer";
import { Paint, PaintStyle } from "rive/paint";
import { Path } from "rive/path";
import { Vector } from "rive/vector";
import { Color } from "rive/color";
import { Mat4 } from "rive/mat4";
/**
 * P6 Fashion multi-view — one cloth volume, three Mat4.lookAt cameras.
 * Front / three-quarter / side share world XYZ; only the view matrix changes.
 */
export class Main extends Layout {
    frame: Paint = new Paint();
    cloth: Paint = new Paint();
    fold: Paint = new Paint();
    axisX: Paint = new Paint();
    axisY: Paint = new Paint();
    axisZ: Paint = new Paint();
    w: f32 = 1600; h: f32 = 900; t: f32 = 0;
    path: Path = new Path();
    clip: StaticArray<f32> = new StaticArray<f32>(4);
    mvp: Mat4 = Mat4.identity();
    tmp: Mat4 = Mat4.identity();

    override init(context: Context): bool {
        this.frame.color = Color.rgb(255, 255, 255);
        this.cloth.color = Color.rgb(240, 124, 99);
        this.fold.color = Color.rgb(155, 226, 209);
        this.axisX.color = Color.rgb(240, 124, 99);
        this.axisY.color = Color.rgb(155, 226, 209);
        this.axisZ.color = Color.rgb(232, 197, 108);
        this.frame.thickness = 2; this.cloth.thickness = 2.6;
        this.fold.thickness = 2; this.axisX.thickness = 2.2;
        this.axisY.thickness = 2.2; this.axisZ.thickness = 2.2;
        this.frame.style = PaintStyle.stroke;
        this.cloth.style = PaintStyle.stroke;
        this.fold.style = PaintStyle.stroke;
        this.axisX.style = PaintStyle.stroke;
        this.axisY.style = PaintStyle.stroke;
        this.axisZ.style = PaintStyle.stroke;
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

    private setCamera(eyeX: f32, eyeY: f32, eyeZ: f32, panelL: f32, panelT: f32, panelW: f32, panelH: f32): void {
        // Local NDC mapped into the panel rectangle (viewport-in-viewport).
        let aspect = panelW / Mathf.max(1, panelH);
        let proj = Mat4.perspective(Mathf.PI / 3.4, aspect, 0.1, 30);
        let view = Mat4.lookAt(eyeX, eyeY, eyeZ, 0, 0.9, 0, 0, 1, 0);
        Mat4.multiply(this.tmp, proj, view);
        this.mvp = this.tmp;
        // Stash panel for project remap — bake offset/scale into a post-pass via fields
        this._pl = panelL; this._pt = panelT; this._pw = panelW; this._ph = panelH;
    }

    _pl: f32 = 0; _pt: f32 = 0; _pw: f32 = 1; _ph: f32 = 1;

    private projectPanel(x: f32, y: f32, z: f32): Vector {
        this.mvp.transformVec4(this.clip, x, y, z, 1);
        let ww = this.clip[3];
        if (Mathf.abs(ww) < 1e-5) ww = 1;
        let ndcX = this.clip[0] / ww;
        let ndcY = this.clip[1] / ww;
        let sx = this._pl + (ndcX * 0.5 + 0.5) * this._pw;
        let sy = this._pt + (1.0 - (ndcY * 0.5 + 0.5)) * this._ph;
        return Vector.xy(sx, sy);
    }

    private lineW(renderer: Renderer, paint: Paint, ax: f32, ay: f32, az: f32, bx: f32, by: f32, bz: f32): void {
        let a = this.projectPanel(ax, ay, az);
        let b = this.projectPanel(bx, by, bz);
        this.path.reset(); this.path.moveTo(a); this.path.lineTo(b);
        renderer.drawPath(this.path, paint);
    }

    private drawCloth(renderer: Renderer, phase: f32): void {
        let drape = Mathf.sin(this.t + phase) * 0.12;
        let hw: f32 = 0.55; let hh: f32 = 1.1; let hd: f32 = 0.28;
        let cy: f32 = 1.0;
        // 8 corners of a soft box (cloth volume)
        let lx = [-hw, hw, hw, -hw, -hw, hw, hw, -hw];
        let ly = [-hh + drape, -hh, hh, hh + drape * 0.35, -hh + drape, -hh, hh, hh + drape * 0.35];
        let lz = [-hd, -hd, -hd, -hd, hd, hd, hd, hd];
        let pts = new Array<Vector>(8);
        for (let i = 0; i < 8; i++) {
            pts[i] = this.projectPanel(lx[i], cy + ly[i], lz[i]);
        }
        this.path.reset();
        this.path.moveTo(pts[4]); this.path.lineTo(pts[5]); this.path.lineTo(pts[6]); this.path.lineTo(pts[7]); this.path.close();
        renderer.drawPath(this.path, this.fold);
        this.path.reset();
        this.path.moveTo(pts[0]); this.path.lineTo(pts[1]); this.path.lineTo(pts[2]); this.path.lineTo(pts[3]); this.path.close();
        renderer.drawPath(this.path, this.cloth);
        this.lineW(renderer, this.fold, lx[0], cy + ly[0], lz[0], lx[4], cy + ly[4], lz[4]);
        this.lineW(renderer, this.fold, lx[1], cy + ly[1], lz[1], lx[5], cy + ly[5], lz[5]);
        this.lineW(renderer, this.fold, lx[2], cy + ly[2], lz[2], lx[6], cy + ly[6], lz[6]);
        this.lineW(renderer, this.fold, lx[3], cy + ly[3], lz[3], lx[7], cy + ly[7], lz[7]);
        // fold cue
        this.lineW(renderer, this.fold, -hw * 0.4, cy, -hd, hw * 0.4, cy - 0.15, -hd);

        // Shared world XYZ triad at origin
        this.lineW(renderer, this.axisX, 0, 0, 0, 0.7, 0, 0);
        this.lineW(renderer, this.axisY, 0, 0, 0, 0, 0.9, 0);
        this.lineW(renderer, this.axisZ, 0, 0, 0, 0, 0, 0.7);
    }

    override draw(renderer: Renderer): void {
        const panels: f32[] = [0.04, 0.35, 0.66];
        // eyes: front (+Z), three-quarter, side (+X)
        const eyesX: f32[] = [0.0, 2.8, 4.2];
        const eyesY: f32[] = [1.4, 1.6, 1.5];
        const eyesZ: f32[] = [4.2, 3.2, 0.2];
        for (let i = 0; i < 3; i++) {
            let x = this.w * panels[i];
            let pw = this.w * 0.29;
            let y = this.h * 0.12;
            let ph = this.h * 0.76;
            // panel frame (screen space)
            this.path.reset();
            this.path.moveTo(Vector.xy(x, y));
            this.path.lineTo(Vector.xy(x + pw, y));
            this.path.lineTo(Vector.xy(x + pw, y + ph));
            this.path.lineTo(Vector.xy(x, y + ph));
            this.path.close();
            renderer.drawPath(this.path, this.frame);

            this.setCamera(eyesX[i], eyesY[i], eyesZ[i], x + 8, y + 8, pw - 16, ph - 16);
            this.drawCloth(renderer, <f32>i * 0.7);
        }
    }
}

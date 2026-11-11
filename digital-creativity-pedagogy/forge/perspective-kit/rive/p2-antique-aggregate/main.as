import { Layout, Context } from "rive/host";
import { Renderer } from "rive/renderer";
import { Paint, PaintStyle } from "rive/paint";
import { Path } from "rive/path";
import { Vector } from "rive/vector";
import { Color } from "rive/color";

/** P2 Antique aggregate / vanishing-axis — no shared VP. */
export class Main extends Layout {
    axis: Paint = new Paint();
    bone: Paint = new Paint();
    body: Paint = new Paint();
    w: f64 = 1600; h: f64 = 900; t: f64 = 0;
    path: Path = new Path();

    override init(context: Context): bool {
        this.axis.color = Color.rgb(232, 197, 108);
        this.bone.color = Color.rgb(255, 255, 255);
        this.body.color = Color.rgb(240, 124, 99);
        this.axis.thickness = 3;
        this.bone.thickness = 2;
        this.body.thickness = 3;
        this.axis.style = PaintStyle.stroke;
        this.bone.style = PaintStyle.stroke;
        this.body.style = PaintStyle.stroke;
        return true;
    }
    override resize(width: f64, height: f64, scale: f64): void { this.w = width; this.h = height; }
    override advance(seconds: f64): bool { this.t += seconds; return true; }
    override draw(renderer: Renderer): void {
        const cx = this.w * 0.5;
        const pulse = 0.5 + 0.5 * Math.sin(this.t);
        // vanishing axis
        const p = this.path; p.reset();
        p.moveTo(Vector.xy(<f32>cx, <f32>(this.h * 0.15)));
        p.lineTo(Vector.xy(<f32>cx, <f32>(this.h * 0.88)));
        renderer.drawPath(p, this.axis);
        // fishbones left/right with drifting endpoints (aggregate instability)
        const pairs = [
            [0.12, 0.28, 0.42], [0.10, 0.40, 0.52], [0.15, 0.58, 0.62],
            [0.88, 0.24, 0.44], [0.90, 0.45, 0.55], [0.85, 0.70, 0.64]
        ];
        for (let i = 0; i < pairs.length; i++) {
            const a = pairs[i];
            const ox = this.w * a[0] + Math.sin(this.t * 0.7 + i) * 12;
            const oy = this.h * a[1];
            const ey = this.h * a[2] + pulse * 8;
            p.reset();
            p.moveTo(Vector.xy(<f32>ox, <f32>oy));
            p.lineTo(Vector.xy(<f32>cx, <f32>ey));
            renderer.drawPath(p, this.bone);
        }
        // discrete bodies
        this.rect(renderer, this.w * 0.20, this.h * 0.35, 90, 140);
        this.rect(renderer, this.w * 0.72, this.h * 0.32, 70, 110);
        this.rect(renderer, this.w * 0.34, this.h * 0.62, 110, 80);
    }
    rect(renderer: Renderer, x: f64, y: f64, rw: f64, rh: f64): void {
        const p = this.path; p.reset();
        p.moveTo(Vector.xy(<f32>x, <f32>y));
        p.lineTo(Vector.xy(<f32>(x + rw), <f32>y));
        p.lineTo(Vector.xy(<f32>(x + rw), <f32>(y + rh)));
        p.lineTo(Vector.xy(<f32>x, <f32>(y + rh)));
        p.close();
        renderer.drawPath(p, this.body);
    }
}

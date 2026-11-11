import { Layout, Context } from "rive/host";
import { Renderer } from "rive/renderer";
import { Paint, PaintStyle } from "rive/paint";
import { Path } from "rive/path";
import { Vector } from "rive/vector";
import { Color } from "rive/color";

/** P3 Mass planes dissolve into a hollow interior. */
export class Main extends Layout {
    mass: Paint = new Paint();
    line: Paint = new Paint();
    w: f64 = 1600; h: f64 = 900; t: f64 = 0;
    path: Path = new Path();
    override init(context: Context): bool {
        this.mass.color = Color.rgb(240, 124, 99);
        this.line.color = Color.rgb(255, 255, 255);
        this.line.thickness = 2.5;
        this.line.style = PaintStyle.stroke;
        this.mass.style = PaintStyle.fill;
        return true;
    }
    override resize(width: f64, height: f64, scale: f64): void { this.w = width; this.h = height; }
    override advance(seconds: f64): bool { this.t += seconds; return true; }
    override draw(renderer: Renderer): void {
        const u = 0.5 + 0.5 * Math.sin(this.t * 0.6); // 0..1
        // mass side fades as interior opens
        for (let i = 0; i < 3; i++) {
            const inset = 40 * i;
            const a = <u8>(160 - i * 30 - <i32>(u * 80));
            this.mass.color = Color.rgb(240, 124, 99);
            const p = this.path; p.reset();
            const x = this.w * 0.08 + inset;
            const y = this.h * 0.22 + inset;
            const rw = this.w * 0.28 - inset * 1.2;
            const rh = this.h * 0.55 - inset * 1.2;
            p.moveTo(Vector.xy(<f32>x, <f32>y));
            p.lineTo(Vector.xy(<f32>(x + rw), <f32>y));
            p.lineTo(Vector.xy(<f32>(x + rw), <f32>(y + rh)));
            p.lineTo(Vector.xy(<f32>x, <f32>(y + rh)));
            p.close();
            renderer.drawPath(p, this.mass);
        }
        // hollow room grows with u
        const open = 0.35 + u * 0.2;
        const x0 = this.w * 0.52; const y0 = this.h * (0.35 - open * 0.1);
        const x1 = this.w * 0.88; const y1 = this.h * (0.75 + open * 0.05);
        const p = this.path; p.reset();
        p.moveTo(Vector.xy(<f32>x0, <f32>y0));
        p.lineTo(Vector.xy(<f32>x1, <f32>y0));
        p.lineTo(Vector.xy(<f32>(x1 + 80), <f32>(y0 - 60)));
        p.lineTo(Vector.xy(<f32>(x0 + 80), <f32>(y0 - 60)));
        p.close();
        renderer.drawPath(p, this.line);
        p.reset();
        p.moveTo(Vector.xy(<f32>x0, <f32>y0));
        p.lineTo(Vector.xy(<f32>x0, <f32>y1));
        p.lineTo(Vector.xy(<f32>x1, <f32>y1));
        p.lineTo(Vector.xy(<f32>x1, <f32>y0));
        p.close();
        renderer.drawPath(p, this.line);
    }
}

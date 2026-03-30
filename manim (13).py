from manim import *
import numpy as np


class QuadraticEquation(Scene):
    def construct(self):
        # ── Color palette ─────────────────────────────────────
        BG_COLOR   = "#1a1a2e"
        CURVE_CLR  = "#00d2ff"
        ROOT_CLR   = "#ff6b6b"
        VERTEX_CLR = "#feca57"
        AXIS_CLR   = "#a29bfe"
        LABEL_CLR  = "#dfe6e9"
        ACCENT     = "#55efc4"

        self.camera.background_color = BG_COLOR

        # ══════════════════════════════════════════════════════
        # PART 1 — Title & Equation
        # ══════════════════════════════════════════════════════
        title = Text("Quadratic Equation", font_size=48, color=ACCENT)
        title.to_edge(UP, buff=0.6)

        equation = MathTex(
            r"f(x) = x^2 - 4x + 3",
            font_size=42,
            color=WHITE,
        )
        equation.next_to(title, DOWN, buff=0.4)

        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(equation, shift=UP * 0.3), run_time=1)
        self.wait(0.5)

        # ══════════════════════════════════════════════════════
        # PART 2 — Factored & Standard forms
        # ══════════════════════════════════════════════════════
        forms = VGroup(
            MathTex(r"\text{Standard: } ax^2 + bx + c", font_size=28, color=LABEL_CLR),
            MathTex(r"a=1,\; b=-4,\; c=3", font_size=28, color=ACCENT),
            MathTex(r"\text{Factored: } (x-1)(x-3)", font_size=28, color=ROOT_CLR),
        ).arrange(DOWN, buff=0.25)
        forms.next_to(equation, DOWN, buff=0.5)

        for form in forms:
            self.play(Write(form), run_time=0.8)
        self.wait(0.8)

        # ══════════════════════════════════════════════════════
        # PART 3 — Transition to graph
        # ══════════════════════════════════════════════════════
        self.play(
            title.animate.scale(0.6).to_corner(UL, buff=0.3),
            equation.animate.scale(0.7).to_corner(UR, buff=0.3),
            FadeOut(forms, shift=DOWN * 0.5),
            run_time=1,
        )

        # ══════════════════════════════════════════════════════
        # PART 4 — Axes & parabola
        # ══════════════════════════════════════════════════════
        axes = Axes(
            x_range=[-1, 5.5, 1],
            y_range=[-1.5, 6, 1],
            x_length=8,
            y_length=5.5,
            axis_config={
                "color": LABEL_CLR,
                "stroke_width": 2,
                "include_numbers": True,
                "font_size": 22,
            },
            tips=True,
        )
        axes.shift(DOWN * 0.3)

        x_label = axes.get_x_axis_label("x", direction=RIGHT, buff=0.2)
        y_label = axes.get_y_axis_label("y", direction=UP, buff=0.2)
        x_label.set_color(LABEL_CLR).scale(0.8)
        y_label.set_color(LABEL_CLR).scale(0.8)

        self.play(Create(axes), Write(x_label), Write(y_label), run_time=1.5)

        # ── Grid lines (subtle) ──────────────────────────────
        grid_lines = VGroup()
        for x in range(0, 6):
            grid_lines.add(
                axes.get_vertical_line(
                    axes.c2p(x, 6), color=WHITE, stroke_width=0.3
                )
            )
        for y in range(0, 6):
            grid_lines.add(
                DashedLine(
                    axes.c2p(-1, y), axes.c2p(5.5, y),
                    color=WHITE, stroke_width=0.3, dash_length=0.05,
                )
            )
        self.play(FadeIn(grid_lines), run_time=0.6)

        # ── Parabola ─────────────────────────────────────────
        def f(x):
            return x**2 - 4 * x + 3

        parabola = axes.plot(f, x_range=[-0.3, 4.3], color=CURVE_CLR, stroke_width=3.5)

        # Animate drawing with a glowing dot tracing the curve
        trace_dot = Dot(color=CURVE_CLR, radius=0.08)
        trace_dot.add_updater(lambda m: m.move_to(parabola.get_end()))

        self.add(trace_dot)
        self.play(Create(parabola), run_time=2.5, rate_func=smooth)
        self.remove(trace_dot)
        self.wait(0.3)

        # Glow effect on parabola
        glow = parabola.copy().set_stroke(width=10, opacity=0.3)
        self.play(FadeIn(glow), run_time=0.5)

        # ══════════════════════════════════════════════════════
        # PART 5 — Roots (x-intercepts)
        # ══════════════════════════════════════════════════════
        root_header = Text("Roots", font_size=24, color=ROOT_CLR)
        root_header.to_edge(LEFT, buff=0.4).shift(DOWN * 1.5)

        root1_pos = axes.c2p(1, 0)
        root2_pos = axes.c2p(3, 0)

        dot_r1 = Dot(root1_pos, color=ROOT_CLR, radius=0.1)
        dot_r2 = Dot(root2_pos, color=ROOT_CLR, radius=0.1)

        lbl_r1 = MathTex("x=1", font_size=24, color=ROOT_CLR).next_to(dot_r1, DOWN + LEFT, buff=0.15)
        lbl_r2 = MathTex("x=3", font_size=24, color=ROOT_CLR).next_to(dot_r2, DOWN + RIGHT, buff=0.15)

        # Pulsing rings around roots
        ring1 = Circle(radius=0.2, color=ROOT_CLR, stroke_width=2).move_to(root1_pos)
        ring2 = Circle(radius=0.2, color=ROOT_CLR, stroke_width=2).move_to(root2_pos)

        self.play(
            GrowFromCenter(dot_r1), GrowFromCenter(dot_r2),
            Write(lbl_r1), Write(lbl_r2),
            run_time=0.8,
        )
        self.play(
            Create(ring1), Create(ring2),
            ring1.animate.scale(2).set_opacity(0),
            ring2.animate.scale(2).set_opacity(0),
            run_time=0.8,
        )
        self.remove(ring1, ring2)
        self.wait(0.3)

        # ══════════════════════════════════════════════════════
        # PART 6 — Vertex
        # ══════════════════════════════════════════════════════
        vx, vy = 2, -1
        vertex_pos = axes.c2p(vx, vy)

        dot_v = Dot(vertex_pos, color=VERTEX_CLR, radius=0.1)
        lbl_v = MathTex(
            r"\text{Vertex } (2,\,-1)", font_size=24, color=VERTEX_CLR
        ).next_to(dot_v, DOWN, buff=0.2)

        self.play(GrowFromCenter(dot_v), Write(lbl_v), run_time=0.8)

        # ── Axis of symmetry ─────────────────────────────────
        sym_line = DashedLine(
            axes.c2p(2, -1.5), axes.c2p(2, 6),
            color=AXIS_CLR, stroke_width=2, dash_length=0.1,
        )
        sym_label = MathTex(
            r"x = 2", font_size=22, color=AXIS_CLR
        ).next_to(sym_line, UP, buff=0.15)

        self.play(Create(sym_line), Write(sym_label), run_time=1)
        self.wait(0.5)

        # ══════════════════════════════════════════════════════
        # PART 7 — Discriminant formula box
        # ══════════════════════════════════════════════════════
        disc_box = VGroup(
            MathTex(r"\Delta = b^2 - 4ac", font_size=28, color=WHITE),
            MathTex(r"= (-4)^2 - 4(1)(3)", font_size=28, color=LABEL_CLR),
            MathTex(r"= 16 - 12 = 4", font_size=28, color=ACCENT),
            MathTex(r"\Delta > 0 \Rightarrow \text{2 real roots}", font_size=26, color=ROOT_CLR),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)

        box_bg = SurroundingRectangle(
            disc_box, color=ACCENT, fill_color=BG_COLOR,
            fill_opacity=0.9, corner_radius=0.15, buff=0.25,
        )
        disc_group = VGroup(box_bg, disc_box)
        disc_group.to_corner(DR, buff=0.4)

        self.play(FadeIn(box_bg), run_time=0.5)
        for line in disc_box:
            self.play(Write(line), run_time=0.7)
        self.wait(1)

        # ══════════════════════════════════════════════════════
        # PART 8 — Quadratic formula
        # ══════════════════════════════════════════════════════
        self.play(FadeOut(disc_group, shift=RIGHT * 0.5), run_time=0.6)

        qf_title = Text("Quadratic Formula", font_size=28, color=ACCENT)
        qf = MathTex(
            r"x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}",
            font_size=36,
            color=WHITE,
        )
        qf_result = MathTex(
            r"x = \frac{4 \pm \sqrt{4}}{2} = \frac{4 \pm 2}{2}",
            font_size=32,
            color=LABEL_CLR,
        )
        qf_roots = MathTex(
            r"x_1 = 1, \quad x_2 = 3",
            font_size=34,
            color=ROOT_CLR,
        )

        formula_group = VGroup(qf_title, qf, qf_result, qf_roots).arrange(
            DOWN, buff=0.3
        )
        formula_bg = SurroundingRectangle(
            formula_group, color=ACCENT, fill_color=BG_COLOR,
            fill_opacity=0.92, corner_radius=0.15, buff=0.3,
        )
        formula_full = VGroup(formula_bg, formula_group)
        formula_full.to_corner(DR, buff=0.35)

        self.play(FadeIn(formula_bg), run_time=0.4)
        for item in formula_group:
            self.play(Write(item), run_time=0.9)
        self.wait(0.5)

        # Highlight final roots
        highlight = SurroundingRectangle(
            qf_roots, color=ROOT_CLR, buff=0.1, corner_radius=0.08,
        )
        self.play(Create(highlight), run_time=0.6)
        self.play(
            highlight.animate.set_stroke(width=5),
            run_time=0.3,
        )
        self.play(
            highlight.animate.set_stroke(width=2),
            run_time=0.3,
        )
        self.wait(1)

        # ══════════════════════════════════════════════════════
        # PART 9 — Y-intercept
        # ══════════════════════════════════════════════════════
        y_int_pos = axes.c2p(0, 3)
        dot_y = Dot(y_int_pos, color=ACCENT, radius=0.1)
        lbl_y = MathTex(
            r"(0,\,3)", font_size=24, color=ACCENT
        ).next_to(dot_y, LEFT, buff=0.15)

        self.play(
            FadeOut(formula_full), FadeOut(highlight),
            run_time=0.6,
        )
        self.play(GrowFromCenter(dot_y), Write(lbl_y), run_time=0.8)
        self.wait(0.5)

        # ══════════════════════════════════════════════════════
        # PART 10 — Summary box
        # ══════════════════════════════════════════════════════
        summary = VGroup(
            Text("Summary", font_size=26, color=ACCENT, weight=BOLD),
            Text("• Roots: x = 1, x = 3", font_size=22, color=ROOT_CLR),
            Text("• Vertex: (2, −1)", font_size=22, color=VERTEX_CLR),
            Text("• Axis of symmetry: x = 2", font_size=22, color=AXIS_CLR),
            Text("• Y-intercept: (0, 3)", font_size=22, color=ACCENT),
            Text("• Opens upward (a > 0)", font_size=22, color=CURVE_CLR),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)

        sum_bg = SurroundingRectangle(
            summary, color=ACCENT, fill_color=BG_COLOR,
            fill_opacity=0.92, corner_radius=0.15, buff=0.25,
        )
        sum_full = VGroup(sum_bg, summary)
        sum_full.to_corner(DR, buff=0.35)

        self.play(FadeIn(sum_bg), run_time=0.4)
        for line in summary:
            self.play(FadeIn(line, shift=RIGHT * 0.2), run_time=0.4)
        self.wait(2)

        # ══════════════════════════════════════════════════════
        # PART 11 — Fade out
        # ══════════════════════════════════════════════════════
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.5)
        self.wait(0.5)

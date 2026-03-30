from manim import *

class DifferentialCalculus(Scene):
    def construct(self):

        # ─────────────────────────────────────────────
        # SCENE 1 — TITLE  (~0:00 – 0:20)
        # ─────────────────────────────────────────────
        title = Text("Differential Calculus", font_size=60, color=YELLOW)
        subtitle = Text("The Mathematics of Change", font_size=32, color=WHITE)
        subtitle.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP), run_time=1)
        self.wait(5)
        self.play(FadeOut(title), FadeOut(subtitle))

        # ─────────────────────────────────────────────
        # SCENE 2 — REAL-LIFE HOOK: CAR SPEEDOMETER  (~0:20 – 1:00)
        # ─────────────────────────────────────────────
        hook = Text("Imagine you're driving a car…", font_size=40, color=WHITE)
        self.play(Write(hook), run_time=2)
        self.wait(4)
        self.play(FadeOut(hook))

        question1 = Text("How do you know your speed", font_size=36, color=BLUE)
        question2 = Text("at EXACTLY this moment?", font_size=36, color=YELLOW)
        question2.next_to(question1, DOWN, buff=0.3)
        self.play(FadeIn(question1), run_time=1.5)
        self.play(FadeIn(question2), run_time=1.5)
        self.wait(5)
        self.play(FadeOut(question1), FadeOut(question2))

        answer = Text("That's what a derivative does!", font_size=42, color=GREEN)
        self.play(Write(answer), run_time=2)
        self.wait(4)
        self.play(FadeOut(answer))

        # ─────────────────────────────────────────────
        # SCENE 3 — AVERAGE vs INSTANTANEOUS RATE  (~1:00 – 1:50)
        # ─────────────────────────────────────────────
        avg_title = Text("Average Rate of Change", font_size=40, color=YELLOW)
        avg_title.to_edge(UP)
        self.play(Write(avg_title), run_time=1.5)
        self.wait(2)

        axes1 = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 36, 6],
            x_length=8,
            y_length=4.5,
            axis_config={"color": WHITE},
            x_axis_config={"numbers_to_include": [1, 2, 3, 4, 5]},
            y_axis_config={"numbers_to_include": [6, 12, 18, 24, 30]},
        ).shift(DOWN * 0.5)

        x_label = axes1.get_x_axis_label("t \\; (seconds)", edge=RIGHT, direction=RIGHT)
        y_label = axes1.get_y_axis_label("d \\; (meters)", edge=UP, direction=UP)

        curve1 = axes1.plot(lambda x: x**2, color=BLUE, x_range=[0, 5.5])

        self.play(Create(axes1), Write(x_label), Write(y_label), run_time=2)
        self.play(Create(curve1), run_time=2)
        self.wait(3)

        dot_A = Dot(axes1.c2p(1, 1), color=RED)
        dot_B = Dot(axes1.c2p(4, 16), color=GREEN)
        label_A = MathTex("A(1,1)", font_size=28, color=RED).next_to(dot_A, LEFT)
        label_B = MathTex("B(4,16)", font_size=28, color=GREEN).next_to(dot_B, RIGHT)

        secant = axes1.plot_line_graph(
            x_values=[1, 4], y_values=[1, 16], line_color=ORANGE, add_vertex_dots=False
        )

        self.play(FadeIn(dot_A), FadeIn(dot_B), Write(label_A), Write(label_B), run_time=1.5)
        self.play(Create(secant), run_time=1.5)

        avg_formula = MathTex(
            r"\text{Avg Speed} = \frac{\Delta d}{\Delta t} = \frac{16-1}{4-1} = 5 \; m/s",
            font_size=30, color=ORANGE
        ).to_edge(DOWN)
        self.play(Write(avg_formula), run_time=2)
        self.wait(6)

        self.play(FadeOut(avg_title), FadeOut(axes1), FadeOut(curve1),
                  FadeOut(dot_A), FadeOut(dot_B), FadeOut(label_A),
                  FadeOut(label_B), FadeOut(secant), FadeOut(avg_formula),
                  FadeOut(x_label), FadeOut(y_label))

        # ─────────────────────────────────────────────
        # SCENE 4 — LIMIT CONCEPT: ZOOMING IN  (~1:50 – 2:40)
        # ─────────────────────────────────────────────
        limit_title = Text("What if we zoom in closer?", font_size=40, color=YELLOW)
        limit_title.to_edge(UP)
        self.play(Write(limit_title), run_time=1.5)
        self.wait(3)

        axes2 = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 36, 6],
            x_length=8,
            y_length=4.5,
            axis_config={"color": WHITE},
        ).shift(DOWN * 0.5)

        curve2 = axes2.plot(lambda x: x**2, color=BLUE, x_range=[0, 5.5])
        self.play(Create(axes2), Create(curve2), run_time=2)

        point_p = Dot(axes2.c2p(2, 4), color=YELLOW, radius=0.1)
        label_p = MathTex("P(2,4)", font_size=28, color=YELLOW).next_to(point_p, UL)
        self.play(FadeIn(point_p), Write(label_p))
        self.wait(2)

        h_values = [2.0, 1.0, 0.5, 0.1]
        colors   = [RED, ORANGE, GREEN, PURPLE]

        for h, col in zip(h_values, colors):
            x1, y1 = 2, 4
            x2 = 2 + h
            y2 = x2**2
            slope = (y2 - y1) / h
            sec = axes2.plot_line_graph(
                x_values=[x1 - 0.5, x2 + 0.3],
                y_values=[y1 - 0.5 * slope, y2 + 0.3 * slope],
                line_color=col, add_vertex_dots=False, stroke_width=2
            )
            label_h = MathTex(
                f"h={h} \\Rightarrow slope={slope:.1f}", font_size=24, color=col
            ).to_corner(DR)
            self.play(Create(sec), Write(label_h), run_time=0.8)
            self.wait(1.8)
            self.play(FadeOut(sec), FadeOut(label_h), run_time=0.3)

        self.wait(2)
        self.play(FadeOut(limit_title), FadeOut(axes2), FadeOut(curve2),
                  FadeOut(point_p), FadeOut(label_p))

        # ─────────────────────────────────────────────
        # SCENE 5 — FORMAL DEFINITION  (~2:40 – 3:20)
        # ─────────────────────────────────────────────
        def_title = Text("The Formal Definition", font_size=44, color=YELLOW)
        def_title.to_edge(UP)
        self.play(Write(def_title), run_time=1.5)
        self.wait(3)

        limit_def = MathTex(
            r"f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}",
            font_size=52, color=WHITE
        )
        self.play(Write(limit_def), run_time=2.5)
        self.wait(5)

        box = SurroundingRectangle(limit_def, color=YELLOW, buff=0.3)
        self.play(Create(box), run_time=1)
        self.wait(4)

        words = Text("This is called the DERIVATIVE", font_size=34, color=GREEN)
        words.next_to(limit_def, DOWN, buff=0.8)
        self.play(Write(words), run_time=1.5)
        self.wait(5)

        self.play(FadeOut(def_title), FadeOut(limit_def), FadeOut(box), FadeOut(words))

        # ─────────────────────────────────────────────
        # SCENE 6 — WORKED EXAMPLE: d(x²)/dx  (~3:20 – 4:10)
        # ─────────────────────────────────────────────
        ex_title = Text("Example: f(x) = x²", font_size=44, color=YELLOW)
        ex_title.to_edge(UP)
        self.play(Write(ex_title), run_time=1.5)
        self.wait(3)

        steps = VGroup(
            MathTex(r"f'(x)=\lim_{h\to 0}\frac{(x+h)^2-x^2}{h}", font_size=36),
            MathTex(r"=\lim_{h\to 0}\frac{x^2+2xh+h^2-x^2}{h}", font_size=36),
            MathTex(r"=\lim_{h\to 0}\frac{2xh+h^2}{h}", font_size=36),
            MathTex(r"=\lim_{h\to 0}(2x+h)", font_size=36),
            MathTex(r"= 2x", font_size=44, color=GREEN),
        ).arrange(DOWN, buff=0.4).shift(DOWN * 0.3)

        for step in steps:
            self.play(Write(step), run_time=1.5)
            self.wait(2.5)

        self.wait(3)
        self.play(FadeOut(ex_title), FadeOut(steps))

        # ─────────────────────────────────────────────
        # SCENE 7 — TANGENT LINE VISUALISATION  (~4:10 – 4:55)
        # ─────────────────────────────────────────────
        tan_title = Text("Derivative = Slope of Tangent", font_size=40, color=YELLOW)
        tan_title.to_edge(UP)
        self.play(Write(tan_title), run_time=1.5)
        self.wait(3)

        axes3 = Axes(
            x_range=[-3, 4, 1],
            y_range=[-1, 16, 2],
            x_length=9,
            y_length=5,
            axis_config={"color": WHITE},
            x_axis_config={"numbers_to_include": [-2, -1, 0, 1, 2, 3]},
            y_axis_config={"numbers_to_include": [0, 4, 8, 12]},
        ).shift(DOWN * 0.3)

        curve3 = axes3.plot(lambda x: x**2, color=BLUE, x_range=[-2.5, 3.5])
        label_curve = MathTex("f(x)=x^2", font_size=28, color=BLUE).next_to(
            axes3.c2p(3, 9), RIGHT
        )

        self.play(Create(axes3), Create(curve3), Write(label_curve), run_time=2)
        self.wait(2)

        x_tracker = ValueTracker(1)

        def get_tangent():
            x0 = x_tracker.get_value()
            y0 = x0**2
            slope = 2 * x0
            return axes3.plot(
                lambda x: slope * (x - x0) + y0,
                color=RED,
                x_range=[x0 - 1.5, x0 + 1.5],
            )

        def get_point():
            x0 = x_tracker.get_value()
            return Dot(axes3.c2p(x0, x0**2), color=YELLOW, radius=0.08)

        def get_slope_label():
            x0 = x_tracker.get_value()
            slope = 2 * x0
            return MathTex(
                f"f'({x0:.1f}) = {slope:.1f}", font_size=32, color=RED
            ).to_corner(DR)

        tangent_line  = always_redraw(get_tangent)
        moving_dot    = always_redraw(get_point)
        slope_label   = always_redraw(get_slope_label)

        self.play(Create(tangent_line), FadeIn(moving_dot), Write(slope_label), run_time=1.5)
        self.wait(2)
        self.play(x_tracker.animate.set_value(3), run_time=4, rate_func=smooth)
        self.wait(1)
        self.play(x_tracker.animate.set_value(-2), run_time=4, rate_func=smooth)
        self.wait(2)

        self.play(FadeOut(tan_title), FadeOut(axes3), FadeOut(curve3),
                  FadeOut(label_curve), FadeOut(tangent_line),
                  FadeOut(moving_dot), FadeOut(slope_label))

        # ─────────────────────────────────────────────
        # SCENE 8 — QUICK RULES  (~4:55 – 5:30)
        # ─────────────────────────────────────────────
        rules_title = Text("Key Differentiation Rules", font_size=44, color=YELLOW)
        rules_title.to_edge(UP)
        self.play(Write(rules_title), run_time=1.5)
        self.wait(3)

        rules = VGroup(
            MathTex(r"\textbf{Power Rule:} \quad \frac{d}{dx}x^n = nx^{n-1}", font_size=34, color=WHITE),
            MathTex(r"\textbf{Constant:} \quad \frac{d}{dx}c = 0", font_size=34, color=WHITE),
            MathTex(r"\textbf{Sum Rule:} \quad (f+g)' = f'+g'", font_size=34, color=WHITE),
            MathTex(r"\textbf{Example:} \quad \frac{d}{dx}x^3 = 3x^2", font_size=34, color=GREEN),
        ).arrange(DOWN, buff=0.5).shift(DOWN * 0.3)

        for rule in rules:
            self.play(FadeIn(rule, shift=LEFT), run_time=1.2)
            self.wait(3)

        self.wait(3)
        self.play(FadeOut(rules_title), FadeOut(rules))

        # ─────────────────────────────────────────────
        # SCENE 9 — REAL-LIFE WRAP-UP  (~5:30 – 6:00)
        # ─────────────────────────────────────────────
        wrap_title = Text("Derivatives are Everywhere!", font_size=44, color=YELLOW)
        wrap_title.to_edge(UP)
        self.play(Write(wrap_title), run_time=1.5)
        self.wait(2)

        examples = VGroup(
            Text("🚗  Speed = derivative of distance", font_size=30, color=WHITE),
            Text("📈  Profit optimisation in business", font_size=30, color=WHITE),
            Text("🌡️  Rate of temperature change", font_size=30, color=WHITE),
            Text("💊  Drug concentration in medicine", font_size=30, color=WHITE),
        ).arrange(DOWN, buff=0.45, aligned_edge=LEFT).shift(DOWN * 0.3)

        for ex in examples:
            self.play(FadeIn(ex, shift=RIGHT), run_time=1)
            self.wait(2.5)

        self.wait(3)
        self.play(FadeOut(wrap_title), FadeOut(examples))

        # ─────────────────────────────────────────────
        # SCENE 10 — OUTRO  (~6:00 – 6:10)
        # ─────────────────────────────────────────────
        outro = Text("That's Differential Calculus!", font_size=50, color=YELLOW)
        tagline = Text("Keep learning. Keep growing.", font_size=30, color=WHITE)
        tagline.next_to(outro, DOWN, buff=0.5)

        self.play(Write(outro), run_time=2)
        self.play(FadeIn(tagline), run_time=1.5)
        self.wait(5)
        self.play(FadeOut(outro), FadeOut(tagline))
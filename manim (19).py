from manim import *
import numpy as np

class DerivativeIntro(Scene):
    def construct(self):
        # Configuration for axes to ensure it fits well within the screen
        AXES_CONFIG = {
            "x_range": [-1, 5, 1],
            "y_range": [-1, 10, 2],
            "axis_config": {"include_numbers": True},
            "tips": True
        }
        
        # Scaling down and shifting slightly to make room for titles and formulas
        axes = Axes(**AXES_CONFIG).scale(0.8).shift(DOWN * 0.5)
        
        # ─── PART 1: y = 2x ───
        title1 = Text("১. ধ্রুবক ঢাল: y = 2x", color=BLUE, font_size=36, font="Shonar Bangla").to_edge(UP)
        f1 = lambda x: 2*x
        graph1 = axes.plot(f1, x_range=[0, 4.5], color=BLUE)
        label1 = MathTex("y = 2x", color=BLUE).next_to(graph1, UR, buff=0.1)
        
        self.play(Write(title1))
        self.play(Create(axes), Create(graph1), Write(label1), run_time=1.5)
        self.wait(1)
        
        # Show slope for linear function
        t_tracker = ValueTracker(1)
        # The tangent for a straight line is the line itself. 
        # alpha = (current_x - x_min) / (x_max - x_min)
        tangent1 = always_redraw(lambda: 
            TangentLine(graph1, alpha=t_tracker.get_value()/4.5, length=4, color=YELLOW)
        )
        slope_label1 = always_redraw(lambda: 
            VGroup(
                Text("ঢাল = ", font_size=24, font="Shonar Bangla"),
                MathTex("2", color=YELLOW)
            ).arrange(RIGHT).to_corner(UR, buff=1)
        )
        
        self.play(Create(tangent1), Write(slope_label1))
        self.play(t_tracker.animate.set_value(3.5), run_time=2, rate_func=linear)
        self.wait(1)
        
        # ─── TRANSITION: Transform 2x into x^2 ───
        title2 = Text("২. পরিবর্তনশীল ঢাল: y = x²", color=GREEN, font_size=36, font="Shonar Bangla").to_edge(UP)
        f2 = lambda x: x**2
        graph2 = axes.plot(f2, x_range=[0, 3.1], color=GREEN)
        label2 = MathTex("y = x^2", color=GREEN).next_to(graph2, UR, buff=0.1)

        self.play(
            ReplacementTransform(title1, title2),
            ReplacementTransform(graph1, graph2),
            ReplacementTransform(label1, label2),
            FadeOut(tangent1),
            FadeOut(slope_label1),
            run_time=2
        )
        self.wait(1)
        
        
        # Moving tangent to show how slope changes dynamically
        t_tracker.set_value(0.5)
        tangent2 = always_redraw(lambda: 
            TangentLine(graph2, alpha=t_tracker.get_value()/3.1, length=4, color=YELLOW)
        )
        slope_label2 = always_redraw(lambda: 
            VGroup(
                Text("x =", font_size=24, font="Shonar Bangla"),
                MathTex(f"{t_tracker.get_value():.1f}", color=WHITE),
                Text(" বিন্দুতে ঢাল ", font_size=24, font="Shonar Bangla"),
                MathTex(f"{2*t_tracker.get_value():.1f}", color=YELLOW)
            ).arrange(RIGHT, buff=0.15).to_corner(UR, buff=0.8)
        )
        
        self.play(Create(tangent2), Write(slope_label2))
        self.play(t_tracker.animate.set_value(2.5), run_time=4, rate_func=smooth)
        self.wait(1)
        
        # Clear only labels to make room for Part 3 while keeping graph
        self.play(FadeOut(title2), FadeOut(label2), FadeOut(tangent2), FadeOut(slope_label2))

        # ─── PART 3: Visualize the Limit Definition ───
        title3 = Text("৩. অন্তরজের সূত্রের দৃশ্যমান উপস্থাপনা", color=YELLOW, font_size=32, font="Shonar Bangla").to_edge(UP)
        self.play(Write(title3))
        
        x_fixed = 2.0
        h_tracker = ValueTracker(1.0)
        
        # Point P(x, f(x))
        dot_x = Dot(axes.c2p(x_fixed, f2(x_fixed)), color=RED)
        line_x = axes.get_vertical_line(dot_x.get_center(), color=RED, stroke_width=2)
        label_x = MathTex("x", color=RED).next_to(line_x, DOWN)
        line_f_x = axes.get_horizontal_line(dot_x.get_center(), color=RED, stroke_width=2)
        label_f_x = MathTex("f(x)", color=RED, font_size=30).next_to(line_f_x, LEFT)
        
        # Point Q(x+h, f(x+h))
        dot_xh = always_redraw(lambda: Dot(
            axes.c2p(x_fixed + h_tracker.get_value(), f2(x_fixed + h_tracker.get_value())), 
            color=YELLOW
        ))
        line_xh = always_redraw(lambda: axes.get_vertical_line(dot_xh.get_center(), color=YELLOW, stroke_width=2))
        label_xh = always_redraw(lambda: MathTex("x+h", color=YELLOW, font_size=30).next_to(line_xh, DOWN))
        line_f_xh = always_redraw(lambda: axes.get_horizontal_line(dot_xh.get_center(), color=YELLOW, stroke_width=2))
        label_f_xh = always_redraw(lambda: MathTex("f(x+h)", color=YELLOW, font_size=30).next_to(line_f_xh, LEFT))

        # Braces for Delta x (h) and Delta y
        h_brace = always_redraw(lambda: BraceBetweenPoints(
            axes.c2p(x_fixed, 0), axes.c2p(x_fixed + h_tracker.get_value(), 0), DOWN, buff=0.8
        ))
        h_label = always_redraw(lambda: MathTex(r"\Delta x = h", color=YELLOW).next_to(h_brace, DOWN, buff=0.1))

        dy_brace = always_redraw(lambda: BraceBetweenPoints(
            axes.c2p(x_fixed + h_tracker.get_value(), f2(x_fixed)),
            axes.c2p(x_fixed + h_tracker.get_value(), f2(x_fixed + h_tracker.get_value())),
            RIGHT, buff=0.1
        ))
        dy_label = always_redraw(lambda: MathTex(r"\Delta y", color=YELLOW, font_size=24).next_to(dy_brace, RIGHT))

        # Dynamic secant line (Average Slope)
        def get_secant():
            h = h_tracker.get_value()
            if abs(h) < 0.001: h = 0.001
            p1 = axes.c2p(x_fixed, f2(x_fixed))
            p2 = axes.c2p(x_fixed + h, f2(x_fixed + h))
            return Line(p1, p2, color=ORANGE).scale(3.5)

        secant = always_redraw(get_secant)
        
        slope_display = always_redraw(lambda: 
            VGroup(
                VGroup(
                    Text("ঢাল", font_size=24, font="Shonar Bangla", color=ORANGE),
                    MathTex(r"= \frac{\Delta y}{\Delta x}", color=ORANGE)
                ).arrange(RIGHT, buff=0.1),
                MathTex(f"= { (f2(x_fixed + h_tracker.get_value()) - f2(x_fixed)) / h_tracker.get_value() :.2f}", color=YELLOW)
            ).arrange(DOWN).to_corner(UR, buff=0.8)
        )
        
        formula = MathTex(
            "f'(x) = \\lim_{h \\to 0} \\frac{f(x+h) - f(x)}{h}",
            font_size=42
        ).to_edge(DOWN, buff=0.4).add_background_rectangle()
        
        self.play(FadeIn(dot_x), Create(line_x), Write(label_x), Create(line_f_x), Write(label_f_x))
        self.play(
            Create(secant), Write(slope_display),
            FadeIn(dot_xh), Create(line_xh), Write(label_xh),
            Create(line_f_xh), Write(label_f_xh),
            GrowFromCenter(h_brace), Write(h_label),
            GrowFromCenter(dy_brace), Write(dy_label)
        )
        self.wait(1)
        self.play(Write(formula))
        self.wait(2)
        
        # The climax: animate h approaching zero (secant becomes tangent)
        final_slope_label = VGroup(
            Text("ঢাল", font_size=24, font="Shonar Bangla", color=YELLOW),
            MathTex(r"\to 2x = 4", color=YELLOW)
        ).arrange(RIGHT, buff=0.1).to_corner(UR, buff=0.8)

        self.play(
            h_tracker.animate.set_value(0.001), 
            FadeOut(h_brace), FadeOut(h_label), 
            FadeOut(line_f_xh), FadeOut(label_f_xh),
            FadeOut(line_xh), FadeOut(label_xh),
            FadeOut(dy_brace), FadeOut(dy_label),
            run_time=6, rate_func=smooth
        )
        self.play(Transform(slope_display, final_slope_label))
        self.wait(3)

        # Final fade out for a clean transition to derivation
        self.play(FadeOut(axes), FadeOut(graph2), FadeOut(title3), FadeOut(dot_x), FadeOut(line_x), 
                  FadeOut(label_x), FadeOut(secant), FadeOut(dot_xh), FadeOut(slope_display), 
                  FadeOut(formula), FadeOut(line_f_x), FadeOut(label_f_x))

        # ─── PART 4: Step-by-Step Derivation ───
        derivation_title = Text("ধাপে ধাপে অন্তরজ নির্ণয়", color=BLUE, font_size=36, font="Shonar Bangla").to_edge(UP)
        self.play(Write(derivation_title))

        steps = VGroup(
            MathTex(r"f(x) = x^2"),
            MathTex(r"f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}"),
            MathTex(r"f'(x) = \lim_{h \to 0} \frac{(x+h)^2 - x^2}{h}"),
            MathTex(r"f'(x) = \lim_{h \to 0} \frac{x^2 + 2xh + h^2 - x^2}{h}"),
            MathTex(r"f'(x) = \lim_{h \to 0} \frac{2xh + h^2}{h}"),
            MathTex(r"f'(x) = \lim_{h \to 0} (2x + h)"),
            MathTex(r"f'(x) = 2x", color=YELLOW)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).scale(0.8).shift(DOWN * 0.5)

        for i, step in enumerate(steps):
            self.play(Write(step))
            self.wait(1)
            if i == 6: # Highlight the final result
                self.play(Indicate(step))

        self.wait(2)
        self.play(FadeOut(steps), FadeOut(derivation_title))

        # ─── PART 5: Importance of Derivation ───
        importance_title = Text("অন্তরজের গুরুত্ব:", color=GOLD, font_size=40, font="Shonar Bangla").to_edge(UP)
        self.play(Write(importance_title))

        importance_points = VGroup(
            Text("• গতির পরিবর্তন পরিমাপ করতে ব্যবহৃত হয় (যেমন: বেগ ও ত্বরণ)।", font_size=28, font="Shonar Bangla"),
            Text("• ব্যবসায়িক মুনাফা সর্বোচ্চ করতে এটি অত্যন্ত সহায়ক।", font_size=28, font="Shonar Bangla"),
            Text("• বিজ্ঞানের বিভিন্ন শাখায় পরিবর্তনের হার বিশ্লেষণে ব্যবহৃত হয়।", font_size=28, font="Shonar Bangla")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).move_to(ORIGIN)

        for p in importance_points:
            self.play(FadeIn(p, shift=RIGHT))
            self.wait(2)

        self.wait(1)
        self.play(FadeOut(importance_title), FadeOut(importance_points))

        # ─── PART 6: Thank You ───
        thanks = Text("ধন্যবাদ!", font="Shonar Bangla", font_size=72, color=WHITE).move_to(ORIGIN)
        underline = Underline(thanks, color=BLUE)
        
        self.play(Write(thanks), GrowFromCenter(underline))
        self.wait(3)
        self.play(FadeOut(thanks), FadeOut(underline))
        self.wait(1)
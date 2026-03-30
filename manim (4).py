from manim import *

class ExpToCircle(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        # ── 1. Axes & e^x graph ──────────────────────────────────────────────
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-0.5, 8, 1],
            x_length=10,
            y_length=6.5,
            axis_config={"color": BLACK, "include_numbers": True, "font_size": 24},
            tips=True,
        )
        axes_labels = axes.get_axis_labels(
            x_label=MathTex("x", color=BLACK),
            y_label=MathTex("e^x", color=BLACK),
        )

        graph = axes.plot(lambda x: np.exp(x), x_range=[-3, 2.05], color=BLUE)
        graph_label = axes.get_graph_label(graph, label=MathTex("e^x", color=BLACK), x_val=1.5, color=BLUE)

        self.play(Create(axes), Write(axes_labels), run_time=1.5)
        self.play(Create(graph), Write(graph_label), run_time=2)
        self.wait(0.5)

        # ── 2. Mark a point on the curve (x=0, y=1) ─────────────────────────
        focus_x = 0
        focus_point_coords = axes.c2p(focus_x, np.exp(focus_x))   # (0, 1)

        dot = Dot(focus_point_coords, color=RED, radius=0.1)
        point_label = MathTex("(0,\\ 1)", color=RED).next_to(dot, UR, buff=0.15)

        self.play(FadeIn(dot, scale=1.5), Write(point_label))
        self.wait(0.5)

        # ── 3. Zoom into that point ──────────────────────────────────────────
        # We scale everything up and shift so the focus point ends up at centre
        zoom_group = VGroup(axes, axes_labels, graph, graph_label, dot, point_label)

        self.play(
            zoom_group.animate
                .scale(4, about_point=focus_point_coords)
                .shift(ORIGIN - focus_point_coords),
            run_time=2.5,
            rate_func=smooth,
        )
        self.wait(0.8)

        # ── 4. Transform the (now-huge) graph curve into a circle ────────────
        # Build the target circle centred at screen origin
        circle = Circle(radius=2.2, color=BLUE, stroke_width=4)
        circle.move_to(ORIGIN)

        # Fade out extra clutter, keep only the graph curve as the morph source
        self.play(
            FadeOut(axes, axes_labels, graph_label, point_label, dot),
            run_time=0.8,
        )

        # The visible portion of the graph after zoom is stored in `graph`.
        # MorphInto / Transform will morph its path into the circle.
        self.play(
            Transform(graph, circle),
            run_time=2.5,
            rate_func=smooth,
        )
        self.wait(0.5)

        # ── 5. Finishing touches ─────────────────────────────────────────────
        circle_label = MathTex(r"x^2 + y^2 = r^2", color=BLACK).scale(0.9).next_to(circle, DOWN, buff=0.4)
        self.play(Write(circle_label))

        # Subtle rotation to celebrate
        self.play(Rotate(graph, angle=TAU, about_point=ORIGIN), run_time=2.5)
        self.wait(1)
        self.play(FadeOut(graph, circle_label))
        self.wait(0.3)

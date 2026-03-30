from manim import *
import numpy as np

class EquationSolving(MovingCameraScene):
    def construct(self):
        # --- Phase 1: Step-by-Step Solving ---
        title = Text("Solving the Quadratic Equation", font_size=36, color=BLUE).to_edge(UP)
        eq = MathTex("x^2 - 2x = 0", font_size=48).next_to(title, DOWN, buff=0.5)
        
        self.play(Write(title))
        self.play(Write(eq))
        self.wait(1)

        step1 = MathTex("x(x - 2) = 0", font_size=42, color=YELLOW).next_to(eq, DOWN, buff=0.6)
        self.play(Write(step1))
        self.wait(1)

        step2 = MathTex("x = 0 \quad \text{or} \quad x - 2 = 0", font_size=42).next_to(step1, DOWN, buff=0.6)
        self.play(Write(step2))
        self.wait(1)

        step3 = MathTex("x_1 = 0, \quad x_2 = 2", font_size=48, color=GREEN).next_to(step2, DOWN, buff=0.6)
        self.play(Write(step3))
        self.wait(2)

        # Clear the screen for the graph to avoid overlapping
        self.play(FadeOut(title), FadeOut(eq), FadeOut(step1), FadeOut(step2), FadeOut(step3))

        # --- Phase 2: Graphing ---
        axes = Axes(
            x_range=[-2, 4, 1],
            y_range=[-2, 4, 1],
            x_length=8,
            y_length=6,
            axis_config={"include_numbers": True, "font_size": 24}
        )
        
        # The function f(x) = x^2 - 2x
        graph = axes.plot(lambda x: x**2 - 2*x, x_range=[-0.8, 2.8], color=BLUE)
        graph_label = axes.get_graph_label(graph, label="f(x) = x^2 - 2x").scale(0.8)

        self.play(Create(axes), run_time=1.5)
        self.play(Create(graph), Write(graph_label), run_time=2)
        self.wait(1)

        # Mark the roots found in Phase 1
        dot1 = Dot(axes.c2p(0, 0), color=RED)
        dot2 = Dot(axes.c2p(2, 0), color=RED)
        label1 = MathTex("0", font_size=24, color=RED).next_to(dot1, DOWN + LEFT, buff=0.1)
        label2 = MathTex("2", font_size=24, color=RED).next_to(dot2, DOWN + RIGHT, buff=0.1)

        self.play(
            FadeIn(dot1, scale=0.5), FadeIn(dot2, scale=0.5),
            Write(label1), Write(label2)
        )
        self.wait(2)

        # --- Phase 3: Zoom and Transform ---
        # We will zoom into the vertex of the parabola (1, -1)
        vertex_coord = axes.c2p(1, -1)
        
        self.play(
            self.camera.frame.animate.scale(0.5).move_to(vertex_coord),
            FadeOut(axes), FadeOut(graph_label), FadeOut(dot1), FadeOut(dot2),
            FadeOut(label1), FadeOut(label2),
            run_time=2
        )
        self.wait(0.5)

        # Transform the blue parabola segment into a green circle
        # We'll create a circle centered at the vertex
        target_circle = Circle(radius=1.0, color=GREEN, stroke_width=4).move_to(vertex_coord)
        
        self.play(
            ReplacementTransform(graph, target_circle),
            run_time=2.5,
            rate_func=smooth
        )
        
        circle_text = Text("Transformation Complete", font_size=20, color=GREEN).next_to(target_circle, UP, buff=0.2)
        self.play(Write(circle_text))
        self.wait(2)
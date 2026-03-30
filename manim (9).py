from manim import *

class QuadraticToCircle(Scene):
    def construct(self):
        # Set background
        self.camera.background_color = WHITE
        
        # Title
        title = Text("Quadratic Function Analysis", font_size=36, color=BLACK)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        
        # ============ PART 1: GRAPH THE FUNCTION ============
        axes = Axes(
            x_range=[-5, 3, 1],
            y_range=[-4, 8, 2],
            axis_config={"color": BLACK},
            tips=False,
        )
        axes.scale(0.7)
        axes.shift(LEFT * 3.5 + DOWN * 0.5)
        
        # Function: f(x) = x^2 + 3x - 2
        func = lambda x: x**2 + 3*x - 2
        graph = axes.plot(func, color=BLUE, stroke_width=2.5)
        
        # Labels
        func_label = Text("f(x) = x² + 3x - 2", font_size=24, color=BLUE)
        func_label.next_to(axes, UP, buff=0.2)
        
        self.play(Create(axes), Write(func_label), run_time=1.5)
        self.play(Create(graph), run_time=2)
        self.wait(0.5)
        
        # ============ PART 2: SOLVE f(x) = 0 ============
        # Using quadratic formula: x = (-3 ± √(9 + 8)) / 2 = (-3 ± √17) / 2
        sqrt_val = np.sqrt(17)
        x1 = (-3 + sqrt_val) / 2  # ≈ 0.56
        x2 = (-3 - sqrt_val) / 2  # ≈ -3.56
        
        # Mark roots on graph
        dot1 = Dot(axes.c2p(x1, 0), color=RED, radius=0.08)
        dot2 = Dot(axes.c2p(x2, 0), color=RED, radius=0.08)
        
        self.play(Create(dot1), Create(dot2), run_time=1)
        
        # Solution text
        solution_text = VGroup(
            Text("Solutions:", font_size=20, color=BLACK, weight=BOLD),
            Text(f"x₁ ≈ {x1:.2f}", font_size=18, color=RED),
            Text(f"x₂ ≈ {x2:.2f}", font_size=18, color=RED),
        )
        solution_text.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        solution_text.to_corner(UR, buff=0.3)
        
        self.play(Write(solution_text), run_time=1.5)
        self.wait(1)
        
        # ============ PART 3: TRANSFORM TO CIRCLE ============
        # Fade out solution text and function label
        self.play(FadeOut(solution_text), FadeOut(func_label), run_time=0.8)
        
        # Create circle
        circle = Circle(radius=1.5, color=GREEN, stroke_width=2.5)
        circle.move_to(axes.get_center())
        
        # Transform graph to circle
        self.play(Transform(graph, circle), run_time=2)
        
        # Circle label
        circle_label = Text("Circle: x² + y² = r²", font_size=22, color=GREEN)
        circle_label.next_to(axes, UP, buff=0.2)
        
        self.play(Write(circle_label), run_time=1)
        self.wait(1)
        
        # Fade out everything
        self.play(FadeOut(axes), FadeOut(graph), FadeOut(dot1), FadeOut(dot2), 
                  FadeOut(circle_label), run_time=1)


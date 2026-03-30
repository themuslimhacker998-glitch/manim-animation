from manim import *
import numpy as np

class ExponentialGraph(Scene):
    def construct(self):
        # Configuration for colors
        AXIS_COLOR = "#888888"
        GRAPH_COLOR = "#FFD700"  # Gold
        TANGENT_COLOR = "#FF69B4" # Hot Pink
        TEXT_COLOR = WHITE
        
        # 1. Setup Axes with a grid
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-1, 15, 5],
            axis_config={
                "color": AXIS_COLOR,
                "include_numbers": True,
                "stroke_width": 2,
            },
            tips=True
        ).scale(0.8)
        
        labels = axes.get_axis_labels(
            x_label="x", 
            y_label="f(x) = e^x"
        ).set_color(AXIS_COLOR)
        
        # 2. Define the exponential function
        func = lambda x: np.exp(x)
        
        # Create the graph
        # We limit the x range slightly so it doesn't shoot off the screen TOO fast
        graph = axes.plot(
            func, 
            x_range=[-5, 2.7], 
            color=GRAPH_COLOR, 
            stroke_width=4
        )
        
        # Mathematical Label
        formula = MathTex("f(x) = e^x", color=GRAPH_COLOR).scale(1.2)
        formula.to_corner(UR, buff=1)
        
        # 3. Introduction: Draw Axes and Graph
        self.camera.background_color = "#121212" # Sleek dark background
        
        self.play(Create(axes), Write(labels), run_time=1.5)
        self.wait(0.5)
        
        # Draw the curve with a nice glow-like effect (using multiple strokes or just bold)
        self.play(Create(graph), Write(formula), run_time=2.5, rate_func=smooth)
        self.wait(1)
        
        # 4. Highlighting properties: The Point (0, 1)
        # This is where the exponential function intercepts the Y-axis
        dot_01 = Dot(axes.c2p(0, 1), color=RED, radius=0.1)
        glow_01 = Dot(axes.c2p(0, 1), color=RED, radius=0.2, fill_opacity=0.3)
        lbl_01 = MathTex("(0, 1)", color=RED, font_size=32).next_to(dot_01, UL, buff=0.1)
        
        self.play(FadeIn(glow_01, scale=0.5), Create(dot_01), Write(lbl_01))
        self.play(Indicate(dot_01, color=RED, scale_factor=1.5))
        self.wait(1)
        
        # 5. Tangent Line Animation (Showing that slope = value)
        # This is a premium feature: a moving tangent line
        t = ValueTracker(-2)
        
        # Redraw the tangent line at the value of 't'
        # Since the graph x_range is [-5, 2.7], we map t to alpha [0, 1]
        tangent = always_redraw(lambda: 
            TangentLine(
                graph, 
                alpha=(t.get_value() + 5) / (2.7 + 5), 
                length=4, 
                color=TANGENT_COLOR
            )
        )
        
        # A dot that follows the curve
        moving_dot = always_redraw(lambda: 
            Dot(axes.c2p(t.get_value(), func(t.get_value())), color=WHITE, radius=0.08)
        )
        
        # A live label showing the slope
        slope_display = always_redraw(lambda: 
            VGroup(
                Text("Current Slope:", font_size=24, color=TANGENT_COLOR),
                MathTex(f"f'({t.get_value():.2f}) = {func(t.get_value()):.2f}", color=TANGENT_COLOR)
            ).arrange(RIGHT).to_corner(UL, buff=0.8)
        )
        
        self.play(FadeIn(moving_dot), Create(tangent), Write(slope_display))
        
        # Move the tracker to animate everything
        self.play(t.animate.set_value(2.5), run_time=4, rate_func=smooth)
        self.wait(0.5)
        self.play(t.animate.set_value(0), run_time=2, rate_func=smooth)
        self.wait(1)
        
        # 6. Conclusion
        conclusion = Text("The slope is always equal to the function's value.", font_size=28)
        conclusion.set_color(TANGENT_COLOR).to_edge(DOWN, buff=0.5)
        
        self.play(Write(conclusion))
        self.wait(2)
        
        # Fade out everything gracefully
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.5
        )
        self.wait(0.5)

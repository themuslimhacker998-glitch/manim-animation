from manim import *

class ExponentialEquation(Scene):
    def construct(self):
        # Create the equation
        equation = MathTex("y = e^{x}").scale(2)
        self.play(Write(equation))
        self.wait(2)
        
        # Create the axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 20, 5],
            axis_config={"color": BLUE},
        )
        self.play(Create(axes))
        self.wait(1)

        # Create the graph of the exponential function
        graph = axes.plot(lambda x: np.exp(x), color=YELLOW)
        graph_label = axes.get_graph_label(graph, label='e^{x}')
        
        self.play(Create(graph), Write(graph_label))
        self.wait(2)

        # Solve the equation manually
        solution_text = MathTex("Solve: e^{x} = 5").scale(1.5)
        self.play(Transform(equation, solution_text))
        self.wait(2)

        # Show the solution steps
        steps = VGroup(
            MathTex("x = \\ln(5)").scale(1.5),
            MathTex("x \\approx 1.609").scale(1.5)
        ).arrange(DOWN, buff=0.5)

        self.play(Write(steps[0]))
        self.wait(1)
        self.play(Write(steps[1]))
        self.wait(2)

        # End the scene
        self.play(FadeOut(equation), FadeOut(steps), FadeOut(graph), FadeOut(graph_label), FadeOut(axes))
        self.wait(1)

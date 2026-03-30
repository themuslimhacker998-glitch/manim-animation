from manim import *

class QuadraticToCircle(Scene):
    def construct(self):
        # Set up axes  
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 5, 1],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": True}
        )
        axes.to_edge(LEFT)

        # Define the quadratic function  
        def func(x):
            return 2 * x**2 - 3 * x + 2

        # Plot the function graph  
        graph = axes.plot(func, color=BLUE)

        # Add the axes and graph to the scene  
        self.play(Create(axes), Create(graph))
        self.wait(1)

        # Annotate the function  
        func_text = MathTex("f(x) = 2x^2 - 3x + 2").to_corner(UL)
        self.play(Write(func_text))
        self.wait(1)

        # Find roots of the quadratic  
        roots = np.roots([2, -3, 2])  # Coefficients: 2x^2 -3x + 2  
        root_points = [axes.c2p(root, 0) for root in roots]

        # Mark roots  
        root_marks = VGroup()
        for point in root_points:
            mark = Dot(point, color=RED)
            label = MathTex(f"{axes.point_to_coords(point)[0]:.2f}").next_to(mark, DOWN)
            root_marks.add(VGroup(mark, label))
        self.play(LaggedStartMap(Create, root_marks))
        self.wait(1)

        # Animate the graph shifting to the left  
        move_distance = 1.5  
        self.play(
            axes.animate.shift(LEFT * move_distance),
            graph.animate.shift(LEFT * move_distance),
            run_time=2  
        )

        # Fade out previous texts  
        self.play(FadeOut(func_text), FadeOut(root_marks))
        self.wait(1)

        # Zoom in the camera  
        self.play(
            self.camera.animate.set_width(2),
            run_time=2  
        )
        self.wait(1)

        # Transform the parabola into a circle  
        circle = Circle(radius=1.5, color=GREEN)
        circle.move_to(axes.c2p(0, 0))
        self.play(Transform(graph, circle), run_time=3)
        self.wait(2)
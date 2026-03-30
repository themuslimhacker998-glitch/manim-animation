from manim import *

class ConeToCylinder(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES)

        axes = ThreeDAxes(
            x_range=[-4, 4], y_range=[-4, 4], z_range=[-4, 4],
            axis_config={"stroke_color": GREY_B, "stroke_width": 2}
        )

        cone = Cone(
            height=3, base_radius=1.5, direction=Z_AXIS,
            fill_opacity=0.6, color=BLUE_C
        ).move_to(ORIGIN)

        # Volume labels fixed on screen
        label = MathTex("V = \\frac{1}{3}\\pi r^2 h", color=BLUE_C).to_corner(UL)
        self.add_fixed_in_frame_mobjects(label)

        self.play(Create(axes), run_time=1)
        self.play(FadeIn(cone), Write(label), run_time=1.5)
        self.wait(0.5)

        cylinder = Cylinder(
            height=3, radius=1.5, direction=Z_AXIS,
            fill_opacity=0.6, color=GREEN_C
        ).move_to(ORIGIN)

        new_label = MathTex("V = \\pi r^2 h", color=GREEN_C).to_corner(UL)

        self.play(
            ReplacementTransform(cone, cylinder),
            Transform(label, new_label),
            run_time=3
        )

        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.wait(0.5)
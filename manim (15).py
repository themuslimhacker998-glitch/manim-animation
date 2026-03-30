from manim import *

class ConeToCylinder(ThreeDScene):
    def construct(self):
        self.camera.background_color = WHITE

        axes = ThreeDAxes(
            x_range=[-4,4],
            y_range=[-4,4],
            z_range=[-4,4]
        )

        self.set_camera_orientation(phi=65 * DEGREES, theta=45 * DEGREES)

        cone = Cone(
            base_radius=1.5,
            height=3,
            direction=DOWN,
            fill_opacity=0.7,
            color=BLUE
        )

        cylinder = Cylinder(
            radius=1.5,
            height=3,
            direction=DOWN,
            fill_opacity=0.7,
            color=GREEN
        )

        cone.move_to(ORIGIN)
        cylinder.move_to(ORIGIN)

        self.play(Create(axes))
        self.play(FadeIn(cone))
        self.wait(1)

        self.play(Transform(cone, cylinder), run_time=3)
        self.wait(2)
from manim import *
import numpy as np


class CircleIntersection(Scene):
    def construct(self):
        # ── 3b1b style config ──
        self.camera.background_color = "#1a1a2e"

        # ── Parameters ──
        r = 2.5  # visual radius (representing 5 cm)
        d = 3.0  # distance between centers (so circles overlap nicely)

        # ── Title ──
        title = Text(
            "Circle Intersection",
            font="sans-serif",
            font_size=48,
            color=WHITE,
        ).to_edge(UP, buff=0.5)
        underline = Line(
            title.get_left(), title.get_right(), color=BLUE, stroke_width=2
        ).next_to(title, DOWN, buff=0.1)

        self.play(Write(title), GrowFromCenter(underline), run_time=1.5)
        self.wait(0.5)

        # ── Circle centers ──
        c1 = LEFT * d / 2
        c2 = RIGHT * d / 2

        # ── Circles ──
        circle1 = Circle(radius=r, color=BLUE, stroke_width=3).move_to(c1)
        circle2 = Circle(radius=r, color=TEAL, stroke_width=3).move_to(c2)

        # ── Draw circles with 3b1b flair ──
        self.play(Create(circle1), Create(circle2), run_time=2, lag_ratio=0.3)
        self.wait(0.3)

        # ── Center dots and labels ──
        dot1 = Dot(c1, color=BLUE_B, radius=0.08)
        dot2 = Dot(c2, color=TEAL_B, radius=0.08)
        label_o1 = MathTex("O_1", color=BLUE_B, font_size=36).next_to(dot1, DOWN, buff=0.2)
        label_o2 = MathTex("O_2", color=TEAL_B, font_size=36).next_to(dot2, DOWN, buff=0.2)

        self.play(
            FadeIn(dot1, scale=0.5),
            FadeIn(dot2, scale=0.5),
            Write(label_o1),
            Write(label_o2),
            run_time=1,
        )

        # ── Compute intersection points A, B ──
        # For two circles of equal radius r, centers separated by d:
        # x_intersect = d/2,  y_intersect = ±sqrt(r² - (d/2)²)  (relative to midpoint)
        # But since c1 is at (-d/2, 0) and c2 at (d/2, 0):
        # intersection x = 0, y = ±sqrt(r² - (d/2)²)
        h = np.sqrt(r**2 - (d / 2) ** 2)
        point_a = UP * h
        point_b = DOWN * h

        # ── Intersection dots and labels ──
        dot_a = Dot(point_a, color=YELLOW, radius=0.1)
        dot_b = Dot(point_b, color=YELLOW, radius=0.1)
        label_a = MathTex("A", color=YELLOW, font_size=40).next_to(dot_a, UR, buff=0.15)
        label_b = MathTex("B", color=YELLOW, font_size=40).next_to(dot_b, DR, buff=0.15)

        self.play(
            Flash(point_a, color=YELLOW, flash_radius=0.4),
            Flash(point_b, color=YELLOW, flash_radius=0.4),
            FadeIn(dot_a, scale=2),
            FadeIn(dot_b, scale=2),
            run_time=1,
        )
        self.play(Write(label_a), Write(label_b), run_time=0.8)
        self.wait(0.3)

        # ── Chord AB ──
        chord = DashedLine(point_a, point_b, color=YELLOW, stroke_width=2, dash_length=0.12)
        chord_label = MathTex("AB", color=YELLOW, font_size=32).next_to(chord, RIGHT, buff=0.2)

        self.play(Create(chord), Write(chord_label), run_time=1)
        self.wait(0.3)

        # ── Distance line between centers ──
        dist_line = DashedLine(c1, c2, color=GREY_B, stroke_width=2, dash_length=0.1)
        dist_label = MathTex(
            "d = 6\\text{ cm}", color=GREY_B, font_size=28
        ).next_to(dist_line, DOWN, buff=0.15)

        self.play(Create(dist_line), Write(dist_label), run_time=1)
        self.wait(0.3)

        # ── Radius indicators ──
        radius_arrow1 = Arrow(
            c1, c1 + UP * r, buff=0, color=BLUE_A, stroke_width=2, max_tip_length_to_length_ratio=0.15
        )
        r_label1 = MathTex("r=5", color=BLUE_A, font_size=28).next_to(radius_arrow1, LEFT, buff=0.1)
        radius_arrow2 = Arrow(
            c2, c2 + UP * r, buff=0, color=TEAL_A, stroke_width=2, max_tip_length_to_length_ratio=0.15
        )
        r_label2 = MathTex("r=5", color=TEAL_A, font_size=28).next_to(radius_arrow2, RIGHT, buff=0.1)

        self.play(
            GrowArrow(radius_arrow1),
            GrowArrow(radius_arrow2),
            Write(r_label1),
            Write(r_label2),
            run_time=1.2,
        )
        self.wait(0.5)

        # ── Highlight intersection region (vesica piscis) ──
        # Build the lens shape from two arcs
        # Arc on circle1 (right side) from angle -alpha to +alpha
        # Arc on circle2 (left side) from angle (pi - alpha) to (pi + alpha)
        alpha = np.arcsin(h / r)  # half-angle subtended at each center

        # Arc from circle 1: goes from point_b to point_a along the right side of circle1
        arc1 = Arc(
            radius=r,
            start_angle=-alpha,
            angle=2 * alpha,
            arc_center=c1,
            color=YELLOW,
        )

        # Arc from circle 2: goes from point_a to point_b along the left side of circle2
        arc2 = Arc(
            radius=r,
            start_angle=PI - alpha,
            angle=2 * alpha,
            arc_center=c2,
            color=YELLOW,
        )

        # Create the filled lens (intersection region)
        lens_path = VMobject(color=YELLOW, fill_color=YELLOW, fill_opacity=0.0, stroke_width=0)
        # Trace: arc1 path then arc2 path
        arc1_points = Arc(
            radius=r, start_angle=-alpha, angle=2 * alpha, arc_center=c1
        ).get_points()
        arc2_points = Arc(
            radius=r, start_angle=PI - alpha, angle=2 * alpha, arc_center=c2
        ).get_points()
        lens_path.set_points(np.concatenate([arc1_points, arc2_points]))
        lens_path.close_path()

        # Animate the highlight
        self.play(
            Create(arc1),
            Create(arc2),
            run_time=1.5,
        )
        self.wait(0.3)

        # Fill the intersection with a glow effect
        lens_fill = lens_path.copy().set_fill(YELLOW, opacity=0.3).set_stroke(width=0)
        # Pulsing glow
        self.play(FadeIn(lens_fill, run_time=1))

        # Pulse effect (3b1b signature style)
        self.play(
            lens_fill.animate.set_fill(opacity=0.5),
            rate_func=there_and_back,
            run_time=1.2,
        )
        self.play(
            lens_fill.animate.set_fill(opacity=0.5),
            rate_func=there_and_back,
            run_time=1.2,
        )
        self.wait(0.3)

        # ── Info box (bottom) ──
        info_texts = VGroup(
            MathTex(r"r_1 = r_2 = 5\text{ cm}", font_size=30, color=WHITE),
            MathTex(r"d(O_1, O_2) = 6\text{ cm}", font_size=30, color=WHITE),
            MathTex(
                r"|AB| = 2\sqrt{r^2 - \left(\tfrac{d}{2}\right)^2} = 8\text{ cm}",
                font_size=30,
                color=YELLOW,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        info_box = SurroundingRectangle(
            info_texts,
            color=BLUE_D,
            fill_color="#1a1a2e",
            fill_opacity=0.9,
            corner_radius=0.15,
            buff=0.3,
        )
        info_group = VGroup(info_box, info_texts).to_edge(DOWN, buff=0.4)

        self.play(FadeIn(info_box), run_time=0.6)
        self.play(Write(info_texts), run_time=2)
        self.wait(1.5)

        # ── Elegant fade out ──
        all_objects = VGroup(
            title, underline,
            circle1, circle2,
            dot1, dot2, label_o1, label_o2,
            dot_a, dot_b, label_a, label_b,
            chord, chord_label,
            dist_line, dist_label,
            radius_arrow1, radius_arrow2, r_label1, r_label2,
            arc1, arc2, lens_fill,
            info_group,
        )
        self.play(FadeOut(all_objects, shift=DOWN * 0.5), run_time=2)
        self.wait(0.5)

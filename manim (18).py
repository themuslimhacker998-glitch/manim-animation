from manim import *
import numpy as np


class IntersectingCircles(Scene):
    def construct(self):
        # ── Title ──────────────────────────────────────────────
        title = Text("Two Intersecting Circles", font_size=40, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title), run_time=1.5)
        self.wait(0.5)

        # ── Parameters ────────────────────────────────────────
        radius = 2.0                       # visual radius (Manim units)
        center_distance = 2.4              # overlap amount
        real_radius_text = "5 cm"          # label text

        center1 = LEFT * (center_distance / 2)
        center2 = RIGHT * (center_distance / 2)

        # ── Draw circles ──────────────────────────────────────
        circle1 = Circle(radius=radius, color="#4FC3F7", stroke_width=3)
        circle2 = Circle(radius=radius, color="#EF5350", stroke_width=3)
        circle1.move_to(center1)
        circle2.move_to(center2)

        self.play(Create(circle1), run_time=1.5)
        self.play(Create(circle2), run_time=1.5)
        self.wait(0.3)

        # ── Center dots & labels ──────────────────────────────
        dot1 = Dot(center1, color="#4FC3F7", radius=0.07)
        dot2 = Dot(center2, color="#EF5350", radius=0.07)
        label_o1 = MathTex("O_1", font_size=30, color="#4FC3F7").next_to(dot1, DOWN, buff=0.15)
        label_o2 = MathTex("O_2", font_size=30, color="#EF5350").next_to(dot2, DOWN, buff=0.15)

        self.play(
            GrowFromCenter(dot1), GrowFromCenter(dot2),
            Write(label_o1), Write(label_o2),
            run_time=0.8,
        )

        # ── Radius arrows with "5 cm" labels ─────────────────
        # Circle 1 radius – pointing upper-left
        angle1 = 135 * DEGREES
        end1 = center1 + radius * np.array([np.cos(angle1), np.sin(angle1), 0])
        radius_line1 = Line(center1, end1, color="#4FC3F7", stroke_width=2.5)
        r_label1 = MathTex(r"r = 5\text{ cm}", font_size=26, color="#4FC3F7")
        r_label1.move_to(radius_line1.get_center()).shift(UL * 0.3)

        # Circle 2 radius – pointing upper-right
        angle2 = 45 * DEGREES
        end2 = center2 + radius * np.array([np.cos(angle2), np.sin(angle2), 0])
        radius_line2 = Line(center2, end2, color="#EF5350", stroke_width=2.5)
        r_label2 = MathTex(r"r = 5\text{ cm}", font_size=26, color="#EF5350")
        r_label2.move_to(radius_line2.get_center()).shift(UR * 0.3)

        self.play(
            Create(radius_line1), Write(r_label1),
            Create(radius_line2), Write(r_label2),
            run_time=1.2,
        )
        self.wait(0.5)

        # ── Distance line between centers ─────────────────────
        dist_line = DashedLine(center1, center2, color=YELLOW, stroke_width=2)
        dist_label = MathTex(
            r"d = 6\text{ cm}", font_size=26, color=YELLOW
        ).next_to(dist_line, DOWN, buff=0.2)

        self.play(Create(dist_line), Write(dist_label), run_time=1)
        self.wait(0.3)

        # ── Intersection points P, Q ──────────────────────────
        d = center_distance
        r = radius
        # half-chord height
        h = np.sqrt(r**2 - (d / 2) ** 2)

        mid = (center1 + center2) / 2
        P = mid + UP * h
        Q = mid + DOWN * h

        dot_P = Dot(P, color=GREEN, radius=0.08)
        dot_Q = Dot(Q, color=GREEN, radius=0.08)
        label_P = MathTex("P", font_size=28, color=GREEN).next_to(P, UP + RIGHT, buff=0.12)
        label_Q = MathTex("Q", font_size=28, color=GREEN).next_to(Q, DOWN + RIGHT, buff=0.12)

        self.play(
            GrowFromCenter(dot_P), Write(label_P),
            GrowFromCenter(dot_Q), Write(label_Q),
            run_time=0.8,
        )

        # ── Common chord PQ ──────────────────────────────────
        chord = DashedLine(P, Q, color=GREEN_A, stroke_width=2)
        self.play(Create(chord), run_time=0.8)
        self.wait(0.5)

        # ── Highlight intersection region ─────────────────────
        # Build the lens (vesica piscis) from two arcs
        # Arc on circle-1 side (between P and Q, arc curving right)
        arc1_angle = 2 * np.arcsin(h / r)
        arc1 = Arc(
            radius=r,
            start_angle=PI / 2 - arc1_angle / 2,
            angle=arc1_angle,
            arc_center=center1,
            color=GOLD,
            stroke_width=4,
        )
        # Arc on circle-2 side (between P and Q, arc curving left)
        arc2 = Arc(
            radius=r,
            start_angle=PI / 2 + arc1_angle / 2,
            angle=-arc1_angle,
            arc_center=center1,
            color=GOLD,
            stroke_width=0,
        )
        # We actually need arcs from each circle:
        # From circle2, the inner arc
        arc2 = Arc(
            radius=r,
            start_angle=PI / 2 - arc1_angle / 2 + PI,
            angle=-arc1_angle,
            arc_center=center2,
            color=GOLD,
            stroke_width=4,
        )

        self.play(Create(arc1), Create(arc2), run_time=1)

        # Pulse the intersection arcs
        for _ in range(2):
            self.play(
                arc1.animate.set_stroke(width=7),
                arc2.animate.set_stroke(width=7),
                run_time=0.25,
            )
            self.play(
                arc1.animate.set_stroke(width=4),
                arc2.animate.set_stroke(width=4),
                run_time=0.25,
            )

        # ── Info box at the bottom ────────────────────────────
        info = VGroup(
            Text("Both circles have radius 5 cm", font_size=24, color=WHITE),
            Text("Distance between centres = 6 cm", font_size=24, color=YELLOW),
            Text("They intersect at points P and Q", font_size=24, color=GREEN),
        ).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=0.4)

        self.play(FadeIn(info, shift=UP * 0.3), run_time=1)
        self.wait(2)

        # ── Fade out everything ───────────────────────────────
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.5)
        self.wait(0.5)

        # ══════════════════════════════════════════════════════
        # ── NEW SECTION: Circle → Line → Sine Wave ───────────
        # ══════════════════════════════════════════════════════

        # Re-create both circles
        circle_a = Circle(radius=2.0, color="#4FC3F7", stroke_width=3).move_to(LEFT * 1.2)
        circle_b = Circle(radius=2.0, color="#EF5350", stroke_width=3).move_to(RIGHT * 1.2)
        label_a = Text("Circle 1", font_size=24, color="#4FC3F7").next_to(circle_a, DOWN, buff=0.3)
        label_b = Text("Circle 2", font_size=24, color="#EF5350").next_to(circle_b, DOWN, buff=0.3)

        self.play(
            Create(circle_a), Create(circle_b),
            Write(label_a), Write(label_b),
            run_time=1.5,
        )
        self.wait(1)

        # ── Step 1: Circle 1 disappears ───────────────────────
        disappear_text = Text("Circle 1 disappears...", font_size=30, color="#4FC3F7").to_edge(UP)
        self.play(Write(disappear_text), run_time=0.6)
        self.play(
            FadeOut(circle_a, scale=0.1),
            FadeOut(label_a),
            run_time=1.5,
        )
        self.play(FadeOut(disappear_text), run_time=0.3)
        self.wait(0.4)

        # ── Step 2: Circle 2 transforms into a line ───────────
        transform_text = Text("Circle 2  →  Line", font_size=30, color="#EF5350").to_edge(UP)
        self.play(Write(transform_text), run_time=0.6)
        self.play(circle_b.animate.move_to(ORIGIN), FadeOut(label_b), run_time=0.7)

        h_line = Line(LEFT * 4, RIGHT * 4, color="#EF5350", stroke_width=3)
        self.play(ReplacementTransform(circle_b, h_line), run_time=2)
        self.wait(0.4)
        self.play(FadeOut(transform_text), run_time=0.3)

        # ── Step 3: Line transforms into a sine wave ──────────
        sine_text = Text("Line  →  Sine Wave", font_size=30, color=GOLD).to_edge(UP)
        self.play(Write(sine_text), run_time=0.6)

        sine_wave = ParametricFunction(
            lambda t: np.array([t, np.sin(2 * t), 0]),
            t_range=np.array([-4.0, 4.0, 0.01]),
            color="#EF5350",
            stroke_width=3,
        )

        self.play(ReplacementTransform(h_line, sine_wave), run_time=2.5)
        self.wait(0.5)

        # Travelling gold highlight
        self.play(ShowPassingFlash(
            sine_wave.copy().set_color(GOLD).set_stroke(width=6),
            time_width=0.3,
            run_time=2,
        ))

        # Equation label
        equation = MathTex(r"y = \sin(2x)", font_size=40, color=GOLD)
        equation.next_to(sine_wave, UP, buff=0.4)
        self.play(FadeOut(sine_text), Write(equation), run_time=1)
        self.wait(0.8)

        # Axes fade in for context
        axes = Axes(
            x_range=[-4.5, 4.5, 1],
            y_range=[-1.5, 1.5, 0.5],
            x_length=9,
            y_length=3,
            axis_config={"color": GREY, "stroke_width": 1.5},
            tips=False,
        )
        self.play(Create(axes), run_time=1)
        self.wait(1)

        # ── Final fade out ────────────────────────────────────
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.5)
        self.wait(0.5)
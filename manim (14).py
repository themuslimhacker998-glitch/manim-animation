from manim import *
import numpy as np


class CircleTheoremProof(Scene):
    def construct(self):

        # ── Colours ────────────────────────────────────────────
        CIRCLE_FILL   = "#F5D57A"   # warm yellow
        CIRCLE_STROKE = "#D4A017"   # gold
        SHADE_FILL    = "#5BC8DC"   # light blue (quadrilateral)
        DOT_COLOR     = "#E07B00"   # orange
        LINE_COLOR    = "#D4A017"   # gold
        TEXT_COLOR    = WHITE

        # ── Geometry ───────────────────────────────────────────
        R = 2.3          # circle radius
        angle_A =  210 * DEGREES   # left
        angle_B =  340 * DEGREES   # lower-right
        angle_C =   80 * DEGREES   # top
        angle_D = angle_C - PI     # opposite C through center

        O_pos = LEFT * 1.0         # shift circle left so proof text fits

        def pt(angle):
            return O_pos + R * np.array([np.cos(angle), np.sin(angle), 0])

        A = pt(angle_A)
        B = pt(angle_B)
        C = pt(angle_C)
        D = pt(angle_D)

        # ── Title ──────────────────────────────────────────────
        title = Text(
            "Circle Theorem",
            font_size=36, color=YELLOW, weight=BOLD,
        ).to_edge(UP)
        subtitle = Text(
            "Angle at centre = 2 × Angle at circumference",
            font_size=22, color=YELLOW_B,
        ).next_to(title, DOWN, buff=0.1)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.8)
        self.wait(0.5)

        # ── Step 1 : Draw circle ───────────────────────────────
        circle = Circle(radius=R, color=CIRCLE_STROKE, stroke_width=3)
        circle.set_fill(CIRCLE_FILL, opacity=0.55)
        circle.move_to(O_pos)

        step1 = Text("Step 1: Draw a circle with centre O",
                     font_size=22, color=TEXT_COLOR).to_edge(RIGHT).shift(UP * 2)

        self.play(Create(circle), Write(step1), run_time=1.5)
        self.wait(0.6)

        # ── Step 2 : Mark points A, B, C on circumference ─────
        dot_A = Dot(A, color=DOT_COLOR, radius=0.10)
        dot_B = Dot(B, color=DOT_COLOR, radius=0.10)
        dot_C = Dot(C, color=DOT_COLOR, radius=0.10)
        dot_O = Dot(O_pos, color=DOT_COLOR, radius=0.10)

        lbl_A = Text("A", font_size=26, color=DOT_COLOR).next_to(A, LEFT,  buff=0.12)
        lbl_B = Text("B", font_size=26, color=DOT_COLOR).next_to(B, RIGHT, buff=0.12)
        lbl_C = Text("C", font_size=26, color=DOT_COLOR).next_to(C, UP,    buff=0.12)
        lbl_O = Text("O", font_size=26, color=DOT_COLOR).next_to(O_pos, RIGHT, buff=0.12)

        step2 = Text("Step 2: Mark points A, B on chord\nand C on circumference",
                     font_size=22, color=TEXT_COLOR).to_edge(RIGHT).shift(UP * 2)

        self.play(FadeOut(step1), run_time=0.3)
        self.play(
            GrowFromCenter(dot_A), GrowFromCenter(dot_B),
            GrowFromCenter(dot_C), GrowFromCenter(dot_O),
            Write(lbl_A), Write(lbl_B), Write(lbl_C), Write(lbl_O),
            Write(step2),
            run_time=1.2,
        )
        self.wait(0.6)

        # ── Step 3 : Draw OA, OB, OC, CA, CB (the diagram) ────
        line_OA = Line(O_pos, A, color=LINE_COLOR, stroke_width=2.5)
        line_OB = Line(O_pos, B, color=LINE_COLOR, stroke_width=2.5)
        line_OC = Line(O_pos, C, color=LINE_COLOR, stroke_width=2.5)
        line_CA = Line(C, A, color=LINE_COLOR, stroke_width=2.5)
        line_CB = Line(C, B, color=LINE_COLOR, stroke_width=2.5)
        line_AB = Line(A, B, color=LINE_COLOR, stroke_width=2.5)

        step3 = Text("Step 3: Connect O to A, B, C\nand draw CA, CB, AB",
                     font_size=22, color=TEXT_COLOR).to_edge(RIGHT).shift(UP * 2)

        self.play(FadeOut(step2), run_time=0.3)
        self.play(
            Create(line_OA), Create(line_OB), Create(line_OC),
            Create(line_CA), Create(line_CB), Create(line_AB),
            Write(step3),
            run_time=1.8,
        )
        self.wait(0.6)

        # ── Step 4 : Shade quadrilateral A-C-B-O ──────────────
        shaded = Polygon(A, C, B, O_pos,
                         fill_color=SHADE_FILL, fill_opacity=0.55,
                         stroke_width=0)

        step4 = Text("Step 4: Shade region A-C-B-O\n(two triangles: △OAC and △OBC)",
                     font_size=22, color=TEXT_COLOR).to_edge(RIGHT).shift(UP * 2)

        self.play(FadeOut(step3), run_time=0.3)
        self.play(FadeIn(shaded), Write(step4), run_time=1)
        self.wait(0.6)

        # ── Step 5 : Draw line through O and C → point D ──────
        dot_D   = Dot(D, color=DOT_COLOR, radius=0.10)
        lbl_D   = Text("D", font_size=26, color=DOT_COLOR).next_to(D, DOWN, buff=0.12)
        line_CD = Line(C, D, color=BLUE_B, stroke_width=2.5)

        step5 = Text("Step 5: Extend CO to meet\ncircle again at D",
                     font_size=22, color=TEXT_COLOR).to_edge(RIGHT).shift(UP * 2)

        self.play(FadeOut(step4), run_time=0.3)
        self.play(
            Create(line_CD),
            GrowFromCenter(dot_D), Write(lbl_D),
            Write(step5),
            run_time=1.5,
        )
        self.wait(0.6)

        # ── Step 6 : Angle arcs ────────────────────────────────
        # Angle ACB at C — between CA and CB vectors
        v_CA = A - C;  v_CB = B - C
        a1 = np.arctan2(v_CA[1], v_CA[0])
        a2 = np.arctan2(v_CB[1], v_CB[0])
        if a2 < a1:
            a2 += TAU
        arc_C = Arc(radius=0.3, start_angle=a1, angle=a2 - a1,
                    arc_center=C, color=GREEN, stroke_width=2.5)

        # Angle AOB at O — between OA and OB vectors
        v_OA = A - O_pos;  v_OB = B - O_pos
        b1 = np.arctan2(v_OA[1], v_OA[0])
        b2 = np.arctan2(v_OB[1], v_OB[0])
        if b2 < b1:
            b2 += TAU
        arc_O = Arc(radius=0.3, start_angle=b1, angle=b2 - b1,
                    arc_center=O_pos, color=ORANGE, stroke_width=2.5)

        step6 = Text("Step 6: Mark ∠ACB (green)\nand ∠AOB (orange)",
                     font_size=22, color=TEXT_COLOR).to_edge(RIGHT).shift(UP * 2)

        self.play(FadeOut(step5), run_time=0.3)
        self.play(Create(arc_C), Create(arc_O), Write(step6), run_time=1.2)
        self.wait(0.8)

        # ── Step 7 : Proof text ────────────────────────────────
        proof_lines = VGroup(
            Text("Proof:", font_size=22, color=YELLOW, weight=BOLD),
            Text("OA = OC = OB  (radii)", font_size=19, color=WHITE),
            Text("∠OAC = ∠OCA  (△OAC isosceles)", font_size=19, color=WHITE),
            Text("∠OBC = ∠OCB  (△OBC isosceles)", font_size=19, color=WHITE),
            Text("Exterior angle theorem:", font_size=19, color=WHITE),
            Text("∠AOD = 2 × ∠ACO  … (1)", font_size=19, color=TEAL_B),
            Text("∠DOB = 2 × ∠OCB  … (2)", font_size=19, color=TEAL_B),
            Text("(1)+(2):", font_size=19, color=WHITE),
            Text("∠AOB = 2 × ∠ACB  ✓", font_size=20, color=GREEN, weight=BOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        proof_lines.to_edge(RIGHT).to_edge(DOWN, buff=0.25)

        self.play(FadeOut(step6), run_time=0.3)
        for line in proof_lines:
            self.play(Write(line), run_time=0.6)
        self.wait(1.5)

        # ── Step 8 : Highlight the final result ───────────────
        box = SurroundingRectangle(proof_lines[-1], color=GOLD, buff=0.12)
        self.play(Create(box), run_time=0.8)
        self.play(
            proof_lines[-1].animate.set_color(GOLD),
            run_time=0.5,
        )
        self.wait(2)

        # ── Fade out ───────────────────────────────────────────
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.5)
        self.wait(0.5)

from manim import *

BF = "Shonar Bangla"

def left_panel_title():
    return Text("Previous Results:", font=BF, color=GRAY_B).scale(0.38).to_corner(UL, buff=0.22)

class IntegralSolution(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        left_results = VGroup()
        panel_refs = []

        def add_to_left(mob, panel_refs, left_results):
            mob_copy = mob.copy()
            mob_copy.set_color(GRAY_A)
            if len(panel_refs) == 0:
                mob_copy.scale(0.58).next_to(
                    left_panel_title(), DOWN, buff=0.22, aligned_edge=LEFT
                )
            else:
                mob_copy.scale(0.58).next_to(
                    panel_refs[-1], DOWN, buff=0.18, aligned_edge=LEFT
                )
            mob_copy.align_to(left_panel_title(), LEFT)
            panel_refs.append(mob_copy)
            left_results.add(mob_copy)
            return mob_copy

        title = left_panel_title()

        i1_q = MathTex(
            r"I_1 = \int \frac{\cos x}{\cos x + \sin x}\,dx",
            color=BLUE_B
        ).scale(0.82)
        i2_q = MathTex(
            r"I_2 = \int \frac{\sin x}{\cos x + \sin x}\,dx",
            color=RED_B
        ).scale(0.82)
        question = VGroup(i1_q, i2_q).arrange(DOWN, buff=0.55).move_to(ORIGIN)
        self.play(Write(i1_q), run_time=1.4)
        self.play(Write(i2_q), run_time=1.4)
        self.wait(1)
        self.play(question.animate.shift(UP * 2), run_time=1)

        bq = Text(
            "সবচেয়ে সহজে কিভাবে solve করবো?",
            font=BF, color=YELLOW
        ).scale(0.65).move_to(ORIGIN)
        self.play(FadeIn(bq, shift=UP * 0.3), run_time=1)
        self.wait(2)
        self.play(FadeOut(bq), FadeOut(question), run_time=0.8)
        self.wait(0.3)

        dhari = Text("ধরি,", font=BF, color=BLUE_B).scale(0.68)
        i1_def = MathTex(
            r"I_1 = \int \frac{\cos x}{\cos x + \sin x}\,dx",
            color=BLUE_B
        ).scale(0.82)
        i2_def = MathTex(
            r"I_2 = \int \frac{\sin x}{\cos x + \sin x}\,dx",
            color=RED_B
        ).scale(0.82)
        defs = VGroup(dhari, i1_def, i2_def).arrange(DOWN, buff=0.42).move_to(ORIGIN)
        self.play(Write(dhari), run_time=0.7)
        self.play(Write(i1_def), run_time=1)
        self.play(Write(i2_def), run_time=1)
        self.wait(1.5)

        r1 = add_to_left(i1_def, panel_refs, left_results)
        r2 = add_to_left(i2_def, panel_refs, left_results)
        self.play(
            FadeOut(defs), run_time=0.8
        )
        self.play(FadeIn(title), FadeIn(r1), FadeIn(r2), run_time=0.7)
        self.wait(0.3)

        add_text = Text(
            "এখন দুইটা যদি যোগ করি",
            font=BF, color=GREEN_B
        ).scale(0.62).to_edge(UP, buff=0.5)
        self.play(FadeIn(add_text, shift=UP * 0.2), run_time=0.8)
        self.wait(0.5)

        work_area = RIGHT * 1.5

        a0 = MathTex(r"I_1 + I_2", color=YELLOW).scale(0.85)
        a0.move_to(work_area + UP * 2.2)
        self.play(Write(a0), run_time=0.8)
        self.wait(0.4)

        a1 = MathTex(
            r"= \int \frac{\cos x}{\cos x+\sin x}\,dx",
            r"+ \int \frac{\sin x}{\cos x+\sin x}\,dx",
            color=WHITE
        ).scale(0.78)
        a1.next_to(a0, DOWN, buff=0.38)
        self.play(Write(a1[0]), run_time=1)
        self.play(Write(a1[1]), run_time=1)
        self.wait(0.6)

        a2 = MathTex(
            r"= \int \frac{\cos x + \sin x}{\cos x + \sin x}\,dx",
            color=WHITE
        ).scale(0.82)
        a2.next_to(a1, DOWN, buff=0.38)
        self.play(Write(a2), run_time=1)
        brace_note = Text("(numerator = denominator)", color=GRAY_A, font=BF).scale(0.35)
        brace_note.next_to(a2, RIGHT, buff=0.2)
        self.play(FadeIn(brace_note), run_time=0.5)
        self.wait(0.5)

        a3 = MathTex(r"= \int 1\,dx", color=WHITE).scale(0.85)
        a3.next_to(a2, DOWN, buff=0.38)
        self.play(Write(a3), run_time=0.8)
        self.wait(0.4)

        a4 = MathTex(r"= x + C", color=GREEN).scale(0.9)
        a4.next_to(a3, DOWN, buff=0.38)
        self.play(Write(a4), run_time=0.8)

        lbl1 = MathTex(r"\cdots (1)", color=YELLOW).scale(0.75)
        lbl1.next_to(a4, RIGHT, buff=0.3)
        self.play(Write(lbl1), run_time=0.5)
        self.play(Indicate(a4, color=GREEN, scale_factor=1.12), run_time=0.8)
        self.wait(1.5)

        result1_tex = MathTex(
            r"I_1+I_2=x+C \quad (1)",
            color=GREEN
        )
        r3 = add_to_left(result1_tex, panel_refs, left_results)

        add_group = VGroup(add_text, a0, a1, a2, brace_note, a3, a4, lbl1)
        self.play(FadeOut(add_group), run_time=0.8)
        self.play(FadeIn(r3), run_time=0.6)
        self.wait(0.3)

        sub_text = Text(
            "এখন বিয়োগ করি",
            font=BF, color=RED_B
        ).scale(0.62).to_edge(UP, buff=0.5)
        self.play(FadeIn(sub_text, shift=UP * 0.2), run_time=0.8)
        self.wait(0.5)

        b0 = MathTex(r"I_1 - I_2", color=YELLOW).scale(0.85)
        b0.move_to(work_area + UP * 2.5)
        self.play(Write(b0), run_time=0.8)
        self.wait(0.4)

        b1 = MathTex(
            r"= \int \frac{\cos x}{\cos x+\sin x}\,dx",
            r"- \int \frac{\sin x}{\cos x+\sin x}\,dx",
            color=WHITE
        ).scale(0.78)
        b1.next_to(b0, DOWN, buff=0.35)
        self.play(Write(b1[0]), run_time=1)
        self.play(Write(b1[1]), run_time=1)
        self.wait(0.5)

        b2 = MathTex(
            r"= \int \frac{\cos x - \sin x}{\cos x + \sin x}\,dx",
            color=WHITE
        ).scale(0.82)
        b2.next_to(b1, DOWN, buff=0.35)
        self.play(Write(b2), run_time=1)
        self.wait(0.8)

        self.play(FadeOut(b0), FadeOut(b1), run_time=0.6)
        b2_moved = b2.copy().move_to(work_area + UP * 2.5)
        self.play(Transform(b2, b2_moved), run_time=0.7)
        self.wait(0.3)

        sub_header = Text("Substitution:", font=BF, color=BLUE_C).scale(0.5)
        sub_header.next_to(b2, DOWN, buff=0.4)
        self.play(FadeIn(sub_header), run_time=0.5)

        u_eq = MathTex(
            r"u = \cos x + \sin x",
            color=BLUE_C
        ).scale(0.8)
        u_eq.next_to(sub_header, DOWN, buff=0.22)
        self.play(Write(u_eq), run_time=0.9)
        self.wait(0.3)

        du_deriv = MathTex(
            r"\frac{du}{dx} = -\sin x + \cos x = \cos x - \sin x",
            color=BLUE_C
        ).scale(0.73)
        du_deriv.next_to(u_eq, DOWN, buff=0.22)
        self.play(Write(du_deriv), run_time=1.1)
        self.wait(0.3)

        du_eq = MathTex(
            r"du = (\cos x - \sin x)\,dx",
            color=BLUE_C
        ).scale(0.8)
        du_eq.next_to(du_deriv, DOWN, buff=0.22)
        self.play(Write(du_eq), run_time=0.9)
        self.wait(0.6)

        self.play(FadeOut(b2), FadeOut(sub_header), run_time=0.6)

        subst_summary = MathTex(
            r"u=\cos x+\sin x,\quad du=(\cos x-\sin x)\,dx",
            color=BLUE_C
        ).scale(0.72)
        subst_summary.move_to(work_area + UP * 2.5)
        self.play(
            ReplacementTransform(VGroup(u_eq, du_deriv, du_eq), subst_summary),
            run_time=0.9
        )
        self.wait(0.4)

        b3 = MathTex(r"I_1 - I_2 = \int \frac{du}{u}", color=WHITE).scale(0.85)
        b3.next_to(subst_summary, DOWN, buff=0.45)
        self.play(Write(b3), run_time=0.8)
        self.wait(0.4)

        b4 = MathTex(r"= \ln|u| + C", color=WHITE).scale(0.85)
        b4.next_to(b3, DOWN, buff=0.38)
        self.play(Write(b4), run_time=0.8)
        self.wait(0.4)

        b5 = MathTex(
            r"= \ln|\cos x + \sin x| + C",
            color=GREEN
        ).scale(0.88)
        b5.next_to(b4, DOWN, buff=0.38)
        self.play(Write(b5), run_time=1)

        lbl2 = MathTex(r"\cdots (2)", color=YELLOW).scale(0.75)
        lbl2.next_to(b5, RIGHT, buff=0.3)
        self.play(Write(lbl2), run_time=0.5)
        self.play(Indicate(b5, color=GREEN, scale_factor=1.12), run_time=0.8)
        self.wait(1.5)

        result2_tex = MathTex(
            r"I_1-I_2=\ln|\cos x+\sin x|+C \quad (2)",
            color=GREEN
        )
        r4 = add_to_left(result2_tex, panel_refs, left_results)

        sub_group = VGroup(
            sub_text, subst_summary,
            b3, b4, b5, lbl2
        )
        self.play(FadeOut(sub_group), run_time=0.8)
        self.play(FadeIn(r4), run_time=0.6)
        self.wait(0.3)

        eq_note = Text(
            "(1) + (2) করলে I₁ পাই",
            font=BF, color=YELLOW
        ).scale(0.62).to_edge(UP, buff=0.5)
        self.play(FadeIn(eq_note), run_time=0.8)
        self.wait(0.5)

        c1_label = MathTex(r"(1):", color=YELLOW).scale(0.78)
        c1_eq = MathTex(r"I_1+I_2 = x+C", color=WHITE).scale(0.78)
        c1_row = VGroup(c1_label, c1_eq).arrange(RIGHT, buff=0.25)

        c2_label = MathTex(r"(2):", color=YELLOW).scale(0.78)
        c2_eq = MathTex(
            r"I_1-I_2 = \ln|\cos x+\sin x|+C", color=WHITE
        ).scale(0.78)
        c2_row = VGroup(c2_label, c2_eq).arrange(RIGHT, buff=0.25)

        c_rows = VGroup(c1_row, c2_row).arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        c_rows.move_to(work_area + UP * 0.5)
        self.play(FadeIn(c1_row), run_time=0.7)
        self.play(FadeIn(c2_row), run_time=0.7)
        self.wait(0.5)

        plus_sign = MathTex(r"+", color=GREEN_B).scale(0.85)
        plus_sign.next_to(c_rows, DOWN, buff=0.3).align_to(c_rows, LEFT).shift(RIGHT * 0.3)
        hline = Line(
            c_rows.get_left(), c_rows.get_right(), color=WHITE, stroke_width=1.5
        ).next_to(c_rows, DOWN, buff=0.18)
        self.play(Write(plus_sign), Create(hline), run_time=0.6)
        self.wait(0.3)

        i1_add = MathTex(r"2I_1 = x + \ln|\cos x + \sin x| + 2C", color=WHITE).scale(0.8)
        i1_add.next_to(hline, DOWN, buff=0.35)
        self.play(Write(i1_add), run_time=1.1)
        self.wait(0.5)

        absorb = Text(
            "(constant এ মিলে যায়, C = C১ লিখি)",
            font=BF, color=GRAY_A
        ).scale(0.38)
        absorb.next_to(i1_add, DOWN, buff=0.18)
        self.play(FadeIn(absorb), run_time=0.5)
        self.wait(0.5)

        i1_clean = MathTex(r"2I_1 = x + \ln|\cos x + \sin x|", color=WHITE).scale(0.85)
        i1_clean.next_to(absorb, DOWN, buff=0.28)
        self.play(Write(i1_clean), run_time=1)
        self.wait(0.4)

        i1_final = MathTex(
            r"I_1 = \frac{x + \ln|\cos x + \sin x|}{2}",
            color=TEAL
        ).scale(0.9)
        i1_final.next_to(i1_clean, DOWN, buff=0.35)
        self.play(TransformMatchingShapes(i1_clean.copy(), i1_final), run_time=1.2)

        box1 = SurroundingRectangle(i1_final, color=TEAL, buff=0.18)
        self.play(Create(box1), run_time=0.6)
        self.play(Indicate(i1_final, color=TEAL, scale_factor=1.1), run_time=0.8)
        self.wait(1.5)

        r5 = add_to_left(i1_final, panel_refs, left_results)
        step5_group = VGroup(eq_note, c_rows, plus_sign, hline, i1_add, absorb, i1_clean, i1_final, box1)
        self.play(FadeOut(step5_group), run_time=0.8)
        self.play(FadeIn(r5), run_time=0.6)
        self.wait(0.3)

        i2_text = Text(
            "এখন I₂ বের করি",
            font=BF, color=ORANGE
        ).scale(0.62).to_edge(UP, buff=0.5)
        self.play(FadeIn(i2_text, shift=UP * 0.2), run_time=0.8)
        self.wait(0.5)

        d1_label = MathTex(r"(1):", color=YELLOW).scale(0.78)
        d1_eq = MathTex(r"I_1+I_2 = x+C", color=WHITE).scale(0.78)
        d1_row = VGroup(d1_label, d1_eq).arrange(RIGHT, buff=0.25)

        d2_label = MathTex(r"(2):", color=YELLOW).scale(0.78)
        d2_eq = MathTex(
            r"I_1-I_2 = \ln|\cos x+\sin x|+C", color=WHITE
        ).scale(0.78)
        d2_row = VGroup(d2_label, d2_eq).arrange(RIGHT, buff=0.25)

        d_rows = VGroup(d1_row, d2_row).arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        d_rows.move_to(work_area + UP * 1.2)
        self.play(FadeIn(d1_row), run_time=0.7)
        self.play(FadeIn(d2_row), run_time=0.7)
        self.wait(0.5)

        minus_sign = MathTex(r"-", color=RED_B).scale(0.85)
        minus_sign.next_to(d_rows, DOWN, buff=0.3).align_to(d_rows, LEFT).shift(RIGHT * 0.3)
        hline2 = Line(
            d_rows.get_left(), d_rows.get_right(), color=WHITE, stroke_width=1.5
        ).next_to(d_rows, DOWN, buff=0.18)
        self.play(Write(minus_sign), Create(hline2), run_time=0.6)
        self.wait(0.3)

        i2_calc = MathTex(
            r"2I_2 = x - \ln|\cos x + \sin x|", color=WHITE
        ).scale(0.85)
        i2_calc.next_to(hline2, DOWN, buff=0.38)
        self.play(Write(i2_calc), run_time=1.1)
        self.wait(0.5)

        i2_final = MathTex(
            r"I_2 = \frac{x - \ln|\cos x + \sin x|}{2}",
            color=PINK
        ).scale(0.9)
        i2_final.next_to(i2_calc, DOWN, buff=0.38)
        self.play(TransformMatchingShapes(i2_calc.copy(), i2_final), run_time=1.2)

        box2 = SurroundingRectangle(i2_final, color=PINK, buff=0.18)
        self.play(Create(box2), run_time=0.6)
        self.play(Indicate(i2_final, color=PINK, scale_factor=1.1), run_time=0.8)
        self.wait(1.5)

        step6_group = VGroup(i2_text, d_rows, minus_sign, hline2, i2_calc, i2_final, box2)
        self.play(FadeOut(step6_group), FadeOut(title), FadeOut(left_results), run_time=0.8)
        self.wait(0.3)

        final_i1 = MathTex(
            r"I_1 = \frac{x + \ln|\cos x + \sin x|}{2}",
            color=TEAL
        ).scale(0.88)
        final_i2 = MathTex(
            r"I_2 = \frac{x - \ln|\cos x + \sin x|}{2}",
            color=PINK
        ).scale(0.88)
        final_group = VGroup(final_i1, final_i2).arrange(DOWN, buff=0.75).move_to(ORIGIN)
        self.play(FadeIn(final_group, shift=UP * 0.3), run_time=1)

        fb1 = SurroundingRectangle(final_i1, color=TEAL, buff=0.2)
        fb2 = SurroundingRectangle(final_i2, color=PINK, buff=0.2)
        self.play(Create(fb1), Create(fb2), run_time=0.8)
        self.play(
            Indicate(final_i1, color=TEAL, scale_factor=1.08),
            Indicate(final_i2, color=PINK, scale_factor=1.08),
            run_time=1
        )
        self.wait(3)
        self.play(FadeOut(VGroup(final_group, fb1, fb2)), run_time=1)
        self.wait(0.4)

        gen_title = Text(
            "এখন সাধারণ রূপ দেখি",
            font=BF, color=GOLD
        ).scale(0.7).move_to(ORIGIN)
        self.play(FadeIn(gen_title, shift=UP * 0.3), run_time=1)
        self.wait(1.5)
        self.play(FadeOut(gen_title), run_time=0.7)
        self.wait(0.3)

        g_i3 = MathTex(
            r"I_3 = \int \frac{\cos x}{a\cos x + b\sin x}\,dx",
            color=BLUE_B
        ).scale(0.82)
        g_i4 = MathTex(
            r"I_4 = \int \frac{\sin x}{a\cos x + b\sin x}\,dx",
            color=RED_B
        ).scale(0.82)
        g_defs = VGroup(g_i3, g_i4).arrange(DOWN, buff=0.5).move_to(ORIGIN)
        self.play(Write(g_i3), run_time=1.2)
        self.play(Write(g_i4), run_time=1.2)
        self.wait(1)
        self.play(g_defs.animate.to_edge(UP, buff=0.5), run_time=0.9)
        self.wait(0.3)

        gen_add_text = Text(
            "এখন  aI₃ + bI₄  যোগ করি",
            font=BF, color=GREEN_B
        ).scale(0.6).next_to(g_defs, DOWN, buff=0.35)
        self.play(FadeIn(gen_add_text), run_time=0.7)
        self.wait(0.4)

        ga0 = MathTex(r"aI_3 + bI_4", color=YELLOW).scale(0.88)
        ga0.next_to(gen_add_text, DOWN, buff=0.38)
        self.play(Write(ga0), run_time=0.8)
        self.wait(0.3)

        ga1 = MathTex(
            r"= \int \frac{a\cos x}{a\cos x+b\sin x}\,dx"
            r"+ \int \frac{b\sin x}{a\cos x+b\sin x}\,dx",
            color=WHITE
        ).scale(0.75)
        ga1.next_to(ga0, DOWN, buff=0.35)
        self.play(Write(ga1), run_time=1.2)
        self.wait(0.5)

        ga2 = MathTex(
            r"= \int \frac{a\cos x + b\sin x}{a\cos x + b\sin x}\,dx",
            color=WHITE
        ).scale(0.8)
        ga2.next_to(ga1, DOWN, buff=0.32)
        self.play(Write(ga2), run_time=1)
        self.wait(0.4)

        ga3 = MathTex(r"= \int 1\,dx", color=WHITE).scale(0.85)
        ga3.next_to(ga2, DOWN, buff=0.32)
        self.play(Write(ga3), run_time=0.7)
        self.wait(0.3)

        ga4 = MathTex(r"= x + C", color=GREEN).scale(0.9)
        ga4.next_to(ga3, DOWN, buff=0.32)
        self.play(Write(ga4), run_time=0.7)

        glbl_A = MathTex(r"\cdots (A)", color=YELLOW).scale(0.75)
        glbl_A.next_to(ga4, RIGHT, buff=0.3)
        self.play(Write(glbl_A), run_time=0.5)
        self.play(Indicate(ga4, color=GREEN, scale_factor=1.1), run_time=0.7)
        self.wait(1.5)

        gresA = MathTex(r"aI_3+bI_4=x+C \;\; (A)", color=GREEN)
        gresA_panel = gresA.copy().set_color(GRAY_A).scale(0.52).to_corner(UL, buff=0.25)

        gen_add_group = VGroup(g_defs, gen_add_text, ga0, ga1, ga2, ga3, ga4, glbl_A)
        self.play(FadeOut(gen_add_group), run_time=0.8)
        self.play(FadeIn(gresA_panel), run_time=0.6)
        self.wait(0.3)

        g_i3b = MathTex(
            r"I_3 = \int \frac{\cos x}{a\cos x + b\sin x}\,dx",
            color=BLUE_B
        ).scale(0.78)
        g_i4b = MathTex(
            r"I_4 = \int \frac{\sin x}{a\cos x + b\sin x}\,dx",
            color=RED_B
        ).scale(0.78)
        g_defsb = VGroup(g_i3b, g_i4b).arrange(DOWN, buff=0.4).to_edge(UP, buff=0.5)
        self.play(Write(g_i3b), Write(g_i4b), run_time=1)
        self.wait(0.3)

        gen_sub_text = Text(
            "এখন  bI₃ − aI₄  বিয়োগ করি",
            font=BF, color=RED_B
        ).scale(0.6).next_to(g_defsb, DOWN, buff=0.35)
        self.play(FadeIn(gen_sub_text), run_time=0.7)
        self.wait(0.4)

        gb0 = MathTex(r"bI_3 - aI_4", color=YELLOW).scale(0.88)
        gb0.next_to(gen_sub_text, DOWN, buff=0.38)
        self.play(Write(gb0), run_time=0.8)
        self.wait(0.3)

        gb1 = MathTex(
            r"= \int \frac{b\cos x - a\sin x}{a\cos x + b\sin x}\,dx",
            color=WHITE
        ).scale(0.8)
        gb1.next_to(gb0, DOWN, buff=0.35)
        self.play(Write(gb1), run_time=1.1)
        self.wait(0.6)

        self.play(FadeOut(g_defsb), FadeOut(gen_sub_text), FadeOut(gb0), run_time=0.6)
        gb1_moved = gb1.copy().to_edge(UP, buff=0.6)
        self.play(Transform(gb1, gb1_moved), run_time=0.7)
        self.wait(0.3)

        gsub_hdr = Text("Substitution:", font=BF, color=BLUE_C).scale(0.5)
        gsub_hdr.next_to(gb1, DOWN, buff=0.4)
        self.play(FadeIn(gsub_hdr), run_time=0.4)

        gu = MathTex(r"u = a\cos x + b\sin x", color=BLUE_C).scale(0.8)
        gu.next_to(gsub_hdr, DOWN, buff=0.22)
        self.play(Write(gu), run_time=0.9)

        gdu_deriv = MathTex(
            r"\frac{du}{dx} = -a\sin x + b\cos x = b\cos x - a\sin x",
            color=BLUE_C
        ).scale(0.73)
        gdu_deriv.next_to(gu, DOWN, buff=0.22)
        self.play(Write(gdu_deriv), run_time=1.1)
        self.wait(0.3)

        gdu = MathTex(r"du = (b\cos x - a\sin x)\,dx", color=BLUE_C).scale(0.8)
        gdu.next_to(gdu_deriv, DOWN, buff=0.22)
        self.play(Write(gdu), run_time=0.9)
        self.wait(0.6)

        self.play(FadeOut(gb1), FadeOut(gsub_hdr), run_time=0.6)

        gsubst_sum = MathTex(
            r"u=a\cos x+b\sin x,\quad du=(b\cos x-a\sin x)\,dx",
            color=BLUE_C
        ).scale(0.7)
        gsubst_sum.to_edge(UP, buff=0.6)
        self.play(ReplacementTransform(VGroup(gu, gdu_deriv, gdu), gsubst_sum), run_time=0.9)
        self.wait(0.4)

        gb2 = MathTex(r"bI_3 - aI_4 = \int \frac{du}{u}", color=WHITE).scale(0.85)
        gb2.next_to(gsubst_sum, DOWN, buff=0.45)
        self.play(Write(gb2), run_time=0.8)
        self.wait(0.3)

        gb3 = MathTex(r"= \ln|u| + C", color=WHITE).scale(0.85)
        gb3.next_to(gb2, DOWN, buff=0.38)
        self.play(Write(gb3), run_time=0.7)
        self.wait(0.3)

        gb4 = MathTex(
            r"= \ln|a\cos x + b\sin x| + C",
            color=GREEN
        ).scale(0.88)
        gb4.next_to(gb3, DOWN, buff=0.38)
        self.play(Write(gb4), run_time=1)

        glbl_B = MathTex(r"\cdots (B)", color=YELLOW).scale(0.75)
        glbl_B.next_to(gb4, RIGHT, buff=0.3)
        self.play(Write(glbl_B), run_time=0.5)
        self.play(Indicate(gb4, color=GREEN, scale_factor=1.1), run_time=0.7)
        self.wait(1.5)

        gresB_panel = MathTex(
            r"bI_3-aI_4=\ln|a\cos x+b\sin x|+C \;\; (B)",
            color=GRAY_A
        ).scale(0.52).next_to(gresA_panel, DOWN, buff=0.22, aligned_edge=LEFT)

        gen_sub_group = VGroup(gsubst_sum, gb2, gb3, gb4, glbl_B)
        self.play(FadeOut(gen_sub_group), run_time=0.8)
        self.play(FadeIn(gresB_panel), run_time=0.6)
        self.wait(0.3)

        solve_title = Text(
            "I₃ ও I₄ বের করি",
            font=BF, color=GOLD
        ).scale(0.62).to_edge(UP, buff=0.55)
        self.play(FadeIn(solve_title), run_time=0.7)
        self.wait(0.4)

        eq_A = MathTex(r"(A):\; aI_3 + bI_4 = x + C", color=YELLOW).scale(0.78)
        eq_B = MathTex(
            r"(B):\; bI_3 - aI_4 = \ln|a\cos x+b\sin x| + C",
            color=YELLOW
        ).scale(0.78)
        eq_sys = VGroup(eq_A, eq_B).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        eq_sys.next_to(solve_title, DOWN, buff=0.45)
        self.play(FadeIn(eq_A), run_time=0.7)
        self.play(FadeIn(eq_B), run_time=0.7)
        self.wait(0.5)

        solve_note = Text(
            "a×(A) + b×(B)  →  I₃",
            font=BF, color=GRAY_A
        ).scale(0.5).next_to(eq_sys, DOWN, buff=0.35)
        self.play(FadeIn(solve_note), run_time=0.5)
        self.wait(0.3)

        i3_step = MathTex(
            r"(a^2+b^2)\,I_3 = a\,x + b\ln|a\cos x+b\sin x|",
            color=WHITE
        ).scale(0.78)
        i3_step.next_to(solve_note, DOWN, buff=0.35)
        self.play(Write(i3_step), run_time=1.2)
        self.wait(0.5)

        gi3_final = MathTex(
            r"I_3 = \frac{a\,x + b\ln|a\cos x+b\sin x|}{a^2+b^2}",
            color=TEAL
        ).scale(0.85)
        gi3_final.next_to(i3_step, DOWN, buff=0.38)
        self.play(TransformMatchingShapes(i3_step.copy(), gi3_final), run_time=1.2)
        gbox3 = SurroundingRectangle(gi3_final, color=TEAL, buff=0.18)
        self.play(Create(gbox3), run_time=0.5)
        self.play(Indicate(gi3_final, color=TEAL, scale_factor=1.08), run_time=0.7)
        self.wait(1.2)

        solve_note2 = Text(
            "b×(A) − a×(B)  →  I₄",
            font=BF, color=GRAY_A
        ).scale(0.5)

        i4_step = MathTex(
            r"(a^2+b^2)\,I_4 = b\,x - a\ln|a\cos x+b\sin x|",
            color=WHITE
        ).scale(0.78)

        gi4_final = MathTex(
            r"I_4 = \frac{b\,x - a\ln|a\cos x+b\sin x|}{a^2+b^2}",
            color=PINK
        ).scale(0.85)

        self.play(
            FadeOut(VGroup(solve_title, eq_sys, solve_note, i3_step, gi3_final, gbox3)),
            run_time=0.8
        )
        self.wait(0.2)

        solve_title2 = Text(
            "I₄ বের করি",
            font=BF, color=GOLD
        ).scale(0.62).to_edge(UP, buff=0.55)
        self.play(FadeIn(solve_title2), run_time=0.6)

        solve_note2.next_to(solve_title2, DOWN, buff=0.4)
        self.play(FadeIn(solve_note2), run_time=0.5)
        self.wait(0.3)

        i4_step.next_to(solve_note2, DOWN, buff=0.38)
        self.play(Write(i4_step), run_time=1.2)
        self.wait(0.5)

        gi4_final.next_to(i4_step, DOWN, buff=0.38)
        self.play(TransformMatchingShapes(i4_step.copy(), gi4_final), run_time=1.2)
        gbox4 = SurroundingRectangle(gi4_final, color=PINK, buff=0.18)
        self.play(Create(gbox4), run_time=0.5)
        self.play(Indicate(gi4_final, color=PINK, scale_factor=1.08), run_time=0.7)
        self.wait(1.2)

        self.play(
            FadeOut(VGroup(solve_title2, solve_note2, i4_step, gi4_final, gbox4,
                           gresA_panel, gresB_panel)),
            run_time=0.8
        )
        self.wait(0.4)

        final_gi3 = MathTex(
            r"I_3 = \frac{a\,x + b\ln|a\cos x+b\sin x|}{a^2+b^2}",
            color=TEAL
        ).scale(0.82)
        final_gi4 = MathTex(
            r"I_4 = \frac{b\,x - a\ln|a\cos x+b\sin x|}{a^2+b^2}",
            color=PINK
        ).scale(0.82)
        final_gen = VGroup(final_gi3, final_gi4).arrange(DOWN, buff=0.75).move_to(ORIGIN)
        self.play(FadeIn(final_gen, shift=UP * 0.3), run_time=1)

        fgb1 = SurroundingRectangle(final_gi3, color=TEAL, buff=0.2)
        fgb2 = SurroundingRectangle(final_gi4, color=PINK, buff=0.2)
        self.play(Create(fgb1), Create(fgb2), run_time=0.8)
        self.play(
            Indicate(final_gi3, color=TEAL, scale_factor=1.07),
            Indicate(final_gi4, color=PINK, scale_factor=1.07),
            run_time=1
        )
        self.wait(3.5)
        self.play(FadeOut(VGroup(final_gen, fgb1, fgb2)), run_time=1)

from manim import *

class OlympiadInequality(Scene):
    def construct(self):
        # ==========================================
        # Part 1: Introduction - The Problem
        # ==========================================
        
        # Title
        title = Text("Olympiad Algebra Problem", font_size=48)
        title.to_edge(UP)
        title.set_color(BLUE_C)
        
        self.play(Write(title), run_time=1)
        self.wait(0.5)

        # Constraint
        constraint = MathTex("a, b, c > 0", "\\quad", "a+b+c = 3")
        constraint.next_to(title, DOWN, buff=0.8)
        
        self.play(FadeIn(constraint), run_time=1)
        self.wait(0.5)

        # The Inequality to prove
        statement = MathTex(
            "\\frac{1}{a+b} + \\frac{1}{b+c} + \\frac{1}{c+a}", 
            "\\ge", 
            "\\frac{3}{2}"
        )
        statement.set_color(YELLOW)
        statement.next_to(constraint, DOWN, buff=0.8)
        
        # Boxing the problem
        problem_box = SurroundingRectangle(
            VGroup(constraint, statement), 
            color=WHITE, buff=0.3
        )
        
        self.play(Write(statement), Create(problem_box), run_time=1.5)
        self.wait(1)

        # ==========================================
        # Part 2: The Insight (AM-HM)
        # ==========================================
        
        # Clear the screen elegantly
        self.play(
            FadeOut(title),
            FadeOut(constraint),
            FadeOut(problem_box),
            statement.animate.to_edge(UP) # Move target to top
        )
        
        # Introduce the tool
        tool_text = Text("Key Insight: AM-HM Inequality", font_size=36)
        tool_text.set_color(TEAL)
        tool_text.next_to(statement, DOWN, buff=1)
        
        self.play(FadeIn(tool_text, shift=UP), run_time=0.8)
        
        # AM-HM Formula
        am_hm = MathTex(
            "\\frac{x+y+z}{3}", "\\ge", 
            "\\frac{3}{\\frac{1}{x}+\\frac{1}{y}+\\frac{1}{z}}"
        )
        am_hm.set_color(WHITE)
        am_hm.next_to(tool_text, DOWN, buff=0.5)
        
        self.play(Write(am_hm), run_time=2)
        self.wait(1)
        
        # Fade out tool to start calculation
        self.play(FadeOut(tool_text), FadeOut(am_hm))

        # ==========================================
        # Part 3: The Denominator Trick
        # ==========================================
        
        step1_text = Text("Step 1: Analyze the Denominators", font_size=32)
        step1_text.set_color(GREEN)
        step1_text.next_to(statement, DOWN, buff=0.8)
        self.play(FadeIn(step1_text))

        # Visual calculation of sum of denominators
        # We show: (a+b) + (b+c) + (c+a)
        denom_sum = MathTex(
            "(a+b)", "+", "(b+c)", "+", "(c+a)"
        )
        denom_sum.next_to(step1_text, DOWN, buff=0.5)
        
        # Group them: = 2a + 2b + 2c
        simplified = MathTex("=", "2a", "+", "2b", "+", "2c")
        simplified.next_to(denom_sum, DOWN)
        
        # Factor: = 2(a+b+c)
        factored = MathTex("=", "2", "(a+b+c)")
        factored.next_to(simplified, DOWN)
        
        # Final substitution: = 2(3) = 6
        final_calc = MathTex("=", "6")
        final_calc.set_color(YELLOW)
        final_calc.next_to(factored, DOWN)

        # Animation sequence
        self.play(Write(denom_sum), run_time=1)
        self.wait(0.3)
        
        self.play(Write(simplified), run_time=1)
        self.wait(0.3)
        
        self.play(Write(factored), run_time=1)
        self.wait(0.3)
        
        self.play(
            TransformMatchingTex(
                factored.copy(), 
                final_calc,
                path_arc=PI/2
            ),
            run_time=1
        )
        self.wait(1)

        # ==========================================
        # Part 4: Applying AM-HM
        # ==========================================
        
        # Clear previous step
        self.play(
            FadeOut(step1_text),
            FadeOut(denom_sum),
            FadeOut(simplified),
            FadeOut(factored),
            FadeOut(final_calc)
        )

        step2_text = Text("Step 2: Apply AM-HM", font_size=32)
        step2_text.set_color(GREEN)
        step2_text.next_to(statement, DOWN, buff=0.8)
        self.play(FadeIn(step2_text))

        # Set up x, y, z substitution visually
        subs = MathTex(
            "x=a+b, \\quad y=b+c, \\quad z=c+a"
        )
        subs.set_color(GREY_B)
        subs.next_to(step2_text, DOWN, buff=0.3)
        self.play(FadeIn(subs), run_time=1)

        # The Application
        apply_title = Text("AM ≥ HM implies:", font_size=28)
        apply_title.next_to(subs, DOWN, buff=0.5)
        self.play(FadeIn(apply_title))

        # The big inequality equation
        # Numerator is 6 (from step 1)
        proof_line = MathTex(
            "\\frac{6}{3}", "\\ge", 
            "\\frac{3}{\\frac{1}{a+b} + \\frac{1}{b+c} + \\frac{1}{c+a}}"
        )
        proof_line.next_to(apply_title, DOWN, buff=0.3)
        
        self.play(Write(proof_line), run_time=2)
        self.wait(1)

        # ==========================================
        # Part 5: Final Conclusion
        # ==========================================
        
        # Rearranging the equation
        conclusion_text = Text("Rearranging terms...", font_size=28)
        conclusion_text.next_to(proof_line, DOWN)
        self.play(FadeIn(conclusion_text), run_time=0.5)

        # The final result animation
        # We flip the fraction on the right to the left
        final_line = MathTex(
            "\\frac{1}{a+b} + \\frac{1}{b+c} + \\frac{1}{c+a}", 
            "\\ge", 
            "\\frac{3}{2}"
        )
        final_line.set_color(YELLOW)
        final_line.next_to(conclusion_text, DOWN, buff=0.5)
        
        # Highlight the match with the problem statement
        box_final = SurroundingRectangle(final_line, color=GREEN, buff=0.2)
        
        self.play(
            TransformMatchingTex(proof_line, final_line),
            run_time=1.5
        )
        self.play(Create(box_final), run_time=0.8)
        
        # Equality Case
        equality_case = MathTex("a = b = c = 1")
        equality_case.set_color(BLUE)
        equality_case.next_to(final_line, DOWN, buff=1)
        
        eq_text = Text("Equality when:", font_size=28)
        eq_text.next_to(equality_case, LEFT)
        
        self.play(FadeIn(eq_text), Write(equality_case), run_time=1)
        
        self.wait(2)
        
        # Fade everything out
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1
        )
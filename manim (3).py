from manim import *
import numpy as np

class TriangleExcircleInequality(Scene):
    def construct(self):
        # Title Section with Bangla Text using specific font
        self.title_section()
        
        # Problem Statement
        self.problem_statement()
        
        # Draw Triangle and Excircles
        self.draw_triangle_and_excircles()
        
        # Define Points D, E, F
        self.define_touch_points()
        
        # Mathematical derivation (using English for LaTeX)
        self.mathematical_derivation()
        
        # Conclusion
        self.conclusion()

    def title_section(self):
        # Using Text with Shonar Bangla font
        title = Text("ত্রিভুজের পরিধি সংক্রান্ত অসমতা",
                     font="Shonar Bangla",
                     font_size=48,
                     color=BLUE)
        
        # Fallback: If Shonar Bangla not available, use default
        if not title.font:
            title = Text("Triangle Perimeter Inequality",
                         font_size=48,
                         color=BLUE)
        
        subtitle = Text("এক্সসার্কেল সংক্রান্ত সমস্যা",
                       font="Shonar Bangla",
                       font_size=32,
                       color=WHITE)
        
        if not subtitle.font:
            subtitle = Text("Excircle Related Problem",
                           font_size=32,
                           color=WHITE)
        
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title))
        self.play(Write(subtitle), run_time=1)
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))

    def problem_statement(self):
        # Problem in Bangla with fallback to English
        problem_text = VGroup()
        
        # Try Bangla first
        try:
            prob1 = Text("সমস্যা:", font="Shonar Bangla", font_size=36, color=YELLOW)
            prob2 = Text("ABC একটি ত্রিভুজ। এর বহিঃবৃত্তগুলি", 
                        font="Shonar Bangla", font_size=28)
            prob3 = Text("BC, CA, AB বাহুকে যথাক্রমে D, E, F বিন্দুতে স্পর্শ করে।", 
                        font="Shonar Bangla", font_size=28)
            prob4 = Text("প্রমাণ কর যে:", font="Shonar Bangla", font_size=28)
        except:
            # Fallback to English
            prob1 = Text("Problem:", font_size=36, color=YELLOW)
            prob2 = Text("Let ABC be a triangle. Its excircles touch", font_size=28)
            prob3 = Text("sides BC, CA, AB at points D, E, F respectively.", font_size=28)
            prob4 = Text("Prove that:", font_size=28)
        
        problem_text.add(prob1, prob2, prob3, prob4)
        
        inequality = MathTex("P_{ABC} \\leq 2P_{DEF}", font_size=36, color=GREEN)
        
        problem_text.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        problem_text[0].align_to(problem_text, LEFT)
        
        self.play(Write(problem_text))
        self.play(Write(inequality))
        self.wait(3)
        self.play(FadeOut(problem_text), FadeOut(inequality))

    def draw_triangle_and_excircles(self):
        # Create triangle ABC
        vertices = [
            np.array([-3, -2, 0]),  # A
            np.array([3, -2, 0]),   # B
            np.array([0, 3, 0])     # C
        ]
        
        triangle = Polygon(vertices[0], vertices[1], vertices[2], 
                          color=BLUE, stroke_width=3)
        
        # Labels for triangle
        labels = VGroup(
            MathTex("A").next_to(vertices[0], LEFT + DOWN, buff=0.2),
            MathTex("B").next_to(vertices[1], RIGHT + DOWN, buff=0.2),
            MathTex("C").next_to(vertices[2], UP, buff=0.2)
        )
        
        # Excircles (simplified for visualization)
        a_excircle = Circle(radius=2.5, color=RED, stroke_width=2)
        a_excircle.move_to(np.array([0, -4, 0]))
        
        b_excircle = Circle(radius=2.2, color=GREEN, stroke_width=2)
        b_excircle.move_to(np.array([5, 1, 0]))
        
        c_excircle = Circle(radius=2.2, color=YELLOW, stroke_width=2)
        c_excircle.move_to(np.array([-5, 1, 0]))
        
        # Draw everything
        self.play(Create(triangle))
        self.play(Write(labels))
        self.wait(1)
        
        self.play(
            Create(a_excircle),
            Create(b_excircle),
            Create(c_excircle),
            run_time=2
        )
        
        # Add explanation (Bilingual)
        try:
            explanation = Text("ত্রিভুজের বহিঃবৃত্তসমূহ", 
                              font="Shonar Bangla", 
                              font_size=24,
                              color=WHITE)
        except:
            explanation = Text("Excircles of the triangle", 
                              font_size=24,
                              color=WHITE)
        
        explanation.to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(2)
        self.play(FadeOut(explanation))
        
        # Store
        self.triangle = triangle
        self.vertices = vertices

    def define_touch_points(self):
        # Define touch points (approximate positions)
        D = np.array([1.2, -0.5, 0])   # On BC
        E = np.array([-1.5, 0.5, 0])  # On CA
        F = np.array([0, -1.5, 0])    # On AB
        
        touch_points = VGroup(
            Dot(D, color=RED, radius=0.08),
            Dot(E, color=RED, radius=0.08),
            Dot(F, color=RED, radius=0.08)
        )
        
        point_labels = VGroup(
            MathTex("D").next_to(D, DOWN + RIGHT, buff=0.1),
            MathTex("E").next_to(E, LEFT + UP, buff=0.1),
            MathTex("F").next_to(F, DOWN, buff=0.1)
        )
        
        # Triangle DEF
        def_triangle = Polygon(D, E, F, color=GREEN, stroke_width=3)
        
        self.play(
            Create(touch_points),
            Write(point_labels),
            run_time=1.5
        )
        
        self.play(Create(def_triangle), run_time=1.5)
        
        # Bilingual explanation
        try:
            explanation = Text("D, E, F স্পর্শবিন্দুগুলি", 
                              font="Shonar Bangla", 
                              font_size=24,
                              color=YELLOW)
        except:
            explanation = Text("Touch points D, E, F", 
                              font_size=24,
                              color=YELLOW)
        
        explanation.to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(2)
        self.play(FadeOut(explanation))
        
        # Store
        self.def_triangle = def_triangle

    def mathematical_derivation(self):
        self.clear()
        
        # Title with Bangla
        try:
            title = Text("গাণিতিক প্রমাণ", 
                        font="Shonar Bangla", 
                        font_size=36,
                        color=BLUE)
        except:
            title = Text("Mathematical Proof", 
                        font_size=36,
                        color=BLUE)
        
        title.to_edge(UP)
        
        # Step 1: Projection
        step1 = VGroup(
            MathTex("\\text{Step 1: Projection of } EF \\text{ onto } BC"),
            MathTex("\\text{Projection length} = a - (s-a)(\\cos B + \\cos C)")
        ).arrange(DOWN, buff=0.3)
        
        # Step 2: Cyclic sum
        step2 = VGroup(
            MathTex("\\text{Step 2: Cyclic Sum}"),
            MathTex("P_{DEF} \\geq \\sum [a - (s-a)(\\cos B + \\cos C)]"),
            MathTex("= 2s - \\sum a \\cos A")
        ).arrange(DOWN, buff=0.3)
        
        # Step 3: Trigonometric transformation
        step3 = VGroup(
            MathTex("\\text{Step 3: Trigonometric Transformation}"),
            MathTex("s = R(\\sin A + \\sin B + \\sin C)"),
            MathTex("\\sum a \\cos A = R \\sum \\sin 2A"),
            MathTex("P_{DEF} \\geq R \\sum (\\sin A - \\sin 2A)")
        ).arrange(DOWN, buff=0.3)
        
        # Step 4: Key identity
        step4 = VGroup(
            MathTex("\\text{Step 4: Key Identity}"),
            MathTex("\\sin 2B + \\sin 2C = 2\\sin A \\cos(B-C) \\leq 2\\sin A"),
            MathTex("\\Rightarrow \\sin A + \\sin B + \\sin C \\geq \\sin 2A + \\sin 2B + \\sin 2C")
        ).arrange(DOWN, buff=0.3)
        
        # Step 5: Final inequality
        step5 = VGroup(
            MathTex("\\text{Step 5: Final Inequality}"),
            MathTex("P_{DEF} \\geq 2s - \\sum a \\cos A \\geq s"),
            MathTex("\\Rightarrow P_{ABC} \\leq 2P_{DEF}")
        ).arrange(DOWN, buff=0.3)
        
        self.play(Write(title))
        self.wait(1)
        
        # Animate each step
        steps = [step1, step2, step3, step4, step5]
        for step in steps:
            self.play(Write(step), run_time=2)
            self.wait(2)
            self.play(FadeOut(step))
        
        self.play(FadeOut(title))

    def conclusion(self):
        self.clear()
        
        # Final result with Bangla
        try:
            conclusion_text = VGroup(
                Text("প্রমাণিত!", font="Shonar Bangla", font_size=48, color=GREEN),
                Text("ত্রিভুজের পরিধি সর্বাধিক দ্বিগুণ", 
                     font="Shonar Bangla", font_size=32),
                MathTex("P_{ABC} \\leq 2P_{DEF}", font_size=48, color=YELLOW)
            ).arrange(DOWN, buff=0.5)
        except:
            conclusion_text = VGroup(
                Text("Proved!", font_size=48, color=GREEN),
                Text("Perimeter of triangle is at most twice", font_size=32),
                MathTex("P_{ABC} \\leq 2P_{DEF}", font_size=48, color=YELLOW)
            ).arrange(DOWN, buff=0.5)
        
        self.play(Write(conclusion_text))
        self.wait(3)
        
        # Animated flourish
        star = Star(color=GOLD, fill_opacity=1)
        star.scale(0.5)
        star.move_to(conclusion_text[2].get_right() + RIGHT * 0.5)
        self.play(Create(star))
        
        self.wait(2)
        self.play(FadeOut(conclusion_text), FadeOut(star))
        
        # Thank you message
        try:
            thank_you = Text("ধন্যবাদ!", 
                            font="Shonar Bangla", 
                            font_size=48, 
                            color=BLUE)
        except:
            thank_you = Text("Thank You!", 
                            font_size=48, 
                            color=BLUE)
        
        self.play(Write(thank_you))
        self.wait(2)
        self.play(FadeOut(thank_you))
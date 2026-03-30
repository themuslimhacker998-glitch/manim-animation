from manim import *

class TriangleSumTheorem(Scene):
    def construct(self):
        proof_text = VGroup()
        
        A = np.array([-2, -1.5, 0])
        B = np.array([2, -1.5, 0])
        C = np.array([0, 2, 0])
        
        triangle = Polygon(A, B, C, color=WHITE)
        triangle.shift(LEFT * 3)
        
        A_label = MathTex("A").next_to(triangle.get_vertices()[0], DOWN)
        B_label = MathTex("B").next_to(triangle.get_vertices()[1], DOWN)
        C_label = MathTex("C").next_to(triangle.get_vertices()[2], UP)
        
        triangle_group = VGroup(triangle, A_label, B_label, C_label)
        
        text_position = RIGHT * 3.5 + UP * 2
        
        def show_proof_step(text_content, latex=False):
            nonlocal proof_text
            new_text = MathTex(text_content) if latex else Text(text_content, font_size=24)
            new_text.move_to(text_position)
            
            self.play(
                FadeOut(proof_text),
                FadeIn(new_text),
                run_time=0.5
            )
            proof_text = new_text
        
        self.play(Create(triangle_group))
        show_proof_step("Given: Triangle ABC")
        
        line_length = 6
        angle_a = angle_of_vector(A - C)
        parallel_direction = rotate_vector(A - B, angle_a)
        
        X = C - parallel_direction * line_length
        Y = C + parallel_direction * line_length
        
        line_xy = Line(X, Y, color=YELLOW)
        
        self.play(
            FadeOut(triangle_group),
            Create(line_xy),
            run_time=1
        )
        
        triangle_group_no_fill = VGroup(
            Polygon(A, B, C, color=WHITE),
            A_label, B_label, C_label
        ).shift(LEFT * 3)
        
        self.play(Create(triangle_group_no_fill))
        
        show_proof_step("Construction: Line XY $||$ AB through C", latex=True)
        
        angle_xca = Angle(Line(C, X), Line(C, A), radius=0.5, color=RED)
        angle_a_val = Angle(Line(A, C), Line(A, B), radius=0.5, color=RED)
        
        self.play(Create(angle_xca), Create(angle_a_val))
        show_proof_step("$\\angle XCA = \\angle CAB$ (Alt. Int. Angles)", latex=True)
        self.wait(0.5)
        self.play(FadeOut(angle_xca), FadeOut(angle_a_val))
        
        angle_bcy = Angle(Line(C, B), Line(C, Y), radius=0.6, color=GREEN)
        angle_b_val = Angle(Line(B, A), Line(B, C), radius=0.6, color=GREEN)
        
        self.play(Create(angle_bcy), Create(angle_b_val))
        show_proof_step("$\\angle BCY = \\angle CBA$ (Alt. Int. Angles)", latex=True)
        self.wait(0.5)
        self.play(FadeOut(angle_bcy), FadeOut(angle_b_val))
        
        angle_c_val = Angle(Line(C, A), Line(C, B), radius=0.7, color=BLUE)
        
        self.play(Create(angle_c_val))
        show_proof_step("$\\angle ACB$ is the internal angle", latex=True)
        self.wait(0.5)
        
        final_eq = MathTex(
            "\\angle A + \\angle B + \\angle C = 180^{\\circ}",
            font_size=36
        ).move_to(text_position)
        
        self.play(
            FadeOut(proof_text),
            FadeIn(final_eq),
            Create(angle_xca),
            Create(angle_bcy),
            run_time=1
        )
        
        proof_text = final_eq
        self.wait(2)
        
        self.play(
            FadeOut(triangle_group_no_fill),
            FadeOut(line_xy),
            FadeOut(angle_c_val),
            FadeOut(angle_xca),
            FadeOut(angle_bcy),
            FadeOut(proof_text)
        )
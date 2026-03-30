from manim import *
import numpy as np
config.background_color = "#1a1a2e"
class QuadraticSolution(Scene):
    def construct(self):
        # ============ SCENE 1: Title ============
        title = Text("Solving Quadratic Equations", font_size=56)
        title.to_edge(UP, buff=1)
        
        equation = MathTex(r"4x^2 - 3x + 3 = 0", font_size=64)
        equation.next_to(title, DOWN, buff=1)
        
        self.play(Write(title), run_time=1.5)
        self.wait(0.5)
        self.play(Write(equation), run_time=2)
        self.wait(2)
        self.play(FadeOut(title), FadeOut(equation))
        
        # ============ SCENE 2: Function Parts ============
        title2 = Text("The Quadratic Function", font_size=48)
        title2.to_edge(UP, buff=0.8)
        self.play(Write(title2), run_time=1.5)
        
        func = MathTex(r"f(x) = 4x^2 - 3x + 3", font_size=56)
        func.move_to(UP * 2)
        self.play(Write(func), run_time=1.5)
        self.wait(1)
        
        parts = VGroup(
            MathTex(r"4x^2", font_size=44, color=BLUE),
            MathTex(r"- 3x", font_size=44, color=RED),
            MathTex(r"+ 3", font_size=44, color=GREEN)
        )
        parts.arrange(RIGHT, buff=1)
        parts.move_to(DOWN * 0.5)
        
        labels = VGroup(
            Text("Quadratic term", font_size=22, color=BLUE),
            Text("Linear term", font_size=22, color=RED),
            Text("Constant", font_size=22, color=GREEN)
        )
        for i, label in enumerate(labels):
            label.next_to(parts[i], DOWN, buff=0.3)
        
        for i, part in enumerate(parts):
            self.play(Write(part), run_time=1)
            self.play(Write(labels[i]), run_time=0.5)
            self.wait(0.3)
        
        self.wait(2)
        self.play(FadeOut(title2), FadeOut(func), FadeOut(parts), FadeOut(labels))
        
        # ============ SCENE 3: Coefficients ============
        title3 = Text("Identifying Coefficients", font_size=48)
        title3.to_edge(UP, buff=0.8)
        self.play(Write(title3), run_time=1.5)
        
        func3 = MathTex(r"ax^2 + bx + c = 0", font_size=52)
        func3.move_to(UP * 2)
        self.play(Write(func3), run_time=1.5)
        self.wait(1)
        
        a_box = SurroundingRectangle(MathTex("a", font_size=40), color=BLUE, buff=0.2)
        b_box = SurroundingRectangle(MathTex("b", font_size=40), color=RED, buff=0.2)
        c_box = SurroundingRectangle(MathTex("c", font_size=40), color=GREEN, buff=0.2)
        
        a_label = MathTex("a = 4", font_size=36, color=BLUE).next_to(a_box, DOWN, buff=0.5)
        b_label = MathTex("b = -3", font_size=36, color=RED).next_to(b_box, DOWN, buff=0.5)
        c_label = MathTex("c = 3", font_size=36, color=GREEN).next_to(c_box, DOWN, buff=0.5)
        
        self.play(Create(a_box), Write(a_label), run_time=1)
        self.wait(0.5)
        self.play(Create(b_box), Write(b_label), run_time=1)
        self.wait(0.5)
        self.play(Create(c_box), Write(c_label), run_time=1)
        self.wait(2)
        self.play(FadeOut(title3), FadeOut(func3), FadeOut(a_box), FadeOut(b_box), 
                  FadeOut(c_box), FadeOut(a_label), FadeOut(b_label), FadeOut(c_label))
        
        # ============ SCENE 4: Parabola Graph ============
        title4 = Text("Graphing the Parabola", font_size=48)
        title4.to_edge(UP, buff=0.8)
        self.play(Write(title4), run_time=1.5)
        
        ax = Axes(
            x_range=[-1, 2, 0.5],
            y_range=[0, 6, 1],
            x_length=10,
            y_length=6,
            tips=True
        )
        ax.shift(DOWN * 0.5)
        
        x_label = MathTex("x", font_size=28).next_to(ax.x_axis, RIGHT, buff=0.3)
        y_label = MathTex("y", font_size=28).next_to(ax.y_axis, UP, buff=0.3)
        
        self.play(Create(ax), Write(x_label), Write(y_label), run_time=2)
        self.wait(0.5)
        
        func_label = MathTex("y = 4x^2 - 3x + 3", font_size=32)
        func_label.to_corner(UR).shift(LEFT * 0.5 + DOWN * 0.5)
        func_label.set_color(YELLOW)
        
        self.play(Write(func_label), run_time=1.5)
        self.wait(0.5)
        
        parabola = ax.plot(
            lambda x: 4*x**2 - 3*x + 3,
            x_range=[-0.5, 1.5],
            color=YELLOW,
            stroke_width=3
        )
        
        self.play(Create(parabola), run_time=2)
        self.wait(2)
        self.play(FadeOut(title4), FadeOut(func_label))
        
        # ============ SCENE 5: Vertex Calculation ============
        title5 = Text("Finding the Vertex", font_size=48)
        title5.to_edge(UP, buff=0.8)
        self.play(Write(title5), run_time=1.5)
        
        func5 = MathTex(r"y = 4x^2 - 3x + 3", font_size=44)
        func5.move_to(UP * 2.2)
        self.play(Write(func5), run_time=1.5)
        self.wait(1)
        
        vertex_formula = MathTex(r"x_v = -\frac{b}{2a}", font_size=48)
        vertex_formula.move_to(UP * 1)
        self.play(Write(vertex_formula), run_time=1.5)
        self.wait(1)
        
        substitution = MathTex(r"x_v = -\frac{(-3)}{2(4)} = \frac{3}{8}", font_size=44)
        substitution.next_to(vertex_formula, DOWN, buff=0.5)
        self.play(Write(substitution), run_time=1.5)
        self.wait(1)
        
        y_value = MathTex(r"y_v = 4\left(\frac{3}{8}\right)^2 - 3\left(\frac{3}{8}\right) + 3", font_size=36)
        y_value.next_to(substitution, DOWN, buff=0.5)
        self.play(Write(y_value), run_time=1.5)
        self.wait(0.5)
        
        y_simplified = MathTex(r"y_v = 4 \cdot \frac{9}{64} - \frac{9}{8} + 3", font_size=36)
        y_simplified.next_to(y_value, DOWN, buff=0.3)
        self.play(ReplacementTransform(y_value.copy(), y_simplified), run_time=1.5)
        self.wait(0.3)
        
        y_result = MathTex(r"y_v = \frac{39}{16} = 2.4375", font_size=40, color=YELLOW)
        y_result.next_to(y_simplified, DOWN, buff=0.3)
        self.play(ReplacementTransform(y_simplified.copy(), y_result), run_time=1.5)
        self.wait(1)
        
        vertex_point = MathTex(r"Vertex = \left(\frac{3}{8}, \frac{39}{16}\right)", font_size=36, color=GREEN)
        vertex_point.next_to(y_result, DOWN, buff=0.5)
        self.play(Write(vertex_point), run_time=2)
        self.wait(2)
        self.play(FadeOut(title5), FadeOut(func5), FadeOut(vertex_formula), FadeOut(substitution),
                  FadeOut(y_simplified), FadeOut(y_result), FadeOut(vertex_point))
        
        # ============ SCENE 6: Vertex on Graph ============
        title6 = Text("Vertex on the Graph", font_size=48)
        title6.to_edge(UP, buff=0.8)
        self.play(Write(title6), run_time=1.5)
        
        ax6 = Axes(
            x_range=[-0.5, 1.5, 0.25],
            y_range=[0, 4, 0.5],
            x_length=10,
            y_length=6,
            tips=True
        )
        ax6.shift(DOWN * 0.3)
        
        self.play(Create(ax6), run_time=2)
        
        parabola6 = ax6.plot(
            lambda x: 4*x**2 - 3*x + 3,
            x_range=[-0.2, 1.2],
            color=YELLOW,
            stroke_width=3
        )
        self.play(Create(parabola6), run_time=2)
        
        vertex_x = 0.375
        vertex_y = 4*vertex_x**2 - 3*vertex_x + 3
        
        vertex_dot = Dot(ax6.coords_to_point(vertex_x, vertex_y), color=GREEN, radius=0.1)
        
        dashed_v = DashedLine(
            ax6.coords_to_point(vertex_x, 0),
            ax6.coords_to_point(vertex_x, vertex_y),
            color=GREEN,
            stroke_width=2
        )
        dashed_h = DashedLine(
            ax6.coords_to_point(-0.5, vertex_y),
            ax6.coords_to_point(vertex_x, vertex_y),
            color=GREEN,
            stroke_width=2
        )
        
        self.play(Create(dashed_v), run_time=1)
        self.play(Create(dashed_h), run_time=1)
        self.play(FadeIn(vertex_dot), run_time=1)
        
        vertex_label = MathTex(r"\left(\frac{3}{8}, \frac{39}{16}\right)", font_size=28, color=GREEN)
        vertex_label.next_to(vertex_dot, UP + RIGHT, buff=0.2)
        
        self.play(Write(vertex_label), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(title6), FadeOut(vertex_dot), FadeOut(vertex_label), FadeOut(dashed_v),
                  FadeOut(dashed_h), FadeOut(parabola6), FadeOut(ax6))
        
        # ============ SCENE 7: Discriminant Intro ============
        title7 = Text("The Discriminant", font_size=52)
        title7.to_edge(UP, buff=0.8)
        self.play(Write(title7), run_time=1.5)
        
        disc_formula = MathTex(r"\Delta = b^2 - 4ac", font_size=56)
        disc_formula.move_to(UP * 2)
        self.play(Write(disc_formula), run_time=1.5)
        self.wait(1)
        
        explanation = Text("The discriminant determines the nature of roots", font_size=28, color=GRAY)
        explanation.next_to(disc_formula, DOWN, buff=0.5)
        self.play(Write(explanation), run_time=1.5)
        self.wait(1)
        
        case1 = VGroup(
            MathTex(r"\Delta > 0", font_size=40, color=GREEN),
            MathTex(r"\text{Two distinct real roots}", font_size=28, color=GRAY)
        )
        case1[1].next_to(case1[0], DOWN, buff=0.2)
        
        case2 = VGroup(
            MathTex(r"\Delta = 0", font_size=40, color=YELLOW),
            MathTex(r"\text{One repeated real root}", font_size=28, color=GRAY)
        )
        case2[1].next_to(case2[0], DOWN, buff=0.2)
        
        case3 = VGroup(
            MathTex(r"\Delta < 0", font_size=40, color=RED),
            MathTex(r"\text{No real roots (complex)}", font_size=28, color=GRAY)
        )
        case3[1].next_to(case3[0], DOWN, buff=0.2)
        
        all_cases = VGroup(case1, case2, case3)
        all_cases.arrange(DOWN, buff=0.8)
        all_cases.move_to(DOWN * 1.5)
        
        for case in [case1, case2, case3]:
            self.play(Write(case[0]), run_time=1)
            self.play(Write(case[1]), run_time=0.8)
            self.wait(0.5)
        
        self.wait(2)
        self.play(FadeOut(title7), FadeOut(disc_formula), FadeOut(explanation), FadeOut(case1),
                  FadeOut(case2), FadeOut(case3))
        
        # ============ SCENE 8: Discriminant Calculation ============
        title8 = Text("Calculating the Discriminant", font_size=48)
        title8.to_edge(UP, buff=0.8)
        self.play(Write(title8), run_time=1.5)
        
        formula8 = MathTex(r"\Delta = b^2 - 4ac", font_size=52)
        formula8.move_to(UP * 2.2)
        self.play(Write(formula8), run_time=1.5)
        self.wait(0.5)
        
        values8 = MathTex(r"a = 4, \quad b = -3, \quad c = 3", font_size=40)
        values8.next_to(formula8, DOWN, buff=0.5)
        self.play(Write(values8), run_time=1.5)
        self.wait(1)
        
        substitution8 = MathTex(r"\Delta = (-3)^2 - 4(4)(3)", font_size=48)
        substitution8.next_to(values8, DOWN, buff=0.5)
        self.play(Write(substitution8), run_time=1.5)
        self.wait(0.5)
        
        calculation8 = MathTex(r"\Delta = 9 - 48", font_size=48)
        calculation8.next_to(substitution8, DOWN, buff=0.5)
        self.play(ReplacementTransform(substitution8.copy(), calculation8), run_time=1.5)
        self.wait(0.5)
        
        result8 = MathTex(r"\Delta = -39", font_size=56, color=RED)
        result8.next_to(calculation8, DOWN, buff=0.5)
        self.play(ReplacementTransform(calculation8.copy(), result8), run_time=1.5)
        self.wait(1)
        
        conclusion8 = Text("Since Delta < 0, there are no real roots!", font_size=32, color=RED)
        conclusion8.next_to(result8, DOWN, buff=0.8)
        self.play(Write(conclusion8), run_time=2)
        self.wait(2)
        self.play(FadeOut(title8), FadeOut(formula8), FadeOut(values8), FadeOut(substitution8),
                  FadeOut(calculation8), FadeOut(result8), FadeOut(conclusion8))
        
        # ============ SCENE 9: Quadratic Formula ============
        title9 = Text("The Quadratic Formula", font_size=52)
        title9.to_edge(UP, buff=0.8)
        self.play(Write(title9), run_time=1.5)
        
        formula9 = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}", font_size=60)
        formula9.move_to(UP * 2)
        self.play(Write(formula9), run_time=2)
        self.wait(1)
        
        explanation9 = VGroup(
            Text("-b: opposite of linear coefficient", font_size=24, color=BLUE),
            Text("b^2 - 4ac: the discriminant", font_size=24, color=YELLOW),
            Text("2a: twice the quadratic coefficient", font_size=24, color=GREEN)
        )
        explanation9.arrange(DOWN, buff=0.3)
        explanation9.move_to(DOWN * 1.2)
        
        for exp in explanation9:
            self.play(Write(exp), run_time=1)
            self.wait(0.3)
        
        self.wait(2)
        self.play(FadeOut(title9), FadeOut(formula9), FadeOut(explanation9))
        
        # ============ SCENE 10: Apply Formula ============
        title10 = Text("Applying the Formula", font_size=48)
        title10.to_edge(UP, buff=0.8)
        self.play(Write(title10), run_time=1.5)
        
        formula10 = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}", font_size=44)
        formula10.move_to(UP * 2.2)
        self.play(Write(formula10), run_time=1.5)
        self.wait(0.5)
        
        substitution10 = MathTex(r"x = \frac{-(-3) \pm \sqrt{(-3)^2 - 4(4)(3)}}{2(4)}", font_size=36)
        substitution10.next_to(formula10, DOWN, buff=0.5)
        self.play(Write(substitution10), run_time=1.5)
        self.wait(0.5)
        
        simplified10 = MathTex(r"x = \frac{3 \pm \sqrt{9 - 48}}{8}", font_size=40)
        simplified10.next_to(substitution10, DOWN, buff=0.5)
        self.play(ReplacementTransform(substitution10.copy(), simplified10), run_time=1.5)
        self.wait(0.5)
        
        with_delta10 = MathTex(r"x = \frac{3 \pm \sqrt{-39}}{8}", font_size=44)
        with_delta10.set_color(RED)
        with_delta10.next_to(simplified10, DOWN, buff=0.5)
        self.play(ReplacementTransform(simplified10.copy(), with_delta10), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(title10), FadeOut(formula10), FadeOut(substitution10), 
                  FadeOut(simplified10), FadeOut(with_delta10))
        
        # ============ SCENE 11: Complex Roots ============
        title11 = Text("The Complex Roots", font_size=52, color=PURPLE)
        title11.to_edge(UP, buff=0.8)
        self.play(Write(title11), run_time=1.5)
        
        root_formula = MathTex(r"x = \frac{3 \pm i\sqrt{39}}{8}", font_size=56)
        root_formula.move_to(UP * 2)
        self.play(Write(root_formula), run_time=2)
        self.wait(1)
        
        root1 = MathTex(r"x_1 = \frac{3 + i\sqrt{39}}{8}", font_size=40, color=GREEN)
        root1.next_to(root_formula, DOWN, buff=1)
        self.play(Write(root1), run_time=1.5)
        
        root2 = MathTex(r"x_2 = \frac{3 - i\sqrt{39}}{8}", font_size=40, color=RED)
        root2.next_to(root1, DOWN, buff=0.5)
        self.play(Write(root2), run_time=1.5)
        self.wait(1)
        
        approx1 = MathTex(r"x_1 \approx 0.375 + 0.781i", font_size=36, color=GREEN)
        approx2 = MathTex(r"x_2 \approx 0.375 - 0.781i", font_size=36, color=RED)
        
        approx1.next_to(root2, DOWN, buff=0.8)
        approx2.next_to(approx1, DOWN, buff=0.3)
        
        self.play(Write(approx1), run_time=1.5)
        self.play(Write(approx2), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(title11), FadeOut(root_formula), FadeOut(root1), 
                  FadeOut(root2), FadeOut(approx1), FadeOut(approx2))
        
        # ============ SCENE 12: Complex Plane ============
        title12 = Text("Roots on the Complex Plane", font_size=48)
        title12.to_edge(UP, buff=0.8)
        self.play(Write(title12), run_time=1.5)
        
        ax12 = NumberPlane(
            x_range=[-1.5, 1.5, 0.5],
            y_range=[-1.5, 1.5, 0.5],
            x_length=8,
            y_length=6
        )
        ax12.shift(DOWN * 0.3)
        
        self.play(Create(ax12), run_time=2)
        
        real_label = MathTex("Re", font_size=24).next_to(ax12.x_axis, RIGHT, buff=0.3)
        imag_label = MathTex("Im", font_size=24).next_to(ax12.y_axis, UP, buff=0.3)
        
        self.play(Write(real_label), Write(imag_label), run_time=1)
        
        root1_point = ax12.coords_to_point(0.375, 0.781)
        root2_point = ax12.coords_to_point(0.375, -0.781)
        
        dot1 = Dot(root1_point, color=GREEN, radius=0.08)
        dot2 = Dot(root2_point, color=RED, radius=0.08)
        
        line_between = Line(root1_point, root2_point, color=YELLOW, stroke_width=2)
        
        self.play(Create(line_between), run_time=1.5)
        self.play(FadeIn(dot1), run_time=0.8)
        self.play(FadeIn(dot2), run_time=0.8)
        
        label1 = MathTex(r"x_1", font_size=28, color=GREEN).next_to(dot1, UP + RIGHT, buff=0.2)
        label2 = MathTex(r"x_2", font_size=28, color=RED).next_to(dot2, DOWN + RIGHT, buff=0.2)
        
        self.play(Write(label1), run_time=1)
        self.play(Write(label2), run_time=1)
        
        conjugate_note = Text("Complex conjugates: symmetric about real axis", font_size=24, color=YELLOW)
        conjugate_note.to_edge(DOWN, buff=0.8)
        self.play(Write(conjugate_note), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(title12), FadeOut(ax12), FadeOut(real_label), FadeOut(imag_label),
                  FadeOut(line_between), FadeOut(dot1), FadeOut(dot2), FadeOut(label1), 
                  FadeOut(label2), FadeOut(conjugate_note))
        
        # ============ SCENE 13: Why No Real Roots ============
        title13 = Text("Why No Real Roots?", font_size=48)
        title13.to_edge(UP, buff=0.8)
        self.play(Write(title13), run_time=1.5)
        
        ax13 = Axes(
            x_range=[-1, 2, 0.5],
            y_range=[0, 6, 1],
            x_length=10,
            y_length=6,
            tips=True
        )
        ax13.shift(DOWN * 0.3)
        
        self.play(Create(ax13), run_time=1.5)
        
        parabola13 = ax13.plot(
            lambda x: 4*x**2 - 3*x + 3,
            x_range=[-0.3, 1.3],
            color=YELLOW,
            stroke_width=3
        )
        self.play(Create(parabola13), run_time=2)
        
        vertex_x13 = 0.375
        vertex_y13 = 4*vertex_x13**2 - 3*vertex_x13 + 3
        vertex_dot13 = Dot(ax13.coords_to_point(vertex_x13, vertex_y13), color=GREEN, radius=0.1)
        
        self.play(FadeIn(vertex_dot13), run_time=1)
        
        vertex_label13 = MathTex(r"\text{Vertex: } y = 2.4375 > 0", font_size=28, color=GREEN)
        vertex_label13.to_corner(UR).shift(LEFT * 0.5 + DOWN * 0.5)
        
        self.play(Write(vertex_label13), run_time=1.5)
        self.wait(1)
        
        explanation13 = Text("The parabola lies entirely above the x-axis", font_size=28, color=RED)
        explanation13.to_edge(DOWN, buff=1.5)
        self.play(Write(explanation13), run_time=1.5)
        self.wait(1)
        
        no_cross = Text("It never crosses the x-axis, so no real roots!", font_size=28, color=YELLOW)
        no_cross.next_to(explanation13, DOWN, buff=0.3)
        self.play(Write(no_cross), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(title13), FadeOut(ax13), FadeOut(parabola13), FadeOut(vertex_dot13),
                  FadeOut(vertex_label13), FadeOut(explanation13), FadeOut(no_cross))
        
        # ============ SCENE 14: Summary ============
        title14 = Text("Summary", font_size=56)
        title14.to_edge(UP, buff=0.8)
        self.play(Write(title14), run_time=1.5)
        
        equation14 = MathTex(r"4x^2 - 3x + 3 = 0", font_size=48)
        equation14.move_to(UP * 2)
        self.play(Write(equation14), run_time=1.5)
        
        coefficients14 = MathTex(r"a = 4, \quad b = -3, \quad c = 3", font_size=36)
        coefficients14.next_to(equation14, DOWN, buff=0.5)
        self.play(Write(coefficients14), run_time=1)
        self.wait(0.5)
        
        discriminant14 = MathTex(r"\Delta = (-3)^2 - 4(4)(3) = 9 - 48 = -39 < 0", font_size=36)
        discriminant14.next_to(coefficients14, DOWN, buff=0.5)
        self.play(Write(discriminant14), run_time=1.5)
        self.wait(0.5)
        
        discriminant14.set_color(RED)
        self.wait(0.5)
        
        solutions14 = MathTex(r"x = \frac{3 \pm i\sqrt{39}}{8}", font_size=44, color=PURPLE)
        solutions14.next_to(discriminant14, DOWN, buff=0.5)
        self.play(Write(solutions14), run_time=2)
        self.wait(1)
        
        conclusion14 = Text("Two complex conjugate roots", font_size=32, color=GREEN)
        conclusion14.next_to(solutions14, DOWN, buff=1)
        self.play(Write(conclusion14), run_time=1.5)
        self.wait(3)
        self.play(FadeOut(title14), FadeOut(equation14), FadeOut(coefficients14),
                  FadeOut(discriminant14), FadeOut(solutions14), FadeOut(conclusion14))
        
        # ============ SCENE 15: Credits ============
        thank_you = Text("Thank you!", font_size=72)
        self.play(Write(thank_you), run_time=2)
        
        credit = Text("Created with Manim", font_size=28, color=GRAY)
        credit.next_to(thank_you, DOWN, buff=0.5)
        self.play(Write(credit), run_time=1.5)
        
        self.wait(2)
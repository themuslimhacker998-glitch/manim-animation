from manim import *
import numpy as np

class CircleTheoremProof(Scene):
    def construct(self):
        topic = Text("Circle Theorem", font_size=48, color=BLUE)
        subtitle = Text("Angle at the center is twice the angle at the circumference", font_size=30, color=WHITE)
        topic.next_to(subtitle, UP, buff=0.2)
        title_group = VGroup(topic, subtitle)
        self.play(Write(title_group), run_time=2)
        self.wait(1)
        self.play(FadeOut(title_group), run_time=1.5)

        center_point = np.array([-2.5, 0, 0])
        radius = 3.5
        
        circle = Circle(radius=radius, color=WHITE)
        circle.shift(center_point)
        
        theta_A = 220 * DEGREES
        theta_B = 320 * DEGREES
        theta_C = 280 * DEGREES
        
        points = {
            'O': center_point,
            'A': center_point + radius * np.array([np.cos(theta_A), np.sin(theta_A), 0]),
            'B': center_point + radius * np.array([np.cos(theta_B), np.sin(theta_B), 0]),
            'C': center_point + radius * np.array([np.cos(theta_C), np.sin(theta_C), 0]),
        }
        
        theta_D = (theta_A + theta_B) / 2
        points['D'] = center_point + radius * np.array([np.cos(theta_D), np.sin(theta_D), 0])
        
        self.play(Create(circle), run_time=2)
        
        dots = VGroup()
        for name, point in points.items():
            dot = Dot(point, color=YELLOW, radius=0.08)
            label = Text(name, font_size=28, color=YELLOW)
            if name == 'O':
                label.next_to(dot, DL, buff=0.15)
            elif name == 'A':
                label.next_to(dot, LEFT, buff=0.15)
            elif name == 'B':
                label.next_to(dot, RIGHT, buff=0.15)
            elif name == 'C':
                label.next_to(dot, UP, buff=0.15)
            elif name == 'D':
                label.next_to(dot, DOWN, buff=0.15)
            dots.add(dot, label)
        
        self.play(LaggedStart(*[Create(dot) for dot in dots], lag_ratio=0.1), run_time=1.5)
        
        lines = VGroup()
        
        line_OA = Line(points['O'], points['A'], color=BLUE, stroke_width=2)
        line_OB = Line(points['O'], points['B'], color=BLUE, stroke_width=2)
        line_OC = Line(points['O'], points['C'], color=BLUE, stroke_width=2)
        line_OD = Line(points['O'], points['D'], color=BLUE, stroke_width=2)
        
        line_AC = Line(points['A'], points['C'], color=RED, stroke_width=3)
        line_CB = Line(points['C'], points['B'], color=RED, stroke_width=3)
        line_AB = Line(points['A'], points['B'], color=GREEN, stroke_width=2)
        
        line_CD = Line(points['C'], points['D'], color=PURPLE, stroke_width=2)
        
        lines.add(line_OA, line_OB, line_OC, line_OD, line_AC, line_CB, line_AB, line_CD)
        
        self.play(LaggedStart(*[Create(line) for line in lines], lag_ratio=0.05), run_time=2)
        
        self.wait(1)
        
        diagram_group = VGroup(circle, dots, lines)
        
        self.play(diagram_group.animate.scale(0.8).shift(LEFT * 3.5), run_time=1.5)
        
        theorem_text = Text("∠AOB = 2 × ∠ACB", font_size=42, color=YELLOW)
        theorem_text.next_to(diagram_group, RIGHT, buff=1.2)
        theorem_text.align_to(diagram_group, UP)
        
        self.play(Write(theorem_text), run_time=1.5)
        
        angle_center = Angle(line_OA, line_OB, radius=0.8, color=YELLOW)
        angle_circum = Angle(line_AC, line_CB, radius=0.6, color=YELLOW)
        
        self.play(Create(angle_center), Create(angle_circum), run_time=1)
        
        label_center = MathTex("\\theta", font_size=30, color=YELLOW)
        label_center.move_to(angle_center.point_from_proportion(0.5))
        label_center.shift(UP * 0.3)
        
        label_circum = MathTex("\\alpha", font_size=30, color=YELLOW)
        label_circum.move_to(angle_circum.point_from_proportion(0.5))
        label_circum.shift(UP * 0.2 + LEFT * 0.2)
        
        self.play(Write(label_center), Write(label_circum), run_time=0.8)
        
        brace = Brace(theorem_text, DOWN, buff=0.1)
        brace_text = Text("Theorem 1", font_size=24)
        brace_text.next_to(brace, DOWN, buff=0.1)
        
        self.play(GrowFromCenter(brace), Write(brace_text), run_time=1)
        
        self.wait(2)
        
        self.play(
            theorem_text.animate.set_color(GREEN),
            angle_center.animate.set_color(GREEN),
            angle_circum.animate.set_color(GREEN),
            label_center.animate.set_color(GREEN),
            label_circum.animate.set_color(GREEN),
            run_time=1
        )
        
        self.wait(3)
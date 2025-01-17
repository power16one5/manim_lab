from manim import *



class Function(Scene):
    def construct(self):
        # 좌표축 생성
        axes1 = Axes(
            x_range=[-4, 4],   # x축 범위와 눈금
            y_range=[-2, 10],   # y축 범위와 눈금
            x_length=8,          # x축 길이
            y_length=10,          # y축 길이
        )
        
        axes2 = Axes(
            x_range=[-4, 4],   # x축 범위와 눈금
            y_range=[-2, 10],   # y축 범위와 눈금
            x_length=8,          # x축 길이
            y_length=10,          # y축 길이
        )

        axes1.scale(0.5)
        axes2.scale(0.5)

        axes1.to_edge(LEFT, buff=2)
        axes2.to_edge(RIGHT, buff=2)

        # 2차 함수 y=x^2를 그래프로 그리기
        f1 = lambda x: (x + 1)**2
        f2 = lambda x: x**2 - x

        quadratic_graph1 = axes1.plot(f1, color=BLUE, x_range=[-2.5, 2.1])
        quadratic_graph2 = axes2.plot(f2, color=GREEN, x_range=[-2.1, 2.5])

        x_coords = [-2, -1, 0, 1, 2]
        dots1 = VGroup()
        dots2 = VGroup()
        for x in x_coords:
            dot_posit1 = axes1.c2p(x, f1(x))
            dot_posit2 = axes2.c2p(x, f2(x))
            dot1 = Dot(point=dot_posit1, color=YELLOW)
            dot2 = Dot(point=dot_posit2, color=YELLOW)
            dots1.add(dot1); dots2.add(dot2)
        
        formula1 = MathTex(r"y = x^2 + 2x + 1")
        formula2 = MathTex(r"y = x^2 - x")
        formula1.to_edge(LEFT, buff=2)
        formula2.to_edge(RIGHT, buff=2)


        self.add(formula1, formula2)
        self.wait(1)
        self.play(formula1.animate.next_to(axes1, DOWN, buff=0.5), formula2.animate.next_to(axes2, DOWN, buff=0.5), run_time=1)
        self.play(FadeIn(axes1), FadeIn(axes2))

        self.play(Create(quadratic_graph1), 
                  Create(quadratic_graph2), 
                  run_time=2)
        self.play(Create(dots1), 
                  Create(dots2), run_time=1)
        self.wait(1)

        group = VGroup(axes1, axes2, quadratic_graph1, quadratic_graph2, dots1, dots2)
        self.play(group.animate.shift(UP * 0.5),
                  FadeOut(formula1),
                  FadeOut(formula2),
                  )
        self.wait(1)

        value1 = MathTex(r'[(-2, 1), (-1, 0), (0, 1), (1, 4), (2, 9)]', color=BLUE)
        value2 = MathTex(r'[(-2, 6), (-1, 2), (0, 0), (1, 0), (2, 2)]', color=GREEN)
        value1.scale(0.7); value2.scale(0.7)
        value1.next_to(axes1, DOWN, buff=0.5), value2.next_to(axes2, DOWN, buff=0.5)

        self.play(TransformFromCopy(dots1, value1),
                  TransformFromCopy(dots2, value2),
                  run_time=1
                 )
        self.wait(3)

        group.remove(value1, value2)

        self.play(FadeOut(group),
                  value1.animate.move_to(ORIGIN).scale(1.2),
                  value2.animate.next_to(ORIGIN, DOWN, buff=0.5).scale(1.2))
        self.wait(1)

        times = MathTex(r'\times')
        times.next_to(value2, LEFT, buff=0.5)

        line = Line(ORIGIN, RIGHT)
        line.scale(value2.width + 1)
        line.next_to(value2, DOWN, buff=0.2)

        self.play(Write(times), Write(line))
        self.wait(1)

        value3 = MathTex(r'[(-2, 6), (-1, 0), (0, 0), (1, 0), (2, 18)]', color=RED)
        value3.scale(value2.height / value3.height)
        value3.next_to(line, DOWN, buff=0.2)
        
        self.play(Write(value3))
        self.wait(2)

        axes3 = Axes(
            x_range=[-4, 4],   # x축 범위와 눈금
            y_range=[-2, 20],   # y축 범위와 눈금
            x_length=8,          # x축 길이
            y_length=10,          # y축 길이
        )

        axes3.scale(0.5)
        group = VGroup(value1, value2, line, times)
        self.play(FadeOut(group),
                  FadeIn(axes3),
                  value3.animate.next_to(axes3, DOWN, buff=0.2))
        self.wait(1)

        f3 = lambda x: x**4 + x**3 - x**2 - x
        quadratic_graph3 = axes3.plot(f3, color=RED, x_range=[-2.5, 2.1])

        dots3 = VGroup()
        for x in x_coords:
            dot_posit = axes3.c2p(x, f3(x))
            dots3.add(Dot(point=dot_posit, color=YELLOW))

        self.play(TransformFromCopy(value3, dots3))
        self.wait(1)
        self.play(Create(quadratic_graph3))
        self.wait(3)

        formula3 = MathTex(r"y = x^4 + x^3 - x^2 - x")
        formula3.move_to(value3)
        self.play(Transform(value3, formula3))
        self.wait(3)
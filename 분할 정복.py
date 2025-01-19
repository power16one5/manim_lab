from manim import *



class Function(Scene):
    def construct(self):
        every = VGroup()

        # 첫번째 줄 루트
        root_group1 = VGroup()
        root_group1.add(MathTex(r"x_1"))
        for text in r"-x_1", r"x_2", r"-x_2", r"x_3", r"-x_3", r"x_4", r"-x_4":
            a = MathTex(text)
            a.next_to(root_group1[-1], RIGHT, buff=1)
            root_group1.add(a)

        root_group1.move_to(ORIGIN)
        self.add(root_group1)
        self.wait()

        # 이동
        every.add(root_group1)
        self.play(every.animate.shift(UP))
        self.wait()

        # 두번째 줄 루트
        root_group2 = VGroup()
        root_group2.add(MathTex(r"x_1^2"))
        for text in r"x_2^2", r"x_3^2", r"x_4^2":
            a = MathTex(text)
            a.next_to(root_group2[-1], RIGHT, buff=2.8)
            root_group2.add(a)

        root_group2.next_to(root_group1, DOWN, buff=1)

        line_group1 = VGroup()
        for i, tex in enumerate(root_group1):
            a = Line(tex.get_center(), root_group2[i >> 1].get_center())
            a.set_length(a.get_length() * 0.4)
            line_group1.add(a)

        every.add(root_group2, line_group1)
        self.play(FadeIn(root_group2),
                  FadeIn(line_group1))
        self.wait()

        # 이동
        every.add(root_group2, line_group1)
        self.play(every.animate.shift(UP))
        self.wait()

        # 세번째 줄 루트
        root_group3 = VGroup()
        root_group3.add(MathTex(r"x_1^4"))
        a = MathTex(r"x_3^4")
        a.next_to(root_group3[-1], RIGHT, buff=5.5)
        root_group3.add(a)

        root_group3.next_to(root_group2, DOWN, buff=1)

        line_group2 = VGroup()
        for i, tex in enumerate(root_group2):
            a = Line(tex.get_center(), root_group3[i >> 1].get_center())
            a.set_length(a.get_length() * 0.4)
            line_group1.add(a)

        every.add(root_group3, line_group2)
        self.play(FadeIn(root_group3),
                  FadeIn(line_group2))
        self.wait(2)

        # 두번째 줄 루트 변환
        root1 = MathTex(r"-x_1^2")
        root1.move_to(root_group2[1])
        root2 = MathTex(r"-x_3^2")
        root2.move_to(root_group2[3])

        self.play(Transform(root_group2[1], root1),
                  Transform(root_group2[3], root2))
        self.wait(2)



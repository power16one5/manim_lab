from manim import *



class Function(Scene):
    def construct(self):
        every = VGroup()

        # 첫번째 줄 루트
        root_group1 = VGroup()
        root_group1.add(MathTex("x_1"))
        for text in "-x_1", "x_2", "-x_2":
            a = MathTex(text)
            a.next_to(root_group1[-1], RIGHT, buff=2)
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
        root_group2.add(MathTex("x_1^2"))
        a = MathTex("x_2^2")
        a.next_to(root_group2[-1], RIGHT, buff=4.5)
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
        self.wait(1)

        # 이동
        every.add(root_group1)
        self.play(every.animate.shift(UP))
        self.wait()

        # 세번째 줄 루트
        root_group3 = VGroup()
        root_group3.add(MathTex("x_1^4"))
        root_group3.next_to(root_group2, DOWN, buff=1)

        line_group2 = VGroup()
        for i, tex in enumerate(root_group2):
            a = Line(tex.get_center(), root_group3[i >> 1].get_center())
            a.set_length(a.get_length() * 0.4)
            line_group2.add(a)

        every.add(root_group3, line_group2)
        self.play(FadeIn(root_group3),
                  FadeIn(line_group2))
        self.wait(1)

        framebox1 = SurroundingRectangle(root_group2[1], buff=.1)
        self.play(Create(framebox1))
        self.wait(1)

        root1 = MathTex("-x_1^2")
        root1.move_to(root_group2[1])
        framebox2 = SurroundingRectangle(root1, buff=.1)
        self.play(Transform(root_group2[1], root1),
                  ReplacementTransform(framebox1, framebox2))
        self.wait(1)

        framebox3 = SurroundingRectangle(root_group1[2], buff=.1)
        framebox4 = SurroundingRectangle(root_group1[3], buff=.1)
        box_gruop1 = VGroup(framebox3, framebox4)
        self.play(ReplacementTransform(framebox2, box_gruop1))
        self.wait(1)

        root2, root3 = MathTex("x_1i"), MathTex("-x_1i")
        root2.move_to(root_group1[2]); root3.move_to(root_group1[3])
        framebox5 = SurroundingRectangle(root2, buff=.1)
        framebox6 = SurroundingRectangle(root3, buff=.1)
        box_gruop2 = VGroup(framebox5, framebox6)
        self.play(ReplacementTransform(box_gruop1, box_gruop2),
                  Transform(root_group1[2], root2),
                  Transform(root_group1[3], root3))
        self.wait(3)

        self.play(FadeOut(root_group1, root_group2, root_group3, box_gruop2))
        self.wait(1)

        root4 = MathTex("1")
        root4.move_to(root_group3[0])

        self.play(FadeIn(root4))
        self.wait(1)

        root_group4 = VGroup()
        for text in "1", "-1":
            a = MathTex(text)
            root_group4.add(a)

        for a, b in zip(root_group2, root_group4):
            b.move_to(a)

        self.play(FadeIn(root_group4))
        self.wait(1)

        root_group5 = VGroup()
        for text in "1", "-1", "i", "-i":
            a = MathTex(text)
            root_group5.add(a)

        for a, b in zip(root_group1, root_group5):
            b.move_to(a)

        self.play(FadeIn(root_group5))
        self.wait(1)
        self.wait(3)
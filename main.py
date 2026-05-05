from manim import *

class SceneName(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        text = Text("Hello, GitHub Actions!")
        self.play(Create(circle))
        self.play(Write(text))
        self.wait(1)

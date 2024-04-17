import random
from manim import *
FRAME_WIDTH=2048
FRAME_HEIGHT=1152


class MathFormulas(Scene):
    def construct(self):
        # Fondo
        

        # Lista de fórmulas matemáticas
        formulas = [
            MathTex("\\pi r^2", font_size=random.randint(6, 50)),
            MathTex("e^{i\\pi} + 1 = 0", font_size=random.randint(6, 50)),
            MathTex("F = ma", font_size=random.randint(6, 50)),
            MathTex("a^2 + b^2 = c^2", font_size=random.randint(6, 50)),
            MathTex("\\int_{a}^{b} f(x) \\,dx", font_size=random.randint(6, 50)),
            MathTex("\\frac{d}{dx}(uv) = u\\frac{dv}{dx} + v\\frac{du}{dx}", font_size=random.randint(6, 50)),
            MathTex("e = mc^2", font_size=random.randint(6, 50)),
            MathTex("x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}", font_size=random.randint(6, 50)),
            MathTex("\\sin^2(x) + \\cos^2(x) = 1", font_size=random.randint(6, 50)),
            MathTex("A = \\pi r^2", font_size=random.randint(6, 50)),
        ]

        # Colores de letra para las fórmulas
        colors = ["#FFA500", "#04febe"] * (len(formulas) // 2)

        # Asignar coordenadas a las fórmulas
        coordinates = []
        for i in range(len(formulas)):
            x = i - 5
            y = 5 - i
            coordinates.append((x, y))

 
        axes = Axes(
                    x_range=[-10, 10.3, 1],
                    y_range=[-1.5, 1.5, 1],
                    x_length=10,
                    axis_config={"color": GREEN},
                    x_axis_config={
                        "numbers_to_include": np.arange(-10, 10.01, 2),
                        "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
                    },
                    tips=False,
                )
        axes_labels = axes.get_axis_labels()
        sin_graph = axes.plot(lambda x: np.sin(x), color=colors[0])
        cos_graph = axes.plot(lambda x: np.cos(x), color=colors[1])

        sin_label = axes.get_graph_label(
            sin_graph, "\\sin(x)", x_val=-10, direction=UP / 2
        )
        cos_label = axes.get_graph_label(cos_graph, label="\\cos(x)")

        vert_line = axes.get_vertical_line(
            axes.i2gp(TAU, cos_graph), color=YELLOW, line_func=Line
        )
        line_label = axes.get_graph_label(
            cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
        )

        plot = VGroup(axes, sin_graph, cos_graph, vert_line)
        labels = VGroup(axes_labels, sin_label, cos_label, line_label)
        graf = VGroup(plot,labels)
        self.add(graf.scale(0.5))
        
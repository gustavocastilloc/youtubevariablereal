from manim import *

class Polynomial(Scene):
    def construct(self):
        # Add title
        title = Tex("¿Qué es una función polinomial?").scale(1.2)
        self.play(Write(title))
        self.wait(1)

        # Add polynomial equation
        equation = MathTex("f(x) = a_nx^n + a_{n-1}x^{n-1} + ... + a_1x + a_0").next_to(title, DOWN)
        self.play(Write(equation))
        self.wait(1)

        # Add explanation
        explanation = Text("Una función polinomial es una función matemática que puede ser representada por una ecuación polinómica, donde los coeficientes a_i son constantes y n es un número entero no negativo conocido como grado del polinomio.").scale(0.8).next_to(equation, DOWN)
        self.play(Write(explanation))
        self.wait(1)

        # Highlight coefficients and degree
        
        self.wait(1)

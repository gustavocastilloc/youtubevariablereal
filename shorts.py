from manim import *
Amarillo='#ddf599'
Morado = "#fe04f2"
Celeste = "#0ad6fb"
Rojo = "#fb0a4c"
RosaRed ="#fe0463"
VerdeClaro ="#04febe"
GREEN_SCREEN = '#00FF00'
class valordekya(Scene):
    def construct(self):
        tam=20
        enun0= Tex("Sean $a \in \mathbb R^+$ y la funcion ",font_size=tam).move_to(UP)
        enun1= Tex("$f: \mathbb R  \\rightarrow \mathbb R$ definida por",font_size=tam).next_to(enun0,DOWN)
        enun2 = MathTex(r"f(x)=\frac{kx-1}{x^2+a}",font_size=tam, color=VerdeClaro).next_to(enun1,DOWN)
        enun3 = Tex("Si el punto $P(1,2) \in f$,",font_size=tam).next_to(enun2,DOWN)
        enun4 = Tex("¿el valor numerico de",font_size=tam).next_to(enun3,DOWN)
        enun5 = Tex("$(2k-4a)$ es igual a?",font_size=tam).next_to(enun4,DOWN)
        sol= Tex("Solucion",font_size=tam+3).set_color(YELLOW)
        sol1 = Tex("Considerando $P(1,2) \in f$",font_size=tam).move_to(UP)
        sol2 = MathTex(r"2 = \frac{k-1}{1+a}",font_size=tam).next_to(sol1,DOWN)
        sol3 = MathTex(r"k=2a+3",font_size=tam).next_to(sol2,DOWN)
        sol4 = MathTex(r"(2k-4a)=?",font_size=tam).next_to(sol3,DOWN)
        sol5 = MathTex(r"2(2a+3)-4a=2k-4a",font_size=tam).next_to(sol4,DOWN)
        sol6 = MathTex(r"4a+6-4a=2k-4a",font_size=tam).next_to(sol5,DOWN)
        sol7 = MathTex(r"6=2k-4a",font_size=tam).next_to(sol6,DOWN)
        solucion = VGroup(sol1,sol2,sol3,sol4,sol5,sol6,sol7)
        framebox1 = SurroundingRectangle(solucion[-1], buff = .1)
        self.play(Write(enun0))
        self.play(Write(enun1))
        self.play(Write(enun2))
        self.play(Write(enun3))
        self.play(Write(enun4))
        self.play(Write(enun5))
        self.wait(2)
        self.clear()
        self.play(FadeIn(sol, shift=DOWN, scale=0.66))
        self.play(FadeOut(sol, scale=1.5))
        self.wait()
        for i in solucion:
            self.play(Write(i))
        self.play(
            Create(framebox1)
        )
        self.wait(3)

# http://www.dspace.espol.edu.ec/xmlui/bitstream/handle/123456789/55140/ExFinal%20V0F1.pdf?sequence=1&isAllowed=y
class funcioninversa1(Scene):
    def construct(self):
        tam=20
        enun0= Tex("Sean $f  \mathbb R \\rightarrow \mathbb R $",font_size=tam).move_to(UP)
        enun1= Tex("con regla de correspondencia ",font_size=tam).next_to(enun0,DOWN)


class DistanciaCircunferenciaParabola(Scene):
    def construct(self):
        tam=20
        # number_plane = NumberPlane(
        #     x_range=(-4, 4, 1),
        #     y_range=(-4, 4, 1),
        #     x_length=5,
        #     y_length=5,
        # )
        number_plane = NumberPlane()
        
        parabola = ImplicitFunction(
            lambda x, y: x**2-12*y+24,
            color=YELLOW
        )
        enun0= Tex("Se tiene una circunferencia ",font_size=tam).move_to(UP)
        enun1= Tex("cuya ecuacion es: $C:x^2+y^2=9$ ",font_size=tam).next_to(enun0,DOWN)
        enun2= Tex("y una parabola cuya ecuacion es: ",font_size=tam).next_to(enun1,DOWN)
        enun3= Tex("$P: x^2-12y+24=0$ Entonces, ",font_size=tam).next_to(enun2,DOWN)
        enun4= Tex("la distancia entre el centro ",font_size=tam).next_to(enun3,DOWN)
        enun5= Tex("de $C$ y el vertice de $P$ es?",font_size=tam).next_to(enun4,DOWN)
        enun6= Tex("Cual es la ",font_size=40).move_to(DOWN*2)
        enun7= Tex("distancia de la linea naranja",font_size=40).next_to(enun6,DOWN)
        meaning= Tex("En otras palabras",font_size=tam+3).set_color(YELLOW)
        sol= Tex("solucion",font_size=tam+3).set_color(YELLOW)
        sol1 = MathTex(r"x^2-12y+24=0",font_size=tam).move_to(UP*3)
        sol2 = MathTex(r"y=\frac{-24-x^2}{-12}",font_size=tam).next_to(sol1,DOWN)
        sol3 = Tex("Coord. $x$ vertice: $x=\\frac{-b}{2a}=0$",font_size=tam).next_to(sol2,DOWN)
        sol4 = Tex("Coord. $y$ vertice: $y=2$",font_size=tam).next_to(sol3,DOWN)
        sol5 = Tex("Vertice de $P$: $p1(0,2)$",font_size=tam).next_to(sol4,DOWN)
        sol6 = Tex("Centro de $C$: $p2(0,0)$",font_size=tam).next_to(sol5,DOWN)
        sol7 =Tex("Distancia entre dos puntos:",font_size=tam).next_to(sol6,DOWN)
        sol8 = MathTex(r"d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}",font_size=tam).next_to(sol7,DOWN)
        sol9 = MathTex(r"d=\sqrt{(0-0)^2+(2-0)^2}=2",font_size=tam).next_to(sol8,DOWN)
        sol10 = MathTex(r"d=2",font_size=tam).next_to(sol9,DOWN)
        
        enunciado = VGroup(enun0,enun1,enun2,enun3,enun4,enun5)
        punto1 = Dot(ORIGIN)
        punto2 = Dot(number_plane.coords_to_point(0,2))
        line = Line(punto1.get_center(), punto2.get_center()).set_color(ORANGE)
        b1 = BraceBetweenPoints([0,0,0],[0,2,0])
        grafico = VGroup(parabola,Circle(radius=3.0),punto1,punto2,VGroup(enun6,enun7),line,b1).scale(.5)
        solucion = VGroup(sol1,sol2,sol3,sol4,sol5,sol6,sol7,sol8,sol9,sol10)
        framebox1 = SurroundingRectangle(solucion[-1], buff = .1)
        for i in enunciado:
            self.play(Write(i),run_time=2)
        self.wait(2)
        self.clear()
        self.play(FadeIn(meaning, shift=DOWN, scale=0.66))
        self.play(FadeOut(meaning, scale=1.5))
        for i in grafico:
            self.play(Write(i),run_time=1)
        self.wait(2)
        self.clear()
        self.play(FadeIn(sol, shift=DOWN, scale=0.66))
        self.play(FadeOut(sol, scale=1.5))
        self.wait()
        for i in solucion:
            self.play(Write(i),run_time=2)
        self.play(
            Create(framebox1)
        )
        self.wait()
import math
class Short3(Scene):
    def grafica(self):
        ax = Axes(
            x_range=[-50, 50,7],
            y_range=[-50, 50,7],
            x_length=10,
            y_length=10,
            axis_config={"include_numbers": True},
           
            tips=False,
        )
        original = ax.plot(lambda x: math.log(x+2, 3) -2, color=BLUE, x_range=[7, 50])
        inversa = ax.plot(lambda x:  3**(x+2) -2,color=ORANGE,x_range=[0, 10])
        identidad = ax.plot(lambda x:  x,color=GREEN,x_range=[-50, 50])
        original_label =MathTex(r"f(x)",font_size=24,color=BLUE).move_to(ax.c2p(10,5))
        inversa_label = MathTex(r"f^{-1}(x)",font_size=24,color=ORANGE).move_to(ax.c2p(-7,17))
        graf = VGroup(ax,VGroup(original,original_label),VGroup(inversa,inversa_label),identidad)
        return graf
    def enunciado(self):
        tam=20
        enun0 = Tex("Si $f$ es una función de variable",font_size=tam)
        enun1= Tex(" real invertible y definida por ",font_size=tam)
        enun2= MathTex(r"f(x)=\log_{3}{(x+2)}-2, \ x \geqslant 7",font_size=tam,color=VerdeClaro)
        enun3 = Tex("entonces la regla de correspondencia", font_size=tam)
        enun4 = Tex("de la funcion inversa de $f$ es:", font_size=tam)
        enunciado = VGroup(enun0,enun1,enun2,enun3,enun4).arrange(DOWN,center=True)
        return enunciado
    def desarrollo(self):
        tam=20
        des0 = MathTex(r"y=\log_{3}{(x+2)}-2, \ x \geqslant 7",font_size=tam)
        des1 = MathTex(r"x= \log_{3}{(y+2)}-2",font_size=tam)
        des2 = MathTex(r"x+2 = \log_{3}{(y+2)}",font_size=tam)
        des3 = MathTex(r"3^{x+2}= 3^{\log_{3}{(y+2)}}",font_size=tam)
        des4 = MathTex(r"3^{x+2}= y+2",font_size=tam)
        des5 = MathTex(r"y=3^{x+2}-2",font_size=tam,color=ORANGE)
        des6 = Tex("Considerando que es biyectiva", font_size=tam,color=YELLOW)
        des7 = MathTex(r"dom f^{-1} = rg(f)",font_size=tam,color=VerdeClaro)
        des8 = MathTex(r"si \ x=7 \rightarrow f(7)= \log_{3}{(7+2)}-2=0",font_size=tam)
        des9 = MathTex(r"dom f^{-1} : x \geqslant 0",font_size=tam)
        desarrollo= VGroup(des0,des1,des2,des3,des4,des5,des6,des7,des8,des9).arrange(DOWN,center=True)
        return desarrollo
    def respuestas(self):
        tam=20
        res0 = MathTex(r"f^{-1}(x)=3^{x+2}-2, \ x \geqslant 7",font_size=tam)
        res1 = MathTex(r"f^{-1}(x)=3^{x+2}+2, \ x \geqslant 0",font_size=tam)
        res2 = MathTex(r"f^{-1}(x)=3^{x-2}-2, \ x \geqslant 0",font_size=tam)
        res3 = MathTex(r"f^{-1}(x)=3^{x+2}+2, \ x \geqslant 7",font_size=tam)
        res4 = MathTex(r"f^{-1}(x)=3^{x+2}-2, \ x \geqslant 0",font_size=tam)
        respuestas= VGroup(res0,res1,res2,res3,res4).arrange(DOWN,center=False, aligned_edge=LEFT)
        return respuestas
    def construct(self):
        enunciado = self.enunciado().move_to(UP)
        respuestas1 = self.respuestas().next_to(enunciado,DOWN)
        desarrollo = self.desarrollo().move_to(UP)
        graf = self.grafica()
        interr = MathTex(r"?",font_size=92,color=RED).rotate(PI/6)
        respuesta =  MathTex(r"f^{-1}(x)=3^{x+2}-2, \ x \geqslant 0",font_size=30).next_to(desarrollo,DOWN)
        sol= Tex("Solucion",font_size=26).set_color(YELLOW)
        framebox1 = SurroundingRectangle(respuesta, buff = .1)
        for i in enunciado:
            self.play(Create(i),run_time=1)
        self.wait(3)
        for i in respuestas1:
            self.play(Create(i),run_time=1)
        self.play(FadeIn(interr))
        self.wait(3)
        self.play(Unwrite(respuestas1),FadeOut(interr))
        self.clear()
        self.play(FadeIn(sol, shift=DOWN, scale=0.66))
        self.play(FadeOut(sol, scale=1.5))
        self.wait(1.5)
        for i in desarrollo:
            self.play(Create(i),run_time=1)
        self.wait(1)
        self.play(Create(respuesta))
        self.play(Create(framebox1))
        self.clear()
        for i,shape in enumerate(graf):
            if i==3:
                self.wait(3)
                self.play(Create(shape))
            else:
                self.play(Create(shape))
                self.wait()
        self.wait(3)
class Short4(MovingCameraScene):
    def enungrafica(self):
        ax=NumberPlane(
            x_range=(-50, 50, 1),
            y_range=(-50,50,1),
             background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
            
        ).add_coordinates()
        elipse = ParametricFunction(lambda t: np.array([
            5 + 5 * np.cos(t),
            -3 + 4 * np.sin(t),
            0
        ]), color=BLUE_D, t_range=[0, 2*PI], stroke_width=4)
        
        circle = ParametricFunction(lambda t: np.array([
            5 + 5 * np.cos(t),
            -3 + 5 * np.sin(t),
            0
        ]), color=ORANGE, t_range=[0, 2*PI], stroke_width=4)
        elipse_tex = MathTex(r"\frac{(x-5)^2}{25} + \frac{(y+3)^2}{16}=1", font_size=42,color=BLUE_D).move_to(ax.c2p(5,5))
        circle_tex = MathTex(r"x^2+y^2+Dx+Ey+F=0 \ ??? ", font_size=42,color=ORANGE).move_to(ax.c2p(5,3.5))
        v1 = Dot(ax.c2p(0,-3)).scale(1.5).set_color(VerdeClaro)
        v2 = Dot(ax.c2p(10,-3)).scale(1.5).set_color(VerdeClaro)
        v1_tex = MathTex(r"V_{1}",color=VerdeClaro,font_size=42).next_to(v1,LEFT)
        v2_tex = MathTex(r"V_{2}",color=VerdeClaro,font_size=42).next_to(v2,RIGHT)
        vertices =VGroup(v1,v2,v1_tex,v2_tex)
        graf = VGroup(ax,elipse,elipse_tex,vertices,circle,circle_tex)
        return graf
    def solucgrafica(self):
        ax=NumberPlane(
            x_range=(-50, 50, 1),
            y_range=(-50,50,1),
             background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
            
        ).add_coordinates()
        elipse = ParametricFunction(lambda t: np.array([
            5 + 5 * np.cos(t),
            -3 + 4 * np.sin(t),
            0
        ]), color=BLUE_D, t_range=[0, 2*PI], stroke_width=4)
        
        circle = ParametricFunction(lambda t: np.array([
            5 + 5 * np.cos(t),
            -3 + 5 * np.sin(t),
            0
        ]), color=ORANGE, t_range=[0, 2*PI], stroke_width=4)
        elipse_tex = MathTex(r"\frac{(x-5)^2}{25} + \frac{(y+3)^2}{16}=1", font_size=32,color=BLUE_D).move_to(ax.c2p(5,3))
        circle_tex = MathTex(r"x^2+y^2+Dx+Ey+F=0 \ ??? ", font_size=35,color=ORANGE).move_to(ax.c2p(5,3.5))
        punto=Dot(ax.c2p(5,-3),color=BLUE_D).scale(1.5)
        radio = Line(ax.c2p(5,-3),ax.c2p(10,-3)).set_color(ORANGE)
        centro_elipse_tex =Tex("Centro $O(5,-3)$",font_size=35).next_to(punto,DOWN)
        centro_O_text = MathTex(r"O(h,k)",font_size=42,color=BLUE_D).next_to(punto,UP)
        radio_text = Tex("radio circunferencia: $r=a$",font_size=35,color=ORANGE).move_to(ax.c2p(5,-4))
        v1 = Dot(ax.c2p(0,-3)).scale(1.5).set_color(VerdeClaro)
        v2 = Dot(ax.c2p(10,-3)).scale(1.5).set_color(VerdeClaro)
        v1_tex = MathTex(r"V_{1}",color=VerdeClaro,font_size=42).next_to(v1,LEFT)
        v2_tex = MathTex(r"V_{2}",color=VerdeClaro,font_size=42).next_to(v2,RIGHT)
        vertices =VGroup(v1,v2,v1_tex,v2_tex)
        graf = VGroup(ax,elipse,elipse_tex,VGroup(punto,centro_elipse_tex,centro_O_text),vertices,VGroup(radio,radio_text))
        return graf
    def enunciado(self):
        tam=20
        enun0 = Tex("La ecuación general de la ",font_size=tam)
        enun1= Tex(" circunferencia cuyo centro corresponde",font_size=tam)
        enun2= Tex("al centro de la elipse:",font_size=tam)
        enun3 = MathTex(r"\frac{(x-5)^2}{25} + \frac{(y+3)^2}{16}=1", font_size=tam+3,color=VerdeClaro)
        enun4 = Tex("y contiene a los vértices de la elipse, es:", font_size=tam)
        enunciado = VGroup(enun0,enun1,enun2,enun3,enun4).arrange(DOWN,center=True)
        return enunciado
    def respuestas(self):
        tam=20
        res0 = MathTex(r"a) x^2+y^2+10x+6y+9=0",font_size=tam)
        res1 = MathTex(r"b) x^2+y^2-10x-6y+9=0",font_size=tam)
        res2 = MathTex(r"c) x^2+y^2+10x-6y+9=0",font_size=tam)
        res3 = MathTex(r"d) x^2+y^2-10x+6y+9=0",font_size=tam)
        res4 = MathTex(r"e) x^2+y^2-10x+6y-9=0",font_size=tam)
        respuestas= VGroup(res0,res1,res2,res3,res4).arrange(DOWN,center=False, aligned_edge=LEFT)
        return respuestas
    def desarrollo(self):
        tam=25
        des0 = MathTex(r"\frac{(x-h)^2}{a^2} + \frac{(y-k)^2}{b^2}=1",font_size=tam)
        des1 = MathTex(r"x^2+y^2+Dx+Ey+F=0",font_size=tam)
        des2 = MathTex(r"\frac{(x-5)^2}{25} + \frac{(y+3)^2}{16}=1",font_size=tam)
        des3 = MathTex(r"Centro \ O(h,k)=O(5,-3)",font_size=tam)
        des4 = MathTex(r"D=-2h, \ E=-2k, \\ F=h^2+k^2-r^2",font_size=tam)
        des5 = MathTex(r"D=-2(5), \ E=-2(-3), \\ F=5^2+3^2-5^2",font_size=tam,color=ORANGE)
        des6 = MathTex(r"D=-10, \ E=6,  \ F=9 ", font_size=tam,color=YELLOW)
        # des7 = MathTex(r"x^2+y^2-10x+6y+9=0",font_size=tam,color=VerdeClaro)
        des8 = MathTex(r"",font_size=tam)
        des9 = MathTex(r"",font_size=tam)
        desarrollo= VGroup(des0,des1,des2,des3,des4,des5,des6).arrange(DOWN,center=True)
        return desarrollo

    def construct(self):
        self.camera.frame.save_state()
        enunciado = self.enunciado().move_to(UP)
        respuestas = self.respuestas().next_to(enunciado,DOWN)
        enungraf = self.enungrafica().scale(0.3)
        solucgraf= self.solucgrafica().scale(0.3)
        desarrollo = self.desarrollo().move_to(UP)
        preintro = Text("Es decir", font_size=32,color=BLUE)
        respuesta =  MathTex(r"x^2+y^2-10x+6y+9=0",font_size=30).next_to(desarrollo,DOWN)
        sol= Tex("Solución",font_size=26).set_color(YELLOW)
        framebox1 = SurroundingRectangle(respuesta, buff = .1)
        for i in enunciado:
            self.play(Create(i),run_time=1)
        self.wait(3)
        for i in respuestas:
            self.play(Create(i),run_time=1)
        self.wait(3)
        self.clear()
        self.play(Write(preintro, reverse=True, remover=False))
        self.play(Unwrite(preintro))
        self.play(self.camera.frame.animate.move_to(enungraf[1]),run_time=1)
        for i in enungraf:
            self.play(Create(i))
        self.wait(3)
        self.clear()
        self.play(Restore(self.camera.frame))
        self.play(FadeIn(sol, shift=DOWN, scale=0.66))
        self.play(FadeOut(sol, scale=1.5))
        self.play(self.camera.frame.animate.move_to(solucgraf[1]),run_time=1)
        self.play(Create(solucgraf))
        self.wait(3)
        self.clear()
        self.play(Restore(self.camera.frame))
        for i in desarrollo:
            self.play(Create(i))
            self.wait(1)
        self.wait(1)
        self.play(Create(respuesta))
        self.play(Create(framebox1))
        self.wait(3)

class Short5(MovingCameraScene):
    def grafica(self):
        tam=38
        ax = Axes(
            x_range=[-10, 3],
            y_range=[-3, 3],
            x_length=4, y_length=2,
            x_axis_config={"numbers_to_include": [-8, -2,1]},
            tips=False,
        )
        inter1 = MathTex(r")(",font_size=42,color=ORANGE,stroke_width=2).move_to(ax.c2p(-8,0))
        inter2 = MathTex(r")(",font_size=42,color=ORANGE,stroke_width=2).move_to(ax.c2p(-2,0))
        inter3 = MathTex(r")(",font_size=42,color=ORANGE,stroke_width=2).move_to(ax.c2p(1,0))
        infinitos = VGroup(MathTex(r"-\infty",font_size=32,color=VerdeClaro).move_to(ax.c2p(-11,0)),MathTex(r"+\infty",font_size=32,color=VerdeClaro).move_to(ax.c2p(4,0)))
        intervalos = VGroup(inter1,inter2,inter3)
        fase1 = VGroup(
            MathTex(r"-",color=RED,font_size=tam,stroke_width=3).move_to(ax.c2p(-9,0.1)),
            MathTex(r"+",color=BLUE_D,font_size=tam,stroke_width=3).move_to(ax.c2p(-6,0.1)),
            MathTex(r"+",color=BLUE_D,font_size=tam,stroke_width=3).move_to(ax.c2p(-1,0.1)),
            MathTex(r"+",color=BLUE_D,font_size=tam,stroke_width=3).move_to(ax.c2p(2,0.1)),
        )
        fase2 = VGroup(
            MathTex(r"-",color=RED,font_size=tam,stroke_width=3).move_to(ax.c2p(-10,0.1)),
            MathTex(r"-",color=RED,font_size=tam,stroke_width=3).move_to(ax.c2p(-5,0.1)),
            MathTex(r"+",color=BLUE_D,font_size=tam,stroke_width=3).move_to(ax.c2p(0,0.1)),
            MathTex(r"+",color=BLUE_D,font_size=tam,stroke_width=3).move_to(ax.c2p(3,0.1)),
        )
        fase3 = VGroup(
            MathTex(r"-",color=RED,font_size=tam,stroke_width=3).move_to(ax.c2p(-9.5,0.2)),
            MathTex(r"-",color=RED,font_size=tam,stroke_width=3).move_to(ax.c2p(-4,0.1)),
            MathTex(r"-",color=RED,font_size=tam,stroke_width=3).move_to(ax.c2p(-0.5,0.2)),
            MathTex(r"+",color=BLUE_D,font_size=tam,stroke_width=3).move_to(ax.c2p(2.5,0.2)),
        )
        signos = VGroup(
            MathTex(r"-",color=RED,font_size=tam,stroke_width=3).move_to(ax.c2p(-9.5,0.1)),
            MathTex(r"+",color=BLUE_D,font_size=tam,stroke_width=3).move_to(ax.c2p(-5,0.1)),
            MathTex(r"+",color=BLUE_D,font_size=tam,stroke_width=3).move_to(ax.c2p(2.5,0.1)),
            MathTex(r"-",color=RED,font_size=tam,stroke_width=3).move_to(ax.c2p(-0.5,0.1)),
        )
        fases = VGroup(fase1,fase2,fase3)
        grafica = VGroup(ax,intervalos,infinitos,fases,signos)
        return grafica
    def enunciado(self):
        tam=22
        enun0 = Tex("Sea Re = $\mathbb{R}$ y el predicado",font_size=tam)
        enun1= MathTex(r"p(x)=\frac{x^2+10x+16}{(x-1) |x-1| (x^2+1) } > 0 ",font_size=tam+2)
        enun2= Tex("el conjunto de verdad $Ap(x)$",font_size=tam)
        enun3 = Tex("es el intervalo:", font_size=tam)
        enunciado = VGroup(enun0,enun1,enun2,enun3).arrange(DOWN,center=True)
        return enunciado
    def respuestas(self):
        tam=23
        res0 = MathTex(r"a) \ (-8,-2) \cup (1,+\infty)",font_size=tam)
        res1 = MathTex(r"b) \ [-2,1]",font_size=tam)
        res2 = MathTex(r"c) \ (-2,-\infty)",font_size=tam)
        res3 = MathTex(r"d) \ (-8,1)",font_size=tam)
        res4 = MathTex(r"e) \ (-\infty,-8) \cup (-2,1) ",font_size=tam)
        respuestas= VGroup(res0,res1,res2,res3,res4).arrange(DOWN,center=False, aligned_edge=LEFT)
        return respuestas
    def desarrollo(self):
        tam=22
        des0 = VGroup(Tex("Considero",font_size=tam),MathTex(r"x-1 \neq 0",font_size=tam)).arrange(RIGHT)
        des1 = MathTex(r"Entonces \ x \neq 1",font_size=tam)
        des2 = MathTex(r"x^2+10x+16=0",font_size=tam)
        des3 = MathTex(r"(x+8)(x+2)=0",font_size=tam)
        des4 = Tex("Mis puntos Críticos son:",font_size=tam-2)
        des5 = MathTex(r"x=1,x=-8,x=-2",font_size=tam,color=BLUE_D,stroke_width=2)
        des6 = MathTex(r"", font_size=tam,color=YELLOW)
        # des7 = MathTex(r"x^2+y^2-10x+6y+9=0",font_size=tam,color=VerdeClaro)
        des8 = MathTex(r"",font_size=tam)
        des9 = MathTex(r"",font_size=tam)
        desarrollo= VGroup(des0,des1,des2,des3,des4,des5).arrange(DOWN,center=True)
        return desarrollo
    def construct(self):
        self.camera.frame.save_state()
        enunciado = self.enunciado().move_to(UP)
        respuestas = self.respuestas().next_to(enunciado,DOWN).set_color(Amarillo)
        desarrollo = self.desarrollo()
        grafica = self.grafica()
        respuesta =  MathTex(r"a) \ (-8,-2) \cup (1,+\infty)",font_size=32).move_to([0,-2,0])
        sol= Tex("Solución",font_size=26).set_color(YELLOW)
        framebox1 = SurroundingRectangle(respuesta, buff = .1)
        for i in enunciado:
            self.play(Create(i),run_time=1)
        self.wait(3)
        for i in respuestas:
            self.play(Create(i),run_time=1)
        self.wait(3)
        self.clear()
        self.play(FadeIn(sol, shift=DOWN, scale=0.66))
        self.play(FadeOut(sol, scale=1.5))
        for i in desarrollo:
            self.play(Create(i),run_time=1)
        self.wait(2)
        self.clear()
        for i, shape in enumerate(grafica):
            if i==3:
                self.camera.frame.scale(0.5)
                for i in shape:
                    # self.play(Create(i))
                    for s in i:
                        self.play(self.camera.frame.animate.move_to(s),run_time=1)
                        self.play(Create(s))
                    self.wait(1)
            elif i==4:
                self.play(Restore(self.camera.frame))
                self.play(Transform(grafica[3], shape))
                self.wait(2)
            else:
                self.play(Create(shape))
        self.wait(2)
        self.play(Create(respuesta))
        self.play(Create(framebox1))
        self.wait(3)

class Short6(Scene):
    def enunciado(self):
        tam=20
        enun0 = Tex("Si 10 Obreros pueden hacer un trabajo",font_size=tam)
        enun1= Tex("en 24 días. La cantidad de obreros de",font_size=tam)
        enun2= Tex("igual rendiemiento que se necesitarán",font_size=tam)
        enun3 = Tex("para hacer un trabajo de 7 veces más", font_size=tam)
        enun4 = Tex("considerable, en un tiempo de un 1/5", font_size=tam)
        enun5 = Tex("de lo anterior es:", font_size=tam)
        enunciado = VGroup(enun0,enun1,enun2,enun3,enun4,enun5).arrange(DOWN,center=True)
        return enunciado
        
    def analisis(self):
        tam=20
        enun0 = Tex("Si aumenta la dificultad ",font_size=tam)
        enun1= Tex("se requieren mas obreros. ",font_size=tam)
        enun2= Tex("Si hay menos dias para hacer",font_size=tam)
        enun3 = Tex("el trabajo, se requerirán más", font_size=tam)
        enun4 = Tex("obreros.", font_size=tam)
        #enun3 = Tex("de lo anterior es:", font_size=tam)
        enunciado = VGroup(enun0,enun1,enun2,enun3,enun4).arrange(DOWN,center=True)
        return enunciado
    def desarrollo(self):
        tam=27
        t0 = Table(
            [["24", "1"],
            ["24/5","7"]],
            row_labels=[Text("10"), Text("x")],
            col_labels=[Text("dias"), Text("dificultad")],
            top_left_entry=Text("Obreros"))
        
        t0.add_highlighted_cell((3,1), color=GREEN)
        des1= MathTex(r"\frac{10}{x}=\frac{\frac{24}{5}}{24} \cdot \frac{1}{7} ",font_size=tam)
        des2= MathTex(r"x= 10 \cdot 7 \cdot 5  ",font_size=tam)
        des3= MathTex(r"x= 350",font_size=tam)
        lista = VGroup(t0.scale(0.4),des1,des2,des3).arrange(DOWN,center=True)
        return lista
    def construct(self):
        enunciado = self.enunciado().move_to(UP)
        analisis = self.analisis().move_to(UP)
        desarrollo = self.desarrollo().move_to(UP)
        sol= Tex("Solución",font_size=26).set_color(YELLOW)
        for i in enunciado:
            self.play(Create(i),run_time=1)
        self.wait(3)
        self.clear()
        self.play(FadeIn(sol, shift=DOWN, scale=0.66))
        self.play(FadeOut(sol, scale=1.5))
        for i in analisis:
            self.play(Create(i),run_time=1)
        self.wait(3)
        self.play(Unwrite(analisis))
        for i in desarrollo:
            self.play(Create(i),run_time=1)
        self.wait(3)
class Short7(Scene):
    def grafica(self):
        ax=NumberPlane(
            x_range=(-10, 10, 1),
            y_range=(-2,2,1),
             background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            },
            y_length=5,
            x_length=10,
            
        ).add_coordinates()
        func = lambda x : 1/((x-3)*(x+2))
        funcion = ax.plot(
            func,
            discontinuities=[-2, 3],  # discontinuous points
            dt=0.07,  # left and right tolerance of discontinuity
            color=BLUE_D,
           
            )
        return VGroup(ax,funcion)
    def enunciado(self):
        tam=20
        enun0 = Tex("Dada la función de variable real",font_size=tam)
        enun1= MathTex(r"f(x)=\frac{(x-1)(x^2+x+1)}{(x^2-x-6)(x^3-1)}",font_size=tam)
        enun2= Tex("¿La proposicion FALSA es?",font_size=tam,color=YELLOW)
        
        enunciado = VGroup(enun0,enun1,enun2).arrange(DOWN,center=True)
        return enunciado
    def respuestas(self,tam):
        res0 = VGroup(Tex("a) La función tiene una asíntota vertical ",font_size=tam),Tex("y dos asintotas horizontales",font_size=tam)).arrange(DOWN,center=False,aligned_edge=LEFT)
        res1 = VGroup(Tex("b) La funcion tiene una asintota horizontal",font_size=tam),Tex("y dos asintotas verticales",font_size=tam)).arrange(DOWN,center=False,aligned_edge=LEFT)
        res2 = VGroup(Tex("c) Cuando $x$  tiende a $\infty $, el valor de",font_size=tam),Tex("$f(x)$ es muy cercano a cero.",font_size=tam)).arrange(DOWN,center=False,aligned_edge=LEFT)
        res3 = VGroup(Tex("d) La funcion tiene una asintota",font_size=tam),Tex("vertical en $x=-2$",font_size=tam)).arrange(DOWN,center=False,aligned_edge=LEFT)
        res4 = VGroup(Tex("e) Cuando el valor de $x$ esta muy,",font_size=tam),Tex("cercano a 3, el rango de la funcion",font_size=tam),Tex("es un valor que tiende a infinito ",font_size=tam)).arrange(DOWN,center=False,aligned_edge=LEFT)
        respuestas= VGroup(res0,res1,res2,res3,res4)
        return respuestas
    def desarrollo(self):
        tam=18
        des0 = MathTex(r"f(x)=\frac{(x-1)(x^2+x+1)}{(x^2-x-6)(x^3-1)}",font_size=tam)
        des1 = MathTex(r"f(x)=\frac{(x-1)(x^2+x+1)}{(x-3)(x+2)(x-1)(x^2+x+1)}",font_size=tam)
        des2 = MathTex(r"f(x)=\frac{1}{(x-3)(x+2)}",font_size=tam)
        des3 = Tex("Asintotas Verticales:",font_size=tam,color=YELLOW)
        des4 = MathTex(r"(x-3)(x+2) \neq 0",font_size=tam)
        des5 = MathTex(r"x=3 \ x=-2 ",font_size=tam,color=ORANGE)
        des6 = Tex("Asintotas Horizontales:", font_size=tam,color=YELLOW)
        des7 = MathTex(r"\lim_{x \to \infty } \frac{1}{(x-3)(x+2)}  =0",font_size=tam)
        des8 = Tex("Literal e)",font_size=tam)
        des9 = MathTex(r"\lim_{x \to 3 } \frac{1}{(x-3)(x+2)}  = \infty",font_size=tam)
        desarrollo= VGroup(des0,des1,des2,des3,des4,des5,des6,des7,des8,des9).arrange(DOWN,center=True)
        return desarrollo
    def construct(self):
        enunciado = self.enunciado().move_to(UP*2)
        respuestas = self.respuestas(20).next_to(enunciado,DOWN).set_color(BLUE_B)
        desarrollo = self.desarrollo().move_to(UP)
        sol= Text("Solucion",font_size=20,font='Akira Expanded')
        respuesta =  VGroup( 
            Tex("¿La proposicion FALSA es?",font_size=22,color=YELLOW),
            VGroup(Tex("a) La función tiene una asíntota vertical ",font_size=20),Tex("y dos asintotas horizontales",font_size=20)).arrange(DOWN,center=False,aligned_edge=LEFT)
        ).arrange(DOWN,center=True)
        framebox1 = SurroundingRectangle(respuesta[1], buff = .1)
        grafica = self.grafica()
        for i in enunciado:
            self.play(Create(i),run_time=1)
        self.wait(3)
        for i in range(len(respuestas)-1):
            if i==0:
                self.play(Create(respuestas[0]))
                self.wait(3)
                self.play(Transform(respuestas[0],respuestas[i+1]),run_time=1)
                self.wait(3)
            else:
                self.play(Transform(respuestas[0],respuestas[i+1]),run_time=1)
                self.wait(3)
            
        self.wait(3)
        self.clear()
        self.play(FadeIn(sol, shift=DOWN, scale=0.66))
        self.play(FadeOut(sol, scale=1.5))
        self.wait(1)
        for i in desarrollo:
            self.play(Create(i),run_time=1)
        self.wait(3)
        self.play(Unwrite(desarrollo))
        for i in respuesta:
            self.play(Create(i),run_time=2)
            self.wait(2)
        self.play(Create(framebox1))
        self.wait(2)
        self.clear()
        self.play(Create(grafica))
        self.wait(3)


class Short8(Scene):
    def enunciado(self):
        tam=22
        enun0 = MathTex(r"Sea \  f : \mathbb{R} \rightarrow  \mathbb{R} ",font_size=tam,color=Amarillo)
        enun1= MathTex(r"f(x)=\begin{cases} 3x-6, &  |x-2|<3 \\0, & x\geqslant 5  \vee x\leqslant -1   \end{cases}",font_size=tam+2)
        enun2= Tex("Entonces,la regla de correspondencia de ",font_size=tam,color=Amarillo)
        enun3 = MathTex(r"3-f(3-x) ", font_size=tam+3)
        enun4= Tex("es:",font_size=tam,color=Amarillo)
        enunciado = VGroup(enun0,enun1,enun2,enun3,enun4).arrange(DOWN,center=True)
        return enunciado
    def soltext(self):
        sol= Text("Solucion",font_size=20,font='Akira Expanded').set_color(YELLOW)
        self.play(FadeIn(sol, shift=DOWN, scale=0.66))
        self.play(FadeOut(sol, scale=1.5))
    def desarrollo(self):
        tam=20
        des0 = MathTex(r" =\begin{cases} 3-[3(3-x)-6], &  |(3-x)-2|<3 \\3, & 3-x\geqslant 5  \vee 3-x\leqslant -1   \end{cases}",font_size=tam)
        des1 = MathTex(r"=\begin{cases} 3-[9-3x-6], &  |1-x|<3 \\3, &  x \leqslant-2 \vee x \geqslant 4   \end{cases}",font_size=tam)
        des2 = MathTex(r"=\begin{cases} 3x, &  |-(x-1)|<3 \\3, &  -2 \geqslant x \geqslant 4   \end{cases}",font_size=tam+2)
        des3 = MathTex(r"=\begin{cases} 3x, &  |x-1|<3 \\3, &   -3 \geqslant x-1 \geqslant 3   \end{cases}",font_size=tam+2)
        des4 = MathTex(r"=\begin{cases} 3x, &  |x-1|<3 \\3, &   |x-1| \geqslant 3   \end{cases}",font_size=tam+2)
        desarrollo= VGroup(des0,des1,des2,des3,des4)
        return desarrollo
    def construct(self):
        enunciado = self.enunciado().move_to(UP)
        enunciadocopy = self.enunciado().move_to(UP)
        # respuestas = self.respuestas(20).next_to(enunciado,DOWN).set_color(BLUE_B)
        desarrollo = self.desarrollo().next_to(enunciadocopy,DOWN)
        framebox1 = SurroundingRectangle(desarrollo[-1], buff = .1)

        for i in enunciado:
            self.play(Create(i))
        self.wait(3)
        self.clear()
        self.soltext()
        self.add(enunciadocopy)
        self.wait(2)
        for i in range(len(desarrollo)-1):
            if i==0:
                self.play(Create(desarrollo[0]))
                self.wait(2)
                self.play(Transform(desarrollo[0],desarrollo[i+1]))
                self.wait(2)
            else:
                self.play(Transform(desarrollo[0],desarrollo[i+1]))
                self.wait(2)
        self.play(Create(framebox1))
        self.wait(2)
        self.wait(3)

class Short9(Scene):
    def enunciado(self):
        tam=22
        enun0 = Tex("Despues de simplificar la expresion algebraica",font_size=tam-2,color=GREEN)
        enun1= MathTex(r"\left(\frac{x^3y-x^2y^2+xy^3}{2x^3y^2-x^2y^3}\right)^{-1}} \div \frac{2x^2+xy-y^2}{x^3+y^3} ",font_size=tam)
        enun2= Tex("Se obtiene: ",font_size=tam,color=Amarillo)
        enunciado = VGroup(enun0,enun1,enun2).arrange(DOWN,center=True)
        return enunciado
    def soltext(self):
        sol= Text("Solucion",font_size=20,font='Akira Expanded').set_color(YELLOW)
        self.play(FadeIn(sol, shift=DOWN, scale=0.66))
        self.play(FadeOut(sol, scale=1.5))
    def respuestas(self):
        tam=22
        res0 = MathTex(r"a) \ x+y",font_size=tam)
        res1 = MathTex(r"b) \ xy",font_size=tam)
        res2 = MathTex(r"c) \ x",font_size=tam)
        res3 = MathTex(r"d) \ y",font_size=tam)
        res4 = MathTex(r"e) \ 1",font_size=tam)
        respuestas= VGroup(res0,res1,res2,res3,res4).arrange(DOWN,center=False, aligned_edge=LEFT)
        return respuestas
    def desarrollo(self):
        tam=23
        des0 = MathTex(r"\left(\frac{x^3y-x^2y^2+xy^3}{2x^3y^2-x^2y^3}\right)^{-1}} \div \frac{2x^2+xy-y^2}{x^3+y^3} ",font_size=tam-3)
        des1 = MathTex(r"\frac{\left(\frac{x^3y-x^2y^2+xy^3}{2x^3y^2-x^2y^3}\right)^{-1}}{\frac{2x^2+xy-y^2}{x^3+y^3}}", font_size=tam+5).scale(1.3)
        des2 = MathTex(r"\frac{ \frac{2x^3y^2-x^2y^3} {x^3y-x^2y^2+xy^3} }  { \frac{2x^2+xy-y^2} {x^3+y^3} }",font_size=tam+5).scale(1.3)
        des3 = MathTex(r"\frac{(2x^3y^2-x^2y^3) (x^3+y^3)} {(x^3y-x^2y^2+xy^3)(2x^2+xy-y^2) }",font_size=tam)
        des4 = MathTex(r"\frac{x^2y^2(2x-y)(x^3+y^3)} {xy(x^2-xy+y^2)[2x(x+y)-y(x+y)]}",font_size=tam)
        des5 = MathTex(r"\frac{x^2y^2(2x-y)(x^3+y^3)} {xy(x^2-xy+y^2)(x+y)(2x-y)}",font_size=tam)
        des6 = MathTex(r"\frac{xy(x^3+y^3)} {(x^2-xy+y^2)(x+y)}", font_size=tam)
        des7 = MathTex(r"\frac{xy(x^3+y^3)} {x^3+y^3}",font_size=tam)
        des8 = MathTex(r"xy",font_size=tam)
        desarrollo= VGroup(des0,des1,des2,des3,des4,des5,des6,des7,des8)
        return desarrollo
    def construct(self):
        enunciado = self.enunciado().move_to(UP)
        respuestas= self.respuestas().next_to(enunciado,DOWN)
        desarrollo = self.desarrollo()
        framebox1 = SurroundingRectangle(desarrollo[-1], buff = .1)
        for i in enunciado:
            self.play(Create(i))
        self.wait(1)
        for i in respuestas:
            self.play(Create(i))
        self.wait(1)
        self.clear()
        self.soltext()
        for i in range(len(desarrollo)-1):
            if i==0:
                self.play(Create(desarrollo[0]))
                self.wait(2)
                self.play(Transform(desarrollo[0],desarrollo[i+1]))
                self.wait(2)
            else:
                self.play(Transform(desarrollo[0],desarrollo[i+1]))
                self.wait(3)
        self.play(Create(framebox1))
        self.wait(3)


class Short10(Scene):
    def enunciado(self):
        tam=22
        enun0 = MathTex(r"Si \  \frac{G+ \tan(x) }{ \frac{1}{1- \sin(x)} } = \cos(x)",font_size=tam)
        enun1= Tex("entonces $G$ es igual a:",font_size=tam,color=GREEN_SCREEN)  
        enunciado = VGroup(enun0,enun1).arrange(DOWN,center=True)
        return enunciado
    def soltext(self):
        sol= Text("Solucion",font_size=20,font='Akira Expanded').set_color(YELLOW)
        self.play(FadeIn(sol, shift=DOWN, scale=0.66))
        self.play(FadeOut(sol, scale=1.5))
    def respuestas(self):
        tam=22
        res0 = MathTex(r"a) \ \cos(x)",font_size=tam)
        res1 = MathTex(r"b) \ \sec(x)",font_size=tam)
        res2 = MathTex(r"c) \ \sin(x)",font_size=tam)
        res3 = MathTex(r"d) \ \cos^2(x)",font_size=tam)
        res4 = MathTex(r"e) \ -1",font_size=tam)
        respuestas= VGroup(res0,res1,res2,res3,res4).arrange(DOWN,center=False, aligned_edge=LEFT)
        return respuestas
    def desarrollo(self):
        tam=23
        des0 = MathTex(r"\frac{G+ \tan(x) }{ \frac{1}{1- \sin(x)} } = \cos(x)",font_size=tam)
        des1 = MathTex(r"G= \frac{\cos(x)}{1-\sin(x)} - \tan(x) ", font_size=tam-3)
        des2 = MathTex(r"G=\frac{\cos(x)-\tan(x)(1-\sin(x))}{ 1-\sin(x) }",font_size=tam-3)
        des3 = MathTex(r"G= \frac{\cos(x)-\tan(x)+\sin(x)\tan(x)} { 1-\sin(x) }",font_size=tam-2)
        des4 = MathTex(r"G= \frac{  \cos(x) - \frac{\sin(x)}{\cos(x)} +\frac{\sin^2(x)}{\cos(x)} }{ 1-\sin(x) }",font_size=tam)
        des5 = MathTex(r"G=\frac{\cos^2(x)-\sin(x)+\sin^2(x)}{\cos(x) \cdot (1-\sin(x))}",font_size=tam)
        des6 = MathTex(r"G=\frac{1-\sin(x)}{\cos(x) \cdot (1-\sin(x))}", font_size=tam)
        des7 = MathTex(r"G=\frac{1}{\cos(x)}",font_size=tam)
        des8 = MathTex(r"G=\sec(x)",font_size=tam)
        desarrollo= VGroup(des0,des1,des2,des3,des4,des5,des6,des7,des8)
        return desarrollo
    def construct(self):
        enunciado = self.enunciado().move_to(UP)
        respuestas= self.respuestas().next_to(enunciado,DOWN)
        desarrollo = self.desarrollo()
        framebox1 = SurroundingRectangle(desarrollo[-1], buff = .1)
        for i in enunciado:
            self.play(Create(i))
        self.wait(1)
        for i in respuestas:
            self.play(Create(i))
        self.wait(1)
        self.clear()
        self.soltext()
        for i in range(len(desarrollo)-1):
            if i==0:
                self.play(Create(desarrollo[0]))
                self.wait(2)
                self.play(Transform(desarrollo[0],desarrollo[i+1]))
                self.wait(2)
            else:
                self.play(Transform(desarrollo[0],desarrollo[i+1]))
                self.wait(3)
        self.play(Create(framebox1))
        self.wait(3)
import math
class Short11(Scene):
    def enunciado(self):
        tam=22
        enun0 = Tex("Si $f$ es una funcion de  $\mathbb{R}$ en $\mathbb{R}$",font_size=tam,color=Amarillo)
        enun1= MathTex(r"f(x)=2\cos|2x|-1",font_size=tam,color=GREEN_SCREEN)  
        enunciado = VGroup(enun0,enun1).arrange(DOWN,center=True)
        return enunciado
    def soltext(self):
        sol= Text("Solucion",font_size=20,font='Akira Expanded').set_color(YELLOW)
        self.play(FadeIn(sol, shift=DOWN, scale=0.66))
        self.play(FadeOut(sol, scale=1.5))
    def respuestas(self):
        tam=22
        res0 = Tex("a) Una cota inferior de $f$ es $y=-2$",font_size=tam)
        res1 = Tex("b) El periodo fundamental de $f$ es $4 \pi$",font_size=tam)
        res2 = MathTex(r"c) \forall x \in \mathbb{R} \left(  f(x+\frac{ \pi }{2}) = f(x) \right)  ",font_size=tam)
        res3 = Tex("d) $f$ es creciente en $[0, \pi/2 ]$",font_size=tam)
        res4 = MathTex(r"e) \ rg(f)=[-3,1]",font_size=tam)
        respuestas= VGroup(res0,res1,res2,res3,res4)
        return respuestas
    def construct(self):
        # Crear los ejes cartesianos
        axes = Axes(
            x_range=[-2*PI, 2*PI, PI/2],
            y_range=[-4, 4, 1],
            x_length=4,
            y_length=4,
            axis_config={"color": BLUE},
            tips=False,
            y_axis_config={"numbers_to_include": [-3, -2, -1, 1, 2, 3]},
        )
        enunciado = self.enunciado().move_to(UP)
        respuestas= self.respuestas().arrange(DOWN,center=False, aligned_edge=LEFT).next_to(enunciado,DOWN).set_color(Amarillo)
        respuestascopy = self.respuestas().next_to(axes,DOWN)
        framebox1 = SurroundingRectangle(respuestascopy[-1], buff = .1)
        # Definir el rango del eje x en términos de pi
        #x_vals = [-2*PI, -3*PI/2, -PI, -PI/2, 0, PI/2, PI, 3*PI/2, 2*PI]
        x_labels = [
            MathTex(r"-2\pi").move_to(axes.c2p(-2*PI, -0.2)),
            MathTex(r"-\frac{3\pi}{2}").move_to(axes.c2p(-3*PI/2,-0.2 )),
            MathTex(r"-\pi").move_to(axes.c2p(-PI, -0.2)),
            MathTex(r"-\frac{\pi}{2}").move_to(axes.c2p(-PI/2, -0.2)),
            MathTex(r"0").move_to(axes.c2p(0, -0.2)),
            MathTex(r"\frac{\pi}{2}").move_to(axes.c2p(PI/2, -0.2)),
            MathTex(r"\pi").move_to(axes.c2p(PI, -0.2)),
            MathTex(r"\frac{3\pi}{2}").move_to(axes.c2p(3*PI/2,-0.2)),
            MathTex(r"2\pi").move_to(axes.c2p(2*PI, -0.2))
        ]
        revision = VGroup(
            Text(r"X",font_size=12,color=RED,font='Akira Expanded'),
            Text(r"X",font_size=12,color=RED,font='Akira Expanded'),
            Text(r"X",font_size=12,color=RED,font='Akira Expanded'),
            Text(r"X",font_size=12,color=RED,font='Akira Expanded'),
            Text(r"ok",font_size=12,color=YELLOW,font='Akira Expanded'),
        )

        # Graficar una función, por ejemplo, seno(x)
        desarrollo = VGroup(
            VGroup(axes.plot(lambda x: np.cos(x), color=GREEN_SCREEN), MathTex(r"\cos(x)", color=GREEN_SCREEN, font_size=30).next_to(axes, UP)),
            VGroup(axes.plot(lambda x: np.cos(np.absolute(x)), color=GREEN_SCREEN), MathTex(r"\cos|x|", color=GREEN_SCREEN, font_size=30).next_to(axes, UP)),
            VGroup(axes.plot(lambda x: np.cos(np.absolute(2*x)), color=GREEN_SCREEN), MathTex(r"\cos|2x|", color=GREEN_SCREEN, font_size=30).next_to(axes, UP)),
            VGroup(axes.plot(lambda x: 2*np.cos(np.absolute(2*x)), color=GREEN_SCREEN), MathTex(r"2\cos|2x|", color=GREEN_SCREEN, font_size=30).next_to(axes, UP)),
            VGroup(axes.plot(lambda x: 2*np.cos(np.absolute(2*x))-1, color=GREEN_SCREEN), MathTex(r"2\cos|2x|-1", color=GREEN_SCREEN, font_size=30).next_to(axes, UP)),
        )
        

        for i in enunciado:
            self.play(Create(i))
        self.wait(1)
        for i in respuestas:
            self.play(Create(i))
        self.wait(1)
        self.clear()
        self.soltext()
        self.play(Create(axes))
        for i in x_labels:
            self.add(i.scale(0.5))
        self.wait(3)
        for i in range(len(desarrollo)-1):
            if i==0:
                self.play(Create(desarrollo[0]))
                self.wait(2)
                self.play(Transform(desarrollo[0],desarrollo[i+1]))
                self.wait(2)
            else:
                self.play(Transform(desarrollo[0],desarrollo[i+1]))
                self.wait(3)
        for i in range(len(respuestascopy)-1):
            if i==0:
                self.play(Create(respuestascopy[0]))
                self.wait(2)
                self.play(Create(revision[i].next_to(respuestascopy[0],DOWN)))
                self.play(Transform(respuestascopy[0],respuestascopy[i+1]))
                self.remove(revision[i])
                self.wait(2)
                self.play(Transform(revision[i],revision[i+1].next_to(respuestascopy[0],DOWN)))
                self.remove(revision[i])
            else:
                self.play(Transform(respuestascopy[0],respuestascopy[i+1]))
                self.remove(revision[i])
                self.wait(3)
                self.play(Transform(revision[0],revision[i+1].next_to(respuestascopy[0],DOWN)))
                
                
        self.play(Create(framebox1))
        self.wait(3)
        
class Short12(MovingCameraScene):
    def grafica(self):
        ax=NumberPlane(
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )
        poly_1 = RegularPolygon(n=6)
        circle_1 = Circle(radius=1.0).set_color(ORANGE)
        circle_2 = Circle(radius=0.85).set_color(RED)
        dashed_1 = DashedLine(ax.c2p(0,0),ax.c2p(0.48,-0.83)).set_color(BLUE_D)
        dashed_2 = DashedLine(ax.c2p(0,0),ax.c2p(0,-0.83)).set_color(Morado)
        e =Exclusion(circle_1, circle_2, color=GREEN_SCREEN, fill_opacity=0.5)
        r1=MathTex(r"r_{1}=4u",font_size=22).move_to(ax.c2p(0.48,-0.48))
        r2=MathTex(r"r_{2}=?",font_size=22).move_to(ax.c2p(-0.48,-0.48))
        b1 = Brace(Line(ax.c2p(0,-0.83),ax.c2p(0.48,-0.83)))
        r1medio = MathTex(r"\frac{r_{1}}{2}",font_size=22).next_to(b1,DOWN)
        return VGroup(poly_1,circle_1,circle_2,e,dashed_1,dashed_2,r1,r2,b1,r1medio)
    def enunciado(self):
        tam=22
        enun0 = Tex("Un Hexagono regular cuyos lados",font_size=tam)
        enun1= Tex("miden 4u, esta inscrito en una",font_size=tam)  
        enun2= Tex("circunferencia $C_{1}$ y circunscrito",font_size=tam)  
        enun3= Tex("a una circunferencia $C_{2}$, ",font_size=tam)  
        enun4= Tex("entonces el área de la corona ",font_size=tam)  
        enun5= Tex("circular comprendida entre ambas",font_size=tam)  
        enun6= Tex("circunferencias es:",font_size=tam)  
        enunciado = VGroup(enun0,enun1,enun2,enun3,enun4,enun5,enun6).arrange(DOWN,center=True)
        return enunciado
    def soltext(self):
        sol= Text("Solucion",font_size=20,font='Akira Expanded').set_color(YELLOW)
        self.play(FadeIn(sol, shift=DOWN, scale=0.66))
        self.play(FadeOut(sol, scale=1.5))
    def respuestas(self):
        tam=22
        res0 = MathTex(r"a) \ \pi u^2",font_size=tam)
        res1 = MathTex(r"b) \ 2 \pi u^2",font_size=tam)
        res2 = MathTex(r"c) \ 3 \pi u^2",font_size=tam)
        res3 = MathTex(r"d) \ 4 \pi u^2",font_size=tam)
        res4 = MathTex(r"e) \ 5 \pi u^2",font_size=tam)
        respuestas= VGroup(res0,res1,res2,res3,res4).arrange(DOWN,center=False, aligned_edge=LEFT)
        return respuestas
    def desarrollop1(self):
        tam=22
        des0=MathTex(r"(r_{1})^2 = (r_{2})^2 +(\frac{r_{1}}{2})^2",font_size=tam)
        des1=MathTex(r"(r_{2})^2 = (r_{1})^2 - \frac{(r_{1})^2}{4}",font_size=tam)
        des2=MathTex(r"(r_{2})^2 = \frac{3}{4} (r_{1})^2",font_size=tam)
        desarrollo= VGroup(des0,des1,des2).arrange(DOWN,center=True)
        return desarrollo
    def desarrollop2(self):
        tam=22
        des0=MathTex(r"A = A_{1}-A_{2}",font_size=tam)
        des1=MathTex(r"A= \pi (r_{1})^2 - \pi (r_{2})^2 ",font_size=tam)
        des2=MathTex(r"A= \pi \left(  (r_{1})^2 -  \frac{3}{4} (r_{1})^2 \right)",font_size=tam)
        des3=MathTex(r"A= \frac{ \pi }{ 4} (r_{1})^2",font_size=tam)
        des4=MathTex(r"A= \frac{ \pi }{ 4} (4u)^2",font_size=tam)
        des5=MathTex(r"A= 4 \pi u^2",font_size=tam)
        desarrollo= VGroup(des0,des1,des2,des3,des4,des5).arrange(DOWN,center=True)
        return desarrollo
    def construct(self):
        self.camera.frame.save_state()
        enunciado = self.enunciado().move_to(UP)
        respuestas= self.respuestas().arrange(DOWN,center=False, aligned_edge=LEFT).next_to(enunciado,DOWN).set_color(Amarillo)
        grafica = self.grafica()
        desarrollo1 = self.desarrollop1().move_to(UP*2)
        desarrollo2 = self.desarrollop2().move_to(DOWN)
        framebox1 = SurroundingRectangle(desarrollo2[-1], buff = .1)
        for i in enunciado:
            self.play(Create(i))
        self.wait(1)
        for i in respuestas:
            self.play(Create(i))
        self.wait(1)
        self.clear()
        self.soltext()
        for i,shape in enumerate(grafica):
            if i<4:
                self.play(Create(shape))
                self.wait(1)
                if i==3:
                    self.wait(3)
            elif i==4:
                self.remove(grafica[i-1])
                self.play(self.camera.frame.animate.scale(0.6).move_to(shape),run_time=1)
                self.play(Create(shape))
            else:
                self.play(Create(shape))
        self.play(Restore(self.camera.frame))
        self.clear()
        for i in desarrollo1:
            self.play(Create(i))
            self.wait(1)
        self.wait(3)
        for i in desarrollo2:
            self.play(Create(i))
            self.wait(1)
        self.play(Create(framebox1))
        self.wait(3)

class Short13(Scene):
    def enunciado(self):
        tam=22
        enun0 = Tex("El valor real de $k$ para que los vectores",font_size=tam)
        enun1= MathTex(r"A=2V_{1}+5V_{2} \ y  \ B= kV_{1}+3V_{2}",font_size=tam,color=GREEN_SCREEN)  
        enun2= Tex("Sean ortogonales, conociendo que los",font_size=tam)  
        enun3= Tex("vectores $V_{1}$ y $V_{2}$ son unitarios ",font_size=tam)  
        enun4= Tex("y la medida del angulo que forman",font_size=tam)  
        enun5= Tex("entre si es $ \pi/3 $ es :",font_size=tam)  
        enunciado = VGroup(enun0,enun1,enun2,enun3,enun4,enun5).arrange(DOWN,center=True)
        return enunciado
    def soltext(self):
        sol= Text("Solucion",font_size=20,font='Akira Expanded').set_color(YELLOW)
        self.play(FadeIn(sol, shift=DOWN, scale=0.66))
        self.play(FadeOut(sol, scale=1.5))
    def desarrollo(self):
        tam=22
        des0=MathTex(r"A \cdot B=0 ",font_size=tam)
        des1=MathTex(r"A \cdot B=(2V_{1}+5V_{2}) \cdot(kV_{1}+3V_{2})=0",font_size=tam)
        des2=MathTex(r"2kV_{1}V_{1}+6V_{1}V_{2}+5kV_{1}V_{2}+15V_{2}V_{2}=0",font_size=tam-3)
        des3=MathTex(r"2k\| V_{1} \|^2 +V_{1}V_{2}(6+5k) + 15\| V_{2} \|^2 =0",font_size=tam)
        des4=MathTex(r"2k+15+V_{1}V_{2} (6+5k) =0",font_size=tam)
        des5=MathTex(r"2k + 15 + \left[ \| V_{1} \| \| V_{2} \| \cos(\frac{\pi}{3})  \right](6+5k)=0 ",font_size=tam-3)
        des6=MathTex(r"2k+15+\frac{6+5k}{2} =0",font_size=tam)
        des7=MathTex(r"4k+30+6+5k=0",font_size=tam)
        des8=MathTex(r"k=-4",font_size=tam)
        desarrollo= VGroup(des0,des1,des2,des3,des4,des5,des6,des7,des8)
        return desarrollo
    def respuestas(self):
        tam=22
        res0 = MathTex(r"a) \ -2",font_size=tam)
        res1 = MathTex(r"b) \ -4",font_size=tam)
        res2 = MathTex(r"c) \ 0",font_size=tam)
        res3 = MathTex(r"d) \ 2",font_size=tam)
        
        respuestas= VGroup(res0,res1,res2,res3).arrange(DOWN,center=False, aligned_edge=LEFT)
        return respuestas
    def construct(self):
        enunciado = self.enunciado().move_to(UP)
        respuestas= self.respuestas().arrange(DOWN,center=False, aligned_edge=LEFT).next_to(enunciado,DOWN).set_color(Amarillo)
        desarrollo = self.desarrollo()
        framebox = SurroundingRectangle(desarrollo[-1], buff = .1)
        for i in enunciado:
            self.play(Create(i))
        self.wait(1)
        for i in respuestas:
            self.play(Create(i))
        self.wait(1)
        self.clear()
        self.soltext()
        for i in range(len(desarrollo)-1):
            if i==0:
                self.play(Create(desarrollo[0]))
                self.wait(2)
                self.play(Transform(desarrollo[0],desarrollo[i+1]))
                self.wait(2)
            else:
                self.play(Transform(desarrollo[0],desarrollo[i+1]))
                self.wait(3)
        self.play(Create(framebox))
        self.wait(3)

class Short14(MovingCameraScene):
    def enungrafica(self):
        ax=NumberPlane(
            x_range=(-10, 10, 1),
            y_range=(-10,10,1),
             background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
            
        ).add_coordinates()
        elipse = ParametricFunction(lambda t: np.array([
            5 * np.cos(t),
            1 + math.sqrt(7) * np.sin(t),
            0
        ]), color=BLUE_D, t_range=[0, 2*PI], stroke_width=4)
        
        circle = ParametricFunction(lambda t: np.array([
            3 * np.cos(t),
            1 + 3 * np.sin(t),
            0
        ]), color=ORANGE, t_range=[0, 2*PI], stroke_width=4)
        centro= Dot(ax.c2p(0,1)).scale(1.5).set_color(VerdeClaro)
        elipse_tex = MathTex(r"7x^2 + 16y^2 -32y -96 =0", font_size=42,color=BLUE_D).move_to(ax.c2p(0,6))
        circle_tex = MathTex(r"x^2+y^2+Dx+Ey+F=0 \ ??? ", font_size=42,color=ORANGE).move_to(ax.c2p(0,5))
        f1 = Dot(ax.c2p(-3,1)).scale(1.5).set_color(GREEN_SCREEN)
        f2 = Dot(ax.c2p(3,1)).scale(1.5).set_color(GREEN_SCREEN)
        f1_tex = MathTex(r"F_{1}",color=VerdeClaro,font_size=42).next_to(f1,LEFT)
        f2_tex = MathTex(r"F_{2}",color=VerdeClaro,font_size=42).next_to(f2,RIGHT)
        vertices =VGroup(f1,f2,f1_tex,f2_tex)
        graf = VGroup(ax,elipse,elipse_tex,centro,vertices,circle,circle_tex)
        return graf
    def desgrafica(self):
        ax=NumberPlane(
            x_range=(-5, 5, 1),
            y_range=(-5,5,1),
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 0.6,
                "stroke_opacity": 0.5
            }
            
        ).add_coordinates()
        elipse = ParametricFunction(lambda t: np.array([
            5 * np.cos(t),
            1 + math.sqrt(7) * np.sin(t),
            0
        ]), color=BLUE_D, t_range=[0, 2*PI], stroke_width=4)
        
        circle = ParametricFunction(lambda t: np.array([
            3 * np.cos(t),
            1 + 3 * np.sin(t),
            0
        ]), color=ORANGE, t_range=[0, 2*PI], stroke_width=4)
        centro= Dot(ax.c2p(0,1)).scale(1.5).set_color(YELLOW)
        elipse_tex = MathTex(r"7x^2 + 16y^2 -32y -96 =0", font_size=42,color=BLUE_D).move_to(ax.c2p(0,7))
        circle_tex = MathTex(r"x^2+y^2+Dx+Ey+F=0 \ ??? ", font_size=42,color=ORANGE).move_to(ax.c2p(0,6))
        f1 = Dot(ax.c2p(-3,1)).scale(1.5).set_color(VerdeClaro)
        f2 = Dot(ax.c2p(3,1)).scale(1.5).set_color(VerdeClaro)
        f1_tex = MathTex(r"F_{1}=(-3,1)",color=VerdeClaro,font_size=42).next_to(f1,UP)
        f2_tex = MathTex(r"F_{2}=(3,1)",color=VerdeClaro,font_size=42).next_to(f2,UP)
        lines_1 = ax.get_lines_to_point(ax.c2p(-3,1), color=GREEN_B)
        lines_2 = ax.get_lines_to_point(ax.c2p(3,1), color=GREEN_B)
        vertices =VGroup(f1,f2,f1_tex,f2_tex,lines_1,lines_2)
        b1=Brace(Line(ax.c2p(0,1),ax.c2p(3,1)))
        b1_text = MathTex(r"r=3").next_to(b1,DOWN).set_color(ORANGE)
        graf = VGroup(VGroup(ax,elipse,elipse_tex,centro,vertices,circle,circle_tex),VGroup(b1,b1_text))
        return graf
    def enunciado(self):
        tam=22
        enun0 = Tex("Si los focos de la elipse",font_size=tam)
        enun1= MathTex(r"7x^2+16y^2-32y-96=0",font_size=tam,color=GREEN_SCREEN)  
        enun2= Tex(" son los extremos del diámetro",font_size=tam)  
        enun3= Tex("de una circunferencia, entonces",font_size=tam)  
        enun4= Tex("la ecuacion general de la",font_size=tam)  
        enun5= Tex("circunferencia es:",font_size=tam)  
        enunciado = VGroup(enun0,enun1,enun2,enun3,enun4,enun5).arrange(DOWN,center=True)
        return enunciado
    def soltext(self):
        sol= Text("Solucion",font_size=20,font='Akira Expanded').set_color(YELLOW)
        self.play(FadeIn(sol, shift=DOWN, scale=0.66))
        self.play(FadeOut(sol, scale=1.5))
    def desarrollop1(self):
        tam=22
        des0=MathTex(r"7x^2+16y^2-32y-96=0",font_size=tam)
        des1=MathTex(r"\frac{7x^2}{16}+\frac{16y^2}{16} - \frac{32y}{16} - \frac{96}{16}=0",font_size=tam)
        des2=MathTex(r"\frac{7}{16}x^2 + y^2 -2y -6 = 0",font_size=tam-3)
        des3=MathTex(r"\frac{7}{16}x^2 + y^2 -2y +1 -1 -6 = 0",font_size=tam)
        des4=MathTex(r"\frac{7}{16}x^2 +(y-1)^2-7 = 0",font_size=tam)
        des5=MathTex(r"\frac{x^2}{16} + \frac{(y-2)^2}{7}=1",font_size=tam)
        des6=MathTex(r"O(h,k)=O(0,1)",font_size=tam)
        des7=MathTex(r"a^2 = 16, \ b^2=7",font_size=tam)
        des8=MathTex(r"F_1(h-c,k), \ F_2(h+c,k) ",font_size=tam)
        des9=MathTex(r"c^2 = a^2 -b^2",font_size=tam)
        des10=MathTex(r"c^2= 16-7 \rightarrow c=3",font_size=tam)
        des11=MathTex(r"F_1(-3,1), \ F_2(3,1)",font_size=tam)
        desarrollo1= VGroup(des0,des1,des2,des3,des4,des5)
        desarrollo2= VGroup(des6,des7,des8,des9,des10,des11)
        return desarrollo1,desarrollo2.arrange(DOWN,center=True)
    def desarrollop2(self):
        tam=22
        des0=MathTex(r"(x-h)^2+(y-k)^2 = r^2",font_size=tam)
        des1=MathTex(r"(x-0)^2+(y-1)^2 = 3^2",font_size=tam)
        des2=MathTex(r"x^2+y^2-2y-8=0",font_size=tam)
        return VGroup(des0,des1,des2)
    def respuestas(self):
        tam=22
        res0 = MathTex(r"a) \ x^2+y^2-2y+10=0",font_size=tam)
        res1 = MathTex(r"b) \ x^2+y^2-2y+8=0",font_size=tam)
        res2 = MathTex(r"c) \ x^2+y^2-2y-10=0",font_size=tam)
        res3 = MathTex(r"d) \ x^2+y^2-2y-8=0",font_size=tam)
        
        respuestas= VGroup(res0,res1,res2,res3).arrange(DOWN,center=False, aligned_edge=LEFT)
        return respuestas
    def construct(self):
        self.camera.frame.save_state()
        enunciado = self.enunciado().move_to(UP)
        respuestas= self.respuestas().arrange(DOWN,center=False, aligned_edge=LEFT).next_to(enunciado,DOWN).set_color(Amarillo)
        desarrollo1,desarrollo2 = self.desarrollop1()
        desarrollop2= self.desarrollop2().move_to([0,-2,0])
        des5=MathTex(r"\frac{x^2}{16} + \frac{(y-2)^2}{7}=1",font_size=22).move_to(UP*2)
        framebox = SurroundingRectangle(desarrollop2[-1], buff = .1)
        enungrafica = self.enungrafica().scale(0.4)
        desgrafica = self.desgrafica().scale(0.4)
        for i in enunciado:
            self.play(Create(i))
        self.wait(1)
        for i in respuestas:
            self.play(Create(i))
        self.wait(1)
        self.clear()
        self.soltext()
        self.wait(2)
        for i in enungrafica:
            self.play(Create(i))
        self.wait(2)
        self.clear()
        for i in range(len(desarrollo1)-1):
            if i==0:
                self.play(Create(desarrollo1[0]))
                self.wait(1)
                self.play(Transform(desarrollo1[0],desarrollo1[i+1]))
                self.wait(1)
            else:
                self.play(Transform(desarrollo1[0],desarrollo1[i+1]))
                self.wait(1)
        self.play(Transform(desarrollo1,des5))
        self.wait(2)
        for i in desarrollo2:
            self.play(Create(i))
        self.wait(3)
        self.clear()
        for i,shape in enumerate(desgrafica):
            if i==0:
                self.play(Create(shape))
                self.wait(1)
            else:
                self.play(self.camera.frame.scale(0.5).animate.move_to(shape))
                self.wait(1)
                self.play(Create(shape))
                self.wait(2)
        self.play(Restore(self.camera.frame))
        for i in range(len(desarrollop2)-1):
            if i==0:
                self.play(Create(desarrollop2[0]))
                self.wait(1)
                self.play(Transform(desarrollop2[0],desarrollop2[i+1]))
                self.wait(1)
            else:
                self.play(Transform(desarrollop2[0],desarrollop2[i+1]))
                self.wait(1)
        self.play(Create(framebox))
        self.wait(3)

class Short15(Scene):
    def enunciado(self):
        tam=22
        enun0 = Tex("Al simplificar la expresion algebraica",font_size=tam-2,color=GREEN)
        enun1= MathTex(r"\left[ \frac{x+2y}{x-y} - \frac{x+y}{x} \right] \left[ \frac{x^2- xy}{y(2x+y)}  \right]",font_size=tam)
        enun2= Tex("Se obtiene: ",font_size=tam,color=Amarillo)
        enunciado = VGroup(enun0,enun1,enun2).arrange(DOWN,center=True)
        return enunciado
    def soltext(self):
        sol= Text("Solucion",font_size=20,font='Akira Expanded').set_color(YELLOW)
        self.play(FadeIn(sol, shift=DOWN, scale=0.66))
        self.play(FadeOut(sol, scale=1.5))
    def respuestas(self):
        tam=22
        res0 = MathTex(r"a) \ 0",font_size=tam)
        res1 = MathTex(r"b) \ 1",font_size=tam)
        res2 = MathTex(r"c) \ 2x^2+y",font_size=tam)
        res3 = MathTex(r"d) \ xy+y^2",font_size=tam)
        respuestas= VGroup(res0,res1,res2,res3).arrange(DOWN,center=False, aligned_edge=LEFT)
        return respuestas
    def desarrollo(self):
        tam=21
        des0 = MathTex(r"\left [ \frac{x+2y}{x-y} - \frac{x+y}{x} \right] \left [ \frac{x^2- xy}{y(2x+y)}  \right] ",font_size=tam)
        des1 = MathTex(r"\left [ \frac{x(x+2y)-(x+y)(x-y)}{ x(x-y) } \right] \left [ \frac{x(x-y)}{y(2x+y)}  \right]", font_size=tam)
        des2 = MathTex(r"\frac{x^2+2xy-(x^2-y^2)}{ y(2x+y) }",font_size=tam+2).scale(1.3)
        des3 = MathTex(r"\frac{2xy+y^2}{ y(2x+y)}",font_size=tam+2)
        des4 = MathTex(r"\frac{y(2x+y)}{ y(2x+y)}",font_size=tam+2)
        des5 = MathTex(r"1",font_size=tam+3)
        desarrollo= VGroup(des0,des1,des2,des3,des4,des5)
        return desarrollo
    def imprimirTransform(self,lista):
        for i in range(len(lista)-1):
            if i==0:
                self.play(Create(lista[0]))
                self.wait(2)
                self.play(Transform(lista[0],lista[i+1]))
                self.wait(2)
            else:
                self.play(Transform(lista[0],lista[i+1]))
                self.wait(3)
    def construct(self):
        enunciado = self.enunciado().move_to(UP)
        respuestas= self.respuestas().next_to(enunciado,DOWN)
        desarrollo = self.desarrollo()
        framebox1 = SurroundingRectangle(desarrollo[-1], buff = .1)
        for i in enunciado:
            self.play(Create(i))
        self.wait(1)
        for i in respuestas:
            self.play(Create(i))
        self.wait(1)
        self.clear()
        self.soltext()
        self.imprimirTransform(desarrollo)
        self.play(Create(framebox1))
        self.wait(3)

class Short16(Scene):
    def enunciado(self):
        tam=22
        enun0 = Tex("El valor real $m$ para que el",font_size=tam-2,color=GREEN)
        enun1= Tex("residuo que se obtiene al dividir",font_size=tam,color=GREEN)
        enun2= Tex("el polinomio: ",font_size=tam,color=GREEN)
        enun3= MathTex(r"p(x) = x^5+3mx^2-x+1",font_size=tam)
        enun4= Tex("entre $(x-1)$ sea $-1,$ es",font_size=tam,color=GREEN)
        enunciado = VGroup(enun0,enun1,enun2,enun3,enun4).arrange(DOWN,center=True)
        return enunciado
    def respuestas(self):
        tam=22
        res0 = MathTex(r"a) \ 2/3",font_size=tam)
        res1 = MathTex(r"b) \ -1",font_size=tam)
        res2 = MathTex(r"c) \ -2/3",font_size=tam)
        res3 = MathTex(r"d) \ -1/3",font_size=tam)
        respuestas= VGroup(res0,res1,res2,res3).arrange(DOWN,center=False, aligned_edge=LEFT)
        return respuestas
    def soltext(self):
        sol= Text("Solucion",font_size=20,font='Akira Expanded').set_color(YELLOW)
        self.play(FadeIn(sol, shift=DOWN, scale=0.66))
        self.play(FadeOut(sol, scale=1.5))
    def desarrollo(self):
        ax=NumberPlane().add_coordinates()
        polinomio = MathTex(r"p(x) = x^5+3mx^2-x+1, \\g(x)= x-1 ",font_size=22).move_to(ax.c2p(0,3))
        
        reglon3 = VGroup(
            MathTex(r"1 \ ",font_size=25),
            MathTex(r"1 \ ",font_size=25),
            MathTex(r"1 \ ",font_size=25),
            MathTex(r"3m+1",font_size=20),
            MathTex(r"3m \ ",font_size=22),
            MathTex(r"3m+1",font_size=20),
        ).arrange(RIGHT,center=False).move_to(ax.c2p(0,0))
        coeficientes = VGroup(
            MathTex(r"1 \ ",font_size=25).next_to(reglon3[0],UP*2.5),
            MathTex(r"0 \ ",font_size=25).next_to(reglon3[1],UP*2.5),
            MathTex(r"0 \ ",font_size=25).next_to(reglon3[2],UP*2.5),
            MathTex(r"3m \ ",font_size=25).next_to(reglon3[3],UP*2.5),
            MathTex(r"-1 \ ",font_size=25).next_to(reglon3[4],UP*2.5),
            MathTex(r" \ 1 ",font_size=25).next_to(reglon3[5],UP*2.5),
        )
        reglon2 = VGroup(
            MathTex(r"1",font_size=25).next_to(coeficientes[1],DOWN),
            MathTex(r"1",font_size=25).next_to(coeficientes[2],DOWN),
            MathTex(r"1",font_size=25).next_to(coeficientes[3],DOWN),
            MathTex(r"3m+1",font_size=20).next_to(coeficientes[4],DOWN),
            MathTex(r"3m",font_size=22).next_to(coeficientes[5],DOWN),
        )
        l1 = Line(ax.c2p(1.4,1.2),ax.c2p(1.4,0))
        l2 = Line(ax.c2p(-1.6,0.2),ax.c2p(1.4,0.2))
        coef = MathTex(r"1",font_size=25).next_to(l2,LEFT)
        framebox = SurroundingRectangle(coef, buff = .1).set_color(WHITE)
        residuo= MathTex(r"3m+1=-1",font_size=22).next_to(reglon3,DOWN*2)
        res = MathTex(r"m=-2/3",font_size=22).next_to(residuo,DOWN)
        return VGroup(polinomio,VGroup(l1,l2),coeficientes,VGroup(coef,framebox),reglon3,reglon2,residuo,res)
    def construct(self):
        enunciado = self.enunciado().move_to(UP)
        respuestas= self.respuestas().next_to(enunciado,DOWN)
        desarrollo=self.desarrollo()
        framebox = SurroundingRectangle(desarrollo[-1],buff = .1)
        for i in enunciado:
            self.play(Create(i))
        self.wait(1)
        for i in respuestas:
            self.play(Create(i))
        self.wait(1)
        self.clear()
        self.soltext()
        for i, shape in enumerate(desarrollo):
            if i<3:
                self.play(Create(shape))
                self.wait(1)
            elif i==3:
                self.play(Create(shape))
                self.wait(1)
            elif i==4:
                for k in range(len(shape)):
                    self.play(Create(shape[k]))
                    self.wait(1)
                    if k<(len(shape)-1):
                        self.play(Create(desarrollo[i+1][k]))
                        self.wait(1)
            elif i>5:
                self.play(Create(shape))
        self.play(Create(framebox))
        self.wait(3)

class Short17(Scene):
    def grafica(self):
        # Definir el plano polar
        polar_plane = PolarPlane(
            azimuth_units="PI radians",
            size=3,
            azimuth_step=24,
            stroke_opacity=0.6
            
        ).add_coordinates()
        # Coordenadas polares de los puntos que queremos dibujar
        angle_1 = Angle(Line( LEFT, RIGHT ), Line( LEFT, RIGHT ).rotate(7*PI/4),radius=0.5,stroke_width=5).set_color(ORANGE)
        angle_2 = Angle(Line( LEFT, RIGHT ), Line( LEFT, RIGHT ).rotate(7*PI/6), radius=1,stroke_width=5).set_color(GREEN_SCREEN)
        # Agregar los elementos al escenario
        plano = VGroup(polar_plane,angle_1,angle_2).move_to(UP)
        valores= VGroup(
            MathTex(r"\tan\left(\frac{7\pi}{4}\right) = \frac{\sin\left(\frac{7\pi}{4}\right)}{\cos\left(\frac{7\pi}{4}\right)}", font_size=22),
            MathTex(r"\tan\left(\frac{7\pi}{4}\right) = \frac{\sqrt{2}/2}{-\sqrt{2}/2}=-1", font_size=22),
            MathTex(r"\sin\left(\frac{7\pi}{6}\right) = -\frac{\sqrt{3}}{2}", font_size=22),
        ).arrange(DOWN,center=True).next_to(plano,DOWN)
        return VGroup(plano,valores)
    def enunciado(self):
        tam=22
        enun0 = MathTex(r"Si \ M = \sqrt{\frac{1}{4} \left(  -\tan(\frac{7\pi}{4})  \right) } \ y",font_size=tam-2)
        enun1= MathTex(r"P = \ln \left( e - \mu\left( \sin\left(  \frac{7 \pi} {6} \right) \right) \right)^3",font_size=tam)
        enun2= Tex("el valor numerico de: ",font_size=tam,color=GREEN)
        enun3= MathTex(r"(2M-P)",font_size=tam)
        enun4= Tex("es: ",font_size=tam)
        enunciado = VGroup(enun0,enun1,enun2,enun3,enun4).arrange(DOWN,center=True)
        return enunciado
    def soltext(self):
        sol= Text("Solucion",font_size=20,font='Akira Expanded').set_color(YELLOW)
        self.play(FadeIn(sol, shift=DOWN, scale=0.66))
        self.play(FadeOut(sol, scale=1.5))
    def respuestas(self):
        tam=22
        res0 = MathTex(r"a) \ -5/2",font_size=tam)
        res1 = MathTex(r"b) \ -2",font_size=tam)
        res2 = MathTex(r"c) \ 7/2",font_size=tam)
        res3 = MathTex(r"d) \ 0",font_size=tam)
        respuestas= VGroup(res0,res1,res2,res3).arrange(DOWN,center=False, aligned_edge=LEFT)
        return respuestas
    def desarrollo(self):
        tam=21
        des0 = MathTex(r" M = \sqrt{\frac{1}{4} \left(  -\tan(\frac{7\pi}{4})  \right) }",font_size=tam)
        des1 = MathTex(r"M = \sqrt{\frac{1}{4} -(-1) } ", font_size=tam)
        des2 = MathTex(r"M = \frac{1}{2}  \vee  \frac{-1}{2} ",font_size=tam)
        des3 = MathTex(r"P = \ln \left( e - \mu\left( \sin\left(  \frac{7 \pi} {6} \right) \right) \right)^3",font_size=tam)
        des4 = MathTex(r"P = \ln \left( e - \mu\left( -\frac{\sqrt{3}}{2} \right) \right) \right)^3",font_size=tam)
        des5 = MathTex(r"P = \ln \left( e - 0 \right) \right)^3",font_size=tam)
        des6 = MathTex(r"P=3",font_size=tam)
        des7 = MathTex(r"2M-P=2\frac{1}{2} -3",font_size=tam)
        des8 = MathTex(r"2M-P=-2",font_size=tam)
        desarrollo= VGroup(des0,des1,des2,des3,des4,des5,des6,des7,des8)
        return desarrollo
    
        
    def construct(self):
        enunciado = self.enunciado().move_to(UP)
        respuestas= self.respuestas().next_to(enunciado,DOWN).set_color(Amarillo)
        grafica = self.grafica()
        desarrollo = self.desarrollo()
        framebox = SurroundingRectangle(desarrollo[-1],buff = .1)
        des4 = VGroup(
            Tex("Función escalón unitario:",font_size=22),
            Tex(" $\mu=0$ si $x<0$ ",font_size=22)
        ).arrange(DOWN,center=True).next_to(desarrollo,UP)
        for i in enunciado:
            self.play(Create(i))
        self.wait(1)
        for i in respuestas:
            self.play(Create(i))
        self.wait(1)
        self.clear()
        self.soltext()
        for i,shape in enumerate(grafica):
            if i==0:
                self.play(Create(shape))
            else:
                for k in shape:
                    self.play(Create(k))
                    self.wait(1)
        self.wait(1)
        self.clear()
        for i in range(len(desarrollo)-1):
            if i==0:
                self.play(Create(desarrollo[0]))
                self.wait(2)
                self.play(Transform(desarrollo[0],desarrollo[i+1]))
                self.wait(2)
            elif i==4:
                self.play(Create(des4))
                self.play(Transform(desarrollo[0],desarrollo[i+1]))
                self.wait(2)
            else:
                self.play(Transform(desarrollo[0],desarrollo[i+1]))
                self.wait(2)
        self.play(Create(framebox))
        self.wait(3)

class Short18(Scene):
    def grafica(self):
        principal =BLUE
        axes = Axes(
            x_range=[-5*PI/4, 5*PI/4, PI/4],
            y_range=[-2, 2, 1],
            x_length=4,
            y_length=3,
            axis_config={"color": GREEN },
            tips=False,
            # y_axis_config={"numbers_to_include": [ -1, 1]},
        )
        x_labels = VGroup(
            MathTex(r"-\frac{5\pi}{4}", font_size=15).move_to(axes.c2p(-5*PI/4, -0.2)),
            MathTex(r"-\pi", font_size=15).move_to(axes.c2p(-PI, -0.2)),
            MathTex(r"-\frac{3\pi}{4}", font_size=15).move_to(axes.c2p(-3*PI/4, -0.2)),
            MathTex(r"-\frac{\pi}{2}", font_size=15).move_to(axes.c2p(-PI/2, -0.2)),
            MathTex(r"0", font_size=15).move_to(axes.c2p(0, -0.2)),
            MathTex(r"\frac{\pi}{4}", font_size=15).move_to(axes.c2p(PI/4, -0.2)),
            MathTex(r"\frac{\pi}{2}", font_size=15).move_to(axes.c2p(PI/2, -0.2)),
            MathTex(r"\frac{3\pi}{4}", font_size=15).move_to(axes.c2p(3*PI/4, -0.2)),
            MathTex(r"\pi", font_size=15).move_to(axes.c2p(PI, -0.2)),
            MathTex(r"\frac{5\pi}{4}", font_size=15).move_to(axes.c2p(5*PI/4, -0.2)),
        )


        
        def func(x):
            return np.cos(abs(2*x))
        dots_empty = VGroup(
            Dot(axes.c2p(-3*PI/4,1),radius=0.05).set_color(BLACK),
            Dot(axes.c2p(-3*PI/4,-1),radius=0.05).set_color(BLACK),
            Dot(axes.c2p(-PI/4,-1),radius=0.05).set_color(BLACK),
            Dot(axes.c2p(-PI/4,1),radius=0.05).set_color(BLACK),
            Dot(axes.c2p(PI/4,1),radius=0.05).set_color(BLACK),
            Dot(axes.c2p(PI/4,-1),radius=0.05).set_color(BLACK),
            Dot(axes.c2p(3*PI/4,-1),radius=0.05).set_color(BLACK),
            Dot(axes.c2p(3*PI/4,1),radius=0.05).set_color(BLACK),
        )
        puntos = VGroup(
            Dot(axes.c2p(-5*PI/4, 1)),
            Dot(axes.c2p(-3*PI/4, 1)),
            Dot(axes.c2p(-3*PI/4, 0)),
            Dot(axes.c2p(-3*PI/4, -1)),
            Dot(axes.c2p(-PI/4, -1)),
            Dot(axes.c2p(-PI/4, 0)),
            Dot(axes.c2p(-PI/4, 1)),
            Dot(axes.c2p(PI/4, 1)),
            Dot(axes.c2p(PI/4, 0)),
            Dot(axes.c2p(PI/4, -1)),
            Dot(axes.c2p(3*PI/4, -1)),
            Dot(axes.c2p(3*PI/4, 0)),
            Dot(axes.c2p(3*PI/4, 1)),
            Dot(axes.c2p(5*PI/4, 1)),
        ).set_color(principal)
        sgn = VGroup(
            Line(puntos[0],puntos[1]),
            Line(puntos[3],puntos[4]),
            Line(puntos[6],puntos[7]),
            Line(puntos[9],puntos[10]),
            Line(puntos[12],puntos[13]),
        ).set_color(principal)
        cos_graph = axes.plot(func, color=principal,x_range=[-5*PI/4,5*PI/4] )
        valores = VGroup(
            MathTex(r"P(a,0)",font_size=18).next_to(puntos[5],UP*0.5),
            MathTex(r"Q(0,b)",font_size=18).next_to(sgn[2],UP*0.5),
            MathTex(r"R(c,0)",font_size=18).next_to(puntos[11],UP*0.5),
        )
        enunciado = VGroup(axes,puntos,sgn,dots_empty,valores)
        return enunciado
    def enunciado(self):
        tam=22
        enun0 = VGroup(Tex("Sea la funcion",font_size=tam),MathTex(r"f:[-\pi, \pi] \rightarrow  \mathbb R ",font_size=tam)).arrange(RIGHT)
        enun1= VGroup(Tex("definida por",font_size=tam),MathTex(r"f(x)=sgn(cos|2x|)",font_size=tam)).arrange(RIGHT)
        enun2= Tex("y cuya grafica se muestra, aquí:",font_size=tam)
        enun3= Tex("a continuacion",font_size=tam)
        enunciado = VGroup(enun0,enun1,enun2).arrange(DOWN,center=True)
        return enunciado
    def soltext(self):
        sol= Text("Solucion",font_size=20,font='Akira Expanded').set_color(YELLOW)
        self.play(FadeIn(sol, shift=DOWN, scale=0.66))
        self.play(FadeOut(sol, scale=1.5))
    def respuestas(self):
        tam=22
        enun = Tex("el valor numero de $(c-a+b)$ es:",font_size=22)
        res0 = MathTex(r"a) \ \frac{\pi}{2}",font_size=tam)
        res1 = MathTex(r"b) \  \pi +1 ",font_size=tam)
        res2 = MathTex(r"c) \ \pi+2",font_size=tam)
        res3 = MathTex(r"d) \ 2\pi +1",font_size=tam)
        g1=VGroup(res0,res1).arrange(DOWN)
        g2=VGroup(res2,res3).arrange(DOWN)
        gs=VGroup(g1,g2).arrange(RIGHT)
        respuestas= VGroup(enun,gs).arrange(DOWN,center=True)
        return respuestas
    def imprimirTransform(self,lista):
        for i in range(len(lista)-1):
            if i==0:
                self.play(Create(lista[0]))
                self.wait(2)
                self.play(Transform(lista[0],lista[i+1]))
                self.wait(2)
            else:
                self.play(Transform(lista[0],lista[i+1]))
                self.wait(3)
    def desarrollo(self):
        principal =BLUE
        axes = Axes(
            x_range=[-5*PI/4, 5*PI/4, PI/4],
            y_range=[-2, 2, 1],
            x_length=4,
            y_length=3,
            axis_config={"color": GREEN },
            tips=False,
            # y_axis_config={"numbers_to_include": [ -1, 1]},
        )
        x_labels = VGroup(
            MathTex(r"-\frac{5\pi}{4}", font_size=15).move_to(axes.c2p(-5*PI/4, -0.2)),
            MathTex(r"-\pi", font_size=15).move_to(axes.c2p(-PI, -0.2)),
            MathTex(r"-\frac{3\pi}{4}", font_size=15).move_to(axes.c2p(-3*PI/4, -0.2)),
            MathTex(r"-\frac{\pi}{2}", font_size=15).move_to(axes.c2p(-PI/2, -0.2)),
            MathTex(r"-\frac{\pi}{4}", font_size=15).move_to(axes.c2p(-PI/4, -0.2)),
            MathTex(r"0", font_size=15).move_to(axes.c2p(0, -0.2)),
            MathTex(r"\frac{\pi}{4}", font_size=15).move_to(axes.c2p(PI/4, -0.2)),
            MathTex(r"\frac{\pi}{2}", font_size=15).move_to(axes.c2p(PI/2, -0.2)),
            MathTex(r"\frac{3\pi}{4}", font_size=15).move_to(axes.c2p(3*PI/4, -0.2)),
            MathTex(r"\pi", font_size=15).move_to(axes.c2p(PI, -0.2)),
            MathTex(r"\frac{5\pi}{4}", font_size=15).move_to(axes.c2p(5*PI/4, -0.2)),
        )

        
        def func(x):
            return np.cos(abs(2*x))
        dots_empty = VGroup(
            Dot(axes.c2p(-3*PI/4,1),radius=0.05).set_color(BLACK),
            Dot(axes.c2p(-3*PI/4,-1),radius=0.05).set_color(BLACK),
            Dot(axes.c2p(-PI/4,-1),radius=0.05).set_color(BLACK),
            Dot(axes.c2p(-PI/4,1),radius=0.05).set_color(BLACK),
            Dot(axes.c2p(PI/4,1),radius=0.05).set_color(BLACK),
            Dot(axes.c2p(PI/4,-1),radius=0.05).set_color(BLACK),
            Dot(axes.c2p(3*PI/4,-1),radius=0.05).set_color(BLACK),
            Dot(axes.c2p(3*PI/4,1),radius=0.05).set_color(BLACK),
        )
        puntos = VGroup(
            Dot(axes.c2p(-5*PI/4, 1)),
            Dot(axes.c2p(-3*PI/4, 1)),
            Dot(axes.c2p(-3*PI/4, 0)),
            Dot(axes.c2p(-3*PI/4, -1)),
            Dot(axes.c2p(-PI/4, -1)),
            Dot(axes.c2p(-PI/4, 0)),
            Dot(axes.c2p(-PI/4, 1)),
            Dot(axes.c2p(PI/4, 1)),
            Dot(axes.c2p(PI/4, 0)),
            Dot(axes.c2p(PI/4, -1)),
            Dot(axes.c2p(3*PI/4, -1)),
            Dot(axes.c2p(3*PI/4, 0)),
            Dot(axes.c2p(3*PI/4, 1)),
            Dot(axes.c2p(5*PI/4, 1)),
        ).set_color(principal)
        sgn = VGroup(
            Line(puntos[0],puntos[1]),
            Line(puntos[3],puntos[4]),
            Line(puntos[6],puntos[7]),
            Line(puntos[9],puntos[10]),
            Line(puntos[12],puntos[13]),
        ).set_color(principal)
        func_graph = VGroup(
            VGroup(MathTex(r"\cos(x)",font_size=22).next_to(axes,UP),axes.plot(lambda x: np.cos(x), color=principal,x_range=[-5*PI/4,5*PI/4] )),
            VGroup(MathTex(r"\cos(2x)",font_size=22).next_to(axes,UP),axes.plot(lambda x: np.cos(2*x), color=principal,x_range=[-5*PI/4,5*PI/4] )),
            VGroup(MathTex(r"\cos|2x|",font_size=22).next_to(axes,UP),axes.plot(func, color=principal,x_range=[-5*PI/4,5*PI/4] )),
            VGroup(MathTex(r"sgn(cos|2x|)",font_size=22).next_to(axes,UP),puntos,sgn,dots_empty)
        )
        valores = VGroup(
            MathTex(r"P(-\pi/4,0)",font_size=18).next_to(puntos[5],UP*0.5),
            MathTex(r"Q(0,1)",font_size=18).next_to(sgn[2],UP*0.5),
            MathTex(r"R(3\pi/4,0)",font_size=18).next_to(puntos[11],UP*0.5),
        )
        respuesta =VGroup(
            MathTex(r"c-a+b=\frac{3\pi}{4}-\frac{-\pi}{4}+1",font_size=22),
            MathTex(r"c-a+b=\pi+1",font_size=22),
        ).arrange(DOWN,center=True).next_to(axes,DOWN)
        framebox = SurroundingRectangle(respuesta[-1],buff = .1)
        self.play(Create(axes),Create(x_labels))
        self.wait(1)
        self.imprimirTransform(func_graph)
        self.play(Create(valores))
        self.wait(1)
        self.play(Create(respuesta))
        self.play(Create(framebox))
        
        return 1
    def construct(self):
        enunciado = self.enunciado().move_to(UP*2)
        enungrafica =self.grafica().next_to(enunciado,DOWN)
        respuestas= self.respuestas().next_to(enungrafica,DOWN).set_color(Amarillo)
        for i in enunciado:
            self.play(Create(i))
        self.wait(1)
        self.play(Create(enungrafica))
        for i in respuestas:
            self.play(Create(i))
        self.wait(1)
        self.clear()
        self.soltext()
        self.desarrollo()
        self.wait(3)

class Short19(Scene):
    def enunciado(self):
        tam=22
        enun0 = VGroup(Tex("Si",font_size=tam),MathTex(r"  \left( \pi < \alpha < \frac{3\pi}{2}   \right)  ",font_size=tam)).arrange(RIGHT)
        enun1= VGroup(Tex("y",font_size=tam),MathTex(r"\tan( \alpha ) = \frac{a}{b},",font_size=tam)).arrange(RIGHT)
        enun2= Tex("entonces el valor de",font_size=tam,color=GREEN)
        enun3= MathTex(r"sin(2 \alpha ) \ es:",font_size=tam)
        enunciado = VGroup(enun0,enun1,enun2,enun3).arrange(DOWN,center=True)
        return enunciado
    def soltext(self):
        sol= Text("Solucion",font_size=20,font='Akira Expanded').set_color(YELLOW)
        self.play(FadeIn(sol, shift=DOWN, scale=0.66))
        self.play(FadeOut(sol, scale=1.5))
    def respuestas(self):
        tam=22
        res0 = MathTex(r"a) \ \frac{2ab}{a^2+b^2}",font_size=tam)
        res1 = MathTex(r"b) \ \frac{ab}{a^2+b^2}",font_size=tam)
        res2 = MathTex(r"c) \ -\frac{2ab}{a^2+b^2}",font_size=tam)
        res3 = MathTex(r"d) \ -\frac{ab}{a^2+b^2}",font_size=tam)
        res4 = MathTex(r"e) \ \frac{2ab}{\sqrt{a^2+b^2}}",font_size=tam)
        respuestas= VGroup(res0,res1,res2,res3,res4).arrange(DOWN,center=False, aligned_edge=LEFT)
        return respuestas
    def grafica(self):
        # Coordenadas de los vértices del triángulo
        ax = Axes()
        A = ax.c2p(-1.5, 1)
        B = ax.c2p(1.5, 1)
        C = ax.c2p(1.5, 3)

        # Crear los puntos del triángulo
        punto_A = Dot(A, color=BLUE)
        punto_B = Dot(B, color=BLUE)
        punto_C = Dot(C, color=BLUE)

        # Crear las líneas que forman el triángulo
        linea_AB = Line(A, B)
        linea_AC = Line(A, C)
        linea_CB = Line(C, B)

        # Crear los ángulos y etiquetas
        angulo = Angle( linea_AB,linea_AC,radius=1.2)
        etiqueta_angle = MathTex(r"\alpha", color=RED).move_to(ax.c2p(-0.5,1.3))
        etiqueta_a = MathTex(r"a", color=BLUE_D).move_to(ax.c2p(1.8,2))
        etiqueta_b = MathTex(r"b", color=BLUE_D).move_to(ax.c2p(0,0.6))
        etiqueta_c = MathTex(r"c", color=Morado).move_to(ax.c2p(-0.5,2.1))
        # Agregar todos los elementos a la escena
        grafica =VGroup(punto_A, punto_B, punto_C, linea_AB, linea_AC, linea_CB,angulo,etiqueta_angle,etiqueta_a,etiqueta_b,etiqueta_c)
        return grafica
    def desarrollo(self):
        tam=22
        des0=MathTex(r"\tan( \alpha ) = \frac{a}{b}",font_size=tam)
        des1=MathTex(r"c^2 = a^2+b^2",font_size=tam)
        des2=MathTex(r"\cos( \alpha ) = \frac{b}{\sqrt{a^2+b^2}}",font_size=tam)
        des3=MathTex(r"\sin( \alpha ) = \frac{a}{\sqrt{a^2+b^2}}",font_size=tam)
        des4=MathTex(r"\sin( 2 \alpha )= 2 \sin( \alpha )\cos( \alpha )",font_size=tam)
        des5=MathTex(r"\sin( 2 \alpha )= 2 \frac{a}{\sqrt{a^2+b^2}} \frac{b}{\sqrt{a^2+b^2}}",font_size=tam)
        des6=MathTex(r"\sin( 2 \alpha )= \frac{2ab}{a^2+b^2}",font_size=tam)
        desarrollo=VGroup(des0,des1,des2,des3,des4,des5,des6).arrange(DOWN,center=True)
        return desarrollo
    def construct(self):
        enunciado = self.enunciado().move_to(UP*2)
        respuestas= self.respuestas().next_to(enunciado,DOWN).set_color(Amarillo)
        graf =self.grafica().move_to(UP*2.3).scale(.8)
        desarrollo = self.desarrollo().next_to(graf,DOWN)
        framebox = SurroundingRectangle(desarrollo[-1],buff = .1)
        for i in enunciado:
            self.play(Create(i))
        self.wait(1)
        for i in respuestas:
            self.play(Create(i))
        self.wait(1)
        self.clear()
        self.soltext()
        self.play(Create(graf))
        self.wait(1)
        for i in desarrollo:
            self.play(Create(i))
            self.wait(1)
        self.play(Create(framebox))
        self.wait(3)
class Short20(Scene):
    def enunciado(self):
        tam=20
        enun0 = Tex("Al simplificar la expresion",font_size=tam)
        enun1= MathTex(r"\frac{ \left [ \sin(x+y)+\sin(x-y)  \right] \tan(y)  }{ \cos(x+y)-\cos(x-y)}",font_size=tam)
        enun2= Tex("se obtiene:",font_size=tam)
        enun3 = MathTex(r"", font_size=tam+3,color=VerdeClaro)
        enun4 = Tex("", font_size=tam)
        enunciado = VGroup(enun0,enun1,enun2).arrange(DOWN,center=True)
        return enunciado
    def soltext(self):
        sol= Text("Solucion",font_size=20,font='Akira Expanded').set_color(YELLOW)
        self.play(FadeIn(sol, shift=DOWN, scale=0.66))
        self.play(FadeOut(sol, scale=1.5))
    def respuestas(self):
        tam=20
        res0 = MathTex(r"a) \ -2",font_size=tam)
        res1 = MathTex(r"b) \ -1",font_size=tam)
        res2 = MathTex(r"c) \ -\frac{1}{2}",font_size=tam)
        res3 = MathTex(r"d) \ 1",font_size=tam)
        res4 = MathTex(r"e) \ 2",font_size=tam)
        respuestas= VGroup(res0,res1,res2,res3,res4).arrange(DOWN,center=False, aligned_edge=LEFT)
        return respuestas
    def desarrollo(self):
        tam=20
        des0 = MathTex(r"\frac{ \left [ \sin(x+y)+\sin(x-y)  \right] \tan(y)  }{ \cos(x+y)-\cos(x-y)}",font_size=tam)
        des1 = MathTex(r"\frac{ \left [ \sin(x) \cos(y) + \cos(x) \sin(y) + \sin(x) \cos(y) -\cos(x) \sin(y) \right] \tan(y)  }{ \cos(x) \cos(y) - \sin(x) \sin(y)- [\cos(x) \cos(y) + \sin(x) \sin(y)]}", font_size=tam).scale(0.6)
        des2 = MathTex(r"\frac{2\sin(x)\cos(y)\tan(y)}{-2\sin(x) \sin(y)}",font_size=tam)
        des3 = MathTex(r"\frac{-\tan(y)}{\frac{\sin(y)}{\cos(y)}}",font_size=tam+3)
        des4 = MathTex(r"-1",font_size=tam+3)
        des5 = MathTex(r"",font_size=tam,color=ORANGE)
        des6 = MathTex(r"", font_size=tam,color=YELLOW)
        desarrollo= VGroup(des0,des1,des2,des3,des4)
        return desarrollo
    def imprimirTransform(self,lista):
        for i in range(len(lista)-1):
            if i==0:
                self.play(Create(lista[0]))
                self.wait(2)
                self.play(Transform(lista[0],lista[i+1]))
                self.wait(2)
            else:
                self.play(Transform(lista[0],lista[i+1]))
                self.wait(3)
    def construct(self):
        enunciado = self.enunciado().move_to(UP*2)
        respuestas= self.respuestas().next_to(enunciado,DOWN).set_color(Amarillo)
        desarrollo= self.desarrollo()
        framebox = SurroundingRectangle(desarrollo[-1],buff = .1)
        for i in enunciado:
            self.play(Create(i))
        self.wait(1)
        for i in respuestas:
            self.play(Create(i))
        self.wait(1)
        self.clear()
        self.soltext()
        self.imprimirTransform(desarrollo)
        self.play(Create(framebox))
        self.wait(3)

class Short21(Scene):
    def enunciado(self):
        tam=20
        enun0 = Tex("Sean las matrices cuadradas",font_size=tam)
        enun1= MathTex(r"A_{nxn} \ y \ B_{nxn} ",font_size=tam)
        enun2= Tex("el resultado de la operacion matricial",font_size=tam-2)
        enun3 = MathTex(r"\left[ 2(A+B)^T + 2(BA)^T -(2A^T + 2B^T) \right]", font_size=tam+3,color=VerdeClaro)
        enun4 = Tex("siendo $B$ una matriz simetrica, es:", font_size=tam)
        enunciado = VGroup(enun0,enun1,enun2,enun3,enun4).arrange(DOWN,center=True)
        return enunciado
    def soltext(self):
        sol= Text("Solucion",font_size=20,font='Akira Expanded').set_color(YELLOW)
        self.play(FadeIn(sol, shift=DOWN, scale=0.66))
        self.play(FadeOut(sol, scale=1.5))
    def respuestas(self):
        tam=20
        res0 = MathTex(r"a) \ 2I_{nxn}",font_size=tam)
        res1 = MathTex(r"b) \ 2AB",font_size=tam)
        res2 = MathTex(r"c) \ 2A^TB",font_size=tam)
        res3 = MathTex(r"d) \ 2A^T",font_size=tam)
        res4 = MathTex(r"e) \ 2BA^T",font_size=tam)
        respuestas= VGroup(res0,res1,res2,res3,res4).arrange(DOWN,center=False, aligned_edge=LEFT)
        return respuestas
    def desarrollo(self):
        tam=20
        des0 = MathTex(r"\left[ 2(A+B)^T + 2(BA)^T -(2A^T + 2B^T) \right]", font_size=tam)
        des1 = MathTex(r"2(A^T+b^T) +2(BA)^T -(2A^T + 2B^T)", font_size=tam)
        des2 = MathTex(r"2(BA)^T", font_size=tam)
        des3 = MathTex(r"2A^TB^T", font_size=tam)
        des4 = MathTex(r"2A^TB", font_size=tam)
        desarrollo = VGroup(des0, des1, des2, des3, des4)
        return desarrollo

    def imprimirTransform(self,lista):
        for i in range(len(lista)-1):
            if i==0:
                self.play(Create(lista[0]))
                self.wait(2)
                self.play(Transform(lista[0],lista[i+1]))
                self.wait(2)
            else:
                self.play(Transform(lista[0],lista[i+1]))
                self.wait(2)
    def construct(self):
        enunciado = self.enunciado().move_to(UP*2)
        respuestas= self.respuestas().next_to(enunciado,DOWN).set_color(Amarillo)
        desarrollo= self.desarrollo()
        framebox = SurroundingRectangle(desarrollo[-1],buff = .1)
        for i in enunciado:
            self.play(Create(i))
        self.wait(1)
        for i in respuestas:
            self.play(Create(i))
        self.wait(1)
        self.clear()
        self.soltext()
        self.imprimirTransform(desarrollo)
        self.play(Create(framebox))
        self.wait(3)


class Short22(Scene):
    def enunciado(self):
        tam=20
        enun0 = Tex("Dado el sistema de ecuaciones lineales",font_size=tam)
        enun1= MathTex(r"\begin{cases} x+2y+kz=4 \\x+y-2z=-3 \\x-2y=5   \end{cases}",font_size=tam)
        enun2= Tex("el valor de $k$ para que el",font_size=tam-2)
        enun3 = Tex("sistema sea INCONSISTENTE, es:", font_size=tam)
        enun4 = Tex("", font_size=tam)
        enunciado = VGroup(enun0,enun1,enun2,enun3).arrange(DOWN,center=True)
        return enunciado
    def soltext(self):
        sol= Text("Solucion",font_size=20,font='Akira Expanded').set_color(YELLOW)
        self.play(FadeIn(sol, shift=DOWN, scale=0.66))
        self.play(FadeOut(sol, scale=1.5))
    def respuestas(self):
        tam=20
        res0 = MathTex(r"a) \ -11/3",font_size=tam)
        res1 = MathTex(r"b) \ -8/3",font_size=tam)
        res2 = MathTex(r"c) \ -5/3",font_size=tam)
        res3 = MathTex(r"d) \ 7",font_size=tam)
        res4 = MathTex(r"e) \ 8",font_size=tam)
        respuestas= VGroup(res0,res1,res2,res3,res4).arrange(DOWN,center=False, aligned_edge=LEFT)
        return respuestas
    def desarrollo(self):
        tam=20
        m0 = Matrix([[1,2,"k", "|",4 ], [1, 1,-2,"|",-3],[1,-2,0,"|",5]],v_buff=1.3,h_buff=1.6)
        m1 = Matrix([[1,2,"k", "|",4 ], [0, 1,"k+2","|",7],[1,-2,0,"|",5]],v_buff=1.3,h_buff=1.6)
        m2 = Matrix([[1,2,"k", "|",4 ], [0, 1,"k+2","|",7],[0,4,"k","|",-1]],v_buff=1.3,h_buff=1.6)
        m3 = Matrix([[1,2,"k", "|",4 ], [0, -4,"-4k+8","|",28],[0,4,"k","|",-1]],v_buff=1.3,h_buff=2)
        m4 = Matrix([[1,2,"k", "|",4 ], [0, -4,"-4k+8","|",28],[0,0,"-3k-8","|",-29]],v_buff=1.3,h_buff=2)
        matrices = VGroup(m0,m1,m2,m3,m4).scale(0.4).move_to(UP*2)
        des0 = MathTex(r"-3k-8=0",font_size=22)
        des1 = MathTex(r"k=-\frac{8}{3}",font_size=22)
        desarr = VGroup(des0,des1).arrange(DOWN,center=True).next_to(matrices,DOWN)
        desarrollo = VGroup(matrices,desarr)
        return desarrollo

    def imprimirTransform(self,lista):
        for i in range(len(lista)-1):
            if i==0:
                self.play(Create(lista[0]))
                self.wait(2)
                self.play(Transform(lista[0],lista[i+1]))
                self.wait(2)
            else:
                self.play(Transform(lista[0],lista[i+1]))
                self.wait(2)
                
    def construct(self):
        enunciado = self.enunciado().move_to(UP*2)
        respuestas= self.respuestas().next_to(enunciado,DOWN).set_color(Amarillo)
        desarrollo= self.desarrollo()
        framebox = SurroundingRectangle(desarrollo[-1][-1],buff = .1)
        m4=desarrollo[0][-1]
        for i in enunciado:
            self.play(Create(i))
        self.wait(1)
        for i in respuestas:
            self.play(Create(i))
        self.wait(1)
        self.clear()
        self.soltext()
        for i,shape in enumerate(desarrollo):
            if i==0:
                self.imprimirTransform(shape)
            else:
                self.wait(2)
                self.play(Create(SurroundingRectangle(m4.get_rows()[2]).set_color(GREEN)))
                self.wait(2)
                for i in shape:
                    self.play(Create(i))
                    self.wait(1)
        self.play(Create(framebox))
        self.wait(3)

class Short23(Scene):
    def enungrafica(self):
        ax=Axes(
            x_range=[-PI/4,5*PI/4],
            y_range=[-1,2.5],
            x_length=PI,
            y_length=3,
            tips=False,
        ).set_color(Amarillo)
        def func(x):
            return 1-np.cos(x)
        func_tex=MathTex(r"f(x)=1-\cos(x)",font_size=18).move_to(ax.c2p(PI/2,2.2))
        func_graph= ax.plot(func,color=BLUE_D,x_range=[0,PI])
        recta1 = Line(ax.c2p(0,1-np.cos(0)),ax.c2p(PI,1-np.cos(PI))).set_color(ORANGE)
        recta2 = Line(ax.c2p(0,0),ax.c2p(PI,0)).set_color(ORANGE)
        recta3 = Line(ax.c2p(PI,0),ax.c2p(PI,1-np.cos(PI))).set_color(ORANGE)
        rectax= Line(ax.c2p(PI,-1),ax.c2p(PI,2.5)).set_color(Morado)
        triangulo=VGroup(recta1,recta2,recta3)
        area = ax.get_area(
            func_graph,
            x_range=(0, PI),
            color=(GREEN_B, GREEN_D),
            opacity=0.5,
        )
        letras=VGroup(
            MathTex(r"O",font_size=24).move_to(ax.c2p(-0.2,0.2)),
            MathTex(r"A",font_size=24).move_to(ax.c2p(PI+0.2,1-np.cos(PI))),
            MathTex(r"B",font_size=24).move_to(ax.c2p(PI+0.2,0.2)),
            MathTex(r"0",font_size=24).move_to(ax.c2p(0,-0.2)),
            MathTex(r"\pi",font_size=24).move_to(ax.c2p(PI,-0.2)),
            MathTex(r"x=\pi",font_size=24).move_to(ax.c2p(PI,-1.2)),
        )
        grafica= VGroup(ax,func_tex,func_graph,area,triangulo,letras,rectax)
        return grafica
    def enunciado(self):
        tam=20
        enun0 = Tex("Se desea aproximar el area bajo la curva",font_size=tam)
        enun1= Tex("definida por la funcion $f(x)=1-\cos(x)$",font_size=tam)
        enun2= VGroup(Tex("en el intervalo",font_size=tam),MathTex(r"[0, \pi]",font_size=tam)).arrange(RIGHT)
        enun3 = Tex("en el eje $X$ y la recta $x= \pi,$", font_size=tam)
        enun4 = Tex("considerando la superficie del triangulo", font_size=tam)
        enun5 = Tex("$OAB$, tal com se muestra en la figura", font_size=tam)
        enun6 = Tex("Con este procedimiento, el area en $u^2$, es igual a:", font_size=tam)
        enunciado = VGroup(enun0,enun1,enun2,enun3,enun4,enun5,enun6).arrange(DOWN,center=True)
        return enunciado
    def soltext(self):
        sol= Text("Solucion",font_size=20,font='Akira Expanded').set_color(YELLOW)
        self.play(FadeIn(sol, shift=DOWN, scale=0.66))
        self.play(FadeOut(sol, scale=1.5))
    def desarrollo(self):
        tam=22
        desarrollo=VGroup(
            MathTex(r"Area = \frac{(base) \cdot (altura)}{2}",font_size=20),
            MathTex(r"Area = \frac{\pi (1-\cos(\pi))}{2}",font_size=tam),
            MathTex(r"Area = \frac{\pi (1-(-1))}{2}",font_size=tam),
            MathTex(r"Area = \frac{\pi (2)}{2}",font_size=tam),
            MathTex(r"Area = \pi",font_size=tam),
        )
        return desarrollo.arrange(DOWN,center=True)
    def construct(self):
        enungrafica = self.enungrafica()
        enungraficacopy = enungrafica.copy().scale(0.5).move_to(UP*2)
        desarrollo=self.desarrollo().next_to(enungraficacopy,DOWN)
        framebox = SurroundingRectangle(desarrollo[-1][-1],buff = .1)
        for i, shape in enumerate(enungrafica):
            self.play(Create(shape))
            self.wait(1)
        self.wait(1)
        self.clear()
        self.soltext()
        self.play(Create(enungraficacopy))
        for i in desarrollo:
            self.play(Create(i))
            self.wait(1)
        self.play(Create(framebox))
        self.wait(1)

class Short24(Scene):
    def imprimirTransform(self,lista):
        for i in range(len(lista)-1):
            if i==0:
                self.play(Create(lista[0]))
                self.wait(2)
                self.play(Transform(lista[0],lista[i+1]))
                self.wait(2)
            else:
                self.play(Transform(lista[0],lista[i+1]))
                self.wait(2)
    def enungrafica(self):
        ax=Axes(
            x_range=[-4,4],
            y_range=[-5,3],
            x_length=4,
            y_length=4,
            tips=False,
        ).set_color(Amarillo)
        def func(x):
            return (4/5)*x-2
        numbers_incl = VGroup(
            MathTex(r"-1",font_size=18).move_to(ax.c2p(0.2,-1)),
            MathTex(r"-4",font_size=18).move_to(ax.c2p(0.2,-4)),
        )
        plano = VGroup(
            Line(ax.c2p(-4,0),ax.c2p(4,0)),
            Line(ax.c2p(0,-5),ax.c2p(0,3)),
        ).set_color(Amarillo)
        func_tex=MathTex(r"f(x)=\frac{4}{5}x -2",font_size=22).next_to(ax,UP)
        func_graph= ax.plot(func,color=BLUE_D,x_range=[-4,4])
        func_graphrever= ax.plot(lambda x: -(4/5)*x-2,color=BLUE_D,x_range=[-4,4])
        recta1 = Line(ax.c2p(-2.5,-1),ax.c2p(0,-1)).set_color(ORANGE)
        recta2 = Line(ax.c2p(0,-1),ax.c2p(0,-2)).set_color(ORANGE)
        recta3 = Line(ax.c2p(0,-2),ax.c2p(-2.5,-4)).set_color(ORANGE)
        recta4= Line(ax.c2p(-2.5,-4),ax.c2p(-2.5,-1)).set_color(ORANGE)
        dashed_1 = DashedLine(ax.c2p(0,-4),ax.c2p(-2.5,-4))
        dashed_2 = DashedLine(ax.c2p(0,-4),ax.c2p(2.5,-4))
        trapecio=VGroup(recta1,recta2,recta3,recta4,dashed_1)
        reversotrap= VGroup(
            Line(ax.c2p(2.5,-1),ax.c2p(0,-1)).set_color(ORANGE),
            Line(ax.c2p(0,-1),ax.c2p(0,-2)).set_color(ORANGE),
            Line(ax.c2p(0,-2),ax.c2p(2.5,-4)).set_color(ORANGE),
            Line(ax.c2p(2.5,-4),ax.c2p(2.5,-1)).set_color(ORANGE)
        )
        areatrap = ax.get_area(
            func_graph,
            x_range=(-2.5, 0),
            bounded_graph=ax.plot(lambda x: -1),
            color=(GREEN_B, GREEN_D),
            opacity=1,
        )
        areatrapreverse= ax.get_area(
            func_graphrever,
            x_range=(0,2.5),
            bounded_graph=ax.plot(lambda x: -1),
            color=(GREEN_B, GREEN_D),
            opacity=1,
        )
        ellipse1= Ellipse(width=2.5,height=0.5).set_color(GREEN_B).move_to(ax.c2p(0,-1))
        ellipse2= Ellipse(width=2.5,height=0.5).set_color(GREEN_B).move_to(ax.c2p(0,-4))
        grafica= VGroup(plano,func_tex,func_graph,areatrap,numbers_incl,trapecio)
        solucion = VGroup(areatrapreverse, reversotrap,ellipse1,ellipse2,dashed_2)
        return VGroup(grafica,solucion)
    def enunciado(self):
        tam=20
        enun0 = Tex("La funcion lineal $f$",font_size=tam)
        enun1= Tex("tiene por regla de correspondencia",font_size=tam)
        enun2= MathTex(r"f(x)=\frac{4}{5}x -2",font_size=tam)
        enun3 = Tex("el volumen del solido de revolucion", font_size=tam)
        enun4 = Tex("que se genera al rotar la region", font_size=tam)
        enun5 = Tex("sombreada alrededor del eje $Y$", font_size=tam)
        enun6 = Tex("en $$u^3, es:", font_size=tam)
        enunciado = VGroup(enun0,enun1,enun2,enun3,enun4,enun5,enun6).arrange(DOWN,center=True)
        return enunciado
    def solucion(self):
        tam=20
        desarrollo = VGroup( MathTex(r"V= Cilindro-Cono",font_size=tam)
        ,MathTex(r"V= \pi r^2 h_{cil} - \frac{1}{3} \pi r^2 h_{cono}",font_size=tam)
        ,MathTex(r"\frac{4}{5}x-2=-4 \rightarrow x=-\frac{5}{2}",font_size=tam)
        ,MathTex(r"r= \frac{5}{2}, h_{cil}=3,  h_{cono}=2 ",font_size=tam)
        ,MathTex(r"V =\pi (\frac{5}{2})^2 3 - \frac{1}{3} \pi (\frac{5}{2})^2 2",font_size=tam)
        ,MathTex(r"V = \frac{75\pi}{4}-\frac{25\pi}{6}",font_size=tam)
        ,MathTex(r"V = \frac{175\pi}{12}",font_size=tam)
        )
        return desarrollo 
    def soltext(self):
        sol= Text("Solucion",font_size=20,font='Akira Expanded').set_color(YELLOW)
        self.play(FadeIn(sol, shift=DOWN, scale=0.66))
        self.play(FadeOut(sol, scale=1.5))
    def construct(self):
        grafica= self.enungrafica().scale(0.8)
        desarrollo=self.solucion().next_to(grafica,DOWN)
        framebox = SurroundingRectangle(desarrollo[-1],buff = .1)
        self.play(Create(self.enungrafica()[0].scale(0.8)))
        self.wait(4)
        self.clear()
        self.soltext()
        self.wait(1)
        for i in grafica:
            self.play(Create(i))
            self.wait(2)
        self.wait(2)
        self.imprimirTransform(desarrollo)
        self.play(Create(framebox))
        self.wait(2)







    
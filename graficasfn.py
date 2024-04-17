from manim import *
import time
Amarillo='#ddf599'
Morado = "#fe04f2"
Celeste = "#0ad6fb"
Rojo = "#fb0a4c"
RosaRed ="#fe0463"
VerdeClaro ="#04febe"
GREEN_SCREEN = '#00FF00'
class GraficasFunciones(Scene):
    def construct(self):
        tam=35
        def polinomio(x):
            return 3*x**2+5*x
        title1 = Tex("Representacion Gráfica de funciones",font_size=45,color=YELLOW)
        title2 = Tex("Representacion Gráfica de funciones",font_size=45,color=YELLOW)
        tex1=Tex("Funciones comunes:",font_size=tam)
        tex2=Tex("Funciones comunes:",font_size=tam)
        enun1=VGroup(title1,tex1).arrange(DOWN)
        enun2=VGroup(title2,tex2).arrange(DOWN,center=False, aligned_edge=LEFT).scale(0.8).to_corner(UP+LEFT)
        axfunc5=Axes(x_range=[-2,2,1],y_range=[-4,4],x_length=6,tips=False).set_color(GREEN)
        axpol=Axes(x_range=[-3,2,1],y_range=[-4,4],x_length=6,tips=False).set_color(GREEN).add_coordinates()
        axpol_labels = axpol.get_axis_labels()
        pol_curve = axpol.plot(polinomio,color=ORANGE)
        pol_graph=VGroup(axpol,axpol_labels,pol_curve).to_corner(DOWN+RIGHT)
        ##
        tex3= Tex("Elaboracion de gráfica por evaluacion en la funcion",font_size=tam)
        tex4= Tex("Ejemplo: Graficar $y=3x^2+5x$",font_size=tam)
        texgr1=VGroup(tex3,tex4).arrange(DOWN,center=False, aligned_edge=LEFT).scale(0.8).to_corner(UP+LEFT)
        def graph(fn,color_g,Name,x1,x2):
            ax = Axes(
                x_range=[-4,4,1],
                y_range=[-4,4],
                x_length=6,
                tips=False
            ).set_color(GREEN)
            func= ax.plot(fn,x_range=[x1,x2],color=color_g)
            axes_labels = ax.get_axis_labels()
            func_label = ax.get_graph_label(func, Name)
            return VGroup(ax,axes_labels,func,func_label)
        def graph2(fn,color_g,Name):
            ax = Axes(
                x_range=[-2,2,1],
                y_range=[-4,4],
                x_length=6,
                tips=False
            ).set_color(GREEN)
            func= ax.plot(fn,color=color_g,discontinuities=[0],dt=0.1)
            axes_labels = ax.get_axis_labels()
            func_label = ax.get_graph_label(func, Name)
            return VGroup(ax,axes_labels,func,func_label)
        def graph3(fn1,fn2,color_g,Name):
            ax = Axes(
                x_range=[-4,4,1],
                y_range=[-4,4],
                x_length=6,
                tips=False
            ).set_color(GREEN)
            funcpos= ax.plot(fn1,color=color_g,x_range=[0,4])
            funcneg= ax.plot(fn2,color=color_g,x_range=[-4,0])
            axes_labels = ax.get_axis_labels()
            func_label = ax.get_graph_label(funcpos, Name)
            return VGroup(ax,axes_labels,funcpos,funcneg,func_label)
        func1 = lambda x: x**2
        func2 = lambda x: x**3
        func3 = lambda x: 1/x
        func4 = lambda x: x
        func5= ImplicitFunction(
            lambda x,y: x-y**2,
            color=Celeste,
            y_range=[0,4]
        )
        func6p1 =lambda x: x
        func6p2 =lambda x: -x
        g1= graph(func1,Celeste,Tex("$x^2$"),-2,2).scale(0.7)
        g2= graph(func2,Celeste,Tex("$x^3$"),-4,4).scale(0.7)
        g3= graph2(func3,Celeste,MathTex(r"\frac{1}{x}")).scale(0.7)
        g4= graph(func4,Celeste,MathTex(r"x"),-4,4).scale(0.7)
        g5=VGroup(func5,axfunc5,MathTex(r"\sqrt{x}",color=Celeste).move_to([-1,1,0])).scale(0.7)
        g6= graph3(func6p1,func6p2,Celeste,MathTex(r"|x|")).scale(0.7)
        gfn = VGroup(g1,g2,g3,g4,g4,g6,g5)
        ##pol graph start
        line1tab=Line([-6,1,0],[-3,1,0]).set_color(MAROON)
        line2tab=Line([-4.5,1.5,0],[-4.5,-3,0]).set_color(MAROON)
        tabla=VGroup(line1tab,line2tab,Tex("$x$",font_size=tam).move_to([-5,1.2,0]),Tex("$3x^2+5x$",font_size=tam).move_to([-3.5,1.2,0]))
        x0=-1
        x0_tex=MathTex(str(x0),font_size=tam).move_to([-5,0.5,0])
        fx0_tex=MathTex(str(round(polinomio(-1),2)),font_size=tam).move_to([-4,0.5,0])
        pointx0= axpol.c2p(x0,round(polinomio(-1),2))
        px0= Dot(pointx0).set_color(ORANGE)
        circle = Circle(radius=1, color=ORANGE).move_to(pointx0)
        dytab=0.1
        ##pol graph end
        self.play(Create(enun1),run_time=4)
        self.wait(2)
        self.play(Transform(enun1,enun2))
        self.wait(2)
        self.play(Create(g1))
        self.wait(4)
        for i in range(len(gfn)-1):
            self.play(ReplacementTransform(gfn[i],gfn[i+1]))
            self.wait(3)
        self.wait()
        self.clear()
        self.wait(1)
        self.play(Create(texgr1),run_time=5)
        self.wait(3)
        self.play(Create(tabla),run_time=2)
        #self.play(Create(pol_graph),run_time=2)
        for i in range(len(pol_graph)-1):
            self.play(Create(pol_graph[i]),run_time=0.5)
        self.wait(3)
        self.play(Create(x0_tex))
        self.wait(3)
        self.play(Create(fx0_tex))
        self.play(Create(axpol.get_lines_to_point(pointx0).set_color(ORANGE)))
        self.wait(3)
        self.play(GrowFromCenter(circle))
        self.play(Transform(circle, px0))
        self.wait(3)
        for i in np.arange(-2.2,2,0.4):
            xval=MathTex(str(round(i,2)),font_size=tam)
            yval=MathTex(str(round(polinomio(i),2)),font_size=tam)
            p=MathTex("p("+str(round(i,2))+","+str(round(polinomio(i),2))+")",font_size=tam)
            self.play(Create(xval.move_to([-5,dytab,0])),run_time=0.3)
            self.wait(0.5)
            self.play(Create(yval.move_to([-4,dytab,0])),run_time=0.3)
            self.play(Create(p.move_to([-2.0,dytab,0])),run_time=0.3)
            self.wait(0.5)
            self.play(Transform(p,Dot(axpol.c2p(i,round(polinomio(i),2))).set_color(ORANGE)))
            dytab-=0.4
        for i in np.arange(-2.5,1.2,0.1):
            self.play(Create(Dot(axpol.c2p(i,round(polinomio(i),2))).set_color(ORANGE)),run_time=0.1)

        self.wait(3)
        self.play(Create(pol_graph[-1]),run_time=4)
        self.wait(3)

###################################
class TecnicasMejor(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        tam=35
        title = Tex("Algunas técnicas de Graficacion",font_size=40,color=Amarillo)
        subtitle1 = Tex("Desplazamientos",font_size=tam,color=VerdeClaro)
        subtitle2 = Tex("Compresiones o alargamientos",font_size=tam,color=VerdeClaro)
        subtitle3 = Tex("Reflexiones",font_size=tam,color=VerdeClaro)
        tex0=Tex("$f(x-c)$ : Desplazamiento horizontal a la derecha",font_size=28)
        tex1=Tex("$f(x+c)$ : Desplazamiento horizontal a la izquierda",font_size=28)
        tex2=Tex("$f(x)+c$ : Desplazamiento vertical hacia arriba",font_size=28)
        tex3=Tex("$f(x)-c$ : Desplazamiento vertical hacia abajo",font_size=28)
        tex4=MathTex(r"f(x)=(x-2)^3+4",font_size=tam,color=Celeste)
        tex5=MathTex(r"f(x)=(3x-2)^3+4",font_size=tam,color=Celeste)
        tex6=MathTex(r"f(-x)=(-3x-2)^3+4",font_size=tam,color=Celeste)
        tex7=MathTex(r"-f(x)=-(3x-2)^3-4",font_size=tam,color=Celeste)
        enun = VGroup(title,subtitle1,tex0,tex1,tex2,tex3,tex4).arrange(DOWN,center=False, aligned_edge=LEFT).scale(0.8).to_corner(UP+LEFT)
        def graph(fn,color_g,Name,x1,x2):
            ax = Axes(
                x_range=[-6,6,1],
                y_range=[-6,6],
                y_length=10,
                tips=False
            ).add_coordinates().set_color(GREEN)
            func= ax.plot(fn,x_range=[x1,x2],color=color_g)
            axes_labels = ax.get_axis_labels()
            func_label = ax.get_graph_label(func, Name)
            return VGroup(ax,axes_labels,func,func_label)
        def graph2(fn,color_g,Name,x1,x2,i):
            ax = Axes(
                x_range=[x1,x2,1],
                y_range=[-10,10],
                tips=False
            ).add_coordinates().set_color(GREEN)
            func= ax.plot(fn,x_range=[x1,x2],color=color_g)
            axes_labels = ax.get_axis_labels()
            func_label = ax.get_graph_label(func, Name)
            p=ax.c2p(2/round(i,2),((i*(2/round(i,2))-2)**3)+4)
            linep=ax.get_lines_to_point(p).set_color(ORANGE)
            return VGroup(ax,axes_labels,func,func_label,linep,MathTex(r"("+str(round(2/round(i,2),2))+","+str(((i*(2/round(i,2))-2)**3)+4)+")",font_size=32).next_to(p,UP))
        func1 = lambda x: x**3
        func2 = lambda x: (x-2)**3
        func3 = lambda x: ((x-2)**3)+4
        func4 = lambda x: ((3*x-2)**3)+4
        func5 = lambda x: ((-3*x-2)**3)+4
        func6 = lambda x: (-(3*x-2)**3)-4
        g1= graph(func1,Celeste,Tex("$x^3$"),-2,2).scale(0.7).to_corner(RIGHT)
        g1.add(Dot(g1[0].c2p(0,0)).set_color(ORANGE))
        g2= graph(func2,Celeste,Tex("$(x-2)^3$"),0,4).scale(0.7).to_corner(RIGHT)
        g2.add(Dot(g2[0].c2p(2,0)).set_color(ORANGE))
        g3= graph(func3,Celeste,Tex("$(x-2)^3+4$"),0,4).scale(0.7).to_corner(RIGHT)
        g33= graph(func3,Celeste,Tex("$(x-2)^3+4$"),0,4).scale(0.7)
        g3.add(Dot(g3[0].c2p(2,4)).set_color(ORANGE))
        gfn=VGroup(g1,g2,g3)
        ##
        g4 =graph(func4,Celeste,Tex("$(3x-2)^3+4$"),0,1.5).scale(0.7)
        g44 =graph(func4,Celeste,Tex("$(3x-2)^3+4$"),0,1.5).scale(0.7)
        g441 =graph(func4,Celeste,Tex("$(3x-2)^3+4$"),0,1.5).scale(0.7)
        g5=graph(func5,Celeste,Tex("$(-3x-2)^3+4$"),-1.5,0).scale(0.7)
        g6=graph(func6,Celeste,Tex("$-(3x-2)^3-4$"),0,1.5).scale(0.7)
        ##
        for i in enun:
            self.play(Create(i))
            self.wait(1)
        self.wait(2)
        self.play(Create(g1))
        self.wait(17)
        for i in range(len(gfn)-1):
            self.play(ReplacementTransform(gfn[i],gfn[i+1]))
            self.wait(3)
        g3.add(g3[0].get_lines_to_point(g3[0].c2p(2,4)).set_color(ORANGE))
        self.play(self.camera.frame.animate.move_to([0,3,0]))
        self.wait(2)
        self.clear()
        compresion= VGroup(subtitle2,tex5).arrange(DOWN,center=False, aligned_edge=LEFT).to_corner(UP+LEFT)
        reflexion= VGroup(subtitle3,tex6,tex7).arrange(DOWN,center=False, aligned_edge=LEFT).to_corner(UP+LEFT)
        framebox1 = SurroundingRectangle(reflexion[1] ,buff = .1)
        framebox2 = SurroundingRectangle(reflexion[2], buff = .1)
        self.play(Create(compresion))
        self.wait(2)
        self.play(Create(g33))
        self.wait(23)
        self.play(ReplacementTransform(g33,g4))
        self.wait(2)
        self.remove(compresion)
        self.play(self.camera.frame.animate.move_to([0,0,0]))
        for i in np.arange(3,0.1,-0.2):
            func_i= lambda x: ((i*x-2)**3)+4
            g_i= graph2(func_i,Celeste,Tex("$("+str(round(i,2))+"x-2)^3+4$"),0,4/i,i).scale(0.7)
            self.play(Transform(g4,g_i))
        for i in np.arange(0.2,6,0.2):
            func_i= lambda x: ((i*x-2)**3)+4
            g_i= graph2(func_i,Celeste,Tex("$("+str(round(i,2))+"x-2)^3+4$"),0,4/i,i).scale(0.7)
            self.play(Transform(g4,g_i))
        self.wait(5)
        self.clear()
        self.wait()
        self.play(self.camera.frame.animate.move_to([0,3,0]))
        self.play(Create(reflexion))
        self.play(Create(g44))
        self.wait(15)
        self.play(ReplacementTransform(g44,g5),Create(framebox1))
        self.wait(15)
        self.play(ReplacementTransform(g5,g441))
        self.wait(5)
        self.play(ReplacementTransform(g441,g6.move_to(UP)),ReplacementTransform(framebox1,framebox2))
        self.play(self.camera.frame.animate.move_to([0,0,0]))
        self.wait(5)
        

        


        


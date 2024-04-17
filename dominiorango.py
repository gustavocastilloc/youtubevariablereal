from manim import *
Amarillo='#ddf599'
Morado = "#fe04f2"
Celeste = "#0ad6fb"
Rojo = "#fb0a4c"
RosaRed ="#fe0463"
VerdeClaro ="#04febe"
GREEN_SCREEN = '#00FF00'
class DominioRangoIntro(MovingCameraScene):
    def construct(self):
        # Fondo
        self.camera.frame.save_state()
        img_question= ImageMobject("img/img1.png")
        # create the axes and the curve
        ax = Axes(x_range=[-10, 10], y_range=[-5, 5])
        graph = ax.plot(lambda x: 3*np.sin(x), color=BLUE, x_range=[-3*PI, 3 * PI])

        # create dots based on the graph
        moving_dot = Dot(ax.i2gp(graph.t_min, graph), color=Morado)
        dot_1 = Dot(ax.i2gp(graph.t_min, graph))
        dot_2 = Dot(ax.i2gp(graph.t_max, graph))

        self.add(ax, graph, dot_1, dot_2, moving_dot)
        self.play(self.camera.frame.animate.scale(0.5).move_to(moving_dot),run_time=2)

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.add_updater(update_curve)
        self.play(MoveAlongPath(moving_dot, graph, rate_func=linear),run_time=6)
        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))

        self.clear()
        Domtex_in = Tex("Dominio").scale(3).set_color(YELLOW)
        Rangtex_out = Tex("Rango").scale(3).set_color(YELLOW)
        self.play(FadeIn(Domtex_in, shift=DOWN, scale=0.66))
        self.play(ReplacementTransform(Domtex_in, Rangtex_out))
        self.play(FadeOut(Rangtex_out, shift=DOWN * 2, scale=1.5))
        self.add(img_question)
        self.wait(3)
        self.remove(img_question)
        # add funciones visualization
        axfunc5=Axes(x_range=[-2,2,1],y_range=[-4,4],x_length=6,tips=False).set_color(GREEN)
        axpol=Axes(x_range=[-3,2,1],y_range=[-4,4],x_length=6,tips=False).set_color(GREEN).add_coordinates()
        axpol_labels = axpol.get_axis_labels()
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
        gfn = VGroup(g1,g2,g3,g4,g4,g5)
        self.play(Create(g1))
        for i in range(len(gfn)-1):
            self.play(ReplacementTransform(gfn[i],gfn[i+1]))
            self.wait(0.1)
        self.wait()
        self.clear()
        self.play(
            Rotate(
                Square(side_length=0.5).shift(UP * 2),
                angle=2*PI,
                about_point=ORIGIN,
                rate_func=linear,
            ),
            Rotate(Square(side_length=0.5), angle=2*PI, rate_func=linear),
            
            )
        
        self.clear()
        self.play(
            Rotate(
                Square(side_length=0.5).shift(UP * 2),
                angle=2*PI,
                about_point=ORIGIN,
                rate_func=linear,
            ),
            Rotate(Square(side_length=0.5), angle=2*PI, rate_func=linear),
            
            )
        self.clear()
        self.play(
            Rotate(
                Square(side_length=0.5).shift(UP * 2),
                angle=2*PI,
                about_point=ORIGIN,
                rate_func=linear,
            ),
            Rotate(Square(side_length=0.5), angle=2*PI, rate_func=linear),
            
            )
        self.clear()

# Relleno de espacio 
class GetVerticalLinesToGraph(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 8.0, 1],
            y_range=[-1, 1, 0.2],
            axis_config={"font_size": 24},
        ).add_coordinates()

        curve = ax.plot(lambda x: np.sin(x) / np.e ** 1 * x,x_range=[0, 4])
        curve2 = ax.plot(lambda x: np.cos(x),x_range=[5, 7])

        lines = ax.get_vertical_lines_to_graph(
            curve, x_range=[0, 4], num_lines=30, color=BLUE
        )
        lines2 = ax.get_vertical_lines_to_graph(
            curve2, x_range=[5, 7], num_lines=30, color=BLUE
        )

        self.add(ax, curve,curve2)
        self.play(Write(lines),run_time=8)
        self.play(Write(lines2),run_time=9)
        self.clear(1)

class DefDominioRango(Scene):
    def construct(self):
        Domtex_in = Tex("Dominio").scale(3).set_color(YELLOW)
        Rangtex_in = Tex("Rango").scale(3).set_color(YELLOW)
        funcion = MathTex(r"f(x)=4x-x^2 \ \forall x, \ 0 \leq x \leq 4").to_corner(UP+RIGHT)
        funcdom= MathTex(r"dom \ f = \forall x, \ 0 \leq x \leq 4").next_to(funcion,DOWN)
        funcrg= MathTex(r"Rango \ f = f(x), tal que  \ 0 \leq f(x) \leq 4").move_to(UP*2.6)
        ax = Axes(
            x_range=[0, 5],
            y_range=[0, 6],
            tips=False,
        ).add_coordinates()
        ellipse_2 = Ellipse(width=9.6, height=.8, color=Morado,fill_opacity=0.5).move_to(ax.c2p(2))
        ellipse_3 = Ellipse(width=.8, height=4, color=GREEN,fill_opacity=0.5).move_to(ax.c2p(0,2))
        line_rg = ax.get_horizontal_line(ax.c2p(2,4), line_func=Line,color=GREEN_B)
        labels = ax.get_axis_labels(x_label="x (seg)", y_label="f(x) metros")

        t = ValueTracker(0)

        def func(x):
            return  4 * x - x ** 2
        graph = ax.plot(func , x_range=[0, 4], color=BLUE_C)

        initial_point = [ax.coords_to_point(t.get_value(), func(t.get_value()))]
        dot = Dot(point=initial_point)

        dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), func(t.get_value()))))
        x_space = np.linspace(*ax.x_range[:2],200)
        minimum_index = func(x_space).argmin()
        ###
        lines = ax.get_vertical_lines_to_graph(
            graph, x_range=[0, 4], num_lines=30, color=BLUE
        )
        framebox1 = SurroundingRectangle(funcdom, buff = .1)
        framebox2 = SurroundingRectangle(funcrg, buff = .1)
        self.play(FadeIn(Domtex_in, shift=DOWN, scale=0.66))
        self.play(FadeOut(Domtex_in ,scale=1.5))
        self.add(ax, labels, graph, dot)
        self.play(Write(funcion))
        self.wait(1)
        self.play(t.animate.set_value(x_space[minimum_index]),run_time=5 )      
        self.play(t.animate.set_value(x_space[minimum_index]),run_time=5 )      
        self.wait(10) 
        self.play(Write(ellipse_2),run_time=3)     
        self.wait(3)
        self.play(Write(funcdom))
        self.play(
            Create(framebox1)
        )
        self.wait(2)
        self.clear()
        self.play(FadeIn(Rangtex_in, shift=DOWN, scale=0.66))
        self.play(FadeOut(Rangtex_in ,scale=1.5))
        self.add(ax, labels, graph, dot)
        self.play(Write(funcion),Write(line_rg))
        self.wait(4)
        self.play(Write(ellipse_3),run_time=3)
        self.wait(1)
        self.play(Write(funcrg))
        self.play(
            Create(framebox2)
        )
        self.wait(19)
class Ejemplo1(Scene):
    def construct(self):
        funcion1 = MathTex(r"f(x)=x^2")
        domfuncion1 = MathTex(r"dom f = \mathbb R").next_to(funcion1,DOWN)
        rangfuncion1 = MathTex(r"rango f = f(x) \geqslant 0").to_corner(UP+RIGHT)

        ax = Axes(
                x_range=[-10,10,1],
                y_range=[-1,15],
                x_length=6,
                tips=False
            ).set_color(GREEN)
        func1 = lambda x: x**2
        func= ax.plot(func1,x_range=[-10,10],color=Celeste)
        axes_labels = ax.get_axis_labels()
        func_label = ax.get_graph_label(func, Tex("$x^2$"))
        
        
        g1 = VGroup(ax,axes_labels,func,func_label)
        self.play(Write(funcion1),run_time=3)
        self.wait(3)
        self.play(Write(domfuncion1))
        self.wait(6)
        self.clear()
        self.play(Write(g1))
        self.wait(6)
        for i in np.arange(0,5,0.2):
            self.play(Write(ax.get_lines_to_point(ax.c2p(i,func1(i)), color=GREEN_B)),
            Write(ax.get_lines_to_point(ax.c2p(-i,func1(-i)), color=GREEN_B)),
            run_time=0.2)
        self.wait(4)
        self.play(Write(rangfuncion1),run_time=3)
        self.wait(3)

class Ejemplo2(Scene):
    def construct(self):
        funcion1 = MathTex(r"g(x)=\sqrt{x-4}").move_to(UP)
        
        eq1 = MathTex(r" x-4 \geqslant 0").next_to(funcion1,DOWN)
        eq2 = MathTex(r" x-4+4 \geqslant 0+4").next_to(eq1,DOWN)
        domfuncion1 = MathTex(r"dom \ g = x \geqslant 4").next_to(eq2,DOWN)
        rangofuncion1 = MathTex(r"rango \ g = g(x)\geqslant 0").next_to(domfuncion1,DOWN)
        resp= VGroup(domfuncion1,rangofuncion1)
        framebox1 = SurroundingRectangle(resp, buff = .1)
        self.play(Write(funcion1),run_time=3)
        self.wait(25)
        self.play(Write(eq1),run_time=3)
        self.wait(20)
        self.play(Write(eq2),run_time=3)
        self.wait(5)
        self.play(Write(domfuncion1),run_time=3)
        self.wait(34)
        self.play(Write(rangofuncion1),run_time=3)
        self.wait(9)
        self.clear()
        self.play(Write(resp),run_time=3)
        self.wait()
        self.play(
            Create(framebox1)
        )
        self.wait(15)
        self.clear()
        
class final(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 8.0, 1],
            y_range=[-1, 1, 0.2],
            axis_config={"font_size": 24},
        ).add_coordinates()
        ax2 = Axes(
            x_range=[-8, 8.0, 1],
            y_range=[-4, 4, 1],
            axis_config={"font_size": 24},
        ).add_coordinates()

        curve = ax.plot(lambda x: np.sin(x) / np.e ** 2 * x,x_range=[0, 7], color=GREEN_B)
        discontinuous_function = lambda x: (x ** 2 - 2) / (x ** 2 - 4)
        curve2 = ax2.plot(
            discontinuous_function,
            discontinuities=[-2, 2],  # discontinuous points
            dt=0.1,  # left and right tolerance of discontinuity
            color=GREEN,
        )

        lines = ax.get_vertical_lines_to_graph(
            curve, x_range=[0, 7], num_lines=30, color=BLUE
        )
        lines2 = ax2.get_vertical_lines_to_graph(
            curve2, x_range=[-1.99, 1.99], num_lines=30, color=BLUE
        )
        lines3 = ax2.get_vertical_lines_to_graph(
            curve2, x_range=[-8, -1.99], num_lines=30, color=BLUE
        )
        lines4 = ax2.get_vertical_lines_to_graph(
            curve2, x_range=[ 1.99,8], num_lines=30, color=BLUE
        )
        self.add(ax, curve)
        self.play(Write(lines),run_time=6)
        self.clear()
        self.add(ax2, curve2)
        self.play(Write(lines2),Write(lines3),Write(lines4),run_time=18)
        self.wait(2)
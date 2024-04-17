from manim import *
Amarillo='#ddf599'
Morado = "#fe04f2"
Celeste = "#0ad6fb"
Rojo = "#fb0a4c"
RosaRed ="#fe0463"
VerdeClaro ="#04febe"
GREEN_SCREEN = '#00FF00'

class CirculoUnitario(Scene):
    def angulo(self):
        rotation_center = LEFT

        theta_tracker = ValueTracker(110)
        line1 = Line(LEFT, RIGHT)
        line_moving = Line(LEFT, RIGHT)
        line_ref = line_moving.copy()
        line_moving.rotate(
            theta_tracker.get_value() * DEGREES, about_point=rotation_center
        )
        a = Angle(line1, line_moving, radius=0.5, other_angle=False)
        tex = MathTex(r"\theta").move_to(
            Angle(
                line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )

        self.add(line1, line_moving, a, tex)
        self.wait()

        line_moving.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=rotation_center
            )
        )

        a.add_updater(
            lambda x: x.become(Angle(line1, line_moving, radius=0.5, other_angle=False))
        )
        tex.add_updater(
            lambda x: x.move_to(
                Angle(
                    line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
                ).point_from_proportion(0.5)
            )
        )

        self.play(theta_tracker.animate.set_value(40))
        self.play(theta_tracker.animate.increment_value(140))
        self.play(tex.animate.set_color(GREEN_SCREEN), run_time=0.5)
        self.play(theta_tracker.animate.set_value(350))
        self.clear()
    
    def angulodefinicion(self):
        line1 = Line( LEFT + (1/3) * UP, RIGHT + (1/3) * DOWN ).scale(1.5)
        line2 = Line( DOWN + (1/3) * RIGHT, UP + (1/3) * LEFT ).scale(1.5)
        angles = [
            Angle(line1, line2),
            Angle(line1, line2, radius=0.4, quadrant=(1,-1), other_angle=True),
            
        ]
        
        for i in angles:
            self.play(Write(line1))
            self.play(Write(line2))
            self.play(Write(i))
            self.wait(2)
            self.clear()
    def circuferencia(self):
        circle = Circle(radius=2, color=BLUE)
        ax =NumberPlane(
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 1,
                "stroke_opacity": 0.8
            }
        )
        p=ax.c2p(1.4,1.4)
        punto=Dot(p).set_color(ORANGE)
        lines_1 = ax.get_lines_to_point(p, color=Morado)
        line1 = Line( ORIGIN, RIGHT )
        line2 = Line( ORIGIN, p )
        anglex= Angle(line1, line2).set_color(GREEN)
        texangle  = MathTex(r"x").move_to(
            Angle(
                line1, line2, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )
        arrow = Arrow(ORIGIN, p, buff=0)
        
        textP= MathTex(r"P(a,b)",font_size=27).next_to(p,RIGHT)
        self.play(GrowFromCenter(circle))
        self.play(Write(ax))
        self.play(Write(punto))
        self.play(Write(arrow))
        self.play(Write(lines_1))
        self.play(Write(anglex),Write(texangle),Write(textP))
        #
        
        rotation_center = ORIGIN

        theta_tracker = ValueTracker(45)
        
        line1 = Line(LEFT, RIGHT)
        line_moving = Line(ax.c2p(-2,0),ax.c2p(2,0) ).set_color(ORANGE)
        line_ref = line_moving.copy()
        line_moving.rotate(
            theta_tracker.get_value() * DEGREES, about_point=rotation_center
        )
        a = Angle(line1, line_moving, radius=0.5, other_angle=False)
        tex = MathTex(r"x").move_to(
            Angle(
                line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )
        self.play(Unwrite(arrow),Unwrite(anglex))
        self.add(line1, line_moving, a, tex)
        self.wait()
        self.remove(texangle)
        line_moving.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=rotation_center
            )
        )

        a.add_updater(
            lambda x: x.become(Angle(line1, line_moving, radius=0.5, other_angle=False))
        )
        tex.add_updater(
            lambda x: x.move_to(
                Angle(
                    line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
                ).point_from_proportion(0.5)
            )
        )

        self.play(theta_tracker.animate.set_value(40))
        self.play(theta_tracker.animate.increment_value(140),run_time=40)
        self.play(tex.animate.set_color(GREEN_SCREEN), run_time=0.5)
        self.play(theta_tracker.animate.set_value(350))
        self.clear()

        


    def construct(self):
        titulo1= Tex("Funciones Trigonometricas").set_color(YELLOW)
        titulo2 = Tex("Elementales").set_color(YELLOW).next_to(titulo1,DOWN)
        titulo = VGroup(titulo1,titulo2)
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
        sin_graph = axes.plot(lambda x: np.sin(x), color=BLUE)
        plot = VGroup(axes,axes_labels,sin_graph)
        #puntos extremos
        p1 = Dot(axes.c2p(-10,0)).set_color(ORANGE)
        p2 = Dot(axes.c2p(10,0)).set_color(ORANGE)
        line1p1p2 = Line(p1,p2)
        line2p1p2 =VMobject()
        variableindependiente = VGroup(p1,line1p1p2,line2p1p2)
        self.play(FadeIn(titulo, shift=DOWN, scale=0.66))
        self.wait()
        self.play(FadeOut(titulo, shift=DOWN * 2, scale=1.5))
        self.play(Write(plot))
        self.wait()
        self.play(Write(variableindependiente))
        self.wait()
        line2p1p2.add_updater(lambda x: x.become(Line(axes.c2p(-10,0), p1.get_center()).set_color(ORANGE)))
        self.play(MoveAlongPath(p1,line1p1p2),rate_func=linear, run_time=3)
        self.wait(3)
        self.clear()
        self.angulo()
        self.wait()
        self.angulodefinicion()
        self.wait(3)
        self.circuferencia()
        self.wait(3)



class SineCurveUnitCircle(Scene):
    # contributed by heejin_park, https://infograph.tistory.com/230
    def title(self):
        title = Text("Función Seno", font_size=30).to_edge(UP+LEFT)
        self.play(Write(title))
    def construct(self):
        self.title()
        self.show_axis()
        self.show_circle()
        self.move_dot_and_draw_curve()
        self.wait()

    def show_axis(self):
        x_start = np.array([-6,0,0])
        x_end = np.array([6,0,0])

        y_start = np.array([-4,-2,0])
        y_end = np.array([-4,2,0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        self.add(x_axis, y_axis)
        self.add_x_labels()

        self.origin_point = np.array([-4,0,0])
        self.curve_start = np.array([-4,0,0])

    def add_x_labels(self):
        x_labels = [
            MathTex("\pi"), MathTex("2 \pi"),
            MathTex("3 \pi"), MathTex("4 \pi"),
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-2 + 2*i, 0, 0]), DOWN)
            self.add(x_labels[i])

    def show_circle(self):
        circle = Circle(radius=1).set_color(BLUE)
        circle.move_to(self.origin_point)
        self.add(circle)
        self.circle = circle

    def move_dot_and_draw_curve(self):
        orbit = self.circle
        origin_point = self.origin_point

        dot = Dot(radius=0.08, color=ORANGE)
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.25

        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            # print(self.t_offset)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        def get_line_to_circle():
            return Line(origin_point, dot.get_center(), color=BLUE)

        def get_line_to_curve():
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x,y,0]), color=GREEN, stroke_width=2 )


        self.curve = VGroup()
        self.curve.add(Line(self.curve_start,self.curve_start))
        def get_curve():
            last_line = self.curve[-1]
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            new_line = Line(last_line.get_end(),np.array([x,y,0]), color=GREEN_B)
            self.curve.add(new_line)

            return self.curve

        dot.add_updater(go_around_circle)

        origin_to_circle_line = always_redraw(get_line_to_circle)
        dot_to_curve_line = always_redraw(get_line_to_curve)
        sine_curve_line = always_redraw(get_curve)

        self.add(dot)
        self.add(orbit, origin_to_circle_line, dot_to_curve_line, sine_curve_line)
        self.wait(8.5)

        dot.remove_updater(go_around_circle)

class CosenoCurveUnitCircle(Scene):
    # contributed by heejin_park, https://infograph.tistory.com/230
    def title(self):
        title = Text("Función Coseno", font_size=30).to_edge(UP+LEFT)
        self.play(Write(title))
    def construct(self):
        self.title()
        self.show_axis()
        self.show_circle()
        self.move_dot_and_draw_curve()
        self.wait()

    def show_axis(self):
        x_start = np.array([-6,0,0])
        x_end = np.array([6,0,0])

        y_start = np.array([-4,-2,0])
        y_end = np.array([-4,2,0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        self.add(x_axis, y_axis)
        self.add_x_labels()

        self.origin_point = np.array([-5,0,0])
        self.curve_start = np.array([-5,0,0])

    def add_x_labels(self):
        x_labels = [
            MathTex("\pi"), MathTex("2 \pi"),
            MathTex("3 \pi"), MathTex("4 \pi"),
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-2 + 2*i, 0, 0]), DOWN)
            self.add(x_labels[i])

    def show_circle(self):
        circle = Circle(radius=1).set_color(BLUE)
        circle.move_to(self.origin_point)
        self.add(circle)
        self.circle = circle

    def move_dot_and_draw_curve(self):
        orbit = self.circle
        origin_point = self.origin_point

        dot = Dot(radius=0.08, color=ORANGE)
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.25

        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            # print(self.t_offset)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        def get_line_to_circle():
            return Line(origin_point, dot.get_center(), color=BLUE)

        def get_line_to_curve():
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x,y,0]), color=GREEN, stroke_width=2 )


        self.curve = VGroup()
        self.curve.add(Line(self.curve_start,self.curve_start))
        def get_curve():
            last_line = self.curve[-1]
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            new_line = Line(last_line.get_end(),np.array([x,y,0]), color=GREEN_B)
            self.curve.add(new_line)

            return self.curve

        dot.add_updater(go_around_circle)

        origin_to_circle_line = always_redraw(get_line_to_circle)
        dot_to_curve_line = always_redraw(get_line_to_curve)
        sine_curve_line = always_redraw(get_curve)

        self.add(dot)
        self.add(orbit, origin_to_circle_line, dot_to_curve_line, sine_curve_line)
        self.wait(8.5)

        dot.remove_updater(go_around_circle)

class TangentFunction(Scene):
    def construct(self):
        # Título
        title = Text("Función Tangente", font_size=30).to_edge(UP+LEFT)
        
        # Ejes coordenados
        axes = Axes(
            x_range=[-2*PI, 2*PI],
            y_range=[-3, 3],
            axis_config={"color": BLUE},
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="\\tan(x)")
        
        # Gráfica de la función tangente
        tan_graph = axes.plot(lambda x: np.tan(x),
            discontinuities=[-1.5*PI,-0.5*PI, 0.5*PI,1.5*PI],  # discontinuous points
            dt=0.1, color=YELLOW)
        
        # Anotaciones
        equation = MathTex("\\tan(x) = \\frac{\\sin(x)}{\\cos(x)}",font_size=25)
        equation.to_corner(DOWN)
        
        # Animaciones
        self.play(Write(title))
        self.wait(1)
        self.play(Create(axes), Write(axes_labels))
        self.wait(1)
        self.play(Create(tan_graph))
        self.wait(2)
        self.play(Write(equation))
        self.wait(2)


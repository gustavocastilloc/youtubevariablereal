from manim import *
import time
Amarillo='#ddf599'
Morado = "#fe04f2"
Celeste = "#0ad6fb"
Rojo = "#fb0a4c"
RosaRed ="#fe0463"
VerdeClaro ="#04febe"
GREEN_SCREEN = '#00FF00'
class Logo(Scene):
    def construct(self):
        ax = NumberPlane(
            background_line_style={
            
                "stroke_opacity": 0.4
            }
        ).add_coordinates()
        triangle1 = Triangle().scale(0.8).rotate(180*DEGREES).move_to([0,-0.18,0]).set_color(VerdeClaro)
        ellipse1 = Ellipse(
            width=2.0, height=0.5, color=VerdeClaro, stroke_width=5
        )
        text=VGroup(Text(r"VARIABLE ",font_size=28,color=VerdeClaro,font="Akira Expanded"),Text(r"REAL",font_size=28,color=ORANGE,font="Akira Expanded")).arrange(RIGHT).move_to([0,-1.5,0])
        
        line1 = Line(triangle1.get_end(),[0,-0.9,0]).set_color(VerdeClaro)
        line2 = Line(triangle1.get_corner(UR),[0.8,0.5,0]).set_color(VerdeClaro)
        line3 = Line(triangle1.get_corner(UL),[-0.8,0.5,0]).set_color(VerdeClaro)
        line4 =Line([0,-0.9,0],[-0.8,0.5,0]).set_color(ORANGE)
        line5 =Line([0,-0.9,0],[0.8,0.5,0]).set_color(ORANGE)
        line6 =Line([-0.8,0.5,0],[0.8,0.5,0]).set_color(ORANGE)
        #lines =VGroup(line1,line2,line3,line4,line5,line6)
        lines =VGroup(line1,line2,line3,line4,line5)
        #lines =VGroup(line1,line2,line3)
        self.add(triangle1,lines)
        logo=VGroup(lines,triangle1)
        self.play(FadeIn(Triangle().scale(0.5).rotate(180*DEGREES).move_to([0,-0.18,0]).set_color(VerdeClaro)))
        self.play(FadeIn(Triangle().scale(0.4).rotate(180*DEGREES).move_to([0,-0.18,0]).set_color(VerdeClaro)))
        
        self.play(Write(text),run_time=1)
        self.wait(2)
class Logov2(Scene):
    def construct(self):
        ax = NumberPlane(
            background_line_style={
            
                "stroke_opacity": 0.4
            }
        ).add_coordinates()
        triangle1 = Triangle().scale(0.8).rotate(180*DEGREES).move_to([0,-0.18,0]).set_color(VerdeClaro)
        ellipse1 = Ellipse(
            width=2.0, height=0.5, color=VerdeClaro, stroke_width=5
        )
        text=VGroup(Text(r"VARIABLE ",font_size=28,color=VerdeClaro,font="Akira Expanded"),Text(r"REAL",font_size=28,color=ORANGE,font="Akira Expanded")).arrange(RIGHT).move_to([0,-1.5,0])
        
        line1 = Line(triangle1.get_end(),[0,-0.9,0]).set_color(VerdeClaro)
        line2 = Line(triangle1.get_corner(UR),[0.8,0.5,0]).set_color(VerdeClaro)
        line3 = Line(triangle1.get_corner(UL),[-0.8,0.5,0]).set_color(VerdeClaro)
        line4 =Line([0,-0.9,0],[-0.8,0.5,0]).set_color(ORANGE)
        line5 =Line([0,-0.9,0],[0.8,0.5,0]).set_color(ORANGE)
        line6 =Line([-0.8,0.5,0],[0.8,0.5,0]).set_color(ORANGE)
        #lines =VGroup(line1,line2,line3,line4,line5,line6)
        lines =VGroup(line1,line2,line3,line4,line5)
        #lines =VGroup(line1,line2,line3)
        
        logo=VGroup(lines,triangle1).scale(2)
        
        
        circle_1 = Circle(radius=2.4,color=VerdeClaro,stroke_width=5)
        circle_2 = Circle(radius=2.5,color=ORANGE,stroke_width=5)
        self.add(logo,circle_1,circle_2)
        #tr=Triangle().scale(0.3).set_color(VerdeClaro)
        #self.play(FadeIn(Triangle().scale(1).rotate(180*DEGREES).move_to([0,-0.18,0]).set_color(VerdeClaro)))
        #self.play(FadeIn(Triangle().scale(0.9).rotate(180*DEGREES).move_to([0,-0.18,0]).set_color(VerdeClaro)))
        for i in np.arange(1,-0.1,-0.1):
            self.play(FadeIn(Triangle().scale(i).rotate(180*DEGREES).move_to([0,-0.18,0]).set_color(VerdeClaro)),run_time=0.2)
        #self.play(Rotate(tr, angle=2*PI, rate_func=linear))
        
        #self.play(Write(text),run_time=1)
        self.wait(2)
class LogoP(Scene):
    def construct(self):
        ax = NumberPlane(
            background_line_style={
            
                "stroke_opacity": 0.4
            }
        ).add_coordinates()
        triangle1 = Triangle().scale(0.8).rotate(180*DEGREES).move_to([0,-0.18,0]).set_color(VerdeClaro)
        ellipse1 = Ellipse(
            width=2.0, height=0.5, color=VerdeClaro, stroke_width=5
        )
        text=VGroup(Text(r"VARIABLE ",font_size=15,color=VerdeClaro,font="Akira Expanded"),Text(r"REAL",font_size=15,color=ORANGE,font="Akira Expanded")).arrange(RIGHT).move_to([0,-1.2,0])
        
        line1 = Line(triangle1.get_end(),[0,-0.9,0]).set_color(VerdeClaro)
        line2 = Line(triangle1.get_corner(UR),[0.8,0.5,0]).set_color(VerdeClaro)
        line3 = Line(triangle1.get_corner(UL),[-0.8,0.5,0]).set_color(VerdeClaro)
        line4 =Line([0,-0.9,0],[-0.8,0.5,0]).set_color(ORANGE)
        line5 =Line([0,-0.9,0],[0.8,0.5,0]).set_color(ORANGE)
        line6 =Line([-0.8,0.5,0],[0.8,0.5,0]).set_color(ORANGE)
        #lines =VGroup(line1,line2,line3,line4,line5,line6)
        lines =VGroup(line1,line2,line3,line4,line5)
        #lines =VGroup(line1,line2,line3)
        #self.add(triangle1,lines)
        #logo=VGroup(lines,triangle1)
        #self.play(FadeIn(Triangle().scale(0.5).rotate(180*DEGREES).move_to([0,-0.18,0]).set_color(VerdeClaro)))
        #self.play(FadeIn(Triangle().scale(0.4).rotate(180*DEGREES).move_to([0,-0.18,0]).set_color(VerdeClaro)))
        
        #self.play(Write(text),run_time=4)
        #self.wait(5)
        g=VGroup(triangle1,lines,
        Triangle().scale(0.5).rotate(180*DEGREES).move_to([0,-0.18,0]).set_color(VerdeClaro),
        Triangle().scale(0.4).rotate(180*DEGREES).move_to([0,-0.18,0]).set_color(VerdeClaro),
        text).scale(2)
        self.add(g)
class LogoPv2(Scene):
    def construct(self):
        ax = NumberPlane(
            background_line_style={
            
                "stroke_opacity": 0.4
            }
        ).add_coordinates()
        triangle1 = Triangle().scale(0.8).rotate(180*DEGREES).move_to([0,-0.18,0]).set_color(VerdeClaro)
        ellipse1 = Ellipse(
            width=2.0, height=0.5, color=VerdeClaro, stroke_width=5
        )
        text=VGroup(Text(r"VARIABLE ",font_size=15,color=VerdeClaro,font="Akira Expanded"),Text(r"REAL",font_size=15,color=ORANGE,font="Akira Expanded")).arrange(RIGHT).move_to([0,-1.2,0])
        
        line1 = Line(triangle1.get_end(),[0,-0.9,0]).set_color(VerdeClaro)
        line2 = Line(triangle1.get_corner(UR),[0.8,0.5,0]).set_color(VerdeClaro)
        line3 = Line(triangle1.get_corner(UL),[-0.8,0.5,0]).set_color(VerdeClaro)
        line4 =Line([0,-0.9,0],[-0.8,0.5,0]).set_color(ORANGE)
        line5 =Line([0,-0.9,0],[0.8,0.5,0]).set_color(ORANGE)
        line6 =Line([-0.8,0.5,0],[0.8,0.5,0]).set_color(ORANGE)
        #lines =VGroup(line1,line2,line3,line4,line5,line6)
        lines =VGroup(line1,line2,line3,line4,line5)
        #lines =VGroup(line1,line2,line3)
        #self.add(triangle1,lines)
        #logo=VGroup(lines,triangle1)
        #self.play(FadeIn(Triangle().scale(0.5).rotate(180*DEGREES).move_to([0,-0.18,0]).set_color(VerdeClaro)))
        #self.play(FadeIn(Triangle().scale(0.4).rotate(180*DEGREES).move_to([0,-0.18,0]).set_color(VerdeClaro)))
        
        #self.play(Write(text),run_time=4)
        #self.wait(5)
        g=VGroup(triangle1,lines,
        Triangle().scale(0.5).rotate(180*DEGREES).move_to([0,-0.18,0]).set_color(VerdeClaro),
        Triangle().scale(0.4).rotate(180*DEGREES).move_to([0,-0.18,0]).set_color(VerdeClaro),
        ).scale(2)
        self.add(g)
    
from manim import *
import time
Amarillo='#ddf599'
Morado = "#fe04f2"
Celeste = "#0ad6fb"
Rojo = "#fb0a4c"
RosaRed ="#fe0463"
VerdeClaro ="#04febe"
GREEN_SCREEN = '#00FF00'
class Multiplicacion(Scene):
    def construct(self):
        def suma(a,b,c):
            return a+b+c
        tam=35
        title = Tex("Multiplicacion entre matrices",font_size=60,color=YELLOW)
        #metodologia = Tex("$A_m$x$_n$ $\cdot$ $B_n$x$_p$= $C_m$x$_p$",color=Amarillo)
        metodologia = MathTex(r"A_{mxn} \cdot B_{nxp}= C_{mxp}",color=Amarillo)
        ej0=MathTex(r"A_{4x3} \cdot B_{3x2}= C_{4x2}")
        
        m1 = Matrix([[4, 5,2], [3, 7,9],[1,4,5],[6,3,7]],
        ).set_row_colors(TEAL,GREEN,GOLD,MAROON).to_corner(UP+LEFT)
        m2 = Matrix([[-2, 1], [3, 4],[1,0]],
        ).set_column_colors(PURPLE,BLUE_C).next_to(m1,RIGHT)
        igual=MathTex(r"=",font_size=tam).next_to(m2,RIGHT)
        mc = Matrix([[ suma(4*-2,5*3,2*1)  , suma(4*1,5*4,2*0)], [suma(3*-2,7*3,9*1),suma(3*1,7*4,9*0)],[suma(1*-2,4*3,5*1),suma(1*1,4*4,5*0)],[suma(6*-2,3*3,7*1),suma(6*1,3*4,7*0)]],
        ).set_column_colors(BLACK,BLACK).next_to(igual,RIGHT)
        ##
        lista1 = [[7,8,4,5],[3,11,-7,9],[-1,10,-6,-3],[2,-12,4,1],[3,6,0,11]]
        lista2 = [[16,-1,9],[-4,11,0],[-1,10,-6],[0,-8,19]]
        lista3 = []
        m3 = Matrix(lista1).set_color(MAROON).to_corner(LEFT).scale(0.8)
        m4 = Matrix(lista2).set_color(TEAL).next_to(m3,RIGHT).scale(0.8)
        igualm3=MathTex(r"=",font_size=tam).next_to(m4,RIGHT)
        ##
        frameboxf1= SurroundingRectangle(m1.get_rows()[0])
        frameboxf2= SurroundingRectangle(m1.get_rows()[1])
        frameboxf3= SurroundingRectangle(m1.get_rows()[2])
        frameboxf4= SurroundingRectangle(m1.get_rows()[3])
        frameboxc1= SurroundingRectangle(m2.get_columns()[0])
        frameboxc1r1= SurroundingRectangle(m2.get_columns()[0])
        frameboxc2= SurroundingRectangle(m2.get_columns()[1])
        frameboxc2r2= SurroundingRectangle(m2.get_columns()[1])
        frameboxc2r3= SurroundingRectangle(m2.get_columns()[1])
        frameboxc2r4= SurroundingRectangle(m2.get_columns()[1])
        frameboxc1r2= SurroundingRectangle(m2.get_columns()[0])
        frameboxc1r3= SurroundingRectangle(m2.get_columns()[0])
        frameboxc1r4= SurroundingRectangle(m2.get_columns()[0])
        v1=MathTex(r"V_{a}=[a_{1},a_{2},a_{3}]",font_size=tam)
        v2=MathTex(r"V_{b}=[b_{1},b_{2},b_{3}]",font_size=tam)
        v1v2=MathTex(r"V_{a} \cdot V_{b} = a_{1}b_{1}+a_{2}b_{2}+a_{3}b_{3}",font_size=tam)
        vf1=MathTex(r"V_{a}=[4,5,2]",font_size=tam)
        vf2=MathTex(r"V_{a}=[3,7,9]",font_size=tam)
        vf3=MathTex(r"V_{a}=[1,4,5]",font_size=tam)
        vf4=MathTex(r"V_{a}=[6,3,7]",font_size=tam)
        vc1=MathTex(r"V_{b}=[-2,3,1]",font_size=tam)
        vc2=MathTex(r"V_{b}=[1,4,0]",font_size=tam)
        v1v2n=MathTex(r"V_{a} \cdot V_{b} = 4(-2)+5(3)+2(1) \rightarrow",font_size=tam)
        v1v2n1=MathTex(r"V_{a} \cdot V_{b} = 4(1)+5(4)+2(0) \rightarrow",font_size=tam)
        v1v2n2=MathTex(r"V_{a} \cdot V_{b} = 3(-2)+7(3)+9(1) \rightarrow",font_size=tam)
        v1v2n3=MathTex(r"V_{a} \cdot V_{b} = 3(1)+7(4)+9(0) \rightarrow",font_size=tam)
        v1v2n4=MathTex(r"V_{a} \cdot V_{b} = 1(-2)+4(3)+5(1) \rightarrow",font_size=tam)
        v1v2n5=MathTex(r"V_{a} \cdot V_{b} = 1(1)+4(4)+5(0) \rightarrow",font_size=tam)
        v1v2n6=MathTex(r"V_{a} \cdot V_{b} = 6(-2)+3(3)+7(1) \rightarrow",font_size=tam)
        v1v2n7=MathTex(r"V_{a} \cdot V_{b} = 6(1)+3(4)+7(0) \rightarrow",font_size=tam)
        vect1 = VGroup(v1,v2,v1v2,vf1,vc1,v1v2n).arrange(DOWN,center=False, aligned_edge=LEFT).to_corner(DOWN+LEFT)
        vect2 = VGroup(v1,v2,v1v2,vf1,vc2,v1v2n1).arrange(DOWN,center=False, aligned_edge=LEFT).to_corner(DOWN+LEFT)
        vect3 = VGroup(v1,v2,v1v2,vf2,MathTex(r"V_{b}=[-2,3,1]",font_size=tam),v1v2n2).arrange(DOWN,center=False, aligned_edge=LEFT).to_corner(DOWN+LEFT)
        vect4 = VGroup(v1,v2,v1v2,vf2,MathTex(r"V_{b}=[1,4,0]",font_size=tam),v1v2n3).arrange(DOWN,center=False, aligned_edge=LEFT).to_corner(DOWN+LEFT)
        vect5 = VGroup(v1,v2,v1v2,vf3,MathTex(r"V_{b}=[-2,3,1]",font_size=tam),v1v2n4).arrange(DOWN,center=False, aligned_edge=LEFT).to_corner(DOWN+LEFT)
        vect6 = VGroup(v1,v2,v1v2,vf3,MathTex(r"V_{b}=[1,4,0]",font_size=tam),v1v2n5).arrange(DOWN,center=False, aligned_edge=LEFT).to_corner(DOWN+LEFT)
        vect7 = VGroup(v1,v2,v1v2,vf4,MathTex(r"V_{b}=[-2,3,1]",font_size=tam),v1v2n6).arrange(DOWN,center=False, aligned_edge=LEFT).to_corner(DOWN+LEFT)
        vect8 = VGroup(v1,v2,v1v2,vf4,MathTex(r"V_{b}=[1,4,0]",font_size=tam),v1v2n7).arrange(DOWN,center=False, aligned_edge=LEFT).to_corner(DOWN+LEFT)
        v1v1=MathTex(r"V_{a} \cdot V_{b}=",str(suma(4*-2,5*3,2*1)),font_size=tam).next_to(vect1[-1])
        v1v2=MathTex(r"V_{a} \cdot V_{b}=",str(suma(4*1,5*4,2*0)),font_size=tam).next_to(vect2[-1])
        v1v3=MathTex(r"V_{a} \cdot V_{b}=",str(suma(3*-2,7*3,9*1)),font_size=tam).next_to(vect3[-1])
        v1v4=MathTex(r"V_{a} \cdot V_{b}=",str(suma(3*1,7*4,9*0)),font_size=tam).next_to(vect4[-1])
        v1v5=MathTex(r"V_{a} \cdot V_{b}=",str(suma(1*-2,4*3,5*1)),font_size=tam).next_to(vect5[-1])
        v1v6=MathTex(r"V_{a} \cdot V_{b}=",str(suma(1*1,4*4,5*0)),font_size=tam).next_to(vect6[-1])
        v1v7=MathTex(r"V_{a} \cdot V_{b}=",str(suma(6*-2,3*3,7*1)),font_size=tam).next_to(vect7[-1])
        v1v8=MathTex(r"V_{a} \cdot V_{b}=",str(suma(6*1,3*4,7*0)),font_size=tam).next_to(vect8[-1])
        ##
        dim_ma = Text("4x3",font_size=16,t2c={'3':YELLOW},font="sans-serif",color=Celeste).move_to([-2.8,0.2,0])
        dim_mb = Text("3x2",font_size=16,t2c={'3':YELLOW},font="sans-serif",color=Celeste).move_to([0.15,0.55,0])
        dim_mc = Text("4x2",font_size=16,t2c={'3':YELLOW},font="sans-serif",color=Celeste).move_to([3.5,0.2,0])
        ##
        self.play(Write(title))
        self.wait(2)
        self.play(Transform(title,metodologia))
        self.wait(2)
        self.play(Create(ej0.next_to(metodologia,DOWN)))
        self.wait(30)
        self.clear()
        #self.add(NumberPlane())
        self.play(Write(m1),Write(dim_ma),run_time=3)
        self.wait(3)
        self.play(Create(frameboxf1),run_time=2)
        self.wait(3)
        for i in vect1:
            self.play(Create(i),run_time=3)
            self.wait(3)
        self.play(Create(v1v1))
        self.wait(3)
        self.play(Create(m2),Write(dim_mb),run_time=3)
        self.play(Create(igual),run_time=3)
        self.play(Create(frameboxc1),run_time=2)
        self.wait(3)
        self.play(Create(mc),Write(dim_mc),run_time=3)
        self.wait(3)
        mc.get_entries()[0].set_color(Amarillo)
        self.wait(3)
        self.play(
            ReplacementTransform(frameboxc1,frameboxc2),
            Transform(vect1,vect2),
            Transform(v1v1,v1v2),
            Transform(v1v2n,v1v2n1),
        )
        mc.get_entries()[1].set_color(Amarillo)
        self.wait(3)
        self.play(
            ReplacementTransform(frameboxf1,frameboxf2),
            ReplacementTransform(frameboxc2,frameboxc1r1),
            Transform(vect1,vect3),
            Transform(v1v1,v1v3),
            Transform(v1v2n,v1v2n2),
        )
        mc.get_entries()[2].set_color(Amarillo)
        self.wait(3)
        self.play(
            ReplacementTransform(frameboxc1r1,frameboxc2r2),
            Transform(vect1,vect4),
            Transform(v1v1,v1v4),
            Transform(v1v2n,v1v2n3),
        )
        mc.get_entries()[3].set_color(Amarillo)
        self.wait(3)
        self.play(
            ReplacementTransform(frameboxf2,frameboxf3),
            ReplacementTransform(frameboxc2r2,frameboxc1r2),
            Transform(vect1,vect5),
            Transform(v1v1,v1v5),
            Transform(v1v2n,v1v2n4),
        )
        mc.get_entries()[4].set_color(Amarillo)
        self.wait(3)
        self.play(
            ReplacementTransform(frameboxc1r2,frameboxc2r3),
            Transform(vect1,vect6),
            Transform(v1v1,v1v6),
            Transform(v1v2n,v1v2n5),
        )
        mc.get_entries()[5].set_color(Amarillo)
        self.wait(3)
        self.play(
            ReplacementTransform(frameboxf3,frameboxf4),
            ReplacementTransform(frameboxc2r3,frameboxc1r3),
            Transform(vect1,vect7),
            Transform(v1v1,v1v7),
            Transform(v1v2n,v1v2n6),
        )
        mc.get_entries()[6].set_color(Amarillo)
        self.wait(3)
        self.play(
            ReplacementTransform(frameboxc1r3,frameboxc2r4),
            Transform(vect1,vect8),
            Transform(v1v1,v1v8),
            Transform(v1v2n,v1v2n7),
        )
        mc.get_entries()[7].set_color(Amarillo)
        self.wait(3)
        self.clear()
        self.play(Create(m3))
        self.play(Create(m4))
        self.play(Create(igualm3))
        self.wait(3)
        for i in lista1:
            k=[]
            
            for j in lista2:
                e=0
                
                for indice in range(len(j)):
                    e+=i[indice]*j[indice]
                k.append(e)
            lista3.append(k)
        
        self.wait(3)
class MultiplicacionEj(Scene):
    def construct(self):
        ##
        tam=35
        lista1 = [[7,8,4,5],[3,11,-7,9],[-1,10,-6,-3],[2,-12,4,1],[3,6,0,11]]
        lista2 = [[16,-1,9],[-4,11,0],[-1,10,-6],[0,-8,19]]
        lista2p = [[16,-4,-1,0],[-1,11,10,-8],[9,0,-6,19]]
        lista3 = []
        m3 = Matrix(lista1).set_color(MAROON).to_corner(LEFT).scale(0.7)
        m4 = Matrix(lista2).set_color(TEAL).next_to(m3,RIGHT).scale(0.7)
        igualm3=MathTex(r"=",font_size=tam).next_to(m4,RIGHT)
        m5 = Matrix(lista3).set_color(GREEN).scale(0.7).next_to(igualm3,RIGHT)
        ##
        frameboxf1= SurroundingRectangle(m3.get_rows()[0])
        frameboxc1= SurroundingRectangle(m4.get_columns()[0])
        self.play(Create(m3))
        self.play(Create(m4))
        self.play(Create(igualm3))
        self.wait(3)
        self.play(Create(m5))
        self.play(Create(frameboxf1))
        self.play(Create(frameboxc1))
        #self.add(NumberPlane())
        for i in range(len(lista1)):
            k=[]
            self.play(Transform(frameboxf1,SurroundingRectangle(m3.get_rows()[i])))
            for j in range(len(lista2p)):
                e=0
                self.play(Transform(frameboxc1,SurroundingRectangle(m4.get_columns()[j])))
                cantidades_text=VGroup()
                for indice in range(len(lista2p[j])) :
                    e+=lista1[i][indice]*lista2p[j][indice]
                    if indice!=len(lista2p[j])-1:
                        cantidades_text.add(MathTex(str(lista1[i][indice])+"("+str(lista2p[j][indice])+")+",font_size=tam))
                    else:
                        cantidades_text.add(MathTex(str(lista1[i][indice])+"("+str(lista2p[j][indice])+")=",font_size=tam))
                k.append(e)
                cantidades_text.add(MathTex(str(e),font_size=tam,color=GREEN))
                self.play(Create(cantidades_text.arrange(RIGHT).move_to(DOWN*2.5)))
                self.wait(1)
                self.remove(cantidades_text)
            lista3.append(k)
            self.play(Transform(frameboxf1,SurroundingRectangle(m3.get_rows()[i])))         
            self.play(Transform(m5,Matrix(lista3).set_color(GREEN).scale(0.7).next_to(igualm3,RIGHT)))  
                   
        self.wait(3)
        self.wait(3)

        
        
class Multiplicacion3D(ThreeDScene):
    def construct(self):
        tam=35
        axes = ThreeDAxes(tips=False)
        
        ##
        arrow1 = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([4, 5, 2]),
            resolution=8
        ).set_color(Celeste)
        arrow2 = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([-2, 3, 1]),
            resolution=8
        ).set_color(RED)
        arrow1_text = Tex('$V_{a}$',color=Celeste).next_to(arrow1, RIGHT)
        arrow2_text = Tex('$V_{b}$',color=RED).next_to(arrow2, RIGHT)
        ##
        
        self.set_camera_orientation(phi=45 * DEGREES, theta=-45 * DEGREES)
        self.wait(1)
        self.add(axes)
        self.play(Create(arrow1),run_time=3)
        self.add_fixed_in_frame_mobjects(arrow1_text)
        self.play(Create(arrow2),run_time=3)
        self.add_fixed_in_frame_mobjects(arrow2_text)
        self.begin_3dillusion_camera_rotation(rate=2)
        self.wait(PI/2)
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES)
        self.wait(2)
        self.clear()
        self.wait(1)
       
class MultiplicacionApp(Scene):
    def construct(self):
        tam=35
        title = Tex("Caso de uso",font_size=45,color=Amarillo).to_corner(UP+LEFT)
        ejaxc= MathTex(r"A \cdot X = C",font_size=tam).move_to([0,3,0])
        ej0= MathTex(r"A \cdot X = C",font_size=tam)
        ej1= MathTex(r"A^{-1}A \cdot X = A^{-1}C",font_size=tam)
        ej2= MathTex(r"I \cdot X = A^{-1}C",font_size=tam)
        ej3= MathTex(r"X = A^{-1}C",font_size=tam)
        ej4= MathTex(r"X = A^{-1}C",font_size=tam).move_to([0,3,0])
        x0,x1="x_{0}","x_{1}"
        x2,x3="x_{2}","x_{3}"
        x4,x5="x_{4}","x_{5}"
        x6,x7="x_{6}","x_{7}"
        
        lista1 = [[3,11,-7,9],[-1,1,-6,-3],[2,-12,4,1],[3,6,0,11]]
        lista2 = [[x0,x1],[x2,x3],[x4,x5],[x6,x7]]
        lista3 = [[-72,714],[-99,-140],[12,-185],[31,711]]
        ##
        matrizA = Matrix(lista1).set_color(GOLD_E).to_corner(LEFT).scale(0.7)
        
        matrizX = Matrix(lista2).set_color(MAROON_A).next_to(matrizA,RIGHT).scale(0.7)
        matrizX_copy = Matrix(lista2).set_color(MAROON_A).to_corner(LEFT).scale(0.7)
        igual=MathTex(r"=",font_size=tam).next_to(matrizX,RIGHT)
        igual_copy=MathTex(r"=",font_size=tam).next_to(matrizX_copy,RIGHT)
        matrizA_copy = Matrix(lista1).set_color(GOLD_E).next_to(igual_copy,RIGHT).scale(0.7)
        inversa_text= MathTex(r"-1",color=GOLD_E,font_size=32).next_to(matrizA_copy,UP+RIGHT)
        matrizC = Matrix(lista3).set_color(GREEN_A).next_to(igual,RIGHT).scale(0.7)
        matrizC_copy = Matrix(lista3).set_color(GREEN_A).next_to(matrizA_copy,RIGHT).scale(0.7)
        matrices = VGroup(matrizA,matrizX,igual,matrizC).move_to([0,1,0])
        matrices_copy = VGroup(matrizX_copy,igual_copy,matrizA_copy,inversa_text,matrizC_copy).move_to([0,1,0])
        ej=VGroup(ej0,ej1,ej2,ej3).arrange(DOWN,center=False, aligned_edge=LEFT).next_to(matrices,DOWN)
        ##
        
        #self.add(NumberPlane())
        self.play(Write(title))
        self.wait()
        self.play(Create(ejaxc))
        self.wait(3)
        self.play(Create(matrices))
        self.wait(6)
        for i in ej:
            self.play(Create(i),run_time=3)
            self.wait(3)
        self.remove(ejaxc)
        self.play(Transform(ej,ej4))
        self.wait(3)
        self.play(Transform(matrices,matrices_copy))
        self.wait(6)



class graph(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        tam=35
        axes = Axes(
            x_range=[0, 10.3, 1],
            y_range=[-1, 1,0.2 ],
            x_length=10,
            axis_config={"color": GREEN},
            tips=False,
        ).add_coordinates().set_color(BLACK)
        sin_graph1 = axes.plot(lambda x: np.sin(np.pi*x), color=BLUE)
        sin_graph2 = axes.plot(lambda x: np.sin(-np.pi*x), color=ORANGE)
        cos_graph1 = axes.plot(lambda x: np.cos(2*np.pi*x), color=GREEN_SCREEN)
        cos_graph2 = axes.plot(lambda x: 2*np.cos(2*np.pi*x), color=BLUE_C)
        cos_graph3 = axes.plot(lambda x: 4*np.cos(2*np.pi*x), color=ORANGE)
        #self.add(cos_graph1,cos_graph2,cos_graph3,axes)
        self.add(sin_graph1,sin_graph2,axes)


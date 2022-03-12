from manim import *
import numpy as np

colors = np.array([RED, BLUE])

def complete(n):
    vertices = [i for i in range(n)]
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            edges.append((i, j))
    return (vertices, edges)

def two_colorings(N):
    n = N*(N-1)//2
    colorings = []
    c = np.array([])
    for i in range(2**n):
        c = np.append(c, np.binary_repr(i, width=n))

    for mot in c:
        coloring = []
        for m in mot:
            c = RED if (m=='0') else BLUE
            coloring.append(c)
        colorings.append(coloring)
    return colorings

class LabeledModifiedGraph(Scene):
    def construct(self):
        n = 4
        V, E = complete(n)
        C = two_colorings(n)
        G = []

        for two_col in C:
            coloring = {}
            i=0
            for e in E:
                coloring[e] = {"stroke_color": two_col[i]}
                i += 1

            g = Graph(V, E, layout="circular", layout_scale=1,
                      labels=False,
                      edge_config=coloring).scale(0.3)

            G.append(g)

        print(len(G))
        r1 = VGroup(*G[:16]).arrange()
        r2 = VGroup(*G[16:32]).arrange()
        r3 = VGroup(*G[32:48]).arrange()
        r4 = VGroup(*G[48:64]).arrange()
        self.add(VGroup(r1, r2, r3, r4).arrange(direction=DOWN))

class PaulErdos(Scene):
    def construct(self):


        """ --- INTRODUCTION --- """


        hi = MathTex(r"\text{Hi!}").scale(4)

        erdos= ImageMobject("erdos.gif").scale(1.2).to_edge(RIGHT, buff=2)
        
        text = MarkupText("<u>Paul Erdös (1947)</u>").next_to(erdos, DOWN * 1.5).scale(0.8)

        # quote = MarkupText("\"I hope we'll be able to solve\nthese problems before we leave.\"").next_to(erdos, LEFT * 3).scale(0.7)
        # prob = MathTex(r"\mathbb{P} \left({\mathbf 1_{\text{mono}}(A) = 1}\right)").next_to(quote, DOWN*2)
        g1 = Group(erdos, text)
        # g2 = Group(g1, quote)
        V, E = complete(8)

        coloring = {}
        for e in E:
            coloring[e] = {"stroke_color": np.random.choice([RED, BLUE])}

        graph = Graph(V, E, layout="circular", layout_scale=1,
                      labels=False,
                      edge_config=coloring).scale(2).to_edge(LEFT, buff=2)

        group = ImageMobject("octahedron").to_edge(LEFT, buff=3).scale(0.5)

        title = MarkupText("The Probabilistic Approach").to_edge(UP, buff=0.5)
        h_line = Line(LEFT, RIGHT).scale(config.frame_width/2-1).next_to(title, DOWN)
        g2 = Group(g1, graph)
        g3 = Group(title, h_line)

        self.play(Write(hi), run_time=2)
        self.wait()
        self.play(FadeOut(hi))

        self.play(FadeIn(g1))
        self.wait()

        self.play(Create(graph), run_time=2, lag_ratio=0.2)
        self.play(g2.animate.scale(0.6), run_time=3)

        rect = SurroundingRectangle(g2, buff = 0.3).set_color(WHITE)

        self.play(Create(rect), run_time=2)
        self.wait()

        self.play(Create(h_line), Write(title), run_time=2)
        self.wait(2)

        # self.play(Write(prob))
        self.play(FadeOut(g2), FadeOut(rect))
        
        self.wait()

        postulate = MarkupText("If, in a given set of objects, the probability that all object does not\nhave a certain property is less than 1. Then there must exist an object\nwith this property.")
        postulate.scale(0.6) 

        self.play(Write(postulate), run_time=6)
        self.wait()

        self.play(postulate.animate.set_color("#333333"), run_time=2)

        # set of objects
        self.play(postulate[11:23].animate.set_color("#fcbf49"))
        self.wait()

        # probability less than one
        self.play(postulate[27:38].animate.set_color("#e0aaff"),
                  postulate[80:90].animate.set_color("#e0aaff"))
        self.wait()

        # property
        self.play(postulate[70:78].animate.set_color("#ef639c"))
        self.wait()
        
        # exists
        self.play(postulate[103:108].animate.set_color("#fb5607"))
        self.wait()

        result = MarkupText("Existence Result! ").set_color_by_gradient(BLUE, PINK).next_to(postulate, DOWN*3)

        self.play(Write(result))
        self.wait()

        self.play(FadeOut(result), run_time=1)
        self.wait()

        self.play(FadeOut(postulate))

        """ --- Ramsey numbers --- """

        title2 = MarkupText("Ramsey Numbers").to_edge(UP, buff=0.5)

        self.play(Transform(title, title2))
        self.wait()

        R_ll = MathTex(
            "R(l, l) = \\min \\left\\{ n \\in \\mathbb{N} : \\forall \\chi \\in \\{ R, B\\}^{E(K_n)} \\", "\\exists \\ \\text{monochromatic} \\ K_l", "\\subset K_n \\right\\}"
        ).scale(0.8)

        self.wait()

        self.play(Write(R_ll))
        self.wait()

        self.play(R_ll.animate.shift(UP))
        self.wait()

        graph.move_to(1.5*DOWN + 5*LEFT).scale(1.2)

        # graph2 = graph.copy().move_to(1.5*DOWN + 1.5*LEFT)
        # graph3 = graph.copy().move_to(1.5*DOWN + 1.5*RIGHT)
        # graph4 = graph.copy().move_to(1.5*DOWN + 5*RIGHT)

        V, E = complete(6)

        coloring = {}
        for e in E:
            coloring[e] = {"stroke_color": np.random.choice([RED, BLUE])}

        graph1 = Graph(V, E, layout="circular", layout_scale=1,
                      labels=False,
                      edge_config=coloring).scale(1.5)

        coloring = {}
        for e in E:
            coloring[e] = {"stroke_color": np.random.choice([RED, BLUE])}

        graph2 = Graph(V, E, layout="circular", layout_scale=1,
                      labels=False,
                      edge_config=coloring).scale(1.5)

        coloring = {}
        for e in E:
            coloring[e] = {"stroke_color": np.random.choice([RED, BLUE])}

        graph3 = Graph(V, E, layout="circular", layout_scale=1,
                      labels=False,
                      edge_config=coloring).scale(1.5)

        coloring = {}
        for e in E:
            coloring[e] = {"stroke_color": np.random.choice([RED, BLUE])}

        graph4 = Graph(V, E, layout="circular", layout_scale=1,
                      labels=False,
                      edge_config=coloring).scale(1.5)

        graphs = Group(graph1, graph2, graph3, graph4)
        graphs.arrange(RIGHT).shift(1.5*DOWN)

        self.play(FadeIn(graphs), lag_ratio=0.5, run_time=4)
        self.wait()

        # self.play(Transform(postulate, R_ll))

        # framebox1 = SurroundingRectangle(R_ll[1], buff = .4)
        # framebox2 = SurroundingRectangle(R_ll[3], buff = .4)

        # self.play(Create(framebox1))
        # self.play(Transform(framebox1, framebox2))

        minna = Group(graphs, R_ll)

        self.play(minna.animate.scale(0.75), run_time=2)

        where_proba = MarkupText("What about probabilities ?").set_color("#e0aaff").scale(0.5)

        box = SurroundingRectangle(R_ll[1], buff = 0.1).set_color("#ef639c")
        box2 = SurroundingRectangle(graph2, buff = 0.1)

        label = MarkupText("Property").set_color("#ef639c").next_to(box, UP).scale(0.5)
        label2 = MarkupText("Set of Objects").set_color("#fcbf49").next_to(box2, DOWN).scale(0.5)

        minna2 = Group(box, box2, label, label2)

        self.play(Create(box2), Write(label2))
        self.wait()

        self.play(ReplacementTransform(box2, box),
                  ReplacementTransform(label2, label))
        self.wait()

        minna3 = Group(minna, minna2)

        self.play(FadeOut(minna3))
        self.play(Create(where_proba), where_proba.animate.scale(2))
        self.wait()

        self.play(FadeOut(where_proba))
        self.wait()

        """ --- Intro to probas on graphs --- """

        # Dire que l'on travaille dans l'espace de tous les graphes 2-colorés

        # Dire que l'on utilise une distribution uniforme sur chaque état possible
        # i.e. pour un graphe donné, P(arrête est rouge) = P(arrête est bleue) = 1/2 pour tout arrête dans le graphe.

        self.wait(10)

        



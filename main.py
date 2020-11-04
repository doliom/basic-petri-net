from position import P
from transition import T
from model import Model
from arc import Arc

def main():
    for i in range(3):
        #positions
        p1 = P("p1", 1)
        p2 = P("p2", i)
        p3 = P("p3", 1)
        p4 = P("p4", 0)
        p5 = P("p5", 0)
        p6 = P("p6", 0)

        #transitions
        t1 = T("t1")
        t2 = T("t2")
        t3 = T("t3")
        t4 = T("t4")

        #arcs
        arc1 = Arc(name="from p1 to t1", prevP=p1, nextT=t1, n=1)
        arc2 = Arc(name="from t1 to p1", nextP=p1, n=1)
        arc3 = Arc(name="from t1 to p2", nextP=p2, n=1)
        arc4 = Arc(name="from p2 to t2", prevP=p2, nextT=t2, n=1)
        arc5 = Arc(name="from t2 to p3", nextP=p3, n=1)
        arc6 = Arc(name="from p3 to t2", prevP=p3, nextT=t2, n=1)
        arc7 = Arc(name="from t2 to p4", nextP=p4, n=1)
        arc8 = Arc(name="from p4 to t3", prevP=p4, nextT=t3, n=1)
        arc9 = Arc(name="from t3 to p5", nextP=p5, n=1)
        arc10 = Arc(name="from p4 to t4", prevP=p4, nextT=t4, n=1)
        arc11 = Arc(name="from t4 to p6", nextP=p6, n=1)

        t1.inArcs = [arc1]
        t1.outArcs = [arc2, arc3]
        t2.inArcs = [arc4, arc6]
        t2.outArcs = [arc5, arc7]
        t3.inArcs = [arc8]
        t3.outArcs = [arc9]
        t4.inArcs = [arc10]
        t4.outArcs = [arc11]

        positions = [p1, p2, p3, p4, p5, p6]
        transitions = [t1, t2, t3, t4]
        printInit(positions)

        petriNet = Model(positions, transitions)
        petriNet.simulate(150, i)

def printInit(positions):
    print("Init state")
    for p in positions:
        print("Position: {}  --------   Markers: {}".format(p.name, p.markers))
    print("\n")

if __name__ == "__main__":
    main()
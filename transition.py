class T:
    def __init__(self, name):
        self.name = name
        self.inArcs = []
        self.outArcs = []
        self.choiceProb = 0

    def tСondition(self, positions):
        for arc in self.inArcs:
            if arc.prevP.markers < arc.n:
                return False
        return True

    def perform(self, positions, mP2):
        if mP2 == 0:
            print("Transition {}".format(self.name))
            print("<--- from: ")
        for a in self.inArcs:
            for pos in positions:
                if pos.name == a.prevP.name:
                    pos.markers -= 1
                    break
            if mP2 == 0:
                print("{}".format(a.prevP.name))
        if mP2 == 0:
            print("---> to: ")
        for a in self.outArcs:
            for pos in positions:
                if pos.name == a.nextP.name:
                    pos.markers += 1
                    break
            if mP2 == 0:
                print("{}".format(a.nextP.name))

        return positions
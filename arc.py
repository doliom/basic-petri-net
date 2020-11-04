class Arc:
    def __init__(self, name, n, nextT=None, nextP=None, prevP=None):
        self.name = name
        self.nextT = nextT
        self.nextP = nextP
        self.prevP = prevP
        self.n = n
import numpy as np
from tabulate import tabulate
import pandas as pd

class Model:
    def __init__(self, positions, transitions):
        self.positions = positions
        self.transitions = transitions
        self.nextT = []

    def simulate(self, Imod, mP2):
        iteration = 0
        print("__________________\nSimulation start\n__________________")

        while iteration < Imod:
            if mP2 ==0:
                print(" -- Iteration: {} --".format(iteration+1))
            for p in self.positions:
                p.checkMarkersStat()

            #1
            for t in self.transitions:
                if t.tСondition(self.positions):
                    self.nextT.append(t)

            #2
            for t in self.nextT:
                t.choiceProb = 1/len(self.nextT)

            #3
            probabilities = []
            for t in self.nextT:
                probabilities.append(t.choiceProb)

            choosenT = np.random.choice(self.nextT, p=probabilities)
            self.positions = choosenT.perform(self.positions, mP2)

            self.nextT = []
            iteration += 1
        self.verification(iteration)

    def verification(self, iteration):

        print("\n -- Verification --")

        names, maxp, minp, avgp = [],[],[],[]
        for p in self.positions:
            names.append(p.name)
            maxp.append(p.markersMax)
            minp.append(p.markersMin)
            avgp.append(p.markersAvg/iteration)

        d = {'name': names, 'max num  of markers': maxp, 'min num  of markers': minp, 'avg num  of markers': avgp}
        df_time = pd.DataFrame(data=d)
        print(tabulate(df_time, headers='keys', tablefmt='psql'))

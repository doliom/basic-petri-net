class P:
    def __init__(self, name, markers):
        self.name = name
        self.markers = markers
        self.markersMin = 0
        self.markersMax = 0
        self.markersAvg = 0
        if self.markers:
            self.markersMin = self.markers

    def checkMarkersStat(self):
        if self.markers < self.markersMin:
            self.markersMin = self.markers

        if self.markers > self.markersMax:
            self.markersMax = self.markers

        self.markersAvg += self.markers
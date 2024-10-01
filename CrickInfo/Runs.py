#here it will have parameters like totalrun,runtype,scoredby
#runtype will be enum  and scoredby will be from a player class
class Runs:
    def __init__(self,totalRuns,typee,scoredBy):
        self.totalRuns=totalRuns
        self.typee=typee
        self.scoredBy=scoredBy
#we can add getter and setters later
        
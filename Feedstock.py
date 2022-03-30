import pandas as pd

class Feedstock (object):
    def __init__(self, sourceFile=None, NH4=0, DO2=0, V=0, pH=0):
        self.sourceFile = sourceFile
        if (sourceFile == None):
            self.NH4 = NH4
            self.DO2 = DO2
            self.V = V
            self.pH = pH
        else:
            data = pd.read_csv(sourceFile, header=0)
            self.NH4 = float(data.NH4)
            self.DO2 = float(data.DO2)
            self.V = float(data.V)
            self.pH = float(data.pH)

class Input (Feedstock):
    def __init__(self, sourceFile="input.csv"):
        super().__init__(sourceFile=sourceFile)

class Output (Feedstock):
    def __init__(self, outputFile="output.csv"):
        self.outputFile = outputFile
        super().__init__()

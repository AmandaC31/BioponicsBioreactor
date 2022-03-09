class Instrument (object):
    def __init__(self, variable: str, min: float, max: float, units: str):
        self.variable = variable
        self.range = [min, max]
        self.units = units if (units == 'dS/m' or units == 'pH' or units == '°C' or units == 'g/L') else None
        if self.units == None:
            raise ValueError("An unsopported unit was used in Instrument initiation")
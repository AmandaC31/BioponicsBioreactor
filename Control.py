from Action import Action
from Instrument import Instrument


class Control(object):
    def __init__(self, action: Action, instrument: Instrument):
        self.action = action
        self.instrument = instrument

from Feedstock import Input, Output, Feedstock
from Instrument import Instrument
from Action import Action
from Control import Control

input = Input("example_input.csv")
print(input)

ph_meter = Instrument(variable="pH", units="pH", min=4, max=10)
print(ph_meter)

adjust_ph = Action("batch_lime_addition")
print(adjust_ph)

ph_control = Control(action=adjust_ph, instrument=ph_meter)
print(ph_control)
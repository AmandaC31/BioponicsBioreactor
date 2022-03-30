import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

class Simulation:
    def __init__(self, A, Cv):
        self.A = A
        self.Cv = Cv
    def init(self, t):
        return 0.15

    def deriv(self, h, t):
        return self.init(t) / self.A - self.Cv * np.sqrt(h) / self.A

    def simulate(self):
        # initial condition
        initialCondition = [0.0]
        # setting the time-steps
        t = np.linspace(0, 200, 101)
        h = odeint(self.deriv, initialCondition, t)

        plt.plot(t,h)
        plt.xlabel('minutes')
        plt.ylabel('meters')
        plt.title('Gravity-Drained Tank')
        plt.legend(['Liquid Level'])
import math
from math import exp

class turbine(object):
    """docstring for turbine."""
    def __init__(self, R, beta, ang_speed_unit = 'RPM', wind_speed_unit = 'km/h'):
        self.radius = R
        self.beta = beta
        self.ang_speed_unit = ang_speed_unit
        self.wind_speed_unit = wind_speed_unit
        self.rho = 1.225 # air density

    def cp(self, alfa, beta):
        #alfa is the Tip Speed Ratio and beta is the pitch angle
        alfa_i = (1/(alfa + 0.08*beta)) - 0.035/(beta**3 + 1)
        print('alfa_i ' + str(alfa_i))
        c1 = 0.5
        c2 = 116*alfa_i
        c3 = 0.4
        c4 = 0
        c5 = 5
        c6 = 21*alfa_i
        x = 1.5
        cp = c1*(c2 - c3*beta - c4*(beta**x) - c5) * exp(-c6)
        print('cp ' + str(cp))
        return cp

    def mech_power(self, wind_speed, angular_speed):
        wind_speed = wind_speed * 0.277778 # km/h to m/s
        angular_speed = angular_speed * 0.1047 # RPM to rad/s
        alfa = ((angular_speed * self.radius) / (wind_speed))
        print('alfa ' + str(alfa))
        cp = self.cp(alfa, self.beta)
        A = math.pi*self.radius**2
        pm = cp * self.rho * A * (wind_speed**3) / 2
        return pm

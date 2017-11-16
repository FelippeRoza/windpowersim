import numpy as np
import matplotlib.pyplot as plt
import math

class turbine(object):
    """docstring for turbine."""
    def __init__(self, R, beta, ang_speed_unit = 'RPM', wind_speed_unit = 'km/h'):
        self.radius = R
        self.beta = beta
        self.ang_speed_unit = ang_speed_unit
        self.wind_speed_unit = wind_speed_unit
        self.rho = 1.225 # air density
        self.kmh_to_ms = 0.277778 # convert km/h to m/s
        self.rpm_to_rads = 0.1047 # convert RPM to rad/s

    def cp(self, alfa):
        #turbine power coeficient
        #alfa is the Tip Speed Ratio and beta is the pitch angle
        alfa_i = (1/(alfa + 0.08*self.beta)) - 0.035/(self.beta**3 + 1)
        c1 = 0.5
        c2 = 116*alfa_i
        c3 = 0.4
        c4 = 0
        c5 = 5
        c6 = 21*alfa_i
        x = 1.5
        cp = c1*(c2 - c3*self.beta - c4*(self.beta**x) - c5) * np.exp(-c6)
        return cp

    def print_cp(self, wind_speed, angular_speed):
        #wind_speed and angular_speed are pandas Series
        alfa = self.alfa(wind_speed, angular_speed)
        cp = self.cp(alfa)
        plt.plot(alfa,cp)
        plt.show()

    def available_power(self, wind_speed):
        #wind kinetic energy
        if self.wind_speed_unit == 'km/h':
            wind_speed = wind_speed*self.kmh_to_ms
        A = math.pi*self.radius**2
        pw = self.rho * A * (wind_speed**3) / 2
        return pw

    def alfa(self, wind_speed, angular_speed):
        if self.ang_speed_unit == 'RPM':
            angular_speed = angular_speed*self.rpm_to_rads
        if self.wind_speed_unit == 'km/h':
            wind_speed = wind_speed*self.kmh_to_ms
        return ((angular_speed * self.radius) / (wind_speed))

    def mech_power(self, wind_speed, angular_speed):
        #turbine power
        alfa = self.alfa(wind_speed, angular_speed)
        cp = self.cp(alfa)
        pm = cp * self.available_power(wind_speed)
        return pm

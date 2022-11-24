#!/usr/bin/env python
# Created by "Thieu" at 17:13, 23/11/2022 ----------%                                                                               
#       Email: nguyenthieu2102@gmail.com            %                                                    
#       Github: https://github.com/thieu1995        %                         
# --------------------------------------------------%

import numpy as np
from mealpy.utils.problem import Problem
from scipy.io import loadmat


class WaterSupplyReservoirProblem(Problem):
    def __init__(self, lb=None, ub=None, minmax="min", name="Water Supply Reservoir Problem", datafile=None, **kwargs):
        self.NT = len(lb)  # Number of time-step

        self.D_max = 831.10  # Maximum of demand (MCM)
        self.S_initial = 1430  # The initial storage of reservoir (Million Cubic Meters - MCM)
        self.S_min = 830
        self.S_max = 3340

        self.x0 = 11.291
        self.x1 = 0.0157
        self.x2 = self.x3 = 0

        self.Storage = np.zeros(self.NT)  # Storage of reservoir in the of periods

        self.MUL = 0.3858  # A coefficient for converting Release(i,1) from MCM/month to M3/s ( 1e6 / 30*24*3600 )
        self.C_min = 100  # Used to calculate penalty function
        self.g = 9.81
        self.eta = 0.9
        self.PF = 0.417

        data = loadmat(datafile)
        self.Inflow = data[f"Inflow{self.NT}"].flatten()
        self.Demand = data[f"Demand{self.NT}"].flatten()
        self.Loss = data[f"Loss{self.NT}"].flatten()

        super().__init__(lb, ub, minmax, **kwargs)
        self.name = f"{name} {self.n_dims}-month"
        self.filename = f"wsrp_{self.n_dims}m"

    def fit_func(self, solution):
        R = solution.copy()
        self.Storage[0] = self.S_initial + self.Inflow[0] - R[0] - (self.Loss[0]/1000)*(self.x0 + self.x1*self.S_initial)

        self.Pen_min = np.zeros(self.NT)
        if self.Storage[0] < self.S_min:    # Always store more than min, less than min will be punished
            self.Pen_min[0] = self.C_min * (1 - self.Storage[0] / self.S_min)
        if self.Storage[0] > self.S_max:
            self.Storage[0] = self.S_max

        for idx in range(1, self.NT):
            self.Storage[idx] = self.Storage[idx-1] + self.Inflow[idx] - R[idx] - (self.Loss[idx]/1000)*(self.x0 + self.x1*self.Storage[idx-1])
            if self.Storage[idx] < self.S_min:
                self.Pen_min[idx] = self.C_min * (1 - self.Storage[idx] / self.S_min)
            if self.Storage[idx] > self.S_max:
                self.Storage[idx] = self.S_max

        # Fit = Objective Function + Penalty Function
        objs = ((R - self.Demand)/self.D_max)**2
        return np.sum(objs) + np.sum(self.Pen_min)


class HydropowerReservoirOperationProblem(Problem):
    def __init__(self, lb=None, ub=None, minmax="min", name="Hydropower Reservoir Operation Problem", datafile=None, **kwargs):
        self.NT = len(lb)   # Number of time-step
        self.D_max = 831.10     # Maximum of demand (MCM)
        self.S_initial = 1430   # The initial storage of reservoir (Million Cubic Meters - MCM)
        self.S_min = 830
        self.S_max = 3340
        self.TWL = 172 # tail water level in downstream is assumed constant at 172 m above sea level (m)
        self.power = 650 # Total capacity of hydroelectric plant (MegaWats - MW)

        self.a = 249.83364
        self.b = 0.58720
        self.c = -1.37e-5
        self.d = 1.562e-9

        self.x0 = 11.291
        self.x1 = 0.0157
        self.x2 = self.x3 = 0

        self.H_initial = self.a + self.b * self.S_initial + self.c * self.S_initial**2 + self.d * self.S_initial**3
        self.Storage = np.zeros(self.NT)        # Storage of reservoir in the of periods
        self.H = np.zeros(self.NT)              # Water Elevation of reservoir in the of periods
        self.p_t = np.zeros(self.NT)            # Power generated in the periods (MW)
        self.h_t = np.zeros(self.NT)            # Mean water elevation in the of periods

        self.MUL = 0.3858               # A coefficient for converting Release(i,1) from MCM/month to M3/s ( 1e6 / 30*24*3600 )
        self.C_min = 100                # Used to calculate penalty function
        self.g = 9.81
        self.eta = 0.9
        self.PF = 0.417

        data = loadmat(datafile)
        self.Inflow = data[f"Inflow{self.NT}"].flatten()
        self.Demand = data[f"Demand{self.NT}"].flatten()
        self.Loss = data[f"Loss{self.NT}"].flatten()

        super().__init__(lb, ub, minmax, **kwargs)
        self.name = f"{name} {self.n_dims}-month"
        self.filename = f"hrop_{self.n_dims}m"

    def fit_func(self, solution):
        R = solution.copy()
        self.Storage[0] = self.S_initial + self.Inflow[0] - R[0] - (self.Loss[0]/1000)*(self.x0 + self.x1*self.S_initial)
        self.Pen_min = np.zeros(self.NT)
        if self.Storage[0] < self.S_min:    # Always store more than min, less than min will be punished
            self.Pen_min[0] = self.C_min * (1 - self.Storage[0] / self.S_min)
        if self.Storage[0] > self.S_max:
            self.Storage[0] = self.S_max

        self.H[0] = self.a + self.b * self.Storage[0] + self.c * self.Storage[0]**2 + self.d * self.Storage[0]**3
        self.h_t[0] = (self.H_initial + self.H[0]) / 2 - self.TWL
        self.p_t[0] = min((self.g * self.eta * R[0]) / self.PF * (self.h_t[0] / 1000) * self.MUL, self.power)

        for idx in range(1, self.NT):
            self.Storage[idx] = self.Storage[idx-1] + self.Inflow[idx] - R[idx] - (self.Loss[idx]/1000)*(self.x0 + self.x1*self.Storage[idx-1])

            if self.Storage[idx] < self.S_min:
                self.Pen_min[idx] = self.C_min * (1 - self.Storage[idx] / self.S_min)
            if self.Storage[idx] > self.S_max:
                self.Storage[idx] = self.S_max

            self.H[idx] = self.a + self.b * self.Storage[idx] + self.c * self.Storage[idx]**2 + self.d * self.Storage[idx]**3
            self.h_t[idx] = (self.H[idx-1] + self.H[idx]) / 2 - self.TWL
            self.p_t[idx] = min((self.g * self.eta * R[idx]) / self.PF * (self.h_t[idx] / 1000) * self.MUL, self.power)

        # Fit = Objective Function + Penalty Function
        objs = 1 - self.p_t / self.power
        return np.sum(objs) + np.sum(self.Pen_min)

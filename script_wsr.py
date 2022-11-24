#!/usr/bin/env python
# Created by "Thieu" at 00:03, 06/10/2022 ----------%                                                                               
#       Email: nguyenthieu2102@gmail.com            %                                                    
#       Github: https://github.com/thieu1995        %                         
# --------------------------------------------------%

import numpy as np
from src.models.problem import WaterSupplyReservoirProblem
from src.config import Config, MhaConfig
from src.models.base_class import BaseClass
from pathlib import Path
from sklearn.model_selection import ParameterGrid

# Reproducibility
np.random.seed(Config.SEED)
datafile = f"{Config.DATA_DIRECTORY}/Dez_data.mat"


for system in MhaConfig.SYSTEMS:
    for opt_paras in list(ParameterGrid(system["param_grid"])):
        for ndim in MhaConfig.N_DIMS:
            for idx_trial in range(1, Config.N_TRIALS + 1):
                problem = WaterSupplyReservoirProblem(lb=[0.] * ndim, ub=[1000.] * ndim, minmax="min", datafile=datafile)
                pathsave = f"{Config.DATA_RESULTS}/{problem.filename}"
                Path(pathsave).mkdir(parents=True, exist_ok=True)

                model = BaseClass(system['name'], opt_paras)
                model.solve(problem, idx_trial, pathsave, Config.VERBOSE)

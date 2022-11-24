#!/usr/bin/env python
# Created by "Thieu" at 21:08, 10/11/2022 ----------%                                                                               
#       Email: nguyenthieu2102@gmail.com            %                                                    
#       Github: https://github.com/thieu1995        %                         
# --------------------------------------------------%

import uuid
from src.models.mha import dict_optimizer_classes
from src.utils.io_util import save_results_to_csv
from src.utils.model_util import save_system
from src.utils.visual.line import draw_multiple_lines
from src.config import Const


class BaseClass:

    def __init__(self, opt_name:str, opt_paras:dict):
        self.optimizer = dict_optimizer_classes[opt_name](**opt_paras)
        self.paras = str(opt_paras)
        self.filename = f"{opt_name}-{str(uuid.uuid4().hex)}"
        self.problem, self.solution, self.best_fit, self.loss_train = None, None, None, None

    def solve(self, problem, idx_trial, pathsave, verbose):
        self.problem = problem
        self.solution, self.best_fit = self.optimizer.solve(problem)
        self.loss_train = self.optimizer.history.list_global_best_fit

        #### Draw demand-release
        draw_multiple_lines([self.problem.Demand, self.solution], Const.LEGEND_DEMAND_RELEASE,
                            Const.Y1Y2_COLORS, Const.Y1Y2_LINESTYLES, Const.Y1Y2_MARKERS, Const.XY_DEMAND_RELEASE,
                            self.problem.name, f"{self.filename}-{Const.FILENAME_DEMAND_RELEASE}", pathsave, Const.FILE_FIGURE_TYPES, verbose)

        ## Save system
        save_system(self, f"{pathsave}/{self.filename}-{Const.FILENAME_MODEL}")

        ## Calculate performance metrics and save it to csv file
        metrics = {
            "system": self.optimizer.name,
            "filename": self.filename,
            "paras": self.paras,
            "trial": idx_trial,
            "best_fit": self.best_fit
        }
        save_results_to_csv(metrics, Const.FILENAME_METRICS_ALL_MODELS, pathsave)
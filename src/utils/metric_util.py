#!/usr/bin/env python
# Created by "Thieu" at 13:00, 13/09/2021 ----------%
#       Email: nguyenthieu2102@gmail.com            %                                                    
#       Github: https://github.com/thieu1995        %                         
# --------------------------------------------------%

from permetrics.regression import RegressionMetric
from src.config import Config


def my_regression_metrics(y_true, y_pred, prefix="train", decimal=4):
    evaluator = RegressionMetric(y_true, y_pred, decimal=decimal)
    mm2 = evaluator.get_metrics_by_list_names(Config.METRICS_FOR_TESTING_PHASE, Config.LIST_PARA_METRICS)
    mm = {}
    for key, value in mm2.items():
        mm[f"{prefix}_{key}"] = value
    return mm

# !/usr/bin/env python
# Created by "Thieu" at 18:03, 29/11/2021 ----------%
#       Email: nguyenthieu2102@gmail.com            %
#       Github: https://github.com/thieu1995        %
# --------------------------------------------------%

import pandas as pd
import pickle


def save_system(system, pathfile=None):
    system.optimizer.history.list_population = []
    name_obj = open(f'{pathfile}.pkl', 'wb')
    pickle.dump(system, name_obj)
    name_obj.close()


def load_system(pathfile=None):
    system = pickle.load(open(f"{pathfile}.pkl", 'rb'))
    return system


# def get_best_parameter_kfold(dataframe):
#     def fitness(cols):
#         return Series([np.sum(cols * ConfigKfold.BEST_MODEL_WEIGHT_TUNE_PARAS)])
#
#     dataframe['fitness'] = dataframe[ConfigKfold.BEST_MODEL_METRIC_TUNE_PARAS].apply(fitness, axis=1)
#     if is_min_operator_fitness(ConfigKfold.BEST_MODEL_METRIC_TUNE_PARAS):
#         minvalueIndexLabel = dataframe['fitness'].idxmin()
#         best_data = dataframe.iloc[[minvalueIndexLabel]]
#     else:
#         maxvalueIndexLabel = dataframe['fitness'].idxmax()
#         best_data = dataframe.iloc[[maxvalueIndexLabel]]
#     return best_data


def get_best_parameter_retrain(pathload, model_name, paras):
    df = pd.read_csv(pathload, usecols=["model_name", "model_paras"])
    paras_series = df[df['model_name'] == model_name]["model_paras"]
    paras_string = paras_series.values.tolist()[0]
    paras_list = []
    for para in paras_string.split('-'):
        if para.isalpha():
            paras_list.append(para)
        else:
            paras_list.append(eval(para))
    # paras_list = list(map(eval, paras_string.split('-')))
    paras_new = {}
    for idx, key in enumerate(paras.keys()):
        paras_new[key] = paras_list[idx]
    return paras_new


# def update_best_paras_for_models_cv(models):
#     def find_best_list_paras(model_name):
#         list_names = []
#         for path in Path(f"{ConfigKfold.DATA_RESULTS_RETRAIN}").rglob(f"*/{model_name}/*metrics.csv"):
#             list_names.append(path.name)
#         paras_string = str(list_names[0]).replace("-metrics.csv", "")
#         paras_list = []
#         for para in paras_string.split('-'):
#             if para.isalpha():
#                 paras_list.append([para])
#             else:
#                 paras_list.append([eval(para)])
#         return paras_list
#
#     list_models = []
#     for idx_model, model in enumerate(models):
#         paras_list = find_best_list_paras(model['name'])
#         paras_new = {}
#         for idx_para, key in enumerate(model['param_grid'].keys()):
#             paras_new[key] = paras_list[idx_para]
#         model['param_grid'] = paras_new
#         list_models.append(model)
#     return list_models


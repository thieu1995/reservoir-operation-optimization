#!/usr/bin/env python
# Created by "Thieu" at 17:31, 21/04/2022 ----------%                                                                               
#       Email: nguyenthieu2102@gmail.com            %                                                    
#       Github: https://github.com/thieu1995        %                         
# --------------------------------------------------%

from copy import deepcopy
from pathlib import Path
from pandas import read_csv
from sklearn.model_selection import ParameterGrid
from src.utils.visual.line import draw_multiple_lines


def get_loss_lines(df):
    values = df.values
    line_train = [values[:, 0], values[:, 1]]  # Train loss
    line_valid = [values[:, 0], values[:, 2]]  # Validation loss or Test loss
    return line_train, line_valid


def draw_convergence_chart_models(compared_models, pathread, pathsave, suf_file_read, cols_header, obj, sur_file_save_train, sur_file_save_test):
    ## Draw loss/fitness value (convergence chart) for all models (each model with 1 set of parameter only)
    list_lines_train = []
    list_lines_valid = []
    list_legends = []
    for model in compared_models:
        parameters_grid = list(ParameterGrid(model["param_grid"]))
        keys = model["param_grid"].keys()
        mha_paras = parameters_grid[0]

        # Load loss
        filename = "".join([f"-{mha_paras[key]}" for key in keys])
        df = read_csv(f"{pathread}/{model['name']}/{filename[1:]}-{suf_file_read}.csv", usecols=cols_header)
        line_train, line_valid = get_loss_lines(df)
        list_lines_train.append(line_train)
        list_lines_valid.append(line_valid)
        list_legends.append(f"{model['name']}")

    Path(pathsave).mkdir(parents=True, exist_ok=True)
    draw_multiple_lines(list_lines_train, list_legends, None, None, ["Iterations", f"{obj}"],
                        title=None, filename=sur_file_save_train, pathsave=pathsave, exts=[".png", ".pdf"], verbose=False)
    draw_multiple_lines(list_lines_valid, list_legends, None, None, ["Iterations", f"{obj}"],
                        title=None, filename=sur_file_save_test, pathsave=pathsave, exts=[".png", ".pdf"], verbose=False)


def draw_convergence_chart_epochs_popsizes(models, pathread, pathsave, suf_file_read, cols_header, obj, validation_used,
                                           legend_epoch="Number of Generations = "):
    ## Draw comparison of multiple paras combinations configuration in each model
    for model in models:
        pathsave_img = f"{pathsave}/{model['name']}"
        Path(pathsave_img).mkdir(parents=True, exist_ok=True)

        ## Draw for Epoch
        paras_dict = deepcopy(model["param_grid"])
        epochs = paras_dict.pop("epoch")

        for mha_paras in list(ParameterGrid(paras_dict)):
            list_legends = []
            list_lines_train = []
            list_lines_valid = []
            for epoch in epochs:
                # Load loss
                filename_read = f"{epoch}" + "".join([f"-{mha_paras[key]}" for key in paras_dict.keys()])
                df = read_csv(f"{pathread}/{model['name']}/{filename_read}-{suf_file_read}.csv", usecols=cols_header)
                line_train, line_valid = get_loss_lines(df)
                list_lines_train.append(line_train)
                list_lines_valid.append(line_valid)
                list_legends.append(f"{legend_epoch}{epoch}")

            filename_save = "".join([f"-{mha_paras[key]}" for key in paras_dict.keys()])
            filename_save = f"{filename_save[1:]}"
            draw_multiple_lines(list_lines_train, list_legends, None, None, ["Iterations", f"{obj}"], title=None,
                                filename=f"{filename_save}-train-loss-Epochs", pathsave=pathsave_img, exts=[".png", ".pdf"], verbose=False)
            sur_file_save_test = "valid-loss-Epochs" if validation_used else "test-loss-Epochs"
            draw_multiple_lines(list_lines_valid, list_legends, None, None, ["Iterations", f"{obj}"], title=None,
                                filename=f"{filename_save}-{sur_file_save_test}", pathsave=pathsave_img, exts=[".png", ".pdf"], verbose=False)

        ## Draw for Pop-size
        paras_dict = deepcopy(model["param_grid"])
        epochs = paras_dict.pop("epoch")
        if "pop_size" not in paras_dict:
            break
        pop_sizes = paras_dict.pop("pop_size")
        parameters_grid = list(ParameterGrid(paras_dict))
        for epoch in epochs:
            for mha_paras in parameters_grid:
                list_legends = []
                list_lines_train = []
                list_lines_valid = []
                for pop_size in pop_sizes:
                    if len(paras_dict.keys()) < 1:
                        filename_read = f"{epoch}-{pop_size}"
                    else:
                        filename_read = f"{epoch}-{pop_size}" + "".join([f"-{mha_paras[key]}" for key in paras_dict.keys()])
                    # Load loss
                    df = read_csv(f"{pathread}/{model['name']}/{filename_read}-{suf_file_read}.csv", usecols=cols_header)
                    line_train, line_valid = get_loss_lines(df)
                    list_lines_train.append(line_train)
                    list_lines_valid.append(line_valid)
                    list_legends.append(f"{legend_epoch}{pop_size}")

                if len(paras_dict.keys()) < 1:
                    filename_save = f"{epoch}"
                else:
                    filename_save = f"{epoch}" + "".join([f"-{mha_paras[key]}" for key in paras_dict.keys()])
                draw_multiple_lines(list_lines_train, list_legends, None, None, ["Iterations", f"{obj}"], title=None,
                                    filename=f"{filename_save}-train-loss-PopSize", pathsave=pathsave_img, exts=[".png", ".pdf"], verbose=False)
                filename_img = "valid-loss-PopSize" if validation_used else "test-loss-PopSize"
                draw_multiple_lines(list_lines_valid, list_legends, None, None, ["Iterations", f"{obj}"], title=None,
                                    filename=f"{filename_save}-{filename_img}", pathsave=pathsave_img, exts=[".png", ".pdf"], verbose=False)


def draw_fitness_chart_algorithms(compared_models, pathread, pathsave, suf_file_read, cols_header, sur_file_save):
    ## Draw loss/fitness value (convergence chart) for all models (each model with 1 set of parameter only)
    list_lines_fitness = []
    list_legends = []
    for model in compared_models:
        parameters_grid = list(ParameterGrid(model["param_grid"]))
        keys = model["param_grid"].keys()
        mha_paras = parameters_grid[0]

        # Load loss
        filename = "".join([f"-{mha_paras[key]}" for key in keys])
        df = read_csv(f"{pathread}/{model['name']}/{filename[1:]}-{suf_file_read}.csv", usecols=cols_header)
        line_fitness = [df.values[:, 0], df.values[:, 1]]
        list_lines_fitness.append(line_fitness)
        list_legends.append(f"{model['name']}")

    Path(pathsave).mkdir(parents=True, exist_ok=True)
    draw_multiple_lines(list_lines_fitness, list_legends, None, None, ["#Iterations", "Fitness"],
                        title=None, filename=sur_file_save, pathsave=pathsave, exts=[".png", ".pdf"], verbose=False)


def draw_fitness_chart_epochs_popsizes(models, pathread, pathsave, suf_file_read, cols_header, legend_epoch="Number of Generations = "):
    ## Draw comparison of multiple paras combinations configuration in each model
    for model in models:
        pathsave_img = f"{pathsave}/{model['name']}"
        Path(pathsave_img).mkdir(parents=True, exist_ok=True)

        ## Draw for Epoch
        paras_dict = deepcopy(model["param_grid"])
        epochs = paras_dict.pop("epoch")

        for mha_paras in list(ParameterGrid(paras_dict)):
            list_legends = []
            list_lines_fitness = []
            for epoch in epochs:
                # Load loss
                filename_read = f"{epoch}" + "".join([f"-{mha_paras[key]}" for key in paras_dict.keys()])
                df = read_csv(f"{pathread}/{model['name']}/{filename_read}-{suf_file_read}.csv", usecols=cols_header)
                line_fitness = [df.values[:, 0], df.values[:, 1]]
                list_lines_fitness.append(line_fitness)
                list_legends.append(f"{legend_epoch}{epoch}")

            filename_save = "".join([f"-{mha_paras[key]}" for key in paras_dict.keys()])
            filename_save = f"{filename_save[1:]}"
            draw_multiple_lines(list_lines_fitness, list_legends, None, None, ["#Iterations", "Fitness"], title=None,
                                filename=f"{filename_save}-fitness-Epochs", pathsave=pathsave_img, exts=[".png", ".pdf"], verbose=False)

        ## Draw for Pop-size
        paras_dict = deepcopy(model["param_grid"])
        epochs = paras_dict.pop("epoch")
        if "pop_size" not in paras_dict:
            break
        pop_sizes = paras_dict.pop("pop_size")
        parameters_grid = list(ParameterGrid(paras_dict))
        for epoch in epochs:
            for mha_paras in parameters_grid:
                list_legends = []
                list_lines_fitness = []
                for pop_size in pop_sizes:
                    if len(paras_dict.keys()) < 1:
                        filename_read = f"{epoch}-{pop_size}"
                    else:
                        filename_read = f"{epoch}-{pop_size}" + "".join([f"-{mha_paras[key]}" for key in paras_dict.keys()])
                    # Load loss
                    df = read_csv(f"{pathread}/{model['name']}/{filename_read}-{suf_file_read}.csv", usecols=cols_header)

                    line_fitness = [df.values[:, 0], df.values[:, 1]]
                    list_lines_fitness.append(line_fitness)
                    list_legends.append(f"{legend_epoch}{pop_size}")

                if len(paras_dict.keys()) < 1:
                    filename_save = f"{epoch}"
                else:
                    filename_save = f"{epoch}" + "".join([f"-{mha_paras[key]}" for key in paras_dict.keys()])
                draw_multiple_lines(list_lines_fitness, list_legends, None, None, ["Iterations", "Fitness"], title=None,
                                    filename=f"{filename_save}-fitness-PopSize", pathsave=pathsave_img, exts=[".png", ".pdf"], verbose=False)


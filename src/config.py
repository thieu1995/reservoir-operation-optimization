#!/usr/bin/env python
# Created by "Thieu" at 23:27, 22/02/2021 ----------%
#       Email: nguyenthieu2102@gmail.com            %
#       Github: https://github.com/thieu1995        %
# --------------------------------------------------%

from os.path import abspath, dirname

basedir = abspath(dirname(__file__))


VALIDATION_USED = False

if VALIDATION_USED:
    FILE_METRIC_CSV = ["AS_train", "PS_train", "RS_train", "F1S_train", "F2S_train", "MCC_train", "LS_train",
                       "AS_valid", "PS_valid", "RS_valid", "F1S_valid", "F2S_valid", "MCC_valid", "LS_valid",
                       "AS_test", "PS_test", "RS_test", "F1S_test", "F2S_test", "MCC_test", "LS_test"]
else:
    FILE_METRIC_CSV = ["AS_train", "PS_train", "RS_train", "F1S_train", "F2S_train", "MCC_train", "LS_train",
                       "AS_test", "PS_test", "RS_test", "F1S_test", "F2S_test", "MCC_test", "LS_test"]


class Const:

    FILENAME_DEMAND_RELEASE = "demand_release"
    LEGEND_DEMAND_RELEASE = ["Demand", "Release"]
    XY_DEMAND_RELEASE = ["Time step (month)", "MCM"]
    Y1Y2_COLORS = ["blue", "red"]
    Y1Y2_LINESTYLES = ["-", "--"]
    Y1Y2_MARKERS = ["o", "*"]

    FILE_METRIC_NAME = "metrics-results"

    FILENAME_LOSS_TRAIN = "loss_train"
    FILENAME_CONVERGENCE = "convergence"
    FILENAME_PERFORMANCE = "performance"
    FILENAME_METRICS = "metrics"
    FILENAME_MODEL = "model"
    FILENAME_METRICS_ALL_MODELS = "all-models-metrics"

    FILE_MIN = "min.csv"
    FILE_MEAN = "mean.csv"
    FILE_MAX = "max.csv"
    FILE_STD = "std.csv"
    FILE_CV = "cv.csv"
    FOLDERNAME_STATISTICS = "statistics"
    FOLDER_VISUALIZE = "visualize"

    FILE_LOSS_HEADER = ["epoch", "loss", "val_loss"]
    FILE_FIGURE_TYPES = [".png", ".pdf"]    #[".png", ".pdf", ".eps"]


class Config:
    DATA_DIRECTORY = f'{basedir}/data'
    DATA_RESULTS = f'{DATA_DIRECTORY}/results'

    LEGEND_EPOCH = "Number of Generations = "
    LEGEND_POP_SIZE = "Population size = "

    MHA_MODE_TRAIN_PHASE1 = "sequential"        # Don't change this value

    N_CPUS_RUN = 8
    SEED = 20
    VERBOSE = False
    N_TRIALS = 2                # Number of trials for each model
    MHA_LB = [-1]  # Lower bound for metaheuristics
    MHA_UB = [1]  # Upper bound for metaheuristics


class MhaConfig:
    EPOCH = [500]         # Number of generations or epoch in neural network and metaheuristics
    POP_SIZE = [50]     # Number of population size in metaheuristics
    N_DIMS = [60, 240, 480]

    ## Evolutionary-based group
    ep_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "bout_size": [0.05],  # percentage of child agents implement tournament selection
    }
    es_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "lamda": [0.75],  # Percentage of child agents evolving in the next generation, default=0.75
    }
    ma_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "pc": [0.85],  # crossover probability
        "pm": [0.15],  # mutation probability
        "p_local": [0.5], # Probability of local search for each agent, default=0.5
        "max_local_gens": [10], # Number of local search agent will be created during local search mechanism, default=10
    }
    ga_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "pc": [0.85],  # crossover probability
        "pm": [0.05]  # mutation probability
    }
    de_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "wf": [0.85],  # weighting factor
        "cr": [0.8],  # crossover rate
        "strategy": [1]     #
    }
    fpa_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "p_s": [0.85],  # switch probability, default = 0.8
        "levy_multiplier": [0.01],   # multiplier factor of Levy-flight trajectory
    }
    cro_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "po": [0.85],  # The rate between free/occupied at the beginning
        "Fb": [0.9],  # BroadcastSpawner/ExistingCorals rate
        "Fa": [0.1],  # fraction of corals duplicates its self and tries to settle in a different part of the reef
        "Fd": [0.1],  # fraction of the worse health corals in reef will be applied depredation
        "Pd": [0.1],  # Probability of depredation
        "GCR": [0.1],  #
        "gamma_min": [0.02],  #
        "gamma_max": [0.2],     #
        "n_trials": [3],  # number of attempts for a larvar to set in the reef.
    }

    ## Swarm-based group
    abc_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "n_elites": [16], # number of bees which provided for good location and other location
        "n_others": [4],
        "patch_size": [5.0], # patch_variables = patch_variables * patch_factor (0.985)
        "patch_reduction": [0.985],
        "n_sites": [3], # 3 bees (employed bees, onlookers and scouts), 1 good partition
        "n_elite_sites": [1],
    }
    acor_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "sample_count": [50],  # Number of Newly Generated Samples
        "intent_factor": [0.5],  # Intensification Factor (Selection Pressure)
        "zeta": [1.0],  # Deviation-Distance Ratio
    }
    agto_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "p1": [0.03],   # p in the paper)
        "p2": [0.8],    # w in the paper
        "beta": [3.0], # coefficient in updating equation
    }
    alo_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }
    ao_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }
    aro_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }
    avoa_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "p1": [0.6],    # probability of status transition
        "p2": [0.4],    # probability of status transition
        "p3": [0.6],    # probability of status transition
        "alpha": [0.8], # probability of 1st best
        "gama": [2.5]   # a factor in the paper
    }
    ba_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "loudness": [0.8],  # (A_min, A_max): loudness, default = (1.0, 2.0)
        "pulse_rate": [0.95], # (r_min, r_max): pulse rate / emission rate
        "pf_min": [0.], # (pf_min, pf_max): pulse frequency
        "pf_max": [10.],
    }
    beesa_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "selected_site_ratio": [0.5],  # (selected_site_ratio, elite_site_ratio)
        "elite_site_ratio": [0.4],
        "selected_site_bee_ratio": [0.1], # (selected_site_bee_ratio, elite_site_bee_ratio)
        "elite_site_bee_ratio": [2.0],
        "dance_radius": [0.1],# Bees Dance Radius
        "dance_reduction": [0.99],
    }
    bes_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "a_factor": [10, ],  # default: 10, determining the corner between point search in the central point, in [5, 10]
        "R_factor": [1.5],  # default: 1.5, determining the number of search cycles, in [0.5, 2]
        "alpha": [2., ],  # default: 2, parameter for controlling the changes in position, in [1.5, 2]
        "c1": [2., ],  # default: 2, in [1, 2]
        "c2": [2., ],  # c1 and c2 increase the movement intensity of bald eagles towards the best and centre points
    }
    bfo_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "C_s": [0.1, ],  # default: 10, determining the corner between point search in the central point, in [5, 10]
        "C_e": [0.001],  # default: 1.5, determining the number of search cycles, in [0.5, 2]
        "Ped": [4, ],  # default: 2, parameter for controlling the changes in position, in [1.5, 2]
        "Ns": [4, ],  # default: 2, in [1, 2]
        "N_adapt": [2, ],  # c1 and c2 increase the movement intensity of bald eagles towards the best and centre points
        "N_split": [40,]
    }
    bsa_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "ff": [10],  # flight frequency - default = 10
        "pff": [0.8],  # the probability of foraging for food - default = 0.8
        "c1": [1.5], # [c1, c2]: Cognitive accelerated coefficient, Social accelerated coefficient same as PSO
        "c2": [1.5],
        "a1": [1.0],# [a1, a2]: The indirect and direct effect on the birds' vigilance behaviours.
        "a2": [1.0],
        "fl": [0.5, ]  # The followed coefficient- default = 0.5
    }
    coa_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "n_coyotes": [5, ] # number of coyotes per group
    }
    csa_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "p_a": [0.3]  # probability a
    }
    cso_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "mixture_ratio": [0.15 ],  # joining seeking mode with tracing mode
        "smp": [5],  # seeking memory pool, 10 clones  (larger is better but time-consuming)
        "spc": [False],  # self-position considering
        "cdc": [0.8 ],  # counts of dimension to change  (larger is more diversity but slow convergence)
        "srd": [0.15 ],  # seeking range of the selected dimension (smaller is better but slow convergence)
        "c1": [0.4],  # same in PSO
        "w_min": [0.5],# same in PSO
        "w_max": [0.9],
        "selected_strategy": [1],  # 0: best fitness, 1: tournament, 2: roulette wheel, else: random (decrease by quality)
    }
    dmoa_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "peep": [2],
    }
    do_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }
    eho_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "alpha": [0.5],  # a factor that determines the influence of the best in each clan
        "beta": [0.5],  # a factor that determines the influence of the x_center
        "n_clans": [5],  # number of clans
    }
    fa_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "max_sparks": [50],  # parameter controlling the total number of sparks generated by the pop_size fireworks
        "p_a": [0.04],  # const parameter
        "p_b": [0.8],  # const parameter
        "max_ea": [40],  # maximum explosion amplitude
        "m_sparks": [5],  # number of sparks generated in each explosion generation
    }
    ffa_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "gamma": [0.001],  # Light Absorption Coefficient
        "beta_base": [2],  # Attraction Coefficient Base Value
        "alpha": [0.2],  # Mutation Coefficient
        "alpha_damp": [0.99],  # Mutation Coefficient Damp Rate
        "delta": [0.05],  # Mutation Step Size
        "exponent": [2],  # Exponent
    }
    foa_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }
    goa_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "c_min": [0.00004],
        "c_max": [1.0],
    }
    gwo_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }
    gwo_woa_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }
    hba_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }
    hgs_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "PUP": [0.03],  # Switching updating  position probability
        "LH": [1000],  # Largest hunger / threshold
    }
    hho_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }
    ja_paras = levy_ja_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }
    mfo_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }
    mpa_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }
    mrfo_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "somersault_range": [2, ]  # somersault factor that decides the somersault range of manta rays
    }
    msa_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "n_best": [5, ],  # how many of the best moths to keep from one generation to the next
        "partition": [0.5, ],  # The proportional of first partition
        "max_step_size": [1.0, ], # Max step size used in Levy-flight technique, default=1.0
    }
    nmra_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "bp": [0.75],  # breeding probability (0.75)
    }
    pfa_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }
    pso_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "c1": [1.2],  # local coefficient
        "c2": [1.2],  # global coefficient
        "w_min": [0.4],  # weight min factor
        "w_max": [0.9],  # weight max factor
    }
    ppso_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }
    cpso_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "c1": [2.05],  # local coefficient
        "c2": [2.05],  # global coefficient
        "w_min": [0.4],  # weight min factor
        "w_max": [0.9],  # weight max factor
    }
    clpso_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "c_local": [1.2],  # local coefficient
        "w_min": [0.4],  # weight min factor
        "w_max": [0.9],  # weight max factor
        "max_flag": [7],
    }
    scso_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }
    sfo_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "pp": [0.2, ],  # the rate between SailFish and Sardines (N_sf = N_s * pp) = 0.25, 0.2, 0.1
        "AP": [4.0, ],  # A = 4, 6,...
        "epsilon": [0.0001, ],  # = 0.0001, 0.001
    }
    sho_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "h_factor": [5],  # default = 5, coefficient linearly decreased from 5 to 0
        "N_tried": [10, ],  # default = 10,
    }
    slo_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }
    srsr_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }
    ssa_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "ST": [0.8],  # ST in [0.5, 1.0], safety threshold value
        "PD": [0.2],  # number of producers
        "SD": [0.1],  # number of sparrows who perceive the danger
    }
    sso_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }
    sspidera_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "r_a": [1.0],     # the rate of vibration attenuation when propagating over the spider web, default=1.0
        "p_c": [0.7],  # controls the probability of the spiders changing their dimension mask in the random walk step, default=0.7
        "p_m": [0.1]  # the probability of each value in a dimension mask to be one, default=0.1
    }
    sspidero_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "fp_min": [0.65], # (fp_min, fp_max): Female Percent, default = (0.65, 0.9)
        "fp_max": [0.9],
    }
    woa_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }

    ## Physics-based group
    sa_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "max_sub_iter": [5],  # Maximum Number of Sub-Iteration (within fixed temperature), default=5
        "t0": [1000],
        "t1": [1],
        "move_count": [5],  # Move Count per Individual Solution, default=5
        "mutation_rate": [0.1],  # Mutation Rate, default=0.1
        "mutation_step_size": [0.1],  # Mutation Step Size, default=0.1
        "mutation_step_size_damp": [0.99],
    }
    wdo_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "RT": [3],  # RT coefficient
        "g_c": [0.2],  # gravitational constant
        "alp": [0.4],  # constants in the update equation
        "c_e": [0.4],  # coriolis effect
        "max_v": [0.3],  # maximum allowed speed
    }
    mvo_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "wep_min": [0.2], # Wormhole Existence Probability (min in Eq.(3.3) paper, default = 0.2
        "wep_max": [1.0], # Wormhole Existence Probability (max in Eq.(3.3) paper, default = 1.0
    }
    two_paras = otwo_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }
    efo_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "r_rate": [0.3],  # default = 0.3     # Like mutation parameter in GA but for one variable, mutation probability
        "ps_rate": [0.85],  # default = 0.85    # Like crossover parameter in GA, crossover probability
        "p_field": [0.1],  # default = 0.1     # portion of population, positive field
        "n_field": [0.45],  # default = 0.45    # portion of population, negative field
    }
    nro_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }
    hgso_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "n_clusters": [2]  # Number of clusters
    }
    aso_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "alpha": [10, ],  # Depth weight
        "beta": [0.2, ],  # Multiplier weight
    }
    eo_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }
    archoa_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "c1": [2, ],  # Default belongs [1, 2]
        "c2": [6, ],  # Default belongs [2, 4, 6]
        "c3": [2, ],  # Default belongs [1, 2]
        "c4": [0.5, ],  # Default belongs [0.5, 1]
        "acc_max": [0.9, ],  # Default 0.9
        "acc_min": [0.1, ],  # Default 0.1
    }
    bro_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "threshold": [3]
    }

    ## Human-based group
    bso_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "m_clusters": [5, ],  # m: number of clusters
        "p1": [0.2, ],  # probability
        "p2": [0.8, ],  # probability
        "p3": [0.4, ],  # probability
        "p4": [0.5, ],  # probability
        "slope": [20, ],  # k: factor that changing logsig() function's slope
    }
    ca_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "accepted_rate": [0.15 ],  # probability of accepted rate, default: 0.15
    }
    chio_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "brr": [0.15, ],    # Basic reproduction rate, default=0.15
        "max_age": [10, ],  # Maximum infected cases age, default=10
    }
    fbio_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }
    gska_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "pb": [0.1, ],  # percent of the best   0.1%, 0.8%, 0.1%
        "kf": [0.5],
        "kr": [0.9, ],  # knowledge ratio
        "kg": [5],
    }
    ica_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "empire_count": [5, ],  # Number of Empires (also Imperialists)
        "assimilation_coeff": [1.5, ],  # Assimilation Coefficient (beta in the paper)
        "revolution_prob": [0.05, ],  # Revolution Probability
        "revolution_rate": [0.1, ],  # Revolution Rate (mu)
        "revolution_step_size": [0.1, ],  # Revolution Step Size (sigma)
        "zeta": [0.1, ],  # Colonies Coefficient in Total Objective Value of Empires
    }
    lco_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "r1": [2.35]  # step size coefficient
    }
    qsa_paras = improved_qsa_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }
    saro_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "se": [0.5, ],
        "mu": [15, ],
    }
    ssdo_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }
    tlo_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }
    spbo_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }

    ## Bio-based group
    bbo_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "p_m": [0.01],
        "elites": [2]  # Number of elites solution
    }
    eoa_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "p_c": [0.9],  # default = 0.9, crossover probability
        "p_m": [0.01],  # default = 0.01 initial mutation probability
        "n_best": [2],  # default = 2, how many of the best earthworm to keep from one generation to the next
        "alpha": [0.98],  # default = 0.98, similarity factor
        "beta": [0.9],  # default = 1, the initial proportional factor
        "gamma": [0.9],  # default = 0.9, a constant that is similar to cooling factor of a cooling schedule in the simulated annealing.
    }
    iwo_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "seed_min": [2], # (Min, Max) Number of Seeds
        "seed_max": [10],
        "exponent": [2],  # Variance Reduction Exponent
        "sigma_start": [1.0],# (Initial, Final) Value of Standard Deviation
        "sigma_end": [0.01],
    }
    sbo_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "alpha": [0.94, ],  # the greatest step size
        "p_m": [0.05, ],  # mutation probability
        "psw": [0.02]  # percent of the difference between the upper and lower limit (Eq. 7)
    }
    sma_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "p_t": [0.03],  # probability threshold
    }
    vcs_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "lamda": [0.5],  # Number of the best will keep (percentage %)
        "sigma": [1.5],  # Weight factor
    }
    who_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "n_explore_step": [3],  # default = 3, number of exploration step
        "n_exploit_step": [3],  # default = 3, number of exploitation step
        "eta": [0.15],  # default = 0.15, learning rate
        "p_hi": [0.9],  # default = 0.9, the probability of wildebeest move to another position based on herd instinct
        "local_alpha": [0.9], # default = (0.9, 0.3), (alpha 1, beta 1) - control local movement
        "local_beta": [0.3],
        "global_alpha": [0.2],# default = (0.2, 0.8), (alpha 2, beta 2) - control global movement
        "global_beta": [0.8],
        "delta_w": [2.0], #  default = (2.0, 2.0) , (delta_w, delta_c) - (dist to worst, dist to best)
        "delta_c": [2.0],
    }
    bmo_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "pl": [5],  # [1, pop_size - 1], barnacle’s threshold
    }
    sos_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }
    soa_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "fc": [2], # [1, 5], freequency of employing variable A (A linear decreased from fc to 0), default = 2
    }
    tsa_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }

    ## System-based group
    gco_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "cr": [0.7],  # Same as DE algorithm  # default: 0.7, crossover-rate
        "wf": [1.25],  # Same as DE algorithm  # default: 1.25, weighting factor
    }
    wca_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "nsr": [4],  # Number of rivers + sea (sea = 1)
        "wc": [2.0],  # Coefficient
    }
    aeo_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }
    aaeo_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }

    ## Math-based group
    aoa_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "alpha": [5],  # fixed parameter, sensitive exploitation parameter, Default: 5,
        "miu": [0.5],  # fixed parameter , control parameter to adjust the search process, Default: 0.5,
        "moa_min": [0.2],  # range min of Math Optimizer Accelerated, Default: 0.2,
        "moa_max": [0.9],  # range max of Math Optimizer Accelerated, Default: 0.9,
    }
    cgo_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }
    gbo_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "pr": [0.5],  # Probability Parameter, default = 0.5
        "beta_min": [0.2],
        "beta_max": [1.2], # Fixed parameter (no name in the paper), default = (0.2, 1.2)
    }
    hc_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "neighbour_size": [10],  # fixed parameter, sensitive exploitation parameter, Default: 10
    }
    pss_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "acceptance_rate": [0.9],  # the probability of accepting a solution in the normal range, default = 0.9
        "sampling_method": ["LHS"],  #  'LHS': Latin-Hypercube or 'MC': 'MonteCarlo', default = "LHS"
    }
    sca_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }
    info_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }
    run_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
    }
    circlesa_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "c_factor": [0.8]
    }
    hs_paras = {
        "epoch": EPOCH, "pop_size": POP_SIZE,
        "c_r": [0.95],  # Harmony Memory Consideration Rate, default = 0.15
        "pa_r": [0.05],  # Pitch Adjustment Rate, default=0.5

    }

    models = [
        # Evolutionary-based
        {"name": "EP-RBFN", "class": "EpRbfn", "param_grid": ep_paras},  # Evolutionary Programming (EP)
        {"name": "ES-RBFN", "class": "EsRbfn", "param_grid": es_paras},  # Evolution Strategies (ES)
        {"name": "MA-RBFN", "class": "MaRbfn", "param_grid": ma_paras},  # Memetic Algorithm (MA)
        {"name": "DE-RBFN", "class": "DeRbfn", "param_grid": de_paras},  # Differential Evolution (DE)
        {"name": "GA-RBFN", "class": "GaRbfn", "param_grid": ga_paras},  # Genetic Algorithm (GA)
        {"name": "FPA-RBFN", "class": "FpaRbfn", "param_grid": fpa_paras},  # Flower Pollination Algorithm (FPA)
        {"name": "CRO-RBFN", "class": "CroRbfn", "param_grid": cro_paras},  # Coral Reefs Optimization (CRO)

        ## Swarm-based
        {"name": "ABC-RBFN", "class": "AbcRbfn", "param_grid": abc_paras},  # Artificial Bee Colony (ABC)
        {"name": "ACOR-RBFN", "class": "AcorRbfn", "param_grid": acor_paras},  # Ant Colony Optimization Continuous (ACOR)
        {"name": "AGTO-RBFN", "class": "AgtoRbfn", "param_grid": agto_paras},  # Artificial Gorilla Troops Optimization (AGTO)
        {"name": "ALO-RBFN", "class": "AloRbfn", "param_grid": alo_paras},  # Ant Lion Optimizer (ALO)
        {"name": "AO-RBFN", "class": "AoRbfn", "param_grid": ao_paras},  # Aquila Optimization (AO)
        {"name": "ARO-RBFN", "class": "AroRbfn", "param_grid": aro_paras},  # Artificial Rabbits Optimization (ARO)
        {"name": "AVOA-RBFN", "class": "AvoaRbfn", "param_grid": aro_paras},  # African Vultures Optimization Algorithm (AVOA)
        {"name": "BA-RBFN", "class": "BaRbfn", "param_grid": ba_paras},  # Bat Algorithm (BA)
        {"name": "BeesA-RBFN", "class": "BeesaRbfn", "param_grid": beesa_paras},  # Bees Algorithm (BeesA)
        {"name": "BES-RBFN", "class": "BesRbfn", "param_grid": bes_paras},  # Bald Eagle Search (BES)
        {"name": "BFO-RBFN", "class": "BfoRbfn", "param_grid": bfo_paras},  # Adaptive Bacterial Foraging Optimization (ABFO)
        {"name": "BSA-RBFN", "class": "BsaRbfn", "param_grid": bsa_paras},  # Bird Swarm Algorithm (BSO)
        {"name": "COA-RBFN", "class": "CoaRbfn", "param_grid": coa_paras},  # Coyote Optimization Algorithm (COA)
        {"name": "CSA-RBFN", "class": "CsaRbfn", "param_grid": csa_paras},  # Cuckoo Search Algorithm (CSA)
        {"name": "CSO-RBFN", "class": "CsoRbfn", "param_grid": cso_paras},  # Cat Swarm Optimization (CSO)
        {"name": "DMOA-RBFN", "class": "DmoaRbfn", "param_grid": dmoa_paras},  # Dwarf Mongoose Optimization Algorithm (DMOA)
        {"name": "DO-RBFN", "class": "DoRbfn", "param_grid": do_paras},  # Dragonfly Optimization (DO)
        {"name": "EHO-RBFN", "class": "EhoRbfn", "param_grid": eho_paras},  # Elephant Herding Optimization (EHO)
        {"name": "FA-RBFN", "class": "FaRbfn", "param_grid": fa_paras},  # Fireworks Algorithm (FA)
        {"name": "FFA-RBFN", "class": "FfaRbfn", "param_grid": ffa_paras},  # Firefly Algorithm (FireflyA)
        {"name": "FOA-RBFN", "class": "FoaRbfn", "param_grid": foa_paras},  # Fruit-fly Optimization Algorithm (FOA)
        {"name": "GOA-RBFN", "class": "GoaRbfn", "param_grid": goa_paras},  # Grasshopper Optimization Algorithm (GOA)
        {"name": "GWO-RBFN", "class": "GwoRbfn", "param_grid": gwo_paras},  # Grey Wolf Optimizer (GWO)
        {"name": "GWO-WOA-RBFN", "class": "GwoWoaRbfn", "param_grid": gwo_woa_paras},  # Hybrid Grey Wolf - Whale Optimization Algorithm (GWO_WOA)
        {"name": "HBA-RBFN", "class": "HbaRbfn", "param_grid": hba_paras},  # Honey Badger Algorithm (HBA)
        {"name": "HGS-RBFN", "class": "HgsRbfn", "param_grid": hgs_paras},  # Hunger Games Search (HGS)
        {"name": "HHO-RBFN", "class": "HhoRbfn", "param_grid": hho_paras},  # Harris Hawks Optimization (HHO)
        {"name": "JA-RBFN", "class": "JaRbfn", "param_grid": ja_paras},  # Jaya Algorithm (JA)
        {"name": "LEVY-JA-RBFN", "class": "LevyJaRbfn", "param_grid": levy_ja_paras},  # Levy Jaya Algorithm (JA)
        {"name": "MFO-RBFN", "class": "MfoRbfn", "param_grid": mfo_paras},  # Moth-flame optimization (MFO)
        {"name": "MPA-RBFN", "class": "MpaRbfn", "param_grid": mpa_paras},  # Marine Predators Algorithm (MPA)
        {"name": "MRFO-RBFN", "class": "MrfoRbfn", "param_grid": mrfo_paras},  # Manta Ray Foraging Optimization (MRFO)
        {"name": "MSA-RBFN", "class": "MsaRbfn", "param_grid": msa_paras},  # Moth Search Algorithm (MSA)
        {"name": "NMRA-RBFN", "class": "NmraRbfn", "param_grid": nmra_paras},  # Naked Mole-rat Algorithm (NMRA)
        {"name": "PFA-RBFN", "class": "PfaRbfn", "param_grid": pfa_paras},  # Pathfinder Algorithm (PFA)
        {"name": "PSO-RBFN", "class": "PsoRbfn", "param_grid": pso_paras},  # Particle Swarm Optimization (PSO)
        {"name": "PPSO-RBFN", "class": "PPsoRbfn", "param_grid": ppso_paras},  # Phasor Particle Swarm Optimization (P-PSO)
        {"name": "CPSO-RBFN", "class": "CPsoRbfn", "param_grid": cpso_paras},  # Chaos Particle Swarm Optimization (C-PSO)
        {"name": "CLPSO-RBFN", "class": "ClPsoRbfn", "param_grid": clpso_paras},  # Comprehensive Learning Particle Swarm Optimization (CL-PSO)
        {"name": "SCSO-RBFN", "class": "ScsoRbfn", "param_grid": scso_paras},  # Sand Cat Swarm Optimization (SCSO)
        {"name": "SFO-RBFN", "class": "SfoRbfn", "param_grid": sfo_paras},  # Sailfish Optimizer (SFO)
        {"name": "SHO-RBFN", "class": "ShoRbfn", "param_grid": sho_paras},  # Spotted Hyena Optimizer (SHO)
        {"name": "SLO-RBFN", "class": "SloRbfn", "param_grid": slo_paras},  # Sea Lion Optimization Algorithm (SLO)
        {"name": "SRSR-RBFN", "class": "SrsrRbfn", "param_grid": srsr_paras},  # Swarm Robotics Search And Rescue (SRSR)
        {"name": "SSA-RBFN", "class": "SsaRbfn", "param_grid": ssa_paras},  # Sparrow Search Algorithm (SpaSA)
        {"name": "SSO-RBFN", "class": "SsoRbfn", "param_grid": sso_paras},  # Salp Swarm Optimization (SSO)
        {"name": "SSpiderA-RBFN", "class": "SspideraRbfn", "param_grid": sspidera_paras},  # Social Spider Algorithm (SSpiderA)
        {"name": "SSpiderO-RBFN", "class": "SspideroRbfn", "param_grid": sspidero_paras},  # Social Spider Optimization (SSpiderO)
        {"name": "WOA-RBFN", "class": "WoaRbfn", "param_grid": woa_paras},  # Whale Optimization Algorithm (WOA)

        ## Physics-based
        {"name": "SA-RBFN", "class": "SaRbfn", "param_grid": sa_paras},  # Simulated Annealing (SA)
        {"name": "WDO-RBFN", "class": "WdoRbfn", "param_grid": wdo_paras},  # Wind Driven Optimization (WDO)
        {"name": "MVO-RBFN", "class": "MvoRbfn", "param_grid": mvo_paras},  # Multi-Verse Optimizer (MVO)
        {"name": "TWO-RBFN", "class": "TwoRbfn", "param_grid": two_paras},  # Tug of War Optimization (TWO)
        {"name": "EFO-RBFN", "class": "EfoRbfn", "param_grid": efo_paras},  # Electromagnetic Field Optimization (EFO)
        {"name": "NRO-RBFN", "class": "NroRbfn", "param_grid": nro_paras},  # Nuclear Reaction Optimization (NRO)
        {"name": "HGSO-RBFN", "class": "HgsoRbfn", "param_grid": hgso_paras},  # Henry Gas Solubility Optimization (HGSO)
        {"name": "ASO-RBFN", "class": "AsoRbfn", "param_grid": aso_paras},  # Atom Search Optimization (ASO)
        {"name": "EO-RBFN", "class": "EoRbfn", "param_grid": eo_paras},  # Equilibrium Optimizer (EO)
        {"name": "ArchOA-RBFN", "class": "ArchoaRbfn", "param_grid": archoa_paras},  # Archimedes Optimization Algorithm (ArchOA)

        # Human-based added
        {"name": "BRO-RBFN", "class": "BroRbfn", "param_grid": bro_paras},  # Battle Royale Optimization (BRO)
        {"name": "BSO-RBFN", "class": "BsoRbfn", "param_grid": bso_paras},  # Brain Storm Optimization (BSO)
        {"name": "CA-RBFN", "class": "CaRbfn", "param_grid": ca_paras},  # Culture Algorithm (CA)
        {"name": "CHIO-RBFN", "class": "ChioRbfn", "param_grid": chio_paras},  # Coronavirus Herd Immunity Optimization (CHIO)
        {"name": "FBIO-RBFN", "class": "FbioRbfn", "param_grid": fbio_paras},  # Forensic-Based Investigation Optimization (FBIO)
        {"name": "GSKA-RBFN", "class": "GskaRbfn", "param_grid": gska_paras},  # Gaining Sharing Knowledge-based Algorithm (GSKA)
        {"name": "ICA-RBFN", "class": "IcaRbfn", "param_grid": ica_paras},  # Imperialist Competitive Algorithm (ICA)
        {"name": "LCO-RBFN", "class": "LcoRbfn", "param_grid": lco_paras},  # Life Choice-based Optimization (LCO)
        {"name": "QSA-RBFN", "class": "QsaRbfn", "param_grid": qsa_paras},  # Queuing search algorithm (QSA)
        {"name": "ImprovedQSA-RBFN", "class": "ImprovedQsaRbfn", "param_grid": improved_qsa_paras},  # Queuing search algorithm (QSA)
        {"name": "SARO-RBFN", "class": "SaroRbfn", "param_grid": saro_paras},  # Search And Rescue Optimization (SARO)
        {"name": "SSDO-RBFN", "class": "SsdoRbfn", "param_grid": ssdo_paras},  # Social Ski-Driver Optimization (SSDO)
        {"name": "TLO-RBFN", "class": "TloRbfn", "param_grid": tlo_paras},  # Teaching Learning-based Optimization (TLO)
        {"name": "SPBO-RBFN", "class": "SpboRbfn", "param_grid": spbo_paras},  # Student Psychology Based Optimization (SPBO)

        ## Bio-based
        {"name": "BBO-RBFN", "class": "BboRbfn", "param_grid": bbo_paras},  # Biogeography-based optimization (BBO)
        {"name": "EOA-RBFN", "class": "EoaRbfn", "param_grid": eoa_paras},  # Earthworm Optimisation Algorithm (EOA)
        {"name": "IWO-RBFN", "class": "IwoRbfn", "param_grid": iwo_paras},  # Invasive weed colonization (IWO)
        {"name": "SBO-RBFN", "class": "SboRbfn", "param_grid": sbo_paras},  # Satin Bowerbird Optimizer (SBO)
        {"name": "SMA-RBFN", "class": "SmaRbfn", "param_grid": sma_paras},  # Slime Mould Algorithm (SMA)
        {"name": "VCS-RBFN", "class": "VcsRbfn", "param_grid": vcs_paras},  # Virus Colony Search (VCS)
        {"name": "WHO-RBFN", "class": "WhoRbfn", "param_grid": who_paras},  # Wildebeest Herd Optimization (WHO)
        {"name": "BMO-RBFN", "class": "BmoRbfn", "param_grid": bmo_paras},  # Barnacles Mating Optimizer (BMO)
        {"name": "SOS-RBFN", "class": "SosRbfn", "param_grid": sos_paras},  # Symbiotic Organisms Search (SOS)
        {"name": "SOA-RBFN", "class": "SoaRbfn", "param_grid": soa_paras},  # Seagull Optimization Algorithm (SOA)
        {"name": "TSA-RBFN", "class": "TsaRbfn", "param_grid": tsa_paras},  # Tunicate Swarm Algorithm (TSA)

        ## System-based
        {"name": "GCO-RBFN", "class": "GcoRbfn", "param_grid": gco_paras},  # Germinal Center Optimization (GCO)
        {"name": "WCA-RBFN", "class": "WcaRbfn", "param_grid": wca_paras},  # Water Cycle Algorithm (WCA)
        {"name": "AEO-RBFN", "class": "AeoRbfn", "param_grid": aeo_paras},  # Artificial Ecosystem-based Optimization (AEO)
        {"name": "AAEO-RBFN", "class": "AaeoRbfn", "param_grid": aaeo_paras},  # Augment Artificial Ecosystem-based Optimization (AAEO)

        ## Math-based
        {"name": "AOA-RBFN", "class": "AoaRbfn", "param_grid": aoa_paras},  # Arithmetic Optimization Algorithm (AOA)
        {"name": "CGO-RBFN", "class": "CgoRbfn", "param_grid": cgo_paras},  # Chaos Game Optimization (CGO)
        {"name": "GBO-RBFN", "class": "GboRbfn", "param_grid": gbo_paras},  # Gradient-Based Optimizer (GBO)
        {"name": "HC-RBFN", "class": "HcRbfn", "param_grid": hc_paras},  # Hill Climbing (HC)
        {"name": "PSS-RBFN", "class": "PssRbfn", "param_grid": pss_paras},  # Pareto-like Sequential Sampling (PSS)
        {"name": "SCA-RBFN", "class": "ScaRbfn", "param_grid": sca_paras},  # Sine Cosine Algorithm (SCA)
        {"name": "INFO-RBFN", "class": "InfoRbfn", "param_grid": info_paras},  # weIghted meaN oF vectOrs (INFO)
        {"name": "RUN-RBFN", "class": "RunRbfn", "param_grid": run_paras},  # RUNge Kutta optimizer (RUN)
        {"name": "CircleSA-RBFN", "class": "CirclesaRbfn", "param_grid": circlesa_paras},  # Circle Search Algorithm (CircleSA)

        ## Music-based group
        {"name": "HS-RBFN", "class": "HsRbfn", "param_grid": hs_paras},  # Harmony Search (HS)
    ]



    SYSTEMS = [
        # Evolutionary-based
        {"name": "DE", "class": "DeElm", "param_grid": de_paras},  # Differential Evolution (DE)

        # ## Swarm-based
        # {"name": "GWO-WOA", "class": "GwoWoaElm", "param_grid": gwo_woa_paras},  # Hybrid Grey Wolf - Whale Optimization Algorithm (GWO_WOA)
        # {"name": "CLPSO", "class": "ClPsoElm", "param_grid": clpso_paras},  # Comprehensive Learning Particle Swarm Optimization (CL-PSO)
        # {"name": "WOA", "class": "WoaElm", "param_grid": woa_paras},  # Whale Optimization Algorithm (WOA)
        #
        # ## Physics-based
        # {"name": "NRO", "class": "NroElm", "param_grid": nro_paras},  # Nuclear Reaction Optimization (NRO)
        # {"name": "ASO", "class": "AsoElm", "param_grid": aso_paras},  # Atom Search Optimization (ASO)
        #
        # # Human-based added
        # # {"name": "CHIO", "class": "ChioElm", "param_grid": chio_paras},  # Coronavirus Herd Immunity Optimization (CHIO)
        # {"name": "FBIO", "class": "FbioElm", "param_grid": fbio_paras},  # Forensic-Based Investigation Optimization (FBIO)
        # {"name": "TLO", "class": "TloElm", "param_grid": tlo_paras},  # Teaching Learning-based Optimization (TLO)
        #
        # ## Bio-based
        # {"name": "SMA", "class": "SmaElm", "param_grid": sma_paras},  # Slime Mould Algorithm (SMA)
        # {"name": "SOA", "class": "SoaElm", "param_grid": soa_paras},  # Seagull Optimization Algorithm (SOA)
        #
        # ## System-based
        # {"name": "AEO", "class": "AeoElm", "param_grid": aeo_paras},  # Artificial Ecosystem-based Optimization (AEO)
        #
        # ## Math-based
        # {"name": "GBO", "class": "GboElm", "param_grid": gbo_paras},  # Gradient-Based Optimizer (GBO)
        # {"name": "INFO", "class": "InfoElm", "param_grid": info_paras},  # weIghted meaN oF vectOrs (INFO)
        # {"name": "RUN", "class": "RunElm", "param_grid": run_paras},  # RUNge Kutta optimizer (RUN)
        #
        # ## Music-based group
        # {"name": "HS", "class": "HsElm", "param_grid": hs_paras},  # Harmony Search (HS)
    ]

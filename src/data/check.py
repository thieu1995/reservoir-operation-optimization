#!/usr/bin/env python
# Created by "Thieu" at 17:34, 23/11/2022 ----------%                                                                               
#       Email: nguyenthieu2102@gmail.com            %                                                    
#       Github: https://github.com/thieu1995        %                         
# --------------------------------------------------%

from scipy.io import loadmat

data = loadmat("./Dez_data.mat")

# print(type(data))
# print(data["Demand"])
# print(data["Loss"])
print(data.keys())

# ['Demand', 'Demand60', 'Demand240', 'Demand480', 'Inflow60', 'Inflow240', 'Inflow480', 'Loss', 'Loss60', 'Loss240', 'Loss480']
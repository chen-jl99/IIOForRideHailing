import numpy as np

N_train = 10000 # size of the training data
N_hist = 10000 # size of the historical data (used to obtain the Lagrange multiplier)
N_incoming = 1000 # size of incoming data

# number of features used in clustering algorithm
num_feature = 3
feature_name = ['total_distance','fare','compensation']

# possible levels of incentives
passenger_incentive_list = np.array([0, 0.05, 0.1, 0.15])
driver_incentive_list = np.array([0, 0.05, 0.1, 0.15])

eta = 0.7 # minimum ratios of final earnings (of the driver) to the final payment (of the passenger)
B = 300 # the total budget
B_hist = B * N_hist / N_incoming # the adjusted total budget for offline component

K = 100 # the cluster size
gamma = 10 # parameter used in the kernel function 
r = 0.01 # parameter used in the uncertainty set
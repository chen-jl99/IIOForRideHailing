# IIOForRideHailing-ICDE2023

This is the demo code of the paper **Two-Sided Instant Incentive Optimization under a Shared Budget in Ride-Hailing Services**.

## Dataset

In the numerical experiment section of our paper, we use the real data as input, which are restricted to access inside Meituan. Here we generate some "fake" data to run the code.

## Usage

0. Set the parameter

The parameters should be first set in 'params.py'.

1. Generate simulation data

Run '1_Data_generation.ipynb' to generate simulation data, the output data are saved in 'data/'.

2. Run the offline component of the algorithm

Depending on the candidate approach you choose, you can run '2_Offline_component_SEP.ipynb'/'2_Offline_component_SHR.ipynb'/'2_Offline_component_SHR_CLUSTER.ipynb'/'2_Offline_component_SHR_ROBUST.ipynb'/'2_Offline_component_SHR_FULL.ipynb' to get the results of offline component. The output is saved in 'results/'.

3. Run the online component of the algorithm

Depending on the candidate approach you choose, you can run '3_Online_component_SEP.ipynb'/'3_Online_component_SHR.ipynb'/'3_Online_component_SHR_CLUSTER.ipynb'/'3_Online_component_SHR_ROBUST.ipynb'/'3_Online_component_SHR_FULL.ipynb' to get the results of offline component. The output is saved in 'results/'.

4. Compare and evaluate different approaches

First run '4_Calculate_OPTIMIZE.ipynb' to get the optimal solution, then run '3_Evaluate.ipynb' to calculate evaluation metrics.

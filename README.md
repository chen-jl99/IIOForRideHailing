# IIOForRideHailing-ICDE2023

This is the demo code of the paper **Two-Sided Instant Incentive Optimization under a Shared Budget in Ride-Hailing Services**.

## Dataset

In the numerical experiment section of our paper, we use the real data as input, which are restricted to access inside Meituan. Here we generate some "fake" data to run the code.

## Usage

*  Set the parameter

The parameters should be first set in `params.py`.

* Generate simulation data

Run `0_Data_generation.ipynb` to generate simulation data, the output data are saved in `data/`.

*  Run the offline component of the algorithm

Depending on the candidate approach you choose, you can run `1_Offline_component_SEP.ipynb`/`1_Offline_component_SHR.ipynb`/`1_Offline_component_SHR_CLUSTER.ipynb`/`1_Offline_component_SHR_ROBUST.ipynb`/`1_Offline_component_SHR_FULL.ipynb` to get the results of offline component. The output is saved in `results/`.

*  Run the online component of the algorithm

Depending on the candidate approach you choose, you can run `2_Online_component_SEP.ipynb`/`2_Online_component_SHR.ipynb`/`2_Online_component_SHR_CLUSTER.ipynb`/`2_Online_component_SHR_ROBUST.ipynb`/`2_Online_component_SHR_FULL.ipynb` to get the results of offline component. The output is saved in `results/`.

*  Compare and evaluate different approaches

First run `3_Calculate_OPTIMIZE.ipynb` to get the optimal solution, then run `3_Evaluate.ipynb` to calculate evaluation metrics.

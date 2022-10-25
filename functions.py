import numpy as np
import random
from scipy.optimize import minimize
from scipy import optimize

def set_seed(seed):
    np.random.seed(seed)
    random.seed(seed)

# solve the Lagrange multiplier for the shared-budget constraint setting
def solve_largrange_multiplier(N, pred_prob, fare, compensation, passenger_incentive_list, driver_incentive_list, eta, B, r):
    
    # initial minimum value
    lambda_left = 0
    # initial maximum value
    lambda_right = max(1/(min(fare)*passenger_incentive_list[1]), 1/(min(compensation)*driver_incentive_list[1]))

    while True:
        
        delta = lambda_right - lambda_left
        lambda_mid = (lambda_left + lambda_right) / 2
        
        if (delta < 1e-4):
            break
        
        # check the result under current midpoint
        h_total = 0

        for n in range(0,N):
            l_best = -np.inf
            for i in range(0, len(passenger_incentive_list)):
                for j in range(0, len(driver_incentive_list)):
                    c = (pred_prob[n,i,j] - r)
                    h = (pred_prob[n,i,j] + r)*(fare[n]*passenger_incentive_list[i]+compensation[n]*driver_incentive_list[j])
                    if eta*fare[n]*(1-passenger_incentive_list[i]) < compensation[n]*(1+driver_incentive_list[j]):
                        if c - lambda_mid * h > l_best:
                            l_best = c - lambda_mid * h
                            h_best = h

            h_total += h_best

        if (h_total < B):
            lambda_right = lambda_mid
        else:
            lambda_left = lambda_mid
    
    print('Finish solving Lagrange multiplier, the constraint function is:', h_total)
    return lambda_mid

# solve the Lagrange multiplier when only passenger-side budget exists
def solve_largrange_multiplier_only_passenger(N, pred_prob, fare, compensation, passenger_incentive_list, driver_incentive_list, eta, B):
    
    lambda_left = 0
    lambda_right = 1/(min(fare)*passenger_incentive_list[1])

    while True:
        
        delta = lambda_right - lambda_left
        lambda_mid = (lambda_left + lambda_right) / 2
        
        if (delta < 1e-4):
            break
        
        h_total = 0

        for n in range(0,N):
            l_best = -np.inf
            j = 0
            for i in range(0, len(passenger_incentive_list)):
                c = pred_prob[n,i,j]
                h = pred_prob[n,i,j]*(fare[n]*passenger_incentive_list[i]+compensation[n]*driver_incentive_list[j])
                if eta*fare[n]*(1-passenger_incentive_list[i]) < compensation[n]*(1+driver_incentive_list[j]):
                    if c - lambda_mid * h > l_best:
                        l_best = c - lambda_mid * h
                        h_best = h

            h_total += h_best

        if (h_total < B):
            lambda_right = lambda_mid
        else:
            lambda_left = lambda_mid
    
    print('Finish solving Lagrange multiplier, the constraint function is:', h_total)
    return lambda_mid

# solve the Lagrange multiplier when only driver-side budget exists
def solve_largrange_multiplier_only_driver(N, pred_prob, fare, compensation, passenger_incentive_list, driver_incentive_list, eta, B):
    
    lambda_left = 0
    lambda_right = 1/(min(compensation)*driver_incentive_list[1])

    while True:
        
        delta = lambda_right - lambda_left
        lambda_mid = (lambda_left + lambda_right) / 2
        
        if (delta < 1e-4):
            break
        
        h_total = 0

        for n in range(0,N):
            l_best = -np.inf
            i = 0
            for j in range(0, len(driver_incentive_list)):
                c = pred_prob[n,i,j]
                h = pred_prob[n,i,j]*(fare[n]*passenger_incentive_list[i]+compensation[n]*driver_incentive_list[j])
                if eta*fare[n]*(1-passenger_incentive_list[i]) < compensation[n]*(1+driver_incentive_list[j]):
                    if c - lambda_mid * h > l_best:
                        l_best = c - lambda_mid * h
                        h_best = h

            h_total += h_best

        if (h_total < B):
            lambda_right = lambda_mid
        else:
            lambda_left = lambda_mid
    
    print('Finish solving Lagrange multiplier, the constraint function is:', h_total)
    return lambda_mid

# solve the Lagrange multiplier when giving the seperate budget constraint setting (both the passenger-side budget and the driver-side budget exist)
def solve_largrange_multiplier_sep(N, pred_prob, fare, compensation, passenger_incentive_list, driver_incentive_list, eta, B, passenger_percentage):
    
    def subproblem_optimization(lambda_1, lambda_2):
        
        h_1_total = 0
        h_2_total = 0

        for n in range(0,N):
            l_best = -np.inf
            for i in range(0, len(passenger_incentive_list)):
                for j in range(0, len(driver_incentive_list)):

                    c = pred_prob[n,i,j]
                    h_1 = pred_prob[n,i,j]*fare[n]*passenger_incentive_list[i]
                    h_2 = pred_prob[n,i,j]*compensation[n]*driver_incentive_list[j]
                    if eta*fare[n]*(1-passenger_incentive_list[i]) < compensation[n]*(1+driver_incentive_list[j]):
                        if c - lambda_1 * h_1 - lambda_2 * h_2 > l_best:
                            l_best = c - lambda_1 * h_1 - lambda_2 * h_2
                            h_1_best = h_1
                            h_2_best = h_2

            h_1_total += h_1_best
            h_2_total += h_2_best
            
        return h_1_total, h_2_total
    
    lambda_1_left = 0
    lambda_2_left = 0
    lambda_1_right = 1/(min(fare)*passenger_incentive_list[1])
    lambda_2_right = 1/(min(compensation)*driver_incentive_list[1])

    n_iter = 0
    
    while True:
        
        n_iter += 1
        
        delta_1 = lambda_1_right - lambda_1_left
        delta_2 = lambda_2_right - lambda_2_left
        
        lambda_1 = (lambda_1_left + lambda_1_right) / 2
        lambda_2 = (lambda_2_left + lambda_2_right) / 2
        
        if (delta_1 < 1e-4 and delta_2 < 1e-4):
            break
        
        h_1_total_left, h_2_total_left = subproblem_optimization(lambda_1_left, lambda_2_left)
        h_1_total_right, h_2_total_right = subproblem_optimization(lambda_1_right, lambda_2_right)
        h_1_total, h_2_total = subproblem_optimization(lambda_1, lambda_2)

        if (n_iter%2==0):
            
            if (h_1_total_left < B * passenger_percentage and h_1_total_right < B * passenger_percentage):
                lambda_1_right = lambda_1_left
                lambda_1_left = max(0, lambda_1_right - delta_1)
                
            elif (h_1_total_left > B * passenger_percentage and h_1_total_right > B * passenger_percentage):
                lambda_1_left = lambda_1_right
                lambda_1_right = lambda_1_left + delta_1   
                
            elif (h_1_total < B * passenger_percentage):
                lambda_1_right = lambda_1
                
            else:
                lambda_1_left = lambda_1
                
        else:   

            if (h_2_total_left < B * (1-passenger_percentage) and h_2_total_right < B * (1-passenger_percentage)):
                lambda_2_right = lambda_2_left
                lambda_2_left = max(0, lambda_2_right - delta_2)
                
            elif (h_2_total_left > B * (1-passenger_percentage) and h_2_total_right > B * (1-passenger_percentage)):
                lambda_2_left = lambda_2_right
                lambda_2_right = lambda_2_left + delta_2     
                
            elif (h_2_total < B * (1-passenger_percentage)):
                lambda_2_right = lambda_2
                
            else:
                lambda_2_left = lambda_2
                
    print('Finish solving Lagrange multiplier, the constraint function is:', h_1_total, h_2_total)
    return lambda_1, lambda_2
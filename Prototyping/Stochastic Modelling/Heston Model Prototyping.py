import numpy as np
import matplotlib.pyplot as plt


#First stochastic differential equation
def Pricing_Equation(num_of_paths,start_price,mu,k,theta,sigma,r,time_duration,time_steps):
    dt = time_duration/time_steps
    t = np.linspace(0, time_duration, time_steps + 1)
    Vt = Volatility_Equation(num_of_paths,start_price,mu,k,theta,sigma,r,time_duration,time_steps,dt)
    wiener_process = np.random.multivariate_normal(size=(num_of_paths,r,time_steps))
    wiener_process = np.concatenate((np.zeros((num_of_paths, 1)) , wiener_process), axis=1)
    cumulative_sum = np.cumsum((mu - 0.5 * Vt**2) * dt + np.sqrt(Vt) * wiener_process, axis=1)
    current_price = start_price * np.exp(cumulative_sum) # price generated

    return t , current_price


#parameters:
# mu is the drift coefficient
# k is the rate of reversion of volatility to long-term mean
# theta is the long-term mean level of variance
# sigma is the volatility of variance
# r is the covariance/correlation coefficient between the wiener processes


#differential modelling inequality
def Volatility_Equation(num_of_paths,start_price,mu,k,theta,sigma,r,time_duration,time_steps,dt):
    
    wiener_process = np.random.multivariate_normal(size=(num_of_paths,r,time_steps))
    wiener_process = np.concatenate((np.zeros((num_of_paths, 1)) , wiener_process), axis=1)
    cumulative_sum = np.cumsum((mu   - 0.5 * Vt**2) * dt + np.sqrt(Vt) * wiener_process, axis=1)
    current_price = start_price * np.exp(cumulative_sum) # price generated

    
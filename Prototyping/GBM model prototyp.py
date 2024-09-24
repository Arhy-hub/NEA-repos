import numpy as np
import matplotlib.pyplot as plt

#equation function
def geometric_brownian_motion(number_of_paths,start_price,drift_coefficient,volatility,time_duration,time_steps):
    dt = time_duration/time_steps #change in time
    t = np.linspace(0, time_duration,time_steps + 1) #equal spaced time intervals
    wiener_process = np.random.normal(size=(number_of_paths, time_steps)) * np.sqrt(dt) #generating wiener process
    wiener_process = np.concatenate((np.zeros((number_of_paths, 1)) , wiener_process), axis=1)
    cumulative_sum = np.cumsum((drift_coefficient - 0.5 * volatility**2) * dt + volatility * wiener_process, axis=1)
    current_price = start_price * np.exp(cumulative_sum) # price generated

    return t , current_price

#parameters
number_of_paths = 100000
start_price = 5218.19
drift_coefficient = 0.0000000005
volatility = 1
time_duration = 6
time_steps = 24

t , current_price = geometric_brownian_motion(number_of_paths, start_price, drift_coefficient, volatility, time_duration, time_steps)
final_prices = current_price[:, -1]
mean_final_price = np.mean(final_prices)

#displaying the information
print(f"Mean final price: {mean_final_price:.2f}")

plt.figure(figsize=(10,6))
plt.title('Geometric Brownian Motion - Monte Carlo Simulation')
plt.xlabel('Time')
plt.ylabel('Stock Price')

for i in range(min(number_of_paths, 10000)):
    plt.plot(t, current_price[i], label='_nolegend_')
mean_path = np.mean(current_price, axis=0)
plt.plot(t, mean_path, 'b-', lw=2, label='Mean Path', alpha=0.8)
plt.legend()
plt.grid(True)
plt.show()
import numpy as np
import matplotlib.pyplot as plt




#parameters
St = 42.98 #initial price
mu = 2.4323 #drift coefficient
sigma = 0.542 #volatility
time_duration = 1 #forecasting length of time
time_steps = 365 #number of steps e.g. interval
num_paths = 1000 #number of pathways evaluated for monte carlo sim

def GBM(St,mu,sigma,time_duration,time_steps,k):
    dt = time_duration/time_steps
    t = k*dt
    Wt = np.random.normal(0,t)
    St = St*np.exp((mu-(sigma**2)/2)*dt + sigma*Wt)
    return  St


values = []
time = []
for a in range(0,num_paths):
    path = []
    St_current = St
    for b in range(0,time_steps):
        St_current = GBM(St,mu,sigma,time_duration,time_steps,b)
        path.append(St_current)
    values.append(path)
   

values =np.array(values)
final_prices = values[: ,-1]
mean_final_price = np.mean(final_prices)
time = np.linspace(0,time_duration,time_steps)

print("Mean final price is ",mean_final_price)

plt.title('Geometric Brownian Motion Model - Monte Carlo')
plt.xlabel('Time')
plt.ylabel('Stock Price')

for i in range (0 , num_paths):
    plt.plot(time, values[i], label='_nolegend_')

plt.show()
mean_path = np.mean(values, axis=0)
plt.plot(time, mean_path, 'b-', lw=2, label='Mean Path', alpha=0.8)
plt.legend()
plt.show()
plt.hist(final_prices)
plt.show()










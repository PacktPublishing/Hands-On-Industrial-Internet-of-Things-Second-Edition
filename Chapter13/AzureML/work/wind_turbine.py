import pandas as pd 

import matplotlib.pyplot as plt 
import numpy as np 


def wind_turbine_model(x): 
    # cut-in speed vs cut-out speed 
    if x<4.5 or x>21.5: 
        return 0.0 
    # standard operability 
    return 376.936 - 195.8161*x + 33.75734*x**2 - 2.212492*x**3 + 0.06309095*x**4 - 0.0006533647*x**5 

reference_power = [wind_turbine_model(x) for x in range(0,30)] 

# show data and reference 
fig, ax = plt.subplots() 
ax.plot(reference_power,'k') 
ax.set_xlabel('wind speed (m/s)') 
ax.set_ylabel('power (kW)') 
plt.show() 
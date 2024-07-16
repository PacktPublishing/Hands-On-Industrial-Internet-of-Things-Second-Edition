import numpy as np
import matplotlib.pyplot as plt
def moving_average(data, window_size): 
    window = np.ones(int(window_size))/float(window_size)  
    return np.convolve(data, window, 'same') 

def search_anomalies(y, window_size, sigma=1.0): 
    avg = moving_average(y, window_size).tolist() 
    residual = y - avg 
    
    # Calculate the variation in the distribution of the residual 
    std = np.std(residual) 

    anomalies=[] 
    i=int(window_size)

    for y_i, avg_i in zip(y, avg): 
        if (y_i > avg_i + (sigma*std)) | (y_i < avg_i - (sigma*std)):  
            anomalies.append([i, y_i]) 
        i=i+1 
    
    return {'std': round(std, 3), 'anomalies': np.array(anomalies)}

def plot_anomalies(t, y, t_events, y_events, color='g'):
    plt.plot(t,y, color)
    plt.plot(t_events, y_events, 'or')

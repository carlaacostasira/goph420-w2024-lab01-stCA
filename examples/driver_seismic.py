import numpy as np
import matplotlib.pyplot as plt

"""Loading the data from the s_wave_data.txt

    Inputs
    ------
    time : array_like 
        in seconds [s]
    velocity : array_like
        in milimeter/seconds [mm/s]
       
    Returns
    -------
    Plot of the raw data

    Raises
    ------
    ValueError
        
    """

data = np.loadtxt(r"C:/Users/carla/Repos/goph420-w2024-lab01-stCA/examples/s_wave_data.txt")


time = data[:,0] # First column of data (time)
velocity = data[:,1] # Second column of data (velocity)

max_abs_velocity = np.max(np.abs(velocity)) # Calculating the Max Absolute value of the velocity
threshold_value =  0.005 * max_abs_velocity #Calculation the max velocity greater than 0.5%
last_index = np.max(np.where(velocity > threshold_value)) # Find the last index where velocity is greater than 0.5%

T = time[last_index] 

T_index = np.where(time == T)[0][0]

# Create new arrays for time and velocity up to T
time_up_to_T = time[:T_index+1]
velocity_up_to_T = velocity[:T_index+1]

#plt.plot(time, velocity)
#plt.xlabel('Time (s)')
##plt.ylabel('Velocity (mm/s)')
#plt.title('Raw Data Plot')
#plt.show()

print (time_up_to_T)
print (velocity_up_to_T)

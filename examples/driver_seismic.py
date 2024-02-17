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
last_index = np.max(np.where(velocity > threshold_value))

# Get the corresponding time value
T = time[last_index]
velocity_2 = np.array()
velocity_2 = velocity[:last_index +  1]

time_2_list = [] 

# Iterate over the time array
for i in range(len(time)):
    # If the current time value is less than or equal to T, append it to the list
    if time[i] <= T:
        time_2_list.append(time[i])
    # Otherwise, break the loop because we've reached the end of the desired range
    else:
        break

# Convert the list to a NumPy array
time_2 = np.array(time_2_list)

#plt.plot(time, velocity)
#plt.xlabel('Time (s)')
##plt.ylabel('Velocity (mm/s)')
#plt.title('Raw Data Plot')
#plt.show()

print (time_2)

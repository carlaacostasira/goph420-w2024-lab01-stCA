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

data = np.loadtxt(r"C:/Users/carla/Repos/goph420-w2024-lab01-stCA/examples/s_wave_data.txt") #Loading Data from .txt


time = data[:,0] # First column of data (time)
velocity = data[:,1] # Second column of data (velocity)

max_abs_velocity = np.max(np.abs(velocity)) # Calculating the Max Absolute value of the velocity
threshold_value =  0.005 * max_abs_velocity # Calculating the Max velocity greater than 0.5%
last_index = np.max(np.where(velocity > threshold_value)) #Obtaining the index where that value is located in the velocity column

T = time[last_index] # Getting the corresponding time value T within the criterion
velocity_2 = velocity[:last_index +  1] # Creating a new veloccity array from the index 0 to last index +1
velocity_2 = np.square(velocity_2)

time_2_list = [] # Creating a list that will store the values for the time
for i in range(len(time)):
    if time[i] <= T: # Iterating over the column time and appending the numbers where time value is less than or equal to T
        time_2_list.append(time[i])
    else:
        break

time_2 = np.array(time_2_list) # Converting the list to a NumPy array as time_2

plt.plot(time_2, velocity_2)
plt.xlabel('Time (s)')
plt.ylabel('Velocity (mm/s)')
plt.title('Raw Data Plot')
plt.show()
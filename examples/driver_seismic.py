import numpy as np
import matplotlib.pyplot as plt
import goph420_lab01
from goph420_lab01 import integration as itg

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

max_abs_velocity = np.abs(np.max(velocity)) # Calculating the Max Absolute value of the velocity
threshold_value =  0.005 * max_abs_velocity # Calculating the Max velocity greater than 0.5%
last_index = np.max(np.where(velocity > threshold_value)) #Obtaining the index where that value is located in the velocity column

T = time[last_index] # Getting the corresponding time value T within the criterion
velocity_2 = velocity[:last_index +  1] # Creating a new veloccity array from the index 0 to last index +1
velocity_square = np.square(velocity_2) # Calculating velocity square

time_2_list = [] # Creating a list that will store the values for the time until T
for i in range(len(time)):
    if time[i] <= T: # Iterating over the column time and appending the numbers where time value is less than or equal to T
        time_2_list.append(time[i])
    else:
        break

time_2 = np.array(time_2_list) # Converting the list to a NumPy array as time_2

step_size = np.array([1, 2, 4, 8, 30, 50, 100]) #Defining the different intervals that will be performed

Delta_t = np.zeros (len(step_size)) # Creating an empty array to store the delta t
I_TrapRule = np.zeros(len(step_size)) # Creating an empty array to store the integration values for Trap Rule
I_SimpRule = np.zeros(len(step_size)) # Creating an empty array to store the integration values for Simp Rule
eps_a_trap = np.zeros(len(step_size)) # Creating an empty array to store the approx relative error for Trap Rule
eps_a_simp = np.zeros(len(step_size)) # Creating an empty array to store the approx relative error for Simp Rule. dtype=float

for i in range(len(step_size)):
    Time = time_2[0:-1:step_size[i]] # Getting time values for the integrations. From 0 to T (criterion) w/ step sizes given by the intervals array 
    Delta_t[i]= Time[1] - Time[0]
    Velocity = velocity_square[0:-1:step_size[i]] # Getting velocity square values for the integrations

    I_TrapRule[i] = integration.integrate_newton(Time, Velocity, 'trap')
#    I_SimpRule[i] = integration.integrate_newton(Time, Velocity, 'simp')
    break

plt.plot(time_2, velocity_2)
plt.xlabel('Time (s)')
plt.ylabel('Velocity (mm/s)')
plt.title('Raw Data Plot')
plt.show()
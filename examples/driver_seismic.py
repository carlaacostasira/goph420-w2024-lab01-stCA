import numpy as np
import matplotlib.pyplot as plt
from goph420_lab01.integration import integrate_newton

# """Loading the data from the s_wave_data.txt

#     Inputs
#     ------
#     time : array_like 
#         in seconds [s]
#     velocity : array_like
#         in milimeter/seconds [mm/s]
       
#     Returns
#     -------
#     Plot of the raw data

#     Raises
#     ------
#     ValueError
        
#     """

data = np.loadtxt(r"C:/Users/carla/Repos/goph420-w2024-lab01-stCA/examples/s_wave_data.txt") #Loading Data from .txt

time = data[:,0] # First column of data (time)
velocity = data[:,1] # Second column of data (velocity)

max_abs_velocity = np.abs(np.max(velocity)) # Calculating the Max Absolute value of the velocity
threshold_value =  0.005 * max_abs_velocity # Calculating the Max velocity greater than 0.5%
last_index = np.max(np.where(velocity > threshold_value)) #Obtaining the index where that value is located in the velocity column

T = time[last_index] # Getting the corresponding time value T within the criterion
velocity_2 = velocity[:last_index + 1] # Creating a new veloccity array from the index 0 to last index +1
velocity_square = np.square(velocity_2) # Calculating velocity square

time_2_list = [] # Creating a list that will store the values for the time until T
for i in range(len(time)):
    if time[i] <= T: # Iterating over the column time and appending the numbers where time value is less than or equal to T
        time_2_list.append(time[i])
    else:
        break

time_2 = np.array(time_2_list) # Converting the list to a NumPy array as time_2

plt.plot(time, velocity)
plt.plot(T, 0,'ro', label="Value T = 6.46 s") 
plt.xlabel('Time (s)')
plt.ylabel('Velocity (mm/s)')
plt.title('Raw Data Plot')
plt.legend(loc="upper right")
plt.show()

print(velocity_2[646])

step_size = np.array([1, 2, 4, 8, 17, 30, 53, 100]) #Defining the different intervals that will be performed

I_trap = np.empty(len(step_size)) # Creating an empty array to store the integration values for Trap Rule
I_simp = np.empty(len(step_size)) # Creating an empty array to store the integration values for Simp Rule
eps_a_trap = np.empty(len(step_size)) # Creating an empty array to store the approx relative error for Trap Rule
eps_a_simp = np.empty(len(step_size)) # Creating an empty array to store the approx relative error for Simp Rule. dtype=float

expected_I = (1/T)*((((velocity_2[646])**3)/3-((velocity_2[0])**3)/3)) #Value 1.94766E-10

for i in range(len(step_size)):
    Time = time_2[0:-1:step_size[i]] # Getting time values for the integrations. From 0 to T (criterion) w/ step sizes given by the intervals array 
    Velocity = velocity_2[0:-1:step_size[i]] # Getting velocity square values for the integrations

    I_trap[i] = integrate_newton(Time, Velocity, 'trap')
    eps_a_trap[i] = I_trap[i] - I_trap[i-1] / I_trap[i]
    I_simp[i] = integrate_newton(Time, Velocity, 'simp')
    eps_a_simp[i] = I_simp[i] - I_simp[i-1] / I_simp[i]
    
    break
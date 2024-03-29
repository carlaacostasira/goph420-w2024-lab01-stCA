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

max_abs_velocity = np.max(np.abs(velocity)) # Calculating the Max Absolute value of the velocity
threshold_value =  0.005 * max_abs_velocity # Calculating the Max velocity greater than 0.5%
last_index = np.max(np.where(np.abs(velocity) > threshold_value)) #Obtaining the index where that value is located in the velocity column

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
plt.plot(T, 0,'ro', label="Value T = 6.77 s")
plt.xlabel('Time (s)')
plt.ylabel('Velocity (mm/s)')
plt.title('Raw Data Plot')
plt.legend(loc="upper right")
plt.savefig('C:/Users/carla/Repos/goph420-w2024-lab01-stCA/figures/raw_data_plot.png', format='png')
plt.show()

step_size = np.array([1, 2, 4, 8, 15, 30, 101]) #Defining the different intervals that will be performed
delta_t = np.empty(len(step_size))

#num_points = [len(time_2[::step]) for step in step_size]

for i in range(len(step_size)):
    # Correctly calculate the differences with the step size
    differences = time_2[step_size[i]::step_size[i]] - time_2[:-step_size[i]:step_size[i]]
    # Store the difference for the first element of the differences array
    # If there are no differences (i.e., the step size is too large), store 0
    delta_t[i] = differences[0] if differences.size > 0 else 0

I_trap = np.empty(len(step_size)) # Creating an empty array to store the integration values for Trap Rule
I_simp = np.empty(len(step_size)) # Creating an empty array to store the integration values for Simp Rule
eps_a_trap = np.empty(len(step_size)) # Creating an empty array to store the approx relative error for Trap Rule
eps_a_simp = np.empty(len(step_size)) # Creating an empty array to store the approx relative error for Simp Rule. dtype=float

for i in range(len(step_size)):
    Time = time_2[::step_size[i]] # Getting time values for the integrations. From 0 to T (criterion) w/ step sizes given by the intervals array
    Velocity = velocity_square[::step_size[i]] # Getting velocity square values for the integrations

    I_trap[i] = (integrate_newton(Time,Velocity,'trap'))/T
    I_simp[i] = (integrate_newton(Time,Velocity,'simp'))/T

    # if i == 3: # Check what the values are for the 
    #     print(Time)

for i in range(len(step_size - 1)):
    eps_a_trap[i] = np.abs(I_trap[i] - I_trap[i-1] / I_trap[i])
    eps_a_simp[i] = np.abs(I_simp[i] - I_simp[i-1] / I_simp[i])

error_t = np.empty(len(step_size)) #Calculating the order of the truncation error
for i in range(len(step_size - 1)):
    error_t[i] = delta_t[i]**3

plt.plot(delta_t, eps_a_trap, label="trap |\u03B5_a|", marker='o')
plt.plot(delta_t, eps_a_simp, label="simp |\u03B5_a|",  marker='o')
plt.xscale("log")
plt.yscale("log")
plt.xlabel('Sampling interval, $\Delta$t (s)')
plt.ylabel('Approx. Relative Error, |\u03B5|')
plt.title('Convergence plot')
plt.legend(loc="upper left")
plt.savefig('C:/Users/carla/Repos/goph420-w2024-lab01-stCA/figures/convergence_plot.png', format='png')
plt.show()



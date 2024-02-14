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
    numpy.ndarray, shape=(1, order+1)
        The array of shape function values

    Raises
    ------
    ValueError
        If s cannot be converted to float.
        If order is not in [1].
    """

data = np.loadtxt('C:\Users\carla\Repos\goph420-w2024-lab01-stCA/s_wave_data.txt', delimiter='\t', dtype=float)


time = data[:,  0] # First column of data (time)
velocity = data[:,  1] # Second column of data (velocity)

plt.plot(time, velocity)
plt.xlabel('Time (s)')
plt.ylabel('Velocity (mm/s)')
plt.title('Raw Data Plot')
plt.show()

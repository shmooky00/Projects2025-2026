import numpy as np

# Define our matrices

H = np.array([[1,0]])       # Measurement Function

# Next state function (transition function)
F = np.array([[1 ,1],
              [0, 1]])

# External motion
u = np.array([[0],
              [0]])

# Measurement Uncertainty
R = np.array([[1]])

# Identity Matrix
I = np.array([[1 ,0],
              [0, 1]])

def kalman(x,P, meas):
    '''
    Kalman filter implementation in one dimension where

    x - initial position
    P - initial uncertainty
    meas - initial measurements captured by the sensors
    '''

    # video to help understand how to implement kalman in python: https://www.youtube.com/watch?v=m5Bw1m8jJuY&t=1793s
    # used this for predict and update function structure, used slide 17 fomula but code form: https://machinelearningspace.com/object-tracking-python/
    def predict(x, P):
        x = np.dot(F, x) + u
        P = np.dot(np.dot(F, P), F.T)
        return x, P

    def update(x, P, measurement):
        y = measurement - np.dot(H, x)
        S = np.dot(np.dot(H, P), H.T) + R
        K = np.dot(np.dot(P, H.T), np.linalg.inv(S))
        x = x + np.dot(K, y)
        P = np.dot((I - np.dot(K, H)), P)
        return x, P
    #end of reference
    

    # Loop through each measurement
    for n in range(len(meas)):

        # Noise factor
        g = [0]
        #g = np.random.normal(0,0.005,1)

        # TODO: Implement equations from the lecture to create a working filter

        x, P = predict(x, P)
        x, P = update(x, P, meas[n] + g[0]) 

    return x, P

#
# Run the Kalman Filter
#

    # Initial position
x = np.array([[0], [0]])

# Initial uncertainty
P = np.array([[1000 ,0],
              [0, 1000]])

measurements = [1,2,3]

x, P = kalman(x, P, measurements)

# Print the results
print(f'x: {x}')
print(f'P: {P}')

'''
x: [[3.99966644]  [0.99999983]]

P: [[2.33189042 0.99916761]
    [0.99916761 0.49950058]]

'''
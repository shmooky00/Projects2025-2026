import numpy as np

# TODO: Student defined matrices (H, F, R, etc.) go here

# measurement function, takes position from state 
H = np.array([[1, 0, 0, 0],    
              [0, 0, 1, 0]])   

# transition function, changes over time
F = np.array([[1, 1, 0, 0],    
              [0, 1, 0, 0],    
              [0, 0, 1, 1],    
              [0, 0, 0, 1]])   

# external motion, none so all 0s
u = np.array([[0],
              [0],
              [0],
              [0]])

# measurement uncertainty
R = np.array([[1, 0],
              [0, 1]])

# id matrix
I = np.array([[1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 1]])

def kalman(x,P, meas):

    #imported from the 1d file, adjusted for 2d in the loop
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

    # Loop through each measurement
    for n in range(len(meas)):
        
        # TODO: Student code goes here (includeing the noise)

        # Process Measurement
        # Process Prediction (Motion)

        # standard guassian noise
        g = np.random.normal(0,.5,2)
        # implement g for when uncommented
        meas[n] = [meas[n][0] + g[0], meas[n][1] + g[1]]

        x, P = predict(x, P)
        x, P = update(x, P, np.array([[meas[n][0]], [meas[n][1]]]))
        
    return x, P


# Define our matrices
measurements = [[1.,1.],[3.,2.],[5.,3.], [7.,4.]]

# looked at the demo_kalman function for inspo, made it my own: https://stackoverflow.com/questions/13901997/kalman-2d-filter-in-python
#intial state
x = np.array([[0], [0], [0], [0]])

# initial uncertainty
P = np.array([[1000, 0, 0, 0],
              [0, 1000, 0, 0],
              [0, 0, 1000, 0],
              [0, 0, 0, 1000]])
#end of inspo

# Run the Kalman Filter
x, P = kalman(x, P, measurements)

# Print the results
print(f'x: {x}')
print(f'P: {P}')

'''
x-pos: 8.99903727
x-vel: 2.00001246
y-pos: 4.99951817
y-vel: 1.00001211

Final P: [[1.46050553 0.48956966 1.46050553 0.48956966]
    [0.48560331 0.19673342 0.48560331 0.19673342]
    [1.47228625 0.49254838 1.47228625 0.49254838]
    [0.48078137 0.19473381 0.48078137 0.19473381]]
'''
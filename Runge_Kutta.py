from__future__ import division
import numpy
import pylab


###### Global variables:
m = 1   # mass of 1
k = 1   # spring constant
x_0 = 1 # initial position is 1 meter
v_0 = 0 # initial velocity is zero meters/second
dt_global = 0.001


def Runge_Kutta(f, t, x, dt):
    k1 = f(x, t)*dt
    k2 = f(x + (k1/2),t + (dt/2))*dt
    k3 = f(x + (k2/2), t + (dt/2))*dt
    k4 = f(x + k3, t + dt)*dt
    state = x + (1/6.)*(k1 + 2*k2 + 2*k3 + k4) #If you leave the fraction as integers, this whole line goes to zero
    return state
    
def mass_spring_system(state, t):
    dx_dt = state[1]
    dv_dt = -(k/m)*state[0]
    pos = numpy.array([dx_dt, dv_dt])
    return pos


t_end = 10
t = [0]
state = [numpy.array([x_0,v_0])]
while t[-1] <= t_end:
    state.append(Runge_Kutta(mass_spring_system, t[-1], state[-1], dt_global))
    t.append(t[-1] + dt)
    
position = numpy.array(state)[:,0]   
velocity = numpy.array(state)[:,1]
    
pylab.plot(t, position, label="Position")
pylab.plot(t, velocity, label="Velocity")

pylab.xlabel('Time (note: dt = 0.001)')
pylab.ylabel('Amplitude from equilibrium')
pylab.title('Simple Harmonic Oscillator')
pylab.grid(True)
pylab.legend()
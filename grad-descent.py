# Alaina Kafkes
# Simple Gradient Descent Algorithm for Vector/Matrix Quantities
# 6 October 2015

# Test Function: g(w) = w'w    (where w = 10 x 1 matrix)

from pylab import *
from mpl_toolkits.mplot3d import Axes3D

## Gradient Descent ##
# Prints the value of the function g(w) for 100 iterations
# Shows a plot of function value g(w) vs. iteration
def gradient_descent(w0,alpha):
	w = w0
	g_path = []
	w_path = []
	w_path.append(w)
	g_path.append(dot(w.T,w))
	grad = 1
	iter = 1
	max_its = 100
	
	while iter <= max_its: # no convergence criterion
		grad = 2*w
		w = w - alpha*grad
		w_path.append(w)
		g_path.append(dot(w.T,w))
		s = dot(grad.T,grad)/2
		ans = 'For iteration ' + str(int(iter)) + ' the function value is ' + str(float(dot(w.T,w)))
		print(ans)
		iter+= 1
	
	s = dot(grad.T,grad)/2
	ans = 'The **FINAL** function value is ' + str(float(dot(w.T,w)))
	print(ans)
	
	# Convergence?
	plot(asarray(g_path))
	show()
	
	return (w_path,g_path)
    
def main():
    # alpha = 0.001
    print("For alpha = 0.001: " + "\n")
    alpha = 0.001 								  # step length parameter
    w0 = array([10,10,10,10,10,10,10,10,10,10])
    w_path,g_path = gradient_descent(w0,alpha)    # performs gradient descent
    print("\n\n")

    # alpha = 0.01
    print("For alpha = 0.01: " + "\n")
    alpha = 0.01
    w0 = array([10,10,10,10,10,10,10,10,10,10])
    w_path,g_path = gradient_descent(w0,alpha)
    print("\n\n")
    
    # alpha = 1.001
    print("For alpha = 1.001: " + "\n")
    alpha = 1.001
    w0 = array([10,10,10,10,10,10,10,10,10,10])
    w_path,g_path = gradient_descent(w0,alpha)
    print("\n\n")
    
main()
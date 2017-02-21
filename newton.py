# Alaina Kafkes
# Newton's Method Algorithm

# Test Function: g(w) = log(1+e^(w'w))    (where w = 10 x 1 matrix)

from pylab import *
from mpl_toolkits.mplot3d import Axes3D
from numpy import *
from matplotlib.pyplot import *

## Hessian ##
# Returns the Hessian of a function
def hessian(w):
	a = (1 + exp(dot(w.T,w))) ** -2
	b = 4 * exp(dot(w.T,w)) * outer(w,w)
	c = 2 * exp(dot(w.T,w)) * (1 + exp(dot(w.T,w))) * identity(size(w))
	return a*(b+c)

## Gradient ##
# Returns the gradient of a function
def kgrad(w):
	a = (1/(1+e**(dot(w.T,w))))*(e**(dot(w.T,w)))*2*w
	return a

## Objective Function ##
# Returns the objective function value	
def obj(w):
	a = log(1+e**(dot(w.T,w)))
	return a

## Newton's Method ##
# Prints minimum value of fxn given an initial w0
def newton(w0):
	w = w0
	fxn = obj(w)
	grad_eval = 1
	
	g_path = []
	w_path = []
	w_path.append(w)
	g_path.append(fxn)
	
	hess_eval = 1
	iter = 1
	max_its = 100
	epsilon = 10**-3

	while linalg.norm(grad_eval) > epsilon and iter <= max_its:
		# maximum iterations and convergence criteria
		grad_eval = kgrad(w)
		
		hess_eval = hessian(w)
		
		w = w - linalg.inv(hess_eval).dot(grad_eval)
		
		w_path.append(w)
		g_path.append(obj(w))
		
		iter+= 1

	# Convergence?
	plot(asarray(g_path))
	show()
	
	print("The minimum function value for g(w) lies at\n" + str(float(obj(w))))
	
	return (w,w_path,g_path)
	
def main():
	w0 = array([1,1,1,1,1,1,1,1,1,1])
	w,w_path,g_path = newton(w0)			# performs newton's method

main()		
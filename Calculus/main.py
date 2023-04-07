"""This code is to determine the slope of x1 function at x1 given point"""
import math


# TODO-1: Define Get Derivative function
def get_derivative(func, x1):
    """Get derivative result (slope/rate of change) of any function t given point x1"""
    h = 0.00000001  # Set this value as small as possible
    d = (func(x1 + h) - func(x1)) / h
    return d


# TODO-2: Define custom math function
def parabola(a):
    """Returns parabolic value for given x1"""
    return a ** 2


# TODO-3: Define custom math function
def polynomial(a):
    """Polynomial function """
    return 5*(a**3) - (a**2)/3 + a + 8


# TODO-4: Define custom math function
def complex_function(a):
    """Custom complex function"""
    return 5*(math.e**3) - math.log(a, 2)


# TODO-x: Printing output as per requirement
x = int(input("Enter value of x to calculate slope at given x : "))
print(f"Slope of Parabola at x={x} is, {get_derivative(parabola, x)}")
print(f"Slope of Polynomial at x={x} is, {get_derivative(polynomial, x)}")
print(f"Slope of Complex Function at x={x} is, {get_derivative(complex_function, x)}")

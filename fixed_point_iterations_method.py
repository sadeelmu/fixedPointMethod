"""
The basic idea behind the Fixed Point Method
A numerical method called the Fixed Point Method is used to approximate solutions to transcendental and algebraic equations. 
The fixed point approach is used when solving cubic, bi-quadratic, and transcendental equations becomes extremely exhausting.
 
The fixed-point method revolves around identifying points in a function where the value of the function remains unchanged when the function is applied. 
These points are referred to as fixed points, and mathematically, a number p is considered a fixed point for a given function g if g(p)=p.

The Fixed-Point Theorem states that under certain conditions (The Contraction Theorem conditions), 
if a function g is continuous and the image of x has to be in the closed interval [a,b], then it has at least one fixed point."""

"""
The step-by-step algorithm of Fixed Point Method.

To solve a Fixed Point Method, we must apply the following algorithm:

First, we must note down that with the Fixed Point Method we must answer the following three questions:

1. When does the function have a fixed point?
2. How can we calculate this Fixed Point?
3. What is the relation between the Fixed Point and the Root?

Let us go further into each step of the Fixed Point Method algorithm:

 1. When does the function have a fixed point?
The code must find out if the function satisfy the contraction theorem.

The contraction theorem states that:
Given that [a,b] is the range given in the function g(x)
The function g(x) must satisfy the following conditions: 
1. a function g(x) must be continuous over closed interval [a,b].
2. for every x in the closed interval [a,b], the image of x has to be in the closed interval [a,b].
There is a third condition to determine if the Fixed Point is unique:
If the function satisfied the contraction theorem, determine if the Fixed Point is unique or not. 
To satisfy uniqueness, the fixed point is unique if there exists a constant k.
We find k by checking if the derivative of the function is increasing or decreasing.
If increasing we take the maximum of the range and substitute into the derivative of the function, the image will be k.
If decreasing we take the minimum of the range and substitute into the derivative of the function, the image will be k.
we have to find k and ensure k is between 0 and 1.


2. How can we calculate this Fixed Point?

Use the Fixed Point Theorem.
The Fixed Point Theorem states. 
Let g(x) be a function that satisfies the contraction theorem on range [a,b]. Let P be the fixed point of g(x) in [a,b]. Let P0 be any point in [a,b]. 
Then the sequence Pn+1n = g(Pn), n = 0, 1, 2... converges to The Fixed Point P.

The Error Formulas to find number of iterations (ONLY WHEN TOLERANCE/ACCURACY NOT GIVEN):

|Pn - P| <= (k^n) * max {P0 - a, b - P0} where n = 1, 2, ...
|Pn - P| <= ((k^n)/(1-k)) * |P1 - P0| where n = 2, 3, ....

3. What is the relation between Fixed Point and Root?

To find the root of the original function g(x), we do the following:

We use our original function g(x) to deduce a new function h(x), where h(x) is g(x) rewritten.
Thereafter, we ensure that h(x) satisfies the basic contraction theorem. To clarify, h(x) must satisfy the following conditions:
1.A function h(x) must be continuous over closed interval [a,b].
2. For every x in the closed interval [a,b], the image of x must belong to the closed interval [a,b].

If it does not satisfy the above conditions, we must use g(x) to deduce a new h(x).

Then, the Fixed Point Method is applied onto the h(x) which satisfies the basic contraction theorem. The fixed point of h(x) is the root of g(x). 

Thus, the relation between the fixed point and the root, the fixed point of h(x) is the root of g(x). 

Note that a function h(x) might not have a unique fixed point. 
"""

"""
This code solves any nonlinear equation using Fixed Point Method
By assuming that the functions inputted by the user statisfy the Contraction Theorem, and all inputs are avaliable and given by user.
We apply the Fixed Point method to transform the problem of finding a root into finding a fixed point.

The Fixed Point method transforms the problem of finding a root into finding a fixed point by doing the following:

We use our original function g(x) to deduce a new function h(x), where h(x) is g(x) rewritten. Thereafter, we ensure that h(x) satisfies the basic contraction theorem. To clarify, h(x) must satisfy the following conditions:

For a given range [a,b] of the function h(x). 
A function h(x) must be continuous over closed interval [a,b].
For every x in the closed interval [a,b], the image of x must belong to the closed interval [a,b].

If it does not satisfy the above conditions, we must use g(x) to deduce a new h(x).

Then, the Fixed Point Method is applied onto the h(x) which satisfies the basic contraction theorem. The fixed point of h(x) is the root of g(x). 

Thus, the relation between the fixed point and the root, the fixed point of h(x) is the root of g(x). 

So we use the Fixed Point Theorem to find the fixed point of h(x), thus finding the root of our original function g(x)
Where the Fixed Point Theorem states that
let g(x) be a function that satisfies the contraction theorem on range [a,b]. Let P be the fixed point of g(x) in [a,b]. Let P0 be any point in [a,b]. 
Then the sequence Pn+1n = g(Pn), n = 0, 1, 2... converges to The Fixed Point P.

In our code, the sequence is applied in the for loop, where the for loop continues until max iterations are reached or the accuracy required is reached. 
"""

def fixed_point_iteration(h, initial_guess, tol, max_iter):
    """
    Implement Fixed Point Iteration method to find the fixed point of the function g.
    The fixed point of function g will be the root of the original function f. 

    Parameters:
        g (function): The function for which we want to find the fixed point.
        initial_guess: Initial guess for the fixed point.
        tol: Accuracy for stopping criterion 
        max_iter: Maximum number of iterations allowed.

    Returns:
        fixed_point: Approximation of the fixed point.
        num_iter (int): Number of iterations performed.
    """
    x = initial_guess
    print(f"{'iteration number(n)':<50}{'|':<2}{' Pn':<50}")
    print("-" * 50)
    for i in range(max_iter):
        x_new = h(x)
        print(f"{i+1:<50}| {x_new:.8f}")
        if abs(x_new - x) < tol:
            return x_new, i+1
        x = x_new
    raise ValueError("Fixed point not found within maximum iterations.")

g_expression = input("Enter a non linear function g(x) that you would like to find the root for, where g(x) must satisfy the contraction theorem: ")
def g(x):
    return eval(g_expression)

h_expression = input("Rewrite the original function g(x) in the format x = h(x)), where the h(x) satisfies the contraction theorem: ")
def h(x):
    return eval(h_expression)

a = float(input("What is the starting range: "))
b = float(input("What is the ending range: "))
initial_guess = float(input("What is the initial guess: "))
tolerance = float(input("What is the accuracy required: "))
max_iterations = int(input("What is the maximum iterations: "))

fixed_point, num_iter = fixed_point_iteration(h, initial_guess, tol=tolerance, max_iter=max_iterations)
print(f"The root of g(x) is: {fixed_point}")
print(f"The fixed point of h(x) is: {fixed_point}")
print(f"Number of iterations: {num_iter}")

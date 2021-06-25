import re
import math
import random
from test_functions import *
# from test_functions import f1
# from test_functions import f1_ddx
# from test_functions import f6

"""
Intelligent Systems 1
Week 6 Lab Sheet
Dr James Stovold
This week we are going to focus on local search algorithms. For the purpose of this lab sheet, we
will be minimising all functions.
In order to test our algorithms, we are going to need some test functions, F1, F6, and the Hölder
Table function. Python code for these is provided, the mathematical descriptions and plots are
provided here:
F1: f(x) = |x| + cos(x) , -20 ≤ x ≤ 20
F6: f(x) = (x! + x) cos(x) , -10 ≤ x ≤ 10
Hölder Table function: -10 ≤ x, y ≤ 10
�(�, �) = − 7sin(x)cos(y)exp <71 -
√(x! + y!)
� 7?7
"""


def differentiation(
        expressions):  # not that it works T.T... differentiating is way too much hassle to program (for now ~ during exam season)
    # inputting in x**4 - 6*(x**2) + 2 format for example
    expression_string = str(expressions).split(" ")
    for letter in expression_string:
        variable = letter if letter.isalpha() else "{unknown variable}"
    differented = ""
    for expression in expression_string:
        if "**" in expression and "*" not in expression:
            expression_split = expression.split("**")
            differentiating = expression_split[-1] + variable + "**" + str(int(expression_split[-1]) - 1)
        elif "*" in expression:
            expression_split = re.split("[***()]", expression)
            differentiating = str(int(expression_split[-1]) * int(expression_split[1])) + variable + "**" + str(
                int(expression_split[-1]) - 1)
        else:
            pass
        differented += differentiating
    return differented


expressions = "x**4 - 6*(x**2) + 2"

# print(differentiation(expressions))

"""
. Build the basic one-dimensional gradient descent algorithm from the lectures into Python.
N.B. A reasonable starting value for the learning rate h is 0.05.
a. Test your implementation on the F1 test function. How well does it work? What
about if you change the initial value x"? How does varying h impact the search?
Why?
b. Does your implementation behave in a similar way with F6? What factors may be
affecting how well your algorithm works?"""


# gradient descent algorithm
# one method of gradient descent, assuming f(x) is differentiable, is a repeated update of an estimate x using the formula:
# xvn+1 = xvn - h * f'(xvn), where eta (h) is a very small number which defines our step size (And v is denoting subscript)
# each update is a candidate solution, can be used to find closest local minimum or optimum (but not global - see simple annealing)
# h needs to be small enough so that we don't overshoot any optimum, but also big enough that we can get there in a reasoable amoint of time
# f(x) = x^4 - 6x^2 + 2  <- we want to find the solution for x aka the root, kinda like Newton Raphson Method

# from AI: a modern approach: "The hill-climbing algorithms described so far are incomplete—they often fail to find
# a goal when one exists because they can get stuck on local maxima. Random-restart hill
# climbing adopts the well-knownadage, "If at first you don't succeed, try, try again." It conducts a series of hill-climbing searches from randomly generated initial states, t until a goal
# is found. It is trivially complete with probability approaching 1, because it will eventually
# generate a goal state as the initial state. If each hill-climbing search has a probability p of
# success, then the expected number of restarts required is 1/p. [...] The success of hill climbing depends very much on the shape of the state-space landscape: if there arc few local maxima and plateaux, random-restart hill climbing will find a
# good solution very quickly. On the other hand, many real problems have a landscape that
# looks more like a widely scattered family of balding porcupines on a flat floor, with miniature
# porcupines living on the tip of each porcupine needle, ad infinintum. NP-hard problems typically have an exponential number of local maxima to get stuck on Despite this, a reasonably
# good local maximum can often be found after a small number of restarts. A hill-climbing algorithm that never makes "downhill" moves toward states with lower value
# (or higher cost) is guaranteed to be incomplete, because it can get stuck on a local maximum. In contrast, a purely random walk—that is, moving to a successor chosen uniformly
# at random from the set of successors—is complete but extremely inefficient. Therefore, it
# seems reasonable to try to combine hill climbing with a random walk in some way that yields
# both efficiency and completeness. Simulated annealing is such an algorithm. Hidden beneath the phrase "a is a small constant" lies a huge variety of methods for
# adjusting a. The basic problem is that, if a is too small, too many steps are needed; if a
# is too large, the search could overshoot the maximum. The technique of line search tries to
# overcome this dilemma by extending the current gradient direction—usually by repeatedly
# doubling a—until f starts to decrease again. The point at which this occurs becomes the new
# current state. There are several schools of thought about how the new direction should be
# chosen at this point. "

def f(x):
    return x ** 4 - 6 * (x ** 2) + 2


def f_(x):  # derivative function {manually differentiated T.T} f'(x) or dy/dx
    return 4 * (x ** 3) - 12 * x


def gradient_descent_naive(x, step_size, max_iterations):
    # keeps returning overflow error, result too large  # cuz the method goes down the wrong tangents of the graph into infinity instead of converging
    while max_iterations > 0:
        max_iterations -= 1
        step = step_size * f_(x)
        x -= step  # the closer we get to the method, the smaller the change
    return x


# print(gradient_descent_naive(x, step_size, max_iterations))

def gradient_descent(x0=0.0006, eta=0.05, max_iterations=10000, function=f6, print_rate=25):
    # OverflowError: (34, 'Result too large') when function=f_ (my own function)
    # ValueError: x out of bounds raised when function=f1
    # prints only 2 iterations (so gets to somewhere < 50 and > 25th) when x0=6, eta=0.05, max_iterations=10000, function=f6, print_rate=25
    # lated printed 10000 iterations when x0=1 or x0=0.0006 - so works only with small numbers (must be to do with trigonometric graphs (different constraints for sin, cos etc)
    # gets to the 1000th iteration when function=f1_ddx YAY
    # varying the maximum iterations allows for more consistency in the outputs aka correct to 4 dp when gradient_descent(x0=6, eta=0.01, max_iterations=10000, function=f1_ddx, print_rate=25)
    # decreasing the eta allows for the results to be much less accurate
    # pseudo code problem representation
    # current 4-— MAKE-NODE(problem.INITIAL-STATE)
    # loop do
    #   neighbor {a highest-valued successor of current}
    #   if neighbor.VALUE < curent.VALUE then return current.STATE
    #   current 4 <— neigh bor
    iteration = 0
    xn = x0
    while max_iterations >= iteration:
        xnplus1 = xn - eta * function(xn)
        if xn == xnplus1:  # we found it =)
            break
        xn = xnplus1
        if print_rate > 0 and iteration % print_rate == 0:
            print(str(iteration) + "th iteration gives: " + str(xn))
        iteration += 1
    return xnplus1


# gradient_descent(function=f_)
# gradient_descent(function=f)
# gradient_descent(function=f1)
# gradient_descent(function=f1_ddx)
# gradient_descent(function=f6)

# simulated annealing balances exploring new areas while exploiting what it knows already
# not for higher dimension problems you don't wanna be relying solely on one optimisation method - solutions can interact with each other and influence the others's decisions =0


def simulated_annealing(m0=(12.5,), t0=50, iterations_for_current_temp_version=50, function=f1, function_range=(-20, 20),
                        print_every=25):  # starting point, starting temp, how quickly we want to change our starting variable/rate of change/iteration per temp version, function, function range, how often we want to print a result
    mvn = m0
    temp = t0
    temp_version_change = 0
    dimensions = len(m0)
    incomplete = True

    while incomplete:  # doing until we find some consistency in the answers
        for iteration in range(iterations_for_current_temp_version):
            mvnplus1 = new_move_in_range(dimensions, function_range[0], function_range[1]) # randomisations, hum
            difference = function(mvnplus1) - function(mvn)  # measuring the fitness of those two roots - we've picked this move, is it a better move than the ones we had been doing before?
            # (unlike in gradient descent in which we were only looking at the gradient and not the fitness)
            # in worst case if we pick it thinking it is the better move, it'll just eb gradient descent
            if difference < 0:  # we are trying to find the global minimum - minimising
                mvn = mvnplus1
            elif math.exp(- difference / temp) > random(): # giving it a chance even though it may be a bit too out there cuz may lead to something better
            # simplified version of the Maxwell Boltzmann distribution P(X=i) = ...
            # exponential kinda tells us whether or not this is a good move to take, hum
            # as temp decreases, exponential does too, and so less likely to be greater than the random number, so we take fewer and fewer risks
            # because it is a probability distribution, we statistically decide whether or not to take this move ~ random numbers
            # even if it is a bad move, but it is valid due to the random number, it may lead to a better solution later on
                mvn = mvnplus1
            if print_every > 0 and temp_version_change % print_every == 0:
                print("temp: " + str(temp) + "\t" + "x: " + str(mvn))
            temp_version_change += 1
        temp *= 0.995  # decreasing temp when the for loop for that value of temp finishes
        if temp < 0.005:  # aka indiscernable/negligible - to have a cutting point to the code
            incomplete = False
    return mvn

#simulated_annealing(m0=(12.5,), t0=50, iterations_for_current_temp_version=50, function=f1, function_range=(-20, 20), print_every=25)
simulated_annealing((12.5,), 50, 100, f1, (-20, 20), 2000)
simulated_annealing((3.5, 3.5), 50, 100, holder, (-10, 10), 2000)  # incorporating two dimensions using tuples


"""
3. Extend your simulated annealing implementation to two dimensions.
a. Try to find the minimum of the Hölder Table function.
b. How successful are you? Why?  # kinda it finds the lead to one minimum and sticks to finding it as opposed to jumping around as it used to be prone to. hill climbing searches may get lost on plateuxes
4. How might we reliably compare the performance of these algorithms? What complications  # simulated annealing good for not spiralling into infinity. they're both good for problems that are easy to produce solutions for, bad at first, but better over time.
might you encounter?
Challenge: See if you can apply a local search algorithm (either GD or SA) to the travelling salesman
problem. How well does it work?
"""




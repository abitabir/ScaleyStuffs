import numpy as np
import matplotlib.pyplot as plt

def gradient_descent(f, df, x_0, step_size_fn, max_iteration):
    """
    Performs gradient descent on the given function f, with its gradient df.

    :param f: A function whose input is an x, a column vector, and returns a scalar.
    :param df: A function whose input is an x, a column vector, and returns a column vector representing the gradient of f at x.
    :param x0: An initial value of x, x0, which is a column vector.
    :param step_size: The step size to use in each step
    :param max_iter: The number of iterations to perform

    :return x: the value at the final step
    :return fs: the list of values of f found during all the iterations (including f(x0))
    :return xs: the list of values of x found during all the iterations (including x0)
    """

    # Exercise 1 (d): Todo: Implement here.
    x_t = x_0
    fxs = []
    xs = []

    for t in range(max_iteration):
        fx_t = f(x_t)  # current f(x)
        dfxofx_t = df(x_t)  # current df(x)/dx i.e gradient
        fxs.append(fx_t)  # f(x) values storage
        xs.append(x_t)  # x storage
        if t == max_iteration - 1:
            return x_t, xs, fxs  # returning final theta value
        eta = step_size_fn(t)  # could change eta/step e.g making it smaller as time goes on to prevent overshoooting
        x_t = x_t - eta * dfxofx_t  # quite newton raphson-y


def transform_polynomial_basis_1d(x, order):  # there are no cross terms here because our data is one dimensional =0
    """
    Transforms a single 1-dimensional data point x with a polynomial basis transformation.

    :param x: A numpy array with a single value (d=1).
    :param order: Can be 0, 1, 2 or 3.
    :return: The transformed data point x as a list.
    """
    if order==0:
        return [1]
    if order==1:
        return [1, x]
    if order==2:
        # Todo: Implement the polynomial basis for k=2:
        return [1, x, x ** 2]
    if order==3:
        # Todo: And for k=3:
        return [1, x, x ** 2, x ** 3]


def data_linear_trivial():
    X = np.array([[-6], [-4], [-2], [0], [2], [4], [6]])
    Y = np.array([[-6], [-4], [-2], [0], [2], [4], [6]])
    return X, Y


def data_linear_simple():
    X = np.array([[-6], [-4], [-2], [0], [2], [4], [6]])
    Y = np.array([[-5], [-5], [-3], [1], [2], [5], [6]])
    return X, Y


def data_linear_offset():
    X = np.array([[-6], [-4], [-2], [0], [2], [4], [6]])
    Y = np.array([[-6], [-4], [-2], [0], [2], [4], [6]]) + 6
    return X, Y


def data_quadratic():
    X = np.array([[-6], [-4], [-2], [0], [2], [4], [6]])
    Y = np.array([[12], [3], [1], [0], [1], [3], [12]])
    return X, Y


def data_polynomial():
    X = np.array([[-6], [-4], [-2], [0], [2], [4], [6], [8]])
    Y = np.array([[12], [3], [1], [0], [1], [3], [12], [3]])
    return X, Y


def plot_line_2d(axes, theta, line_style, xmin=-10, xmax=10):
    """
    Takes a 2-dimensional theta and plots the line defined by (theta[1], theta[0]) into the given axes.
    """
    p1_y = theta[0] * xmin + theta[1]
    p2_y = theta[0] * xmax + theta[1]
    ax.plot([xmin, xmax], [p1_y.flatten(), p2_y.flatten()], line_style)


if __name__ == '__main__':
    """
    We'll implement gradient descent, and test it on a simple quadratic function. We'll go on implementing the
    closed-form OLS solution, as well as solving the OLS objective with gradient descent, with various provided data.
    We'll analyse the convergence of gradient descent with various step sizes, and plot the loss (convergence plot).
    The final exercise uses polynomial basis transformation to fit more complex data with linear hypotheses.
    """

    # Exercise 1: Gradient descent to find the minimum of a simple quadratic function
    # -----------
    def f1(x):
        # Our function is f(x) = (3x+4)^2
        return float((3 * x + 4) ** 2)

    def df1(x):
        # 1 (c): Todo: Implement the derivative here
        return float(18 * x + 24)

    # 1 (e): Todo: Plot the function:
    fig_simple, ax_simple = plt.subplots()  # create an empty plot and retrieve the 'ax' handle
    f1_plot_xs = np.arange(-10, 10, 0.05)
    f1_plot_fxs = np.array([f1(x) for x in f1_plot_xs])
    ax_simple.plot(f1_plot_xs, f1_plot_fxs)

    # Todo: Set and plot the initial value:
    x_0 = 0
    ax_simple.plot(x_0, f1(x_0), 'ro')

    # Run gradient descent to find the minimum of the function:
    # Todo: Experiment with step size, max_iter
    x_final, xs, fxs = gradient_descent(f1, df1, x_0, step_size_fn=lambda i: 0.0001, max_iteration=1000)  # sterp_size_fn needs a function, lambda function in python takes one parameter input i, and boringly always returns 0.0001

    # Todo: Plot each step of gradient descent, to see how it converges/diverges
    for x_, fx_ in zip(xs, fxs):
        ax_simple.plot(x_, fx_, 'b+')

    # Todo: Plot the found 'x' value and f(x)
    ax_simple.plot(x_final, f1(x_final), 'gx')
    # should be similar to the x value at the local minima (well, global for this curve of order 2) we calculated on paper when setting dy/dx to 0 and solving for x: -4/3
    # we see that there is little difference between x_0 and final_x, so we increase the step size from 10 to 100 to 1000
    # w can also play around with the step size, however python can't deal with too big a numbers e.g to power 100+ which is what happens when the step size is too big and the gradient descent algorithm diverges
    # if step size too small, can take ages; if step size too large, can diverge, siiighs so balances required, yup
    # there's no set solution that always works, but optimisers are being developed

    # this function is a convex function because it is quadratic i.e has only one global minima or maxima
    # this guarantees that gradient descent will converge given a sufficiently small step size
    # by 'sufficiently small step size' that is for the machine learning practitioner to establish, hmmm
    # (not concave like a cave n)


    # Exercise 2: Least Squares Regression
    # -----------
    # Get some example data (browse the file to see the various data_* functions provided):
    # X, Y = data_linear_trivial()
    X, Y = data_linear_simple()
    # X, Y = data_linear_offset()
    # X, Y = data_quadratic()
    # X, Y = data_polynomial()

    # Create a plot and set up some default plot options:
    fig, ax = plt.subplots()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)
    ax.grid(True, which='both')
    ax.axhline(color='black', linewidth=0.5)
    ax.axvline(color='black', linewidth=0.5)
    ax.set_title("Least squares regression")
    # Todo: Plot the data here (ex. 2.2)
    # plotting data before augmenting it
    ax.plot(X, Y, 'r+')

    # Todo: Feature transformation, add column of ones
    # in order to incorporate theta_0 in a different way
    X_augmented = np.insert(X, X.shape[1], [1], axis=1)

    # Exercise 2.2: Todo: Compute theta* using the analytical OLS solution:
    # ------------
    # 𝜃∗ = (𝑋^𝑇𝑋)^-1𝑋^TY
    theta_star = np.linalg.inv(X_augmented.T @ X_augmented) @ X_augmented.T @ Y
    # will have same dimensions as input data - (2 x 1) dimensional output

    # Todo: Plot the resulting hypothesis into the plot:
    plot_line_2d(ax, theta_star, 'g-')


    # Exercise 2.3 - Solution using gradient descent:
    # ------------

    # Todo: Implement the loss function:
    def squared_loss(x, y, theta):
        return (x @ theta - y) ** 2  # NOTE matrix multiplication is not commutative!!!
    # we don't need to transpose becasue we are not working with single instances of x or y, we are working with the collection of datas as matrices X and Y

    # Todo: Implement the OLS objective function (using the loss):
    # the mean of all the squared errors
    def ols_objective(X, Y, theta):
        return np.mean(squared_loss(X, Y, theta))

    # Todo: Implement the partial derivative of the squared loss w.r.t. theta
    # dJ/d𝜃 = ∇𝜃J = 2/n * X^T (X𝜃 - Y)  # has same shape as theta
    def d_squared_loss_theta(x, y, theta):
        return (2 / x.shape[0]) * (x.T @ (x @ theta - y))  # n = number of rows

    # Todo: Implement the partial derivative of the OLS objective w.r.t. theta (using the partial derivative of the squared loss):
    def d_ols_objective_theta(x, y, theta):
        return d_squared_loss_theta(x, y, theta)

    # Finally, the gradient of our OLS objective is simply d_ols_objective_theta (as theta is our only parameter):
    def ols_objective_grad(X, Y, theta):
        return d_ols_objective_theta(X, Y, theta)

    # And we define the function that we want to minimise as the OLS objective over our dataset (X_augmented, Y):
    def f_ols(theta):
        return ols_objective(X_augmented, Y, theta)

    # And its gradient:
    def df_ols(theta):
        return ols_objective_grad(X_augmented, Y, theta)

    # Todo: Set an initial value for theta_init:
    theta_init = np.zeros((X_augmented.shape[1], 1))

    # We define a step size function - let's return a constant step size, independent of the iteration i:
    def step_size_fn(i):
        return 0.001  # Todo: Experiment with various step sizes

    # Now we're ready to run gradient descent to minimise f_ols:
    closest_theta_to_theta_best_found_thus_far, loss_value_per_theta_iterations, theta_iterations_over_time = gradient_descent(f_ols, df_ols, theta_init, step_size_fn=step_size_fn, max_iteration=250)
    # root at which minima found, and the iterations that got it there - a good value for theta

    # Todo: Plot the found hypothesis into the figure with the data.
    # Todo: Also plot individual steps of gradient descent, to see how the optimisation behaves.
    plot_line_2d(ax, closest_theta_to_theta_best_found_thus_far, "g-")  # plotting line of best fit with theta found programatically (green)
    # as opposed to the theta_star found analytically (blue) {which was also found much more hassle free}
    # gradient descent finds a similar value to theta_star found through the formula, when number of max_iterations is increased

    # Exercise 2.3 iii):
    fig_loss, ax_loss = plt.subplots()  # Create an empty figure for the loss plot
    # Todo: Plot the loss over the iterations
    # this will help us visualise and evaluate how many iterations is a good number for gradient descent
    # x axis iterations and y axis the loss function
    ax_loss.plot(np.linspace(1, len(loss_value_per_theta_iterations), len(loss_value_per_theta_iterations)), theta_iterations_over_time, "b-")
    # in the beginning, lossess very big as you would expect, but then levels out
    # we should actually run this algorithm for longer until it actually converges, hmmm

    # Optional: Exercise 2.4
    # Ex. 2.4 (b) iii): Plot the polynomial separator in 2D:
    X_quad, Y_quad = data_quadratic()
    X_quad_theta_0_removal = np.insert(X_quad, X_quad.shape[1], [1], axis=1)
    X_quad_aug = np.array([transform_polynomial_basis_1d(x[0], order=2) for x in X_quad_theta_0_removal])  # easy cuz only 2D array ~ indexing into only element of each row

    def calculate_theta_star(X, Y):  # best to continue to use analytically than gradient descent - more thourough, quicker and exact
        # for higher dimensional space gradient descent needs longer to get accurate parameters - higher max_iterations and maybe adjustments to step size that are more automated than just a a constricted set value
        return np.linalg.inv(X.T @ X) @ X.T @ Y

    theta_star_quad = calculate_theta_star(X_quad_aug, Y_quad)
    mean_square_error = ols_objective(X_quad_aug, Y_quad, theta_star_quad)  # decreases with augmentation of X
    # some error cuz noisy data for the quadratic one XP - so it's acc a good algorithm, were throwing it off a bit

    # plotting quadratic separator in 2D
    fig_quad, ax_quad = plt.subplots()
    ax_quad.plot(X_quad, Y_quad, "bx")
    x_plot_quad_lobf = np.arange(-10, 10, 0.05)
    x_plot_quad_lobf_aug = np.array([transform_polynomial_basis_1d(x_augmenting, 2) for x_augmenting in x_plot_quad_lobf])
    y_plot_quad_lobf = (theta_star_quad.T @ x_plot_quad_lobf_aug.T).T  # getting the y values to have same dimensions as the x values XOS
    ax_quad.plot(x_plot_quad_lobf, y_plot_quad_lobf, "g-")
    # I don't think anything really changes if we use order 3 or 4 for this quadratic


    # Optional: Optional with Polynomialsss {well, a quadratic with an anomaly to throw the algorithm off to be mean T>T}
    # order = 3

    X_poly, Y_poly = data_polynomial()
    X_poly_theta_0_removal = np.insert(X_poly, X_poly.shape[1], [1], axis=1)
    X_poly_aug = np.array([transform_polynomial_basis_1d(x[0], order=3) for x in
                           X_poly_theta_0_removal])

    theta_star_poly = calculate_theta_star(X_poly_aug, Y_poly)
    mean_square_error_poly = ols_objective(X_poly_aug, Y_poly, theta_star_poly)

    # plotting polynomial separator in 2D
    fig_poly, ax_poly = plt.subplots()
    ax_poly.plot(X_poly, Y_poly, "g+")
    x_plot_poly_lobf = np.arange(-10, 10, 0.05)
    x_plot_poly_lobf_aug = np.array(
        [transform_polynomial_basis_1d(x_augmenting, 3) for x_augmenting in x_plot_poly_lobf])
    y_plot_poly_lobf = (theta_star_poly.T @ x_plot_poly_lobf_aug.T).T
    ax_poly.plot(x_plot_poly_lobf, y_plot_poly_lobf, "g-")
    # dayum smooth curve, it has the capacity to change direction, hmmm
    # could also check how order of two changes things {in x_augs places I think}

    # too integrated to rename them all so just assign poly versions to the originals ~~~ messy messy messy coding me XOS
    X = X_poly
    Y = Y_poly
    X_augmented = np.insert(X, X.shape[1], [1], axis=1)
    closest_theta_poly, loss_values_poly, thetas_poly = gradient_descent(
        f_ols, df_ols, theta_init, step_size_fn=step_size_fn, max_iteration=250)
    fig_poly_loss, ax_poly_loss = plt.subplots()
    ax_poly_loss.plot(np.linspace(1, len(loss_values_poly), len(loss_values_poly)), thetas_poly, "b-")
    # so gradient descent doesn't converge anymore, it diverges {to infinity and beyond}, so we need to tune our step size
    # decreasing step size, it is optimising now, it is in the midst of converging but still nowhere near as much as it should XOS

    print("Finished.")
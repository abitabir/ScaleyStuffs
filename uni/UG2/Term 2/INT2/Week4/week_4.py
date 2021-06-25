import numpy as np
import matplotlib.pyplot as plt


# warm up
def sign_warm_up(x):
    # return "+ve" if x > 0 else "-ve"
    # return True if x > 0 else False
    # however, numpy's sign function returns 0 if input is 0
    if x == 0:
        return 0
    return 1 if x > 0 else -1
    # also, np.sign() can return an array for array input X0
    # advantage of using np.sign() over function by self is reusing code - use library function if it exists, don't
    # reinvent the wheel - Software Engineering questions
    # even if ot is short, a few cases we can do wrong, hum
    # numpy people know this function very well, has been used, tested and maintained for many years
    # they may have also implemented their function in faster and smarter ways
    # this goes for any function in all computer science careers XOS
    # most of the time best to use library function especially in python cuz it has good libraries
    # however sometimes not good to be dependent on libraries cuz things can break when packages get updated lol e.g JavaScript one

# import random  # we instead use np.random package
# random linear classifier
def linear_classify(x, theta, theta_0, k=100):
    """Uses the given theta, theta_0, to linearly classify the given data x. This is our hypothesis or hypothesis class.

    :param x: input data point as vector which is to be transformed to get desired y, of size R^d
    :param theta: the scalars by which input data is to be transformed/multiplied, of size R^d - the weight
    :param theta_0: the real number added to the data, of size R - the offset/bias
    :return: 1 if the given x is classified as positive, -1 if it is negative, and 0 if it lies on the hyperplane.
    """

    # Todo: Implement the linear classifier here that classifies x given theta, theta_0, and returns the result. ## Done
    return np.sign(np.matmul(theta, x) + theta_0)


def Loss(prediction, actual):
    """Computes the loss between the given prediction and actual values.

    :param prediction: the predicted linear classify value
    :param actual: the actual value that the linear classifying should have given
    :return: 1 if accurate classification, 0 otherwise (returing the loss of the prediction)
    """
    # Todo: Implement the loss between a predicted and actual value here, and return the loss.
    return 1 if prediction == actual else 0  # did the class match or not


def E_n(h, data, labels, theta, theta_0, L=Loss):
    """Computes the error for the given data using the given hypothesis and loss.

    :param h: Hypothesis class, for example a linear classifier.
    :param data: A d x n matrix where d is the number of data dimensions and n the number of examples.
    :param labels: A 1 x n matrix with the label (actual value) for each data point.
    :param L: A loss function to compute the error between the prediction and label.
    :param theta: our weight
    :param theta_0:
    :return: total loss divided by number of data points (columns)
    """
    (d, n) = data.shape
    # Todo: Compute the training loss E_n here and return it.
    # we want to loop over the training examples, sum up that loss, and divide by the number of training examples
    total_loss = 0
    for i in range(n):  # n being the number of coulmns so going -> that away through the data
        x = data[:, i:i+1]  # we want the ith column in the training dataset
        y_actual = labels[:, i:i+1]
        y_prediction = h(x, theta, theta_0)
        error_i = L(y_prediction, y_actual)
        total_loss += error_i
    total_loss /= n
    return total_loss

def random_linear_classifier(data, labels, params={}, hook=None):
    """

    :param data: A d x n matrix where d is the number of data dimensions and n the number of examples.
    :param labels: A 1 x n matrix with the label (actual value) for each data point.
    :param params: A dict, containing a key T, which is a positive integer number of steps to run
    :param hook: An optional hook function that is called in each iteration of the algorithm.
    :return:
    """
    k = params.get('k', 100)  # if k is not in params (is dead value), default to 100
    (d, n) = data.shape

    # Todo: Implement the Random Linear Classifier learning algorithm here.
    # Note: To call the hook function, use the following line inside your training loop:
    #   if hook: hook((theta, theta_0))
    thetas = []
    theta_0s = []
    all_errors = []
    for j in range(k):
        # since we kinda know what our data is like, for simplicity and not exploring random numbers that would give us not very relevant hypotheses, we'll stick to (-20, 20)
        theta_j = np.random.uniform(-20, 20, d)
        thetas.append(theta_j)  # drawing random numbers from a uniform distribution - equal chance of getting any value within the given interval
        # d is the size of our input data {number of rows, and we're going column by column in the other loops
        theta_0_j = np.random.uniform(-20, 20, 1)
        theta_0s.append(theta_0_j)
        if hook is not None:
            hook((theta_j, theta_0_j))
        error_j = E_n(linear_classify, data, labels, theta_j, theta_0_j, Loss)
        all_errors.append(error_j)
    j_best = np.argmin(all_errors)  # has least amount of error in our randomings
    return thetas[j_best], theta_0s[j_best]  # returning the best theta and theta_0!

def perceptron(data, labels, params={}, hook=None):
    """The Perceptron learning algorithm.

    :param data: A d x n matrix where d is the number of data dimensions and n the number of examples.
    :param labels: A 1 x n matrix with the label (actual value) for each data point.
    :param params: A dict, containing a key T, which is a positive integer number of steps to run
    :param hook: An optional hook function that is called in each iteration of the algorithm.
    :return:
    """
    T = params.get('T', 100)  # if T is not in params, default to 100
    (d, n) = data.shape

    # Todo: Implement the Perceptron algorithm here.
    theta = np.zeros((d, 1))  # making theta a column vector, so that concatenation doesn't occur
    theta_0 = 0
    for t in range(T):  # we don't want the perceptron to continue running all the way to T even if it has found the perfect values XOS... sooo, not very ideal, hum
        for i in range(n):
            y_i = labels[:, i:i+1]
            x_i = data[:, i:i+1]  # getting all the coulmns ':' and then the ith row of the data
            if (y_i * ((theta.T @ x_i) + theta_0)) <= 0:  # if classification is wrong (cuz -1 * -1 or 1 * 1 will be positive, elsewise is a missclassification)
                for index in range(len(theta)):
                    theta += y_i * x_i
                    theta_0 += y_i  # cuz only changing the y intercept
                    if hook is not None:
                        hook((theta, theta_0))
    return theta, theta_0

# perceptron through origin does not work well with sneaky data XOS


def plot_separator(plot_axes, theta, theta_0):
    """Plots the linear separator defined by theta, theta_0, into the given plot_axes. {helps plot every singe separator}

    :param plot_axes: Matplotlib Axes object
    :param theta:
    :param theta_0:
    """

    # One way we can plot the intercept is to compute the parametric line equation from the implicit form.
    # compute the y-intercept by setting x1 = 0 and then solving for x2:
    y_intercept = -theta_0 / theta[1]
    # compute the slope (-theta[0]/theta[1], I think)
    slope = -theta[0] / theta[1]
    # Then compute two points using:
    xmin, xmax = -15, 15
    # Note: It's not ideal to only plot the lines in a fixed region, but it makes this code simple for now.

    p1_y = slope * xmin + y_intercept
    p2_y = slope * xmax + y_intercept

    # Plot the separator:
    plot_axes.plot([xmin, xmax], [p1_y.flatten(), p2_y.flatten()], '-')
    # Plot the normal:
    # Note: The normal might not appear perpendicular on the plot if ax.axis('equal') is not set - but it is
    # perpendicular. Resize the plot window to equal axes to verify.
    plot_axes.arrow((xmin + xmax) / 2, (p1_y.flatten() + p2_y.flatten()) / 2, float(theta[0]), float(theta[1]))


if __name__ == '__main__':
    """
    We'll define data X with its labels y, plot the data, and then run either the random_linear_classifier or the
    perceptron learning algorithm, to find a hypothesis h from the class of linear classifiers.
    We then plot the best hypothesis, as well as compute the training error. 
    """

    # Let's create some training data and labels:
    #   X is a d x n matrix where d is the number of data dimensions and n the number of examples. So each data point
    #     is a column vector.
    #   y is a 1 x n matrix with the label (actual value) for each data point.
    X = np.array([[2, 3, 9, 12],
                  [5, 2, 6, 5]])
    y = np.array([[1, -1, 1, -1]])

    # To test your algorithm on a larger dataset, uncomment the following code. It generates uniformly distributed
    # random data in 2D, along with their labels.
    # X = np.random.uniform(low=-5, high=5, size=(2, 20))  # d=2, n=20
    # y = np.sign(np.dot(np.transpose([[3], [4]]), X) + 6)  # theta=[3, 4], theta_0=6

    # Plot positive data green, negative data red:
    colors = np.choose(y > 0, np.transpose(np.array(['r', 'g']))).flatten()  # if y > 0 assign to it green, elsewise red
    plt.ion()  # enable matplotlib interactive mode
    fig, ax = plt.subplots()  # create an empty plot and retrieve the 'ax' handle
    ax.scatter(X[0, :], X[1, :], c=colors, marker='o')
    # Set up a pretty 2D plot:
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)
    ax.grid(True, which='both')
    ax.axhline(color='black', linewidth=0.5)
    ax.axvline(color='black', linewidth=0.5)
    ax.set_title("Linear classification")


    # We'll define a hook function that we'll use to plot the separator at each step of the learning algorithm:
    def hook(params):
        (th, th0) = params
        plot_separator(ax, th, th0)


    # Run the RLC or Perceptron: (uncomment the following lines to call the learning algorithms)
    # theta, theta_0 = random_linear_classifier(X, y, {"k": 100}, hook=hook)  # random linear classifier WITH hook
    # theta, theta_0 = random_linear_classifier(X, y, {"k": 100}, hook=None)  # same as above but without hook
    theta, theta_0 = perceptron(X, y, {"T": 100}, hook=hook)  # the PERCEPTRON!!!
    # Plot the returned separator:
    plot_separator(ax, theta, theta_0)

    # Run the RLC, plot E_n over various k:
    # Todo: Your code
    # as in, vary k and plot the E_ns such that we can see what happens and whether it converges
    # for every k, we also want to run the learning algorithm 10 times
    # in order to average out the randomness
    # creating a plot to visualuse k on x axis and E_n average of 10 runs on y axis
    # note the greater the k, the longer it'll take for the algorithm to be carried out as well...
    various_ks = [1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    various_kss_average_training_error = []
    for k in various_ks:
        iterations_errors = []
        for iteration_for_averagings in range(10):
            theta, theta_0 = random_linear_classifier(X, y, {"k": k}, hook=None)
            error_iteration = E_n(linear_classify, X, y, theta, theta_0, Loss)
            iterations_errors.append(error_iteration)
        various_kss_average_training_error.append(np.mean(iterations_errors))
    fig_error, ax_error = plt.subplots()
    ax_error.set_xlabel("k")
    ax_error.set_ylabel("E_n")
    ax_error.set_title("E_n (total training error) over k (number of training itereations)")
    ax_error.plot(various_ks, various_kss_average_training_error)
    # we see E_n decreasing, and then levelling out
    # the less the changes in varied ks, the smoother the plot as well... lol but let's not do a plot for that as well XOS
    print("Finished.")

# how good the separator the random linear classifier comes up with is completely luck dependent; however the greater the hyper parameter k, the greater the chance of getting a good parameter

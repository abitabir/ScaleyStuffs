import numpy as np
import matplotlib.pyplot as plt

def plot_nonlin_separator(predictor, axes, x_min=None, x_max=None, y_min=None, y_max=None, resolution=30):
    # takes in fucntion and how much resolution of resulting graph we want among other things

    # setting up colour maps
    if x_min == None:  # and i.e the following parameters as well
        x_min, x_max = axes.get_xlim()
        y_min, y_max = axes.get_ylim()
    else:
        axes.set_xlim((x_min, x_max))
        axes.set_ylim((y_min, y_max))

    from matplotlib import colors
    cmap = colors.ListedColormap(["black", "white"])
    bounds = [-2, 0, 2]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    # to visualise, we took some points and checked what the classifier returned on the console in debugging mode
    # so now we'll just loop this for every step between two values on x_1 axis (e.g -20 to +20) and then on the x_2 axis,
    # which represents a point in space, and which we predict using classifier
    # basically for each of my points run the predictor and then store them all in the list - simplified due to python magic lollies
    # one way to plot a higher dimensional plane in 2D is just to sample the grid, yup
    ima = np.array([[predictor(x_1_i, x_2_i)
                     for x_1_i in np.linspace(x_min, x_max, resolution)]
                        for x_2_i in np.linspace(y_min, y_max, resolution)])  # we get resolution values between the intervals min and max
    # ima is basically us using an image where each pixel is either 0 or 1, and that's just gonna be plotted
    # # could alternatively:
    # grid = np.zeros((resolution, resolution))  # creating array in which values will be input
    # for x_1_i in np.linspace(x_min, x_max, resolution):
    #     for x_2_i in np.linspace(y_min, y_max, resolution):
    #         grid[x_1_i, x_2_i] = predictor(x_1_i, x_2_i)
    # ima = grid


    im = axes.imshow(np.flipud(ima), interpolation='none', extent=[x_min, x_max, y_min, y_max], cmap=cmap, norm=norm)
    # origin is framework specific, so flip ud flips the origin ~ python technicalities


def transform_polynomial_basis_2d(x, scalar_order):
    """ Returns input vector transformed by a polynomial basis of order specified. Orders suppoerted are 0 to 3.
    Constrained by input restrictions. Doing permutations without these contraints is beyond the scope of this exercise.
    :param x: A two dimensional vector input, of numpy array object type.
    :param scalar_order: Real number input between 0 and 3 inclusive.
    :return: Transformed x with the polynomial basis of order scalar_order applied.
    """
    assert len(x) == 2, "x should be a 2D vector of size (2 x 1)"
    assert scalar_order < 4 and scalar_order >= 0, "order should be in range 0 to 3"
    if scalar_order == 0:
        # [1]
        return [1]
    elif scalar_order == 1:
        # [1, x_1, ..., x_d]  # well since x is only 2D: [1, x_1, x_2]
        return np.concatenate(np.array([1]), x)
    elif scalar_order == 2:
        # [1, x_1, ..., x_d, x_1^2, x_1*x_2, ..., x_1*x_d, x_2^2, ..., x_d^2, ...]
        # in this 2D case: [1, x_1, x_2, x_1*x_1, x_1*x_2, x_2*x_2] {well if we not going by indexes}
        return np.concatenate([np.array([1]), x, np.array([x[0] ** 2, x[0] * x[1], x[1] ** 2])])
    else:  # if scalar_order == 3
        # in this 2D case: [1, x_1, x_2, x_1*x_1, x_1*x_2, x_2*x_2, x_1^3, x_1^2*x_2, x_2^2*x_1, x_2^3] {well if we not going by indexes}
        # basically combinations
        return np.concatenate([np.array([1]), x, np.array([x[0] ** 2, x[0] * x[1], x[1] ** 2, x[0] ** 3, x[0] ** 2 * x[1], x[1] ** 2 * x[0], x[1] ** 3])])


def linear_classify(x, theta, theta_0, k=100):
    """Uses the given theta, to linearly classify the given data x. This is our hypothesis or hypothesis class.

    :param x: input data point as vector which is to be transformed to get desired y, of size R^d
    :param theta: the scalars by which input data is to be transformed/multiplied, of size R^d - the weight
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
    :return: total loss divided by number of data points (columns)
    """
    (d, n) = data.shape
    # Todo: Compute the training loss E_n here and return it.
    # we want to loop over the training examples, sum up that loss, and divide by the number of training examples
    total_loss = 0
    for i in range(n):  # n being the number of coulmns so going -> that away through the data
        x = data[:, i:i+1]  # we want the ith column in the training dataset
        y_actual = labels[:, i:i+1]
        y_prediction = h(x, theta)
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
    for t in range(T):  # we don't want the perceptron to continue running all the way to T even if it has found the perfect values XOS... sooo, not very ideal, hum
        for i in range(n):
            y_i = labels[:, i:i+1]
            x_i = data[:, i:i+1]  # getting all the coulmns ':' and then the ith row of the data
            if (y_i * ((theta.T @ x_i))) <= 0:  # if classification is wrong (cuz -1 * -1 or 1 * 1 will be positive, elsewise is a missclassification)
                for index in range(len(theta)):
                    theta += y_i * x_i
                    if hook is not None:
                        hook((theta))
    return theta


def perceptron_with_offset(data, labels, params={}, hook=None):
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


def plot_separator(plot_axes, theta, theta_0=0):
    """Plots the linear separator defined by theta, into the given plot_axes. {helps plot every singe separator}

    :param plot_axes: Matplotlib Axes object
    :param theta:
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
    original_X = np.array([[2, 3, 9, 12],
                  [5, 2, 6, 5]])
    original_y = np.array([[1, -1, 1, -1]])
    y_xor = np.array([[-1, 1, 1, -1]])
    X_complexer = np.array([
        [2, 4, 9, 12, -1, -8],
        [5, -1, 6, 5, 10, 5]
    ])
    y_complexer = np.array([[-1, 1, 1, -1, 1, -1]])  # remember [[]] makes it column vector
    # poor creature, tries its best with these two complex X and y T.T  # edit: but wai - if we increase T to 1000 it gets pretty accuarate yoooo subanallah
    # there does exist a theta parameter where polynomial of scalar order 2 can solve this - we just need more time and iterations cuz higher dimensions so needs longer to converge
    # increasing the order gives the classifier more options for our classification surface
    # could end up overfitting though, that's why we use regularisation
    X = original_X
    y = original_y  # current y, change to y_xor and block out comments to get cool result
    # X_augmented = np.insert(X, X.shape[0], [1], axis=0)  # adding 1s at index (axis=0) after last (X.shape[0])
    # same output as np.insert(X, X.shape[0], [1, 1, 1, 1, 1], axis=0) cuz automatic adjustment to the dimensions above
    X_transformed = np.array([transform_polynomial_basis_2d(x, scalar_order=2) for x in X.T]).T  # going coulmn wise so using the transpose of X, and then lastly reorienting our data back to the shape it was

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
    def hook(th, th0=0):  # problems working with perceptron without theta_0, so setting to 0
        plot_separator(ax, th, th0)


    # Run the RLC or Perceptron: (uncomment the following lines to call the learning algorithms)
    theta, theta_0 = random_linear_classifier(X, y, {"k": 100}, hook=hook)  # random linear classifier WITH hook
    theta, theta_0 = random_linear_classifier(X, y, {"k": 100}, hook=None)  # same as above but without hook
    theta, theta_0 = perceptron_with_offset(X, y, {"T": 100}, hook=None)  # new perceptron with old values
    # theta_augmented = perceptron(X_augmented, y, {"T": 100}, hook=None)  # new perceptronnn with augumented values (1s in so no theta_0)
    theta_transformed = perceptron(X_transformed, y, {"T": 100}, hook=None)  # new perceptron with transformed values according to polynomial base
    # theta_xor = perceptron(X_transformed, y_xor, {"T": 100}, hook=None)  # theta with xor?  # ehhh y is too all over the place so just assign it to y_xor
    # xor linear classfiication problem (when two points of opposite class difficult to separate)
    # can be solved by transforming data using _some_ polynomial basis of _some_ order
    # if y = np.array([[-1, 1, 1, -1]]), we would have the XOR problem
    # theta_transformed would have same dimension as data input, 6D rn, so difficult to visualise, but we could simplify it down to 2D space, see: new_data_point

    # Plot the returned separator:
    plot_separator(ax, theta, theta_0)
    plot_separator(ax, theta_xor)  # none found for xor

    def predictor(x_0, x_1):
        x_transformed = transform_polynomial_basis_2d([x_0, x_1], scalar_order=2)  # using the same order as we used when training - when defining X_transformed
        # we use lowercase when referring to single vector as opposed to a collection of (matrix of many data points)
        return np.sign(theta_transformed.T @ x_transformed)

    # new_data_point = np.array([2, 6])  # we're going to try and visualise theta using this 2D point, exacting the polynomial basis function upon it
    # so we can visualise the whoel plane using many points
    plot_nonlin_separator(predictor, axes=ax, resolution=200)
    # we see a chunk of our 6D model in 2D! This nonlinear classifier uses a scalar_order of 2, and so has the ability to sqaure values.

    # now let us see how our perceptron deals with the XOR problem... hehehe - but siiiigh messy codeee

    # finally calculating total loss

    def linearly_classifying_with_feature_transform(x, theta, theta_0):
        x_transformed = transform_polynomial_basis_2d([x[0][0], x[1][0]], scalar_order=3)
        return np.sign(theta.T @ x_transformed[1:] + theta_0 * x_transformed[0])

    E_n_jetzt_training_error = E_n(linearly_classifying_with_feature_transform, X, y, theta_transformed[1:], theta_transformed[0])
    print("total error:", E_n_jetzt_training_error)

print("Finished.")

# Original from : 
# Authors: Clay Woolam <clay@woolam.org>
# License: BSD

#############################################################################################################################################################
#                                                                                                                                                           #
#    Modified and commented by : Dr. A. Schelle (support@krealix.de). Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt  #
#                                                                                                                                                           #
#############################################################################################################################################################

# PYTHON ROUTINE zur Normierung von Matrizen #

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

from sklearn import datasets
from sklearn.semi_supervised import LabelSpreading
from sklearn.metrics import classification_report, confusion_matrix

digits = datasets.load_digits() # Import number of digits from dataset 'datasets'
rng = np.random.RandomState(0) # Generate random initial state
indices = np.arange(len(digits.data)) # Count the number of indices
rng.shuffle(indices) # Create a random sample for the number of indices

X = digits.data[indices[:330]] # Implement X Vector for a number of given indices
y = digits.target[indices[:330]] # Implement y Vector for a number of given indices
images = digits.images[indices[:330]] # Implement Image Vector for a number of given indices

n_total_samples = len(y) # Count the number of elements in y
n_labeled_points = 10 # Set the number of labeled points 
max_iterations = 5 # Set the maximum number of iterations to find model accuracy

unlabeled_indices = np.arange(n_total_samples)[n_labeled_points:] # Count the number of unlabed indices
f = plt.figure() # Show figure

for i in range(max_iterations): # Train model 1 to 5 with up to 30 fitting labels / parameters (corresponding to maximal 5 iterations)

    if len(unlabeled_indices) == 0:

        print("No unlabeled items left to label.")

        break

    y_train = np.copy(y)
    y_train[unlabeled_indices] = -1

    lp_model = LabelSpreading(gamma=0.25, max_iter=20)
    lp_model.fit(X, y_train)

    predicted_labels = lp_model.transduction_[unlabeled_indices]
    true_labels = y[unlabeled_indices]

    cm = confusion_matrix(true_labels, predicted_labels, labels=lp_model.classes_)

    print("Iteration %i %s" % (i, 70 * "_")) # Show the number fo iterations with confusion matrix.

    print(
        "Label Spreading model: %d labeled & %d unlabeled (%d total)"
        % (n_labeled_points, n_total_samples - n_labeled_points, n_total_samples)
    )

    print(classification_report(true_labels, predicted_labels))
    print("Confusion matrix")
    print(cm)

    # Compute the entropies of transduced label distributions
    pred_entropies = stats.distributions.entropy(lp_model.label_distributions_.T)

    # Select up to 5 digit examples that the classifier is most uncertain about
    uncertainty_index = np.argsort(pred_entropies)[::-1]

    uncertainty_index = uncertainty_index[
        np.in1d(uncertainty_index, unlabeled_indices)
    ][:5]

    # Keep track of indices that we get labels for
    delete_indices = np.array([], dtype=int)

    # For more than 5 iterations, visualize the gain only on the first 5
    if i < 5:
        f.text(
            0.05,
            (1 - (i + 1) * 0.183),
            "model %d\n\nfit with\n%d labels" % ((i + 1), i * 5 + 10),
            size=10,
        )

    for index, image_index in enumerate(uncertainty_index):
        image = images[image_index]

        # For more than 5 iterations, visualize the gain only on the first 5
        if i < 5:
            sub = f.add_subplot(5, 5, index + 1 + (5 * i))
            sub.imshow(image, cmap=plt.cm.gray_r, interpolation="none")
            sub.set_title(
                "predict: %i\ntrue: %i"
                % (lp_model.transduction_[image_index], y[image_index]),
                size=10,
            )
            sub.axis("off")

        # Labeling 5 points, remote from labeled set
        (delete_index,) = np.where(unlabeled_indices == image_index)
        delete_indices = np.concatenate((delete_indices, delete_index))

    unlabeled_indices = np.delete(unlabeled_indices, delete_indices)
    n_labeled_points += len(uncertainty_index)

f.suptitle(
    "Active learning with Label Propagation.\nRows show 5 most "
    "uncertain labels to learn with the next model.",
    y=1.15,
)
plt.subplots_adjust(left=0.2, bottom=0.03, right=0.9, top=0.9, wspace=0.2, hspace=0.85) # Show model results with subplots
plt.show()
"""

 NN_classifier.py  (author: Anson Wong / git: ankonzoid)

 We train a multi-layer fully-connected neural network from scratch to classify
 the seeds dataset (https://archive.ics.uci.edu/ml/datasets/seeds). An L2 loss
 function, sigmoid activation, and no bias terms are assumed. The weight
 optimization is gradient descent via the delta rule.

"""
import numpy as np
from src.NeuralNetwork import NeuralNetwork
import src.utils as utils
import itertools
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_fscore_support
import matplotlib.pyplot as plt

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()

def main():
    # ===================================
    # Settings
    # ===================================
    csv_filename = "final_two class.csv"
    hidden_layers = [6] # number of nodes in hidden layers i.e. [layer1, layer2, ...]
    eta = 0.1 # learning rate
    n_epochs = 400 # number of training epochs
    n_folds = 6 # number of folds for cross-validation
    seed_crossval = 1 # seed for cross-validation
    seed_weights = 1 # seed for NN weight initialization

    # ===================================
    # Read csv data + normalize features
    # ===================================
    print("Reading '{}'...".format(csv_filename))
    X, y, n_classes = utils.read_csv(csv_filename, target_name="Compression.Preset", normalize=True)
    print(n_classes)
    N, d = X.shape
    print(" -> X.shape = {}, y.shape = {}, n_classes = {}\n".format(X.shape, y.shape, n_classes))

    print("Neural network model:")
    print(" input_dim = {}".format(d))
    print(" hidden_layers = {}".format(hidden_layers))
    print(" output_dim = {}".format(n_classes))
    print(" eta = {}".format(eta))
    print(" n_epochs = {}".format(n_epochs))
    print(" n_folds = {}".format(n_folds))
    print(" seed_crossval = {}".format(seed_crossval))
    print(" seed_weights = {}\n".format(seed_weights))

    # ===================================
    # Create cross-validation folds
    # ===================================
    idx_all = np.arange(0, N)
    idx_folds = utils.crossval_folds(N, n_folds, seed=seed_crossval) # list of list of fold indices

    # ===================================
    # Train/evaluate the model on each fold
    # ===================================
    acc_train, acc_valid = list(), list()  # training/test accuracy score
    print("Cross-validating with {} folds...".format(len(idx_folds)))
    for i, idx_valid in enumerate(idx_folds):

        # Collect training and test data from folds
        idx_train = np.delete(idx_all, idx_valid)
        X_train, y_train = X[idx_train], y[idx_train]
        X_valid, y_valid = X[idx_valid], y[idx_valid]

        # Build neural network classifier model and train
        model = NeuralNetwork(input_dim=d, output_dim=n_classes,
                              hidden_layers=hidden_layers, seed=seed_weights)
        model.train(X_train, y_train, eta=eta, n_epochs=n_epochs)

        # Make predictions for training and test data
        ypred_train = model.predict(X_train)
        ypred_valid = model.predict(X_valid)

        # Compute training/test accuracy score from predicted values
        acc_train.append(100*np.sum(y_train==ypred_train)/len(y_train))
        acc_valid.append(100*np.sum(y_valid==ypred_valid)/len(y_valid))

        np.set_printoptions(precision=2)
        #labels2=['veryfast', 'faster','fast', 'medium', 'slow', 'slower']
        #labels=[0,1,2,3,4,5]
        #print(y_train, y_valid, ypred_train, ypred_valid)
        '''
        confusion_matric = confusion_matrix(y_train.tolist(), ypred_train.tolist(), labels=labels)
        plt.figure()
        plot_confusion_matrix(confusion_matric, classes=labels2,
                      title='Confusion matrix')
        
        confusion_matric2 = confusion_matrix(y_valid.tolist(), ypred_valid.tolist(), labels=labels)
        plt.figure()
        plot_confusion_matrix(confusion_matric2, classes=labels2,
                      title='Confusion matrix')'''
        
        # Print cross-validation result
        print(" Fold {}/{}: acc_train = {:.2f}%, acc_valid = {:.2f}% (n_train = {}, n_valid = {})".format(
            i+1, n_folds, acc_train[-1], acc_valid[-1], len(X_train), len(X_valid)))
        
        print(precision_recall_fscore_support(y_train.tolist(), ypred_train.tolist(), average='weighted'))

        print(precision_recall_fscore_support(y_valid.tolist(), ypred_valid.tolist(), average='weighted'))
        

    # ===================================
    # Print results
    # ===================================
    print("  -> acc_train_avg = {:.2f}%, acc_valid_avg = {:.2f}%".format(
        sum(acc_train)/float(len(acc_train)), sum(acc_valid)/float(len(acc_valid))))

# Driver
if __name__ == "__main__":
    main()
## Complete the Perceptron class.

class Perceptron:
    def __init__(self, epochs=3):
        """
        Args:
            epochs: number of training epochs
        """
        self.epochs = epochs
        self.misclassifications = 0
        # Initialize the weights
        self.w1 = 0.0
        self.w2 = 0.0
        self.b = 0.0
        self.alpha = 1.0
        ## Add any other variables here if you need

    def update_weights(self, features, true_label):
        """
        The weight update rule. Iterates over each weight and updates it.
        Increments self.misclassifications by 1 if there is a misclassification.

        Args:
            features: Dependent variables (x)
            true_label: Target variable (y)
        """
                # Calculate the predicted label
        predicted_label = self.predict(features)
        
        # Check if there is a misclassification
        if predicted_label != true_label:
            self.misclassifications += 1
            # Update weights and bias
            # w += sum(α * y_i * x_i)
            # b = sum(y_i)
            self.w1 += self.alpha * true_label * features[0]
            self.w2 += self.alpha * true_label * features[1]
            self.b += self.alpha * true_label

    def predict(self, features):
        """
        Predict the label for a given set of features.

        Args:
            features: Dependent variables (x)

        Returns:
            Predicted label (1 or -1)
        """
        z = self.w1 * features[0] + self.w2 * features[1] + self.b
        return 1 if z >= 0 else -1

    def train(self, features, true_labels, plotting=True):
        """
        features: dependent variables (x)
        true_labels: target variables (y)
        plotting: plot the decision boundary (True by default)
        """

        # For each epoch
        for epoch in range(self.epochs):
            # Iterate over the training data
            for i in range(len(features)):

                if plotting:
                    print("Iteration {}, Misclassifications = {}".
                      format(epoch * len(features) + i+1, self.misclassifications))

                # Call self.update_weights function to update the weights
                self.update_weights(features[i], true_labels[i])


            print("="*25)
            print("Epoch {}, Accuracy = {}".format(epoch + 1, 1 - self.misclassifications/len(features)))
            print("="*25)
            self.misclassifications = 0


data = [[2.7810836,2.550537003,-1],
        [1.465489372,2.362125076,-1],
        [3.396561688,4.400293529,-1],
        [1.38807019,1.850220317,-1],
        [3.06407232,3.005305973,-1],
        [7.627531214,2.759262235,1],
        [5.332441248,2.088626775,1],
        [6.922596716,1.77106367,1],
        [8.675418651,-0.242068655,1],
        [7.673756466,3.508563011,1]]

## Create a perceptron object
perceptron = Perceptron()

features = [item[:-1] for item in data]
true_labels = [item[-1] for item in data]

perceptron.train(features, true_labels, plotting=True)
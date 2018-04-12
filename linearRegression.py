import math

from IPython import display
from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt

import numpy as np
import pandas as pd

from sklearn import metrics

import tensorflow as tf 

from tensorflow.python.data import Dataset

tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format


# Load the data set

url = "https://storage.googleapis.com/mledu-datasets/california_housing_train.csv"
california_housing_dataframe = pd.read_csv(url, sep=",")


# Randomize the data
california_housing_dataframe = california_housing_dataframe.reindex(
    np.random.permutation(california_housing_dataframe.index)
)
california_housing_dataframe["median_house_value"] /= 1000.0


# Examine the data
california_housing_dataframe.describe()

# Build the model
# step 1: Define features and configure feature columns
my_feature = california_housing_dataframe[["total_rooms"]]
feature_columns = [tf.feature_column.numeric_column("total_rooms")]

# step 2: Define the target/label
targets = california_housing_dataframe["median_house_value"]

# step 3: Configure the LinearRegrssor
# here also apply gradient clipping: ensures the magnitude of the gradients do not become too large
# during training, which can cause gradient descent to fail
my_optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.0000001)
my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(my_optimizer, 5.0)

linear_regressor = tf.estimator.LinearRegressor(
    feature_columns = feature_columns,
    optimizer=my_optimizer
)

# step 4: Define the Input function
def my_input_fn(features, targets, batch_size=1, shuffle=True, num_epochs=None):
    
    features = {key:np.array(value) for key, value in dict(features).items()}

    ds = Dataset.from_tensor_slices((features, targets))
    ds = ds.batch(batch_size).repeat(num_epochs)

    if shuffle:
        ds = ds.shuffle(buffer_size=10000)

    # return the next batch of data
    features, labels = ds.make_one_shot_iterator().get_next()
    return features, labels


# step 5: Train the model

_ = linear_regressor.train(
    input_fn = lambda:my_input_fn(my_feature, targets),
    steps = 100
)


# step 6: Evaluate the model
prediction_input_fn = lambda:my_input_fn(my_feature, targets, num_epochs=1, shuffle=False)

predictions = linear_regressor.predict(input_fn=prediction_input_fn)

predictions = np.array([item['predictions'][0] for item in predictions])

mean_squared_error = metrics.mean_squared_error(predictions, targets)
root_mean_squared_error = math.sqrt(mean_squared_error)

print("mean squared error on the training data: %0.3f" % mean_squared_error)
print("Root mean squared error on the training data: %0.3f" % root_mean_squared_error)

# make a readable scatter plot
sample = california_housing_dataframe.sample(n=300)
x_0 = sample["total_rooms"].min()
x_1 = sample["total_rooms"].max()

# retrieve the final weight and bias generated during training
weight = linear_regressor.get_variable_value('linear/linear_model/total_rooms/weights')[0]
bias = linear_regressor.get_variable_value('linear/linear_model/bias_weights')

y_0 = weight * x_0 + bias
y_1 = weight * x_1 + bias

plt.plot([x_0, x_1], [y_0, y_1], c='r')
plt.ylabel("median_house_value")
plt.xlabel("total_rooms")

plt.scatter(sample["total_rooms"], sample["median_house_value"])
plt.show()







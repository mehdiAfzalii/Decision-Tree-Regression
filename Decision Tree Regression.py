import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor


# Importing Dataset
dataset = pd.read_csv('Position_Salaries.csv')
x = dataset.iloc[:, 1:-1].values
y = np.array(dataset["Salary"].values).reshape(-1, 1)


# Training Decision Tree
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(x, y)


# Predicting a new result
prediction = regressor.predict([[7]])


# Visualising the Decision Tree Regression
plt.scatter(x, y, color='red')
plt.plot(x, regressor.predict(x), color='blue')
plt.grid(True)
plt.show()
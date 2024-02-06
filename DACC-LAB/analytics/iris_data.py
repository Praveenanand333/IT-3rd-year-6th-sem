import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

print("Basic Information about the Iris Dataset:")
print(iris.info())

print("\nDescriptive Statistics:")
print(iris.describe())

print("\nFirst Few Rows of the Dataset:")
print(iris.head())

sns.pairplot(iris, hue="species", markers=["o", "s", "D"])
plt.title("Pairplot of Iris Dataset")
plt.show()

plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
sns.boxplot(x="species", y="sepal_length", data=iris)
plt.subplot(2, 2, 2)
sns.boxplot(x="species", y="sepal_width", data=iris)
plt.subplot(2, 2, 3)
sns.boxplot(x="species", y="petal_length", data=iris)
plt.subplot(2, 2, 4)
sns.boxplot(x="species", y="petal_width", data=iris)
plt.suptitle("Boxplots of Iris Features by Species")
plt.show()

correlation_matrix = iris.drop('species', axis=1).corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix of Iris Dataset")
plt.show()

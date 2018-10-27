# %% [markdown]
# # sklearn-porter
#
# Repository: [https://github.com/nok/sklearn-porter](https://github.com/nok/sklearn-porter)
#
# ## KNeighborsClassifier
#
# Documentation: [sklearn.neighbors.KNeighborsClassifier](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)

# %%
import sys
sys.path.append('../../../../..')

# %% [markdown]
# ### Load data

# %%
from sklearn.datasets import load_iris

iris_data = load_iris()

X = iris_data.data
y = iris_data.target

print(X.shape, y.shape)

# %% [markdown]
# ### Train classifier

# %%
from sklearn.neighbors import KNeighborsClassifier

clf = KNeighborsClassifier(algorithm='brute', n_neighbors=3, weights='uniform')
clf.fit(X, y)

# %% [markdown]
# ### Transpile classifier

# %%
from sklearn_porter import Porter

porter = Porter(clf, language='java')
output = porter.export()

print(output)

# %% [markdown]
# ### Run classification in Java

# %%
# Save classifier:
# with open('KNeighborsClassifier.java', 'w') as f:
#     f.write(output)

# Compile model:
# $ javac -cp . KNeighborsClassifier.java

# Run classification:
# $ java KNeighborsClassifier 1 2 3 4

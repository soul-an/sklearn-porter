# %% [markdown]
# # sklearn-porter
#
# Repository: [https://github.com/nok/sklearn-porter](https://github.com/nok/sklearn-porter)
#
# ## SVC
#
# Documentation: [sklearn.svm.SVC](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)

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
from sklearn import svm

clf = svm.SVC(C=1., gamma=0.001, kernel='rbf', random_state=0)
clf.fit(X, y)

# %% [markdown]
# ### Transpile classifier

# %%
from sklearn_porter import Porter

porter = Porter(clf, language='c')
output = porter.export()

print(output)

# %% [markdown]
# ### Run classification in C

# %%
# Save model:
# with open('svc.c', 'w') as f:
#     f.write(output)

# Compile model:
# $ gcc svc.c -std=c99 -lm -o svc

# Run classification:
# $ ./svc 1 2 3 4

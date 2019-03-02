import pandas as pd

from pred import pred


def get_pos(x):
    return pd.np.array([x, 2*x, 3*x, pd.np.nan])


x = [1, pd.np.nan, 2, 3, 4, pd.np.nan, 5, pd.np.nan]

n = pd.np.array([get_pos(e) for e in x])

a = pd.np.array([
    [1, pd.np.nan, 1, 1, 1],
    [2, 2, 2, pd.np.nan, 2],
    [1, pd.np.nan, 1, 1, 1],
    [2, 2, 2, pd.np.nan, 2],
    [1, pd.np.nan, 1, 1, 1],
])

print(a[:, 3])

nans = [pd.np.nan] * 3

print(nans)

np_nans = pd.np.array(nans)

print(np_nans)

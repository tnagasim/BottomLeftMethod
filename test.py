# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np


# %%
import bottom_left2


# %%
import importlib
importlib.reload(bottom_left2)


# %%
case = bottom_left2.Case(np.array([0, 0, 20, 100]))


# %%
case.stack(bottom_left2.Rect(np.array([0, 0, 9, 4])))


# %%
case.stack(bottom_left2.Rect(np.array([0, 0, 4, 10])))


# %%
case.stacked
# %%

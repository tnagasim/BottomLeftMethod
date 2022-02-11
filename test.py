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
case = bottom_left2.Case([20, 100])


# %%
case.stack([9, 4])


# %%
case.stack([4, 10])


# %%
print(case.stacked)


# %%
case = bottom_left2.Case([1, 1, 2])
# %%
case.stack([1, 1, 1])
# %%
case.stack([1, 1, 1])
# %%
print(case.stacked)
# %%

# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import bottom_left2
import importlib
importlib.reload(bottom_left2)


# %%
case = bottom_left2.Case.create([20, 100])
blm = bottom_left2.BottomLeftMethod(case)
case.stack([9, 4], blm)
case.stack([4, 10], blm)
print(case.stacked)


# %%
case = bottom_left2.Case.create([1, 1, 2])
blm = bottom_left2.BottomLeftMethod(case)
case.stack([1, 1, 1], blm)
case.stack([1, 1, 1], blm)
print(case.stacked)

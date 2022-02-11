import numpy as np
import bottom_left2


def test_stacked():
    case = bottom_left2.Case([20, 100])
    case.stack([9, 4])
    case.stack([4, 10])

    assert((case.stacked == [[[0., 0.], [9., 4.]], [[9., 0.], [13., 10.]]]).all())

def test_stacked3d():
    case = bottom_left2.Case([1, 1, 2])
    case.stack([1, 1, 1])
    case.stack([1, 1, 1])

    assert((case.stacked == [[[0., 0., 0.], [1., 1., 1.]], [[0., 0., 1.], [1., 1., 2.]]]).all())

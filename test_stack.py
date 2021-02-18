import numpy as np
import bottom_left2


def test_stacked():
    case = bottom_left2.Case(np.array([0, 0, 20, 100]))
    case.stack(bottom_left2.Rect(np.array([0, 0, 9, 4])))
    case.stack(bottom_left2.Rect(np.array([0, 0, 4, 10])))

    assert((case.stacked == [[0., 0., 9., 4.], [9., 0., 13., 10.]]).all())

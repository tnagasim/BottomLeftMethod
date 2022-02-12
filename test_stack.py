import bottom_left2


def test_stacked():
    case = bottom_left2.Case.create([20, 100])
    blm = bottom_left2.BottomLeftMethod(case)
    case.stack([9, 4], blm)
    case.stack([4, 10], blm)

    assert((case.stacked == [[[0., 0.], [9., 4.]], [[9., 0.], [13., 10.]]]).all())

def test_stacked3d():
    case = bottom_left2.Case.create([1, 1, 2])
    blm = bottom_left2.BottomLeftMethod(case)
    case.stack([1, 1, 1], blm)
    case.stack([1, 1, 1], blm)

    assert((case.stacked == [[[0., 0., 0.], [1., 1., 1.]], [[0., 0., 1.], [1., 1., 2.]]]).all())

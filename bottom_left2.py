import itertools
import numpy as np


class Rect:
    def __init__(self, l_b_r_t):
        self.l_b_r_t = l_b_r_t  # left, bottom, right, top

    def get_height(self):
        return self.l_b_r_t[3] - self.l_b_r_t[1]

    def get_width(self):
        return self.l_b_r_t[2] - self.l_b_r_t[0]

    def is_feasible_point(self, case):
        if len(case.stacked) == 0:
            return True
        l = np.maximum(self.l_b_r_t[0], case.stacked[:, 0])
        b = np.maximum(self.l_b_r_t[1], case.stacked[:, 1])
        r = np.minimum(self.l_b_r_t[2], case.stacked[:, 2])
        t = np.minimum(self.l_b_r_t[3], case.stacked[:, 3])
        ret = any((l >= r) + (b >= t))
        return any((l >= r) + (b >= t))

    def is_inside_of(self, case):
        return (case.l_b_r_t[0] <= self.l_b_r_t[0]) \
            and (self.l_b_r_t[3] <= case.l_b_r_t[3])


class Case:
    def __init__(self, l_b_r_t):
        self.l_b_r_t = l_b_r_t  # left, bottom, right, top
        self.stacked = np.zeros((0, 4))

    def make_cand0(self):
        cand0 = np.zeros((1, 4))
        return cand0

    def make_candx(self):
        m, _ = self.stacked.shape
        candx = np.zeros((m, 4))
        candx[:, 0] = self.stacked[:, 2]
        return candx

    def make_candy(self):
        m, _ = self.stacked.shape
        candy = np.zeros((m, 4))
        candy[:, 1] = self.stacked[:, 3]
        return candy

    def make_cand2(self):
        perms = itertools.permutations(self.stacked, 2)
        cand2 = np.array([[p0[2], p1[3], 0, 0] for p0, p1 in perms])
        if len(cand2):
            return cand2
        return np.zeros((0, 4))

    def make_candidates(self, rect):
        cand0 = self.make_cand0()
        candx = self.make_candx()
        candy = self.make_candy()
        cand2 = self.make_cand2()
        cand = np.concatenate([cand0, candx, candy, cand2])
        cand[:, 2] = cand[:, 0] + rect.get_width()
        cand[:, 3] = cand[:, 1] + rect.get_height()
        cand = [Rect(p) for p in cand]
        return cand

    def stack(self, rect):
        cand = self.make_candidates(rect)
        blfp = [p for p in cand if p.is_feasible_point(self)]
        min_p = min(blfp, key=lambda v: (v.l_b_r_t[1], v.l_b_r_t[0]))
        min_p = min_p.l_b_r_t.reshape((1, 4))
        self.stacked = np.concatenate([self.stacked, min_p])



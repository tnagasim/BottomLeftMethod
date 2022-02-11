from audioop import reverse
import itertools
import numpy as np
from dataclasses import dataclass


@dataclass
class Rect:
    def __init__(self, size) -> None:
        self.l_b_r_t = np.array([[0] * len(size), size]) if type(size) is list else size

    def get_size(self):
        return self.l_b_r_t[1, :] - self.l_b_r_t[0, :]

    def is_feasible_point(self, case):
        if len(case.stacked) == 0:
            return True
        min_p = np.maximum(self.l_b_r_t[0, :], case.stacked[:, 0, :])
        max_p = np.minimum(self.l_b_r_t[1, :], case.stacked[:, 1, :])
        return (min_p >= max_p).any() and self.is_inside_of(case)

    def is_inside_of(self, case):
        return (case.l_b_r_t[0, :] <= self.l_b_r_t[0, :]).all() \
            and (self.l_b_r_t[1, :] <= case.l_b_r_t[1, :]).all()


@dataclass
class BottomLeftPoint:
    stacked: np.array

    def make_cand0(self):
        _, m, n = self.stacked.shape
        cand0 = np.zeros((1, m, n))
        return cand0

    def make_cand1(self):
        cand1 = []
        for i in range(self.stacked.shape[2]):
            temp = np.zeros_like(self.stacked)
            temp[:, 0, i] = self.stacked[:, 1, i]
            cand1.append(temp)
        return np.concatenate(cand1)

    def make_cand2(self):
        _, m, n = self.stacked.shape
        perms = itertools.permutations(self.stacked, n)
        cand2 = np.array([[[p[i][1, i] for i in range(n)], [0] * n] for p in perms])
        if len(cand2):
            return cand2
        return np.zeros((0, m, n))

    def make_candidates(self, rect):
        rect = Rect(rect)
        cand0 = self.make_cand0()
        cand1 = self.make_cand1()
        cand2 = self.make_cand2()
        cand = np.concatenate([cand0, cand1, cand2])
        cand[:, 1, :] = cand[:, 0, :] + rect.get_size()
        cand = [Rect(p) for p in cand]
        return cand


@dataclass
class Case:
    def __init__(self, size) -> None:
        self.l_b_r_t = np.array([[0] * len(size), size])  # [[left, bottom], [right, top]]
        self.stacked = np.zeros((0, 2, len(size)))

    def stack(self, rect):
        cand = BottomLeftPoint(self.stacked).make_candidates(rect)
        blfp = [p for p in cand if p.is_feasible_point(self)]
        min_p = min(blfp, key=lambda v: [v.l_b_r_t[0, i] for i in reversed(range(self.l_b_r_t.shape[1]))])
        min_p = min_p.l_b_r_t.reshape((1, 2, -1))
        self.stacked = np.concatenate([self.stacked, min_p])

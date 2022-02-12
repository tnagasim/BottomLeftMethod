import itertools
import numpy as np
from dataclasses import dataclass


@dataclass
class Rect:
    minmax_p: np.array

    def get_size(self):
        return self.minmax_p[1, :] - self.minmax_p[0, :]

    def is_feasible_point(self, case):
        if len(case.stacked) == 0:
            return True
        min_p = np.maximum(self.minmax_p[0, :], case.stacked[:, 0, :])
        max_p = np.minimum(self.minmax_p[1, :], case.stacked[:, 1, :])
        return (min_p >= max_p).any() and self.is_inside_of(case)

    def is_inside_of(self, case):
        return (case.minmax_p[0, :] <= self.minmax_p[0, :]).all() \
            and (self.minmax_p[1, :] <= case.minmax_p[1, :]).all()

    @staticmethod
    def create(size):
        minmax_p = np.array([[0] * len(size), size]) if type(size) is list else size
        return Rect(minmax_p)


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

    def make_candidates(self, rect_size):
        rect = Rect.create(rect_size)
        cand0 = self.make_cand0()
        cand1 = self.make_cand1()
        cand2 = self.make_cand2()
        cand = np.concatenate([cand0, cand1, cand2])
        cand[:, 1, :] = cand[:, 0, :] + rect.get_size()
        cand = [Rect(p) for p in cand]
        return cand


@dataclass
class Case:
    minmax_p: np.array
    stacked: np.array

    def stack(self, rect_size):
        cand = BottomLeftPoint(self.stacked).make_candidates(rect_size)
        blfp = [p for p in cand if p.is_feasible_point(self)]
        min_p = min(blfp, key=lambda v: [v.minmax_p[0, i] for i in reversed(range(self.minmax_p.shape[1]))])
        min_p = min_p.minmax_p.reshape((1, 2, -1))
        self.stacked = np.concatenate([self.stacked, min_p])

    @staticmethod
    def create(size):
        minmax_p = np.array([[0] * len(size), size])
        stacked = np.zeros((0, 2, len(size)))
        return Case(minmax_p, stacked)

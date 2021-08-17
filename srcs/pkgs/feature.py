import math


class Feature:
    def __init__(self, n, col):
        self.name = n
        self.count = len(col)
        self.mean = float(sum(col) / len(col))
        col.sort()
        self.min, self.max = col[0], col[-1]
        self.p25, self.p50, self.p75 = col[int(len(col) / 4)], col[int(len(col) / 2)], col[int(len(col) / 4 * 3)]
        self.std = math.sqrt(sum([float((float(x) - self.mean) ** 2) for x in col]) / self.count)

    def getvalue(self, val):
        return {
            '': self.name,
            'Count': self.count,
            'Mean': self.mean,
            'Std': self.std,
            '25%': self.p25,
            '50%': self.p50,
            '75%': self.p75,
            'Min': self.min,
            'Max': self.max
        }[val]
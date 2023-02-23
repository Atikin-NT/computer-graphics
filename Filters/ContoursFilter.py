from Filters.DoubleMatrFilter import DoubleMatrFilter


class EdgeDetection2(DoubleMatrFilter):
    def __init__(self):
        kerx = [
            [0, 0, 0],
            [-1, 0, 1],
            [0, 0, 0]
        ]
        kery = [
            [0, 1, 0],
            [0, 0, 0],
            [0, -1, 0]
        ]
        super().__init__(kerx, kery)


class SobelFilter(DoubleMatrFilter):
    def __init__(self):
        kerx = [
            [-1, 0, 1],
            [-2, 0, 2],
            [-1, 0, 1]
        ]
        kery = [
            [-1, -2, -1],
            [0, 0, 0],
            [1, 2, 1]
        ]
        super().__init__(kerx, kery)


class SharraFilter(DoubleMatrFilter):
    def __init__(self):
        kerx = [
            [3, 0, -3],
            [10, 0, -10],
            [3, 0, -3]
        ]
        kery = [
            [3, 10, 3],
            [0, 0, 0],
            [-3, -10, -3]
        ]
        super().__init__(kerx, kery)


class PrivetaFilter(DoubleMatrFilter):
    def __init__(self):
        kerx = [
            [-1, 0, 1],
            [-1, 0, 1],
            [-1, 0, 1]
        ]
        kery = [
            [-1, -1, -1],
            [0, 0, 0],
            [1, 1, 1]
        ]
        super().__init__(kerx, kery)
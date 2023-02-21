from.MatrixFilter import MatrixFilter


class BlurrFilter(MatrixFilter):
    def __init__(self):
        sizeX = 3
        sizeY = 3
        kernel = [[0]*sizeY]*sizeX
        for i in range(sizeX):
            for j in range(sizeY):
                kernel[i][j] = 1.0 / float(sizeX * sizeY)
        super().__init__(kernel)

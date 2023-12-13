class not2DError(Exception):
    def __str__(self):
        return '[ERROR]: list is not 2D.'

class unevenListError(Exception):
    def __str__(self):
        return '[ERROR]: inner lists are not same in length.'

class improperMatrixError(Exception):
    def __str__(self):
        return '[ERROR]: [a][b]*[c][d] not b==c.'

def mul1d(arr1, arr2):
    return sum(a * b for a, b in zip(arr1, arr2))

class list_D2(list):
    def __init__(self, arr):
        if not all(isinstance(el, list) for el in arr):  
            raise not2DError()
        if not all(len(i) == len(arr[0]) for i in arr):  
            raise unevenListError()
        super().__init__(arr)   

    def __str__(self):
        return f'list_2D: {len(self)}*{len(self[0])}' 

    def transpose(self):
        transposed = [list(i) for i in zip(*self)]
        return list_D2(transposed)

    def __matmul__(self, other):
        if len(self[0]) != len(other):
            raise improperMatrixError()
        result = [[mul1d(row, col) for col in zip(*other)] for row in self]
        return list_D2(result)

    def avg(self):
        total_elements = sum(len(row) for row in self)
        total_sum = sum(sum(row) for row in self)
        return total_sum / total_elements if total_elements else 0.0

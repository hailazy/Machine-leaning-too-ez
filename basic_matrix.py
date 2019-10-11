import numpy as np

# create a n.n matrix
def createSquareMatrix(n):
    matrix = np.random.random((n, n))
    return matrix

# Calculate det() of a matrix
def determinant_recursive(matrix, total=0):
    # convert numpy array to list
    # np.array([[1, 2], [3, 4]]) => [[1, 2], [3, 4]]
    if  type(matrix) is not list:
        matrix = matrix.tolist()

    # Store indices in list for row referencing
    indices = list(range(len(matrix)))
    print("i:", indices)
    # 2x2 matrix
    if len(matrix) == 2 and len(matrix[0]) == 2:
        val = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return val

    # submatrix for focus column (fc)
    for fc in indices:  # for each focus column, ...
        # find the submatrix ...
        s_matrix = matrix.copy()  # make a copy
        s_matrix = s_matrix[1:]  # remove the first row
        height = len(s_matrix)
        print("s_m:", s_matrix)
        print("h:", height)

        for i in range(height):
            # for each remaining row of submatrix ...
            # remove the focus column elements
            s_matrix[i] = s_matrix[i][0:fc] + s_matrix[i][fc + 1:]

        sign = (-1) ** (fc % 2)
        # pass submatrix recursively
        sub_det = determinant_recursive(s_matrix)
        # total all returns from recursion
        total += sign * matrix[0][fc] * sub_det

    return total

# Calculate inverse()

# Main

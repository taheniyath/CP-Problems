# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):
    # list1 = []
    if len(m1[0]) != len(m2):
        return None
    list1 = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            prod = 0
            for k in range(len(m1[0])):
                prod += m1[i][k] * m2[k][j]
            list1[i][j] = prod
    return list1





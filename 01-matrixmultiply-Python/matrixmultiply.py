# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):
    list1 = []
    if(len(m1) != len(m2) or len(m1[0]) != len(m2[0])):
        return None
    else:
        for i in range(len(m1)):
            if i>0 and len(m1[i] != len(m2[i])):
                return None
            res = []
            for j in range (len(m1[0])):
                res.append(m1[i][j]* m2[i][j])
            list1.append(res)
        return list1
    # return None





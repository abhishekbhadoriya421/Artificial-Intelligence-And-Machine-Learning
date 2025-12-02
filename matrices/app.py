import numpy as np

def matrices_addtions(matrix_a, matrix_b):
    shapeOfMatrixA = matrix_a.shape
    shapeOfMatrixB = matrix_b.shape
    if shapeOfMatrixA != shapeOfMatrixB:
        return "Matrices must have the same dimensions to be added."
    
    result = np.zeros(shapeOfMatrixA)
    for i in range(0,shapeOfMatrixA[0]):
    	for j in range(0,shapeOfMatrixA[1]):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
    print("Resultant Matrix after Addition:")
    print(result)      
    return 
    
def matrices_subtractions(matrix_a, matrix_b):
    shapeOfMatrixA = matrix_a.shape
    shapeOfMatrixB = matrix_b.shape
    if shapeOfMatrixA != shapeOfMatrixB:
        return "Matrices must have the same dimensions to be subtracted."
    
    result = np.zeros(shapeOfMatrixA)
    for i in range(0,shapeOfMatrixA[0]):
    	for j in range(0,shapeOfMatrixA[1]):
            result[i][j] = matrix_a[i][j] - matrix_b[i][j]
    print("Resultant Matrix after Subtraction:")
    print(result)      
    return

def matrices_multiplication(matrix_a, matrix_b):
    # shapeOfMatrixA = matrix_a.shape
    # shapeOfMatrixB = matrix_b.shape
    # if shapeOfMatrixA != shapeOfMatrixB:
    #     return "Matrices must have the same dimensions to be matrices_multiplication."
    
    # result = np.zeros(shapeOfMatrixA)
    # for i in range(0,shapeOfMatrixA[0]):
    # 	for j in range(i,shapeOfMatrixA[1]):
    #         element = matrix_a[i][j]
    #         temp = 0
    #         for k in range(0,shapeOfMatrixA[0]):
    #             print( matrix_b[k][i])
    #             element2 = matrix_b[i][k]
    #             temp2 = element * element2
    #             temp += temp2
    #         result[i][j] = temp
    # print("Resultant Matrix after Subtraction:")
    # print(result) 
    result = np.dot(matrix_a, matrix_b)    
    return result


a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]])
b = np.array([
    [10,11,12],
    [13,14,15],
    [16,17,18]])

# matrices_addtions(a,b)
# matrices_subtractions(a,b)

print(matrices_multiplication(a,b))
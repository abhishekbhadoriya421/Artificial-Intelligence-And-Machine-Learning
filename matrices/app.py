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

# print(matrices_multiplication(a,b))

def test():
    # arr = np.array([
    #     [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10],
    #     [11,12,13,14,15,16,17,18,19,20],
    #     [21,22,23,24,25,26,27,28,29,30],
    #     [31,32,33,34,35,36,37,38,39,40],
    #     [41,42,43,44,45,46,47,48,49,50],
    #     [51,52,53,54,55,56,57,58,59,60],
    #     [61,62,63,64,65,66,67,68,69,70],
    #     [71,72,73,74,75,76,77,78,79,80],
    #     [81,82,83,84,85,86,87,88,89,90],
    #     [91,92,93,94,95,96,97,98,99,100]
    # ])
    
    # print(arr)
    # print("Print All Elements of first Row")
    # print(arr[0:1,:])
    # print("\n Print All Elements of first column")
    # print(arr[:,0:1])
    # print("\n Print middle element")
    # print(arr[2:,1:2])
    # print("\n check minus")
    # print(arr[-1:,-1:])
    # print("\nEvery other element in last row:", arr[0, 2::2])
    # print(arr++1)
    arr1 = np.array([
            [1,2,3],
            [4,5,6]
        ])
    arr2 = np.array([7,9])
    
    print(arr1 + arr2)  # Broadcasting in action
test()
import numpy as np


def array_operations():
    arr1 = np.array([1,2,3,4,5])
    arr2 = np.array([7,8,9,5,10])
    arr2D = np.array([
        [1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15]
    ])
    # print("Array 1:", arr2D[1][0])
    
    # addition if both arrays have same shape
    # print("Addition:", arr1 + arr2)
    # print("Subtraction:", arr1 - arr2)
    # print("Multiplication:", arr1 * arr2)
    # print("Division:", arr1 / arr2)
    
    # Statistical operations
    # print("Mean of arr1: ", np.mean(arr1))
    # print('Median of arr2: ', np.median(arr1))
    # print('Standard division: ',np.std(arr1))
    
    # Comparison
    # print("arr1 > arr2:", arr1 > arr2)
    # print("arr1 == arr2:", arr1 == arr2)

    matrix1 = np.arange(1, 10).reshape(3, 3)
    matrix2 = np.arange(10, 19).reshape(3, 3)
    print("Matrix 1:\n", matrix1)
    print("Matrix 1:\n", matrix2)
    # print("\nHorizontal Stack:\n", np.hstack((matrix1, matrix2)))
    # print("\nHorizontal Stack:\n", np.vstack((matrix1, matrix2)))
    
    print("Element-wise Multiplication:\n", matrix1 * matrix2)
    print("Matrix Multiplication (dot product):\n", np.dot(matrix1, matrix2))
if __name__ == "__main__":
    array_operations()
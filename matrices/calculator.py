import numpy as np
import ast
def matrix_cal():
    stringMatrix = input("Enter Matrix A:")
    matrix_a = np.array(ast.literal_eval(stringMatrix)) 
    stringMatrixB = input("Enter Matrix B:")
    matrix_b = np.array(ast.literal_eval(stringMatrixB)) 
    print(matrix_a )
    print(matrix_b)
    print("""
    Choose operation:
    1. Add
    2. Subtract
    3. Multiply
    4. Transpose A
    5. Transpose B
    6. Determinant A
    7. Determinant B
    8. Inverse A
    9. Inverse B
    """)

    while(True):
        choice = input("Enter choice (1-5): ")
        
        if choice == '1':
            print(matrix_a + matrix_b)
        elif choice == '2':
            print(matrix_a - matrix_b)
        elif choice == '3':
            print(np.dot(matrix_a, matrix_b))
        elif choice == '4':
            print(matrix_a.T)
        elif choice == '5':
            print(matrix_b.T)
        elif choice == '6':
            print(np.linalg.det(matrix_a))
        elif choice == '7':
            print(np.linalg.det(matrix_b))
        elif choice == '8':
            print(np.linalg.inv(matrix_a))
        elif choice == '9':
            print(np.linalg.inv(matrix_b))
        
    
matrix_cal()
'[[1,2,3],[4,5,6],[7,8,9]]'
'[[11,12,13],[14,15,16],[17,18,19]]'
'[1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10], [11,12,13,14,15,16,17,18,19,20], [21,22,23,24,25,26,27,28,29,30],[31,32,33,34,35,36,37,38,39,40],[41,42,43,44,45,46,47,48,49,50],[51,52,53,54,55,56,57,58,59,60],[61,62,63,64,65,66,67,68,69,70],[71,72,73,74,75,76,77,78,79,80],[81,82,83,84,85,86,87,88,89,90],[91,92,93,94,95,96,97,98,99,100]'
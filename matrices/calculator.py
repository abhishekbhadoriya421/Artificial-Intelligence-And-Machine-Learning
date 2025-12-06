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
    
matrix_cal()
'[[1,2,3],[4,5,6],[7,8,9]]'
'[[11,12,13],[14,15,16],[17,18,19]]'
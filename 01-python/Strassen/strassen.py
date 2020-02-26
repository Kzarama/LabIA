import numpy as np

def strassen(A, B):

    if type(A) is not np.ndarray or type(B) is not np.ndarray:
        raise Exception('Inputs are not numpy ndarrays')
    # if :
    #     raise Exception('Inputs are not bidimensional')
#   if True:
#     raise Exception('Matrices are not squared')
#   if True:
#     raise Exception('Matrices are not of n power of two')
    else:
        print("ok")
  
#   n = len(A)
# ​
#   if n == 2:
#     return A @ B
# ​
#   h = n//2
# ​
#   A11 = # slice A
#   A12 = # slice A
#   A21 = # slice A
#   A22 = # slice A
#   B11 = # slice B
#   B12 = # slice B
#   B21 = # slice B
#   B22 = # slice B
# ​
#   M1 = # call strassen with corresponding matrices
#   M2 = # call strassen with corresponding matrices
#   M3 = # call strassen with corresponding matrices
#   M4 = # call strassen with corresponding matrices
#   M5 = # call strassen with corresponding matrices
#   M6 = # call strassen with corresponding matrices
#   M7 = # call strassen with corresponding matrices
# ​
#   C = numpy.zeros((n,n))
#   # set C values
# ​
#   return C
import numpy as np
import sympy
A = np.array([[3, -1], [2, 3]])
b = np.array([[7], [1]])


B = np.vstack( (A, np.array([[6, -2]]))  )
b = np.vstack( (b, np.array([[-1   ]]))  )


B_hat = np.hstack((B, b))




if __name__ == "__main__":
    print(B)
    print(b)
    print(np.shape(B))
    print(np.shape(b))
    print
    
    print(B_hat)

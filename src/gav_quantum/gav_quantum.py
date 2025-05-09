import numpy as np

# Returns the operator specified via tensor notation
# INPUTS
#     N - Number of qubits
#     nonidentities - List of tuples specifying qubit number (indexed at 0) in ascending order and Pauli operator.  
#         Example: [(0,X),(2,'Y')]
def operator_from_sparse_pauli(N, nonidentities):
    tup = lambda value, tuples: next(((first, second) for first, second in tuples if first == value), 0)
    
    for iter in range(N):
        result = tup(iter, nonidentities)
        if(iter == 0):
            ret_arr = np.identity(2) if (result == 0) else result[1]
        else:
            ret_arr = np.kron(ret_arr, np.identity(2)) if result == 0 else np.kron(ret_arr, result[1])

    return ret_arr
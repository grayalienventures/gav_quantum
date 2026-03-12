from gav_quantum.core import Paulis_N_k, WeylBrauer
import math
import numpy as np
import unittest

def test_Pauli_3_2():
    Ps, Ps_verbose = Paulis_N_k(3, 2)
    assert(len(Ps) == 37)

def test_Pauli_4_2():
    Ps, Ps_verbose = Paulis_N_k(4, 2)
    assert(len(Ps) == 67)

def test():
    Ps, Ps_verbose = Paulis_N_k(4, 2)
    print(Ps)

class TestWeylBrauer(unittest.TestCase):
    NUM_GENERATORS = 10

    def test_involution(self):
        print('TESTING WEYL-BRAUER INVOLUTION')
        for i in range(self.NUM_GENERATORS+1):
            wb = WeylBrauer(i+1)
            for j in range(i):
                self.assertTrue(np.any(wb[j] @ wb[j] == np.eye(2**(math.ceil((i+1)/2)))))

    def test_hermitian(self):
        print('TESTING WEYL-BRAUER HERMITIAN CONJUGATE')
        for i in range(self.NUM_GENERATORS+1):
            wb = WeylBrauer(i+1)
            for j in range(i):
                self.assertTrue(np.any(wb[j] == wb[j].conj().T))

    def test_antisymmetric(self):
        print('TESTING WEYL-BRAUER CLIFFORD CONDITION')
        for i in range(self.NUM_GENERATORS+1):
            wb = WeylBrauer(i+1)
            for j in range(i):
                self.assertTrue(np.all(wb[i] @ wb[j] == -1 * wb[j] @ wb[i]))
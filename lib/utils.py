import numpy as np
import scipy.linalg as la

def diagonalize(H,S=None):
    """
    Diagonalize a real, symmetrix matrix and return sorted results.
    
    Return the eigenvalues and eigenvectors (column matrix) 
    sorted from lowest to highest eigenvalue.
    """
    E,C = la.eigh(H,S)
    E = np.real(E)
    C = np.real(C)

    idx = E.argsort()
    #idx = (-E).argsort()
    E = E[idx]
    C = C[:,idx]

    return E,C

def matrix_dot(*matrices):
    """Calculate the matrix product of multiple matrices."""
    A = matrices[0].copy()
    for B in matrices[1:]:
        A = np.dot(A,B)
    return A

def tensor_diff(tensor1, tensor2):
    #norm = tensor1.size * np.sum(abs(tensor1)) + 1e-12
    norm = 1.0
    cost = np.sum(abs(tensor1 - tensor2))/norm
    return cost

def to_liouville(rho):
    ns = rho.shape[0]
    if len(rho.shape) == 2:
        # A matrix to a vector
        rho_vec = np.zeros(ns*ns, dtype=np.complex_)
        idx = 0
        for i in range(ns):
            for j in range(ns):
                rho_vec[idx] = rho[i,j]
                idx += 1
        return rho_vec
    else:
        # A tensor to a matrix 
        rho_mat = np.zeros((ns*ns,ns*ns), dtype=np.complex_) 
        I = 0
        for i in range(ns):
            for j in range(ns):
                J = 0
                for k in range(ns):
                    for l in range(ns):
                        rho_mat[I,J] = rho[i,j,k,l]
                        J += 1
                I += 1
        return rho_mat

def from_liouville(rho_vec):
    ns = int(np.sqrt(len(rho_vec)))
    rho = np.zeros((ns,ns), dtype=np.complex_)
    idx = 0
    for i in range(ns):
        for j in range(ns):
            rho[i,j] = rho_vec[idx]
            idx += 1
    return rho

def commutator(A,B):
    return np.dot(A,B) - np.dot(B,A)

def print_banner(text):
    Nchar = len(text)
    Nstar = max(56,Nchar+7) 
    print ""
    print "*"*Nstar
    print "*  ", text, " "*(Nstar-Nchar-7), "*"
    print "*"*Nstar

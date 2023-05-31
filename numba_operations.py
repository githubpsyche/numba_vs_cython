from numba import njit
import numpy as np

@njit
def calc_rho(
    cdot: float, # Dot product between $c$ and $c^{IN}$.
    B: float, # Beta parameter weighting $c^{IN}`$
    ):
    rho = np.sqrt(1 + (B * B) * ((cdot * cdot) - 1)) - (B * cdot)
    return rho
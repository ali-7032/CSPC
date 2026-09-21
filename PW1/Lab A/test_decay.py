"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
import decay
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


# TODO 1: test_rejects_negative_rate
#   Check that calling simulate(...) with a negative lam raises a ValueError.
#   Which pytest tool checks that an error is raised?


# TODO 2: test_matches_law
#   Check that the simulation's AVERAGE over many seeds is close to the
#   physical law  N0 * exp(-lam * t).
#   Which pytest tool compares floating-point values with a tolerance?

def test_simulate_negative_rate_raises_error():

    with pytest.raises(ValueError):
        decay.simulate(1000, -0.1)

def test_simulate_average_matches_theoretical_decay():
   
    n_init = 1000
    p = 0.2
   
    runs = [decay.simulate(n_init, p)[-1] for _ in range(500)]
    avg_remaining = sum(runs) / len(runs)
    
   
    expected = n_init * ((1 - p) ** 10) 
    
  
    assert avg_remaining == pytest.approx(expected, rel=1e-1)
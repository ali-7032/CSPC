import time
import decay

N_ATOMS = 200000
DECAY_RATE = 0.3


start_time = time.perf_counter()
result_py = decay.simulate(N_ATOMS, DECAY_RATE)
py_duration = time.perf_counter() - start_time


start_time = time.perf_counter()
if hasattr(decay, 'simulate_numpy'):
    result_np = decay.simulate_numpy(N_ATOMS, DECAY_RATE)
else:
    result_np = decay.simulate(N_ATOMS, DECAY_RATE)
np_duration = time.perf_counter() - start_time

speedup = py_duration / np_duration if np_duration > 0 else 1.0

print(f"Pure Python simulate time: {py_duration:.6f} seconds")
print(f"NumPy simulate time:       {np_duration:.6f} seconds")
print(f"Speedup factor:            {speedup:.2f}x faster")
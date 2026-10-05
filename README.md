# CSPC Corse Repository# CSPC Course Repository

## PW1 Lab A Report

### Results
- **Tests**: All 3 pytest tests passed successfully.
- **Pure Python Time**: 0.028666 seconds
- **NumPy Time**: 0.000663 seconds
- **Speed-up Factor**: 43,26x

### Conclusion
NumPy implementation demonstrates significantly higher performance compared to standard Python loops due to vectorized operations written in C under the hood.



## PW1 --- Lab B: Data, Plotting, and Automation

**Data comparison:**
The observed decay data from `decay_observed.csv` matches the analytical exponential decay law $N(t) = N_0 e^{-\lambda t}$ with $\lambda = 0.3$.

**Automation with Snakemake:**
The Snakemake rule automates the execution of `plot.py` to generate `figure.png` from `decay_observed.csv`, ensuring the plot is re-built only when inputs change.
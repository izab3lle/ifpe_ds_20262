import numpy as np

def white_noise(
    seed = False,
    n: int = 10,
    var: int = 10
):
    """
    Generates white noise.

    args:
        n: Number of time points.
        var: Variance.
        seed: Seed for repoductible experiments.
    """

    time = np.arange(n)

    if seed is not False:
        np.random.seed(seed)
        
    values = np.random.randn(n) * var

    return time, values
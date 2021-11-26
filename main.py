import copy
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)


def sample(sampling_fn, num_chains=100, chain_length=10000, start=0):
    res = np.zeros((num_chains, chain_length))
    for i in range(num_chains):
        deltas = sampling_fn(size=chain_length)

        link_val = start
        for j in range(chain_length):
            res[i, j] = link_val
            link_val += deltas[j]
    return res


def plot(values, label, color=[0, 0, 1, 1]):
    mean = np.mean(values, axis=0)
    std = np.std(values, axis=0)

    x_vals = np.arange(len(mean))

    blur = copy.deepcopy(color)
    blur[-1] = 0.1

    plt.plot(x_vals, mean, label=label, color=color)
    plt.fill_between(x_vals, mean - std, mean + std, color=blur)

    plt.legend()


chains = sample(np.random.normal)
plot(chains, "Values")
plt.show()

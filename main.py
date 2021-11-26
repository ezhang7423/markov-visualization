import numpy as np

np.random.seed(42)


def sample(sampling_fn, num_chains=100, chain_length=10000, start=0):
    res = []
    for i in range(num_chains):
        chain = []
        deltas = sampling_fn(size=chain_length)
        res.append(chain)

        link_val = start
        for j in range(chain_length):
            chain.append(link_val)
            link_val += deltas[j]
    return res


chains = sample(np.random.normal)
print(chains)


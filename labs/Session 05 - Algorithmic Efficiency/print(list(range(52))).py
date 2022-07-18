import numpy as np
import random

num_samples = int(1e4)
min_sample = int(1e5)
max_sample = int(1e6)

def init_samples(num_samples, min_sample, max_sample):
    samples = [None] * num_samples
    for idx, _ in enumerate(samples):
        samples[idx] = random.randint(min_sample, max_sample)
    return samples

def is_primes(min_sample, max_sample):
    primes = []
    for num in range(min_sample, max_sample):
        prime = True
        for i in range(2, int(np.sqrt(num))):
            if num % i == 0:
                prime = False
        if prime:
            primes.append(num)
    return primes


def count_primes(samples, primes):
    num_primes = 0
    for val in samples:
        for num in primes:
            if val % num == 0:  
                num_primes += 1  
    return num_primes

samples = init_samples(num_samples, min_sample, max_sample)
primes = is_primes(min_sample, max_sample)

print(count_primes(samples, primes))
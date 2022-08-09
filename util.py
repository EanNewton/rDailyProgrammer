from time import sleep, time, perf_counter
from subprocess import Popen
from contextlib import contextmanager
from os import getpid, path
from signal import SIGINT
from resource import getrusage, RUSAGE_SELF
import functools

DEFAULT_DIR = path.dirname(path.abspath(__file__))
VERBOSE = 1
events = [
    "instructions",
    "cache-references",
    "cache-misses",
    "avx_insts.all",
]

@contextmanager
def perf():
    """Benchmark this process with Linux's perf util.
    Example usage:
        with perf():
            x = run_some_code()
            more_code(x)
            all_this_code_will_be_measured()
    """
    p = Popen([
        # Run perf stat
        "perf", "stat",
        # for the current Python process
        "-p", str(getpid()),
        # record the list of events mentioned above
        "-e", ",".join(events)])
    # Ensure perf has started before running more
    # Python code. This will add ~0.1 to the elapsed
    # time reported by perf, so we also track elapsed
    # time separately.
    sleep(0.1)
    start = time()
    try:
        yield
    finally:
        print(f"Elapsed (seconds): {time() - start}")
        print("Peak memory (MiB):",
              int(getrusage(RUSAGE_SELF).ru_maxrss / 1024))
        p.send_signal(SIGINT)


def debug(func):
    """Print the function signature and return value"""
    if VERBOSE >= 1:
        @functools.wraps(func)
        def wrapper_debug(*args, **kwargs):
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)

            print(f"Calling {func.__name__}({signature})\n")
            value = func(*args, **kwargs)
            print(f"{func.__name__!r} returned {value!r}\n")

            return value

        return wrapper_debug
    else:
        return func


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        tic = perf_counter()
        value = func(*args, **kwargs)
        toc = perf_counter()
        elapsed_time = toc - tic
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")
        return value

    return wrapper_timer

# Random numbers

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import time


def pseudo_uniform(low=0,
                   high=1,
                  seed=123456789,
                  size=1):
    """
    Generates uniformly random number between `low` and `high` limits
    """
    return low+(high-low)*pseudo_uniform_good(seed=seed,size=size)


def pseudo_uniform_good(mult=16807,
                        mod=(2**31)-1,
                        seed=123456789,
                        size=1):
    """
    A reasoanbly good pseudo random generator
    """
    U = np.zeros(size)
    x = (seed*mult+1)%mod
    U[0] = x/mod
    for i in range(1,size):
        x = (x*mult+1)%mod
        U[i] = x/mod
    return U

# Example
def sample_pick(lst):
    """
    Picks up a random sample from a given list
    """
    # Sets seed based on the decimal portion of the current system clock
    t = time.perf_counter()
    seed = int(10 ** 9 * float(str(t - int(t))[0:]))
    # Random sample as an index
    l = len(lst)
    s = pseudo_uniform(low=0, high=l, seed=seed, size=1)
    idx = int(s)

    return (lst[idx])


dice_faces = ['one','two','three','four','five','six']
for _ in range(30):
    print(sample_pick(dice_faces),end=', ')


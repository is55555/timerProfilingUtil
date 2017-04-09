# -*- coding: utf-8 -*-

# IS 2017 (MIT licence)
# https://github.com/is55555/timerProfilingUtil

from __future__ import print_function

import functools
import time

PROF_DATA = {}


def profile_time(fn):
    @functools.wraps(fn)
    def with_profiling(*args, **kwargs):
        start_time = time.time()

        ret = fn(*args, **kwargs)

        elapsed_time = time.time() - start_time

        if fn.__name__ not in PROF_DATA:
            PROF_DATA[fn.__name__] = {'count': 0, 'times': [], 'max': -1, 'avg': -1}
        PROF_DATA[fn.__name__]['count'] += 1
        PROF_DATA[fn.__name__]['times'].append(elapsed_time)

        return ret

    return with_profiling


def calc_prof_data():
    for fname, data in PROF_DATA.items():
        max_time = max(data['times'])
        avg_time = sum(data['times']) / len(data['times'])
        PROF_DATA[fname]['max'] = max_time
        PROF_DATA[fname]['avg'] = avg_time


def print_prof_data():  # to be called after calc_prof_data()
    for fname, data in PROF_DATA.items():
        max_time = PROF_DATA[fname]['max']
        avg_time = PROF_DATA[fname]['avg']
        print('\nFunction %s called %d times. Execution time max: %.3f, average: %.3f.' % (fname, data['count'],
                                                                                        max_time, avg_time),)


def clear_profile_time():
    global PROF_DATA
    PROF_DATA = {}


if __name__ == "__main__":
    from time import sleep
    import random

    @profile_time   # it's also possible to just create a new profiled version of the function ...
    #  ... like this: "prof_wait = profile_time(wait_random)" and then calling this new function
    def wait_random(average_wait=1., plus_minus=0.5):  # waits average_wait +- plus_minus seconds (uniform)
        sleep(average_wait + ( (0.5 - random.random()) * 2 * plus_minus))

    for i in range(random.randint(2,11)):
        wait_random()
        print("*", end="")

    calc_prof_data()
    print_prof_data()
    # obviously we can print it differently just by accessing the values in the dict
    print(PROF_DATA)  # this prints out the whole dictionary. Generally this would be impractical in real-life examples
    clear_profile_time()  # clears all profiling data (not needed here, but  might want to do it ...
    # ... in a more complex example)

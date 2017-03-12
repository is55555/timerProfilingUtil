from __future__ import print_function
import time


class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.minutes = 0
        self.seconds = 0

    def __str__(self):
        if self.seconds >= 1.:
            return 'elapsed: %d minutes %f seconds' % (self.minutes, self.seconds)
        else:
            return 'elapsed: %f ms' % (self.seconds * 1000.)

    def __repr__(self):
        return "%d minutes %f seconds" % (self.minutes, self.seconds)

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.seconds = self.end - self.start
        self.minutes = 0
        if self.seconds > 60:
            self.minutes = self.seconds // 60
            self.seconds %= 60

        if self.verbose:
            print(self.__str__())

    def reset(self):
        self.minutes = 0
        self.seconds = 0


if __name__ == "__main__":  # usage example
    from time import sleep
    import random
    with Timer(verbose=True):
        sleep(1. + random.random() - 0.5)

    with Timer() as t:
        for __ in range(65):  # should usually take a bit over a minute
            print("*", end="")
            sleep(1. + random.random() - 0.5)
    print(t)
    print("that took %d minutes and %f seconds" % (t.minutes, t.seconds))
    print("done")

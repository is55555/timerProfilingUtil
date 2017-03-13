from __future__ import print_function

import timeit
import inspect


def timeit_wrapper(func, number=10000):
    name = func.__name__
    module = inspect.getmodule(func).__name__
    t = timeit.Timer("%s()" % name, "from %s import %s" % (module, name))
    return t.timeit(number=number)/float(number)  # seconds per pass


def timeit_wrapper_argstr(func, arg_str, number=10000):
    module = inspect.getmodule(func).__name__
    name = func.__name__
    t = timeit.Timer("%s" % name + arg_str, "from %s import %s" % (module, name))
    return t.timeit(number=number)/float(number)  # seconds per pass

if __name__=="__main__":
    from time import sleep
    import random

    def wait_random(average_wait=0.001, plus_minus=0.0005):  # waits average_wait +- plus_minus seconds (uniform)
        sleep(average_wait + ( (0.5 - random.random()) * 2 * plus_minus))

    test = wait_random

    # example using this wrapper
    print(timeit_wrapper(test, number=100))  # for functions with no required args (can always make up one for this)
    print(timeit_wrapper_argstr(test, "(average_wait=0.05, plus_minus=0.01)",  number=20))  # with arguments

    # how you'd usually call timeit
    t = timeit.Timer("test()", "from __main__ import test")
    print(t.timeit(number=100)/float(100), "seconds/pass")

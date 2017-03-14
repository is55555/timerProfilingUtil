from __future__ import print_function
from functools import wraps

# for annotate_return_value, it would probably make sense to do another one with a function argument ...
# ... to format the printing of the result.


def annotate_calls(func, *args, **kwargs):
    @wraps(func)
    def closure(*args, **kwargs):
        if len(args) > 0:
            comma_ = ""
            args_str = ""
            for i in args:
                args_str += comma_ + repr(i)
                comma_ = ","
            comma = ","
        else:
            args_str = ""
            comma = ""
        kwargs_str = ""
        for i in kwargs.keys():
            kwargs_str += comma + i + '=' + repr(kwargs[i])
        print('calling: %s(%s)' % (func.__name__, args_str + kwargs_str))
        return func(*args, **kwargs)
    return closure


def annotate_return_value(func, *args, **kwargs):
    @wraps(func)
    def closure(*args, **kwargs):
        if len(args) > 0:
            comma_ = ""
            args_str = ""
            for i in args:
                args_str += comma_ + repr(i)
                comma_ = ","
            comma = ","
        else:
            args_str = ""
            comma = ""
        kwargs_str = ""
        for i in kwargs.keys():
            kwargs_str += comma + i + '=' + repr(kwargs[i])
        res = func(*args, **kwargs)
        print('result of: %s(%s) => %s' % (func.__name__, args_str + kwargs_str, str(res)))
        return res
    return closure

if __name__ == "__main__":
    @annotate_calls
    def fact_no_args():
        return 1

    @annotate_calls
    def fact_optional(n=0):
        if n < 2:
            return 1
        else:
            return n * fact_optional(n-1)

    @annotate_calls
    def fact(n):
        if n < 2:
            return 1
        else:
            return n * fact(n-1)

    @annotate_calls
    def fact2(n, n2):
        n += n2
        n2 = 0
        if n < 2:
            return 1
        else:
            return n * fact2(n-1, n2)

    @annotate_calls
    def fact3(n, n2, nothing=None):
        n += n2
        n2 = 0
        if n < 2:
            return 1
        else:
            return n * fact3(n-1, n2, nothing=None)

    @annotate_calls
    def fact4(n, n2, nothing=None, nothing2=None):
        n += n2
        n2 = 0
        if n < 2:
            return 1
        else:
            return n * fact4(n-1, n2, nothing=None, nothing2=None)

    fact(5)
    fact2(5, 4)
    fact3(5, 4)
    fact4(5, 4)
    fact_no_args()
    fact_optional()
    fact_optional(3)
    fact_optional(n=3)


    @annotate_calls
    @annotate_return_value
    def fact_return(n):
        if n < 2:
            return 1
        else:
            return n * fact_return(n-1)

    fact_return(5)

    print("-----")
    for f in [fact, fact2, fact3, fact4, fact_optional, fact_no_args]:
        f = annotate_return_value(f)

    fact = annotate_return_value(fact)
    fact2 = annotate_return_value(fact2)
    fact3 = annotate_return_value(fact3)
    fact4 = annotate_return_value(fact4)
    fact_optional = annotate_return_value(fact_optional)
    fact_no_args = annotate_return_value(fact_no_args)

    fact(5)
    fact2(5, 4)
    fact3(5, 4)
    fact4(5, 4)
    fact_no_args()
    fact_optional()
    fact_optional(3)
    fact_optional(n=3)

    fact(0)

    fact_return(3)
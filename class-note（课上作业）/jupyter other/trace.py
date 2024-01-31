#!/user/bin/python
# coding: utf-8
from sys import settrace

def tracer(frame,event,arg=None):
    func =frame.f_code.co_name
    lineno =frame.f_lineno
    locals =frame.f_locals
    print(f"event:{event},func:{func},lineno:{lineno}),locals:{locals}")
    return tracer


def mysnooper(func):
    def inner(*args,**kwargs):
        old = settrace(tracer)
        returnval = func(*args,**kwargs)
        settrace(old)
        return returnval
    return inner

@mysnooper
def foo(bar):
    buz =1
    if bar+buz >10:
        return 1
    else:
        return 2
#old = settrace(tracer)
foo(11)
#.
settrace(old)
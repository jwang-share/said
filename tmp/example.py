#encoding=utf-8

#generator
import types

##########################################################

##########################################################
def create_data():
    mylist = range(5)
    for item in mylist:
        yield item       

def execute():
    cds = create_data()
    for item in cds:
        print item*2

def create_data_cb(cb):
    #if not isinstance(cb,types.FunctionType):
    if not hasattr(cb, "__call__"):
        return -1
    mylist = range(5)
    for item in mylist:
        cb(item)

def cd_callback(item):
    if not isinstance(item,int):
        return -1
    print item*2

    

##########################################################
def do(func):
    def _do():
        print("before myfunc() called.")
        func()
        print("after myfunc() called.")
    return _do

@do
def show():
    print "show..."
        
def deco(func):
    def _deco(*args, **kwargs):
        print("before %s called." % func.__name__)
        ret = func(*args, **kwargs)
        print("  after %s called. result: %s" % (func.__name__, ret))
        return ret
    return _deco
 
@deco
def myfunc(a, b):
    print(" myfunc(%s,%s) called." % (a, b))
    return a+b
 
@deco
def myfunc2(a, b, c):
    print(" myfunc2(%s,%s,%s) called." % (a, b, c))
    return a+b+c

##########################################################

if __name__ == "__main__":
    execute()
    print "-----------------------------------"
    create_data_cb(cd_callback)
    print "-----------------------------------"
    show()
    myfunc(1,2)
    myfunc2(1,2,3)


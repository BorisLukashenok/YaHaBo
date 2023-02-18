def func():
    a = 1
    a += a


try:
    func()
    print("No Exceptions")
except ValueError:
    print("ValueError")
except TypeError:
    print("TypeError")
except SystemError:
    print("SystemError")

def MyFunction(x):
    return 2*x**2 + x + 3


def MySecondFunction(x):
    return 0.5 * x


def GetDerivative(function, x, deltaX=0.0001):
    deltaY = function(x + deltaX) - function(x)
    return deltaY / deltaX


print(MyFunction(-0.25))
print(GetDerivative(MyFunction, -0.25))

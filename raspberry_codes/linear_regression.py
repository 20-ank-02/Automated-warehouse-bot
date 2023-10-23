from scipy import stats
import math
# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
# y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

# x = [80, 100]
# y = [40, 60]

def getLine(y: [int], x1 : int): # returns angle of interception in radians (- pi/2 to pi/2)
    x = [x1]
    for i in range (0, len(y) - 1):
        x.append(x[i - 1] + 1)  # Translate by 1 cm
    
# x,y
# xi = translateX()
# yi = getDistance()
# x.append(xi)
# y.append(yi)
    
    print(f"y : {y} y.length : {len(y)}")
    print(f"x : {x} x.length : {len(x)}")

    slope, intercept, r, p, std_err = stats.linregress(x, y)

    # res = {}
    # res['slope'] = slope
    # res['theta'] = math.atan(slope)
    res = math.atan(slope)
    return res

def getSlope(x:[int], y: [int]): # returns angle of interception in radians (- pi/2 to pi/2)
    slope, intercept, r, p, std_err = stats.linregress(x, y)
    res = math.atan(slope)
    return res

y = [40, 60]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]
x1 = 80
res = getLine(y, x1)
print(res)

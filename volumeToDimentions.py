import sys, math
#input: volume, max internal height
#asumptions: you don't want a house that you can't walk in; height has a minimum of 2.

# volume=x*y*z
# z=v/(xy)

# s=2xy + 2xz + 2yz
# s=2xy + 2xv/xy + 2yv/xy
# s = 2xy + 2v/y +2v/x

# ds/dx = 2y + 0 -2v/x^2
# ds/dx = -2v/x^2 + 2y

# -2v/x^2 + 2y = 0
# -2v/x^2 = -2y
# 2v/x^2 = 2y
# 2v= 2yx^2
# 2v/2y = x^2
# x^2 = v/y
# x = +- sqrt(v/y)

def main():
    volume = int(sys.argv[1])
    yGuesses = []
    for y in range(2,int(sys.argv[2]) + 1):
        yGuesses.append([math.ceil(math.sqrt(volume/y)),y,math.ceil(volume/(math.sqrt(volume/y) * y))])
    smallestSurfaceArea = 999999
    for guess in yGuesses:
        if ((2*(guess[0]+2)*(guess[2]+2) + 2*(guess[0]+1)*guess[1] + 2*(guess[2]+1)*guess[1]) <= smallestSurfaceArea):
            smallestSurfaceArea = (2*(guess[0]+2)*(guess[2]+2) + 2*(guess[0]+1)*guess[1] + 2*(guess[2]+1)*guess[1])
    smallestDimentionList = []
    for guess in yGuesses:
        if ((2*(guess[0]+2)*(guess[2]+2) + 2*(guess[0]+1)*guess[1] + 2*(guess[2]+1)*guess[1]) == smallestSurfaceArea):
            smallestDimentionList.append([guess[0]+2,guess[1]+2,guess[2]+2])
    print (smallestDimentionList)
if __name__ == '__main__':
    main()

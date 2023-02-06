import sys, math
#input: volume, max internal height

def main():
    volume = int(sys.argv[1])
    yMax = int(sys.argv[2]) + 1
    smallestSurfaceArea = 999999
    smallestDimensionList = []
    for y in range(2, yMax):
        x = math.ceil(math.sqrt(volume/y))
        z = math.ceil(volume/(x * y))
        surfaceArea = 2 * (x + 2) * (z + 2) + 2 * (x + 1) * y + 2 * (z + 1) * y
        if surfaceArea < smallestSurfaceArea:
            smallestSurfaceArea = surfaceArea
            smallestDimensionList = [[x + 2, y + 2, z + 2]]
        elif surfaceArea == smallestSurfaceArea:
            smallestDimensionList.append([x + 2, y + 2, z + 2])
    print(smallestDimensionList)

if __name__ == '__main__':
    main()

pointList = []
lineList = []

def ReplaceABCD(a, b, c, d, string):
    string = string.replace("%a%", a)
    string = string.replace("%b%", b)
    string = string.replace("%c%", c)
    string = string.replace("%d%", d)
    return string

def CreatePoint(x, y):
    point = Point(x, y, len(pointList))
    pointList.append(point)
    return point
def CreateLine(startPoint, endPoint):
    line = Line(startPoint, endPoint, len(lineList))
    lineList.append(line)
    return line

def CreateLinesFromString(lineString):
    lineStrings = str(lineString).split("|")
    lineStrings = list(filter(None, lineStrings))
    points = []
    for line in lineStrings:
        points.append(str(line).split("_"))
    for point in points:
        startPoint = str(point[0]).split(",")
        endPoint = str(point[1]).split(",")
        CreateLine(CreatePoint(int(startPoint[0]), int(startPoint[1])), CreatePoint(int(endPoint[0]), int(endPoint[1])))
        
class Point:
    def __init__(self, x, y, pointID):
        self.x = x
        self.y = y
        self.pointID = pointID

class Line:
     def __init__(self, startPoint, endPoint, lineID):
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.lineID = lineID
        lineFunctionA = ReplaceABCD(str(startPoint.x), str(startPoint.y), str(endPoint.x), str(endPoint.y), "y-%b%=\\left\\{%a%<%c%:\\frac{\\left(%d%-%b%\\right)}{%c%-%a%}\\left(x-%a%\\right)\\left\\{%a%\\le x\\le %c%\\right\\}\\right\\}")
        lineFunctionB = ReplaceABCD(str(startPoint.x), str(startPoint.y), str(endPoint.x), str(endPoint.y), "y-%b%=\\left\\{%c%<%a%:\\frac{\\left(%d%-%b%\\right)}{%c%-%a%}\\left(x-%a%\\right)\\left\\{%c%\\le x\\le %a%\\right\\}\\right\\}")
        print(lineFunctionA)
        print(lineFunctionB)

testLineString = "|0,0_1,1|-1,1_4,3|"
CreateLinesFromString(testLineString)

#CreateLine(CreatePoint(0, 0), CreatePoint(1, 1))

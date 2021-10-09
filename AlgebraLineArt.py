pointList = []
lineList = []
use2Functions = False

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
        pointA = str(point[0]).split(",")
        pointB = str(point[1]).split(",")
        CreateLine(CreatePoint(pointA[0], pointA[1]), CreatePoint(pointB[0], pointB[1]))
        
class Point:
    def __init__(self, x, y, pointID):
        self.x = x
        self.y = y
        self.pointID = pointID
    
    def GetLefter(self, point): return self.x if self.x >= point.x else point.x
    def GetRighter(self, point): return self.x if self.x < point.x else point.x


class Line:
    def __init__(self, pointA: Point, pointB: Point, lineID):
        self.startPoint = pointA.GetLefter(pointB)
        self.endPoint = pointA.GetRighter(pointB)
        self.lineID = lineID
        global use2Functions
        if use2Functions:
            lineFunctionA = ReplaceABCD(str(self.startPoint.x), str(self.startPoint.y), str(self.endPoint.x), str(self.endPoint.y), "y-%b%=\\left\\{%a%<%c%:\\frac{\\left(%d%-%b%\\right)}{%c%-%a%}\\left(x-%a%\\right)\\left\\{%a%\\le x\\le %c%\\right\\}\\right\\}")
            lineFunctionB = ReplaceABCD(str(self.startPoint.x), str(self.startPoint.y), str(self.endPoint.x), str(self.endPoint.y), "y-%b%=\\left\\{%c%<%a%:\\frac{\\left(%d%-%b%\\right)}{%c%-%a%}\\left(x-%a%\\right)\\left\\{%c%\\le x\\le %a%\\right\\}\\right\\}")
            print(lineFunctionA)
            print(lineFunctionB)
        else:
            lineFunction = ReplaceABCD(str(self.startPoint.x), str(self.startPoint.y), str(self.endPoint.x), str(self.endPoint.y), "y-%b%=\\frac{\\left(%d%-%b%\\right)}{%c%-%a%}\\left(x-%a%\\right)\\left\\{%a%\\le x\\le %c%\\right\\}")
            print(lineFunction)

testLineString = "|0,0_1,1|-1,1_4,3|"
CreateLinesFromString(testLineString)

#CreateLine(CreatePoint(0, 0), CreatePoint(1, 1))

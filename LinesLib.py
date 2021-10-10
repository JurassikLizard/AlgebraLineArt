import pyperclip
import main

pointList = []
lineList = []

class Point:
    def __init__(self, x, y, pointID):
        self.x = x
        self.y = y
        self.pointID = pointID
    
    def GetLefter(self, point): return self if self.x <= point.x else point
    def GetRighter(self, point): return self if self.x > point.x else point

class Line:
    def __init__(self, pointA: Point, pointB: Point, lineID):
        self.startPoint = pointA.GetLefter(pointB)
        self.endPoint = pointA.GetRighter(pointB)
        self.lineID = lineID
        global use2Functions
        if main.use2Functions:
            functionString = ReplaceABCD(self.startPoint.x, self.startPoint.y, self.endPoint.x, self.endPoint.y, "y-%b%=\\left\\{%a%<%c%:\\frac{\\left(%d%-%b%\\right)}{%c%-%a%}\\left(x-%a%\\right)\\left\\{%a%\\le x\\le %c%\\right\\}\\right\\}") + "\n"
            functionString += ReplaceABCD(self.startPoint.x, self.startPoint.y, self.endPoint.x, self.endPoint.y, "y-%b%=\\left\\{%c%<%a%:\\frac{\\left(%d%-%b%\\right)}{%c%-%a%}\\left(x-%a%\\right)\\left\\{%c%\\le x\\le %a%\\right\\}\\right\\}") + "\n"
            functionString += ReplaceABCD(self.startPoint.x, self.startPoint.y, self.endPoint.x, self.endPoint.y, "x=\\left\\{%c%=%a%:\\ %a%\\left\\{%b%\\le y\\le %d%\\right\\}\\right\\}") + "\n"
            print(functionString)
            try:
                pyperclip.copy(functionString)
            except:
                return
        else:
            functionString = ReplaceABCD(self.startPoint.x, self.startPoint.y, self.endPoint.x, self.endPoint.y, "y-%b%=\\frac{\\left(%d%-%b%\\right)}{%c%-%a%}\\left(x-%a%\\right)\\left\\{%a%\\le x\\le %c%\\right\\}") + "\n"
            functionString += ReplaceABCD(self.startPoint.x, self.startPoint.y, self.endPoint.x, self.endPoint.y, "x=\\left\\{%c%=%a%:\\ %a%\\left\\{%b%\\le y\\le %d%\\right\\}\\right\\}") + "\n"
            print(functionString)
            main.copyBuffer += functionString

def ReplaceABCD(a, b, c, d, string):
    string = string.replace("%a%", str(a))
    string = string.replace("%b%", str(b))
    string = string.replace("%c%", str(c))
    string = string.replace("%d%", str(d))
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
import pyperclip
from TkinterLib import *
import decimal

decimal.getcontext().prec = 8

pointList = []
lineList = []

use2Functions = False
copyBuffer = ""

class Point:
    def __init__(self, x, y, pointID, isLocal: bool):
        if isLocal:
            self.localPos = Vector2(float(x), float(y))
            self.pos = LocalSpaceToGlobalSpace(Vector2(float(x), float(y)))
        else:
            self.localPos = GlobalSpaceToLocalSpace(Vector2(float(x), float(y)))
            self.pos = Vector2(float(x), float(y))
            
        self.pointID = pointID
    
    def GetLefter(self, point): return self if self.localPos.x <= point.pos.x else point
    def GetRighter(self, point): return self if self.localPos.x > point.pos.x else point

class Line:
    def __init__(self, pointA: Point, pointB: Point, lineID, canvasItemID):
        self.startPoint = pointA.GetLefter(pointB)
        self.endPoint = pointA.GetRighter(pointB)
        self.lineID = lineID
        self.canvasItemID = canvasItemID
        global use2Functions
        global copyBuffer
        localStartPosX = decimal.Decimal(self.startPoint.localPos.x) / decimal.Decimal(30)
        localStartPosY = decimal.Decimal(self.startPoint.localPos.y) / decimal.Decimal(30)
        localEndPosX = decimal.Decimal(self.endPoint.localPos.x) / decimal.Decimal(30)
        localEndPosY = decimal.Decimal(self.endPoint.localPos.y) / decimal.Decimal(30)
        if use2Functions:
            functionString = "\n" + ReplaceABCD(localStartPosX, localStartPosY, localEndPosX, localEndPosY, "y-%b%=\\left\\{%a%<%c%:\\frac{\\left(%d%-%b%\\right)}{%c%-%a%}\\left(x-%a%\\right)\\left\\{%a%\\le x\\le %c%\\right\\}\\right\\}")
            functionString += "\n" + ReplaceABCD(localStartPosX, localStartPosY, localEndPosX, localEndPosY, "y-%b%=\\left\\{%c%<%a%:\\frac{\\left(%d%-%b%\\right)}{%c%-%a%}\\left(x-%a%\\right)\\left\\{%c%\\le x\\le %a%\\right\\}\\right\\}")
            functionString += "\n" + ReplaceABCD(localStartPosX, localStartPosY, localEndPosX, localEndPosY, "x=\\left\\{%c%=%a%:\\ %a%\\left\\{%b%\\le y\\le %d%\\right\\}\\right\\}")
            print(functionString)
            copyBuffer += functionString
        else:
            functionString = "\n" + ReplaceABCD(localStartPosX, localStartPosY, localEndPosX, localEndPosY, "y-%b%=\\frac{\\left(%d%-%b%\\right)}{%c%-%a%}\\left(x-%a%\\right)\\left\\{%a%\\le x\\le %c%\\right\\}")
            functionString += "\n" + ReplaceABCD(localStartPosX, localStartPosY, localEndPosX, localEndPosY, "x=\\left\\{%c%=%a%:\\ %a%\\left\\{%b%\\le y\\le %d%\\right\\}\\right\\}")
            print(functionString)
            copyBuffer += functionString

def ReplaceABCD(a, b, c, d, string):
    string = string.replace("%a%", str(a))
    string = string.replace("%b%", str(b))
    string = string.replace("%c%", str(c))
    string = string.replace("%d%", str(d))
    return string

def CreatePoint(x, y, isLocal: bool):
    point = Point(x, y, len(pointList), isLocal)
    pointList.append(point)
    return point

def CreateLine(startPoint, endPoint, canvasItemID):
    line = Line(startPoint, endPoint, len(lineList), canvasItemID)
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
        CreateLine(CreatePoint(pointA[0], pointA[1], True), CreatePoint(pointB[0], pointB[1], True))

def Copy():
    global copyBuffer
    pyperclip.copy(copyBuffer)
    copyBuffer = ""
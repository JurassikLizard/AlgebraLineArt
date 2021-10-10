import pyperclip
import LinesLib

use2Functions = False
copyBuffer = ""

def Copy():
    global copyBuffer
    pyperclip.copy(copyBuffer)
    copyBuffer = ""

testLineString = "|1,0_1,1|-1,1_4,3|"
LinesLib.CreateLinesFromString(testLineString)
Copy()
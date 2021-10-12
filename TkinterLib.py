import tkinter as tk
from typing import *
from vector import Vector2
import LinesLib

# --- constants --- (UPPER_CASE_NAMES)

# --- main --- (lower_case_names)

center: Vector2 = Vector2(0, 0)
current = None
currentXY = None
c: tk.Canvas = None

def GlobalSpaceToLocalSpace(world: Vector2) -> Vector2:
    position: Vector2 = world - center
    position.y = -position.y
    return position
def LocalSpaceToGlobalSpace(local: Vector2) -> Vector2: 
    position: Vector2 = Vector2(local.x, -local.y)
    return position + center

def main():
    # TODO: Hold Geometry positions relative to center of screen
    
    def create_grid(event=None):
        w = c.winfo_width() # Get current width of canvas
        h = c.winfo_height() # Get current height of canvas
        c.delete('grid_line') # Will only remove the grid_line
        
        global center

        middleVertical = int(round((w / 30) / 2)) # Middle line
        currentVertical = 0
        # Creates all vertical lines at intevals of 20
        for i in range(0, w, 30):
            c.create_line([(i, 0), (i, h)], tag='grid_line') if currentVertical != middleVertical else c.create_line([(i, 0), (i, h)], tag='grid_line', fill="red", width=2)
            if currentVertical == middleVertical: center = Vector2(i, center[1])
            currentVertical += 1

        middleHorizontal = int(round((h / 30) / 2)) # Middle line
        currentHorizontal = 0
        # Creates all horizontal lines at intevals of 20
        for i in range(0, h, 30):
            c.create_line([(0, i), (w, i)], tag='grid_line') if currentHorizontal != middleHorizontal else c.create_line([(0, i), (w, i)], tag='grid_line', fill="red", width=2)
            if currentHorizontal == middleHorizontal: center = Vector2(center[0], i)
            currentHorizontal += 1

        line: LinesLib.Line
        c.delete("line")
        for line in LinesLib.lineList:
            if line.canvasItemID:
                line.startPoint.pos = LocalSpaceToGlobalSpace(line.startPoint.localPos)
                line.endPoint.pos = LocalSpaceToGlobalSpace(line.endPoint.localPos)
                CreateLine(line.startPoint.pos.x, line.startPoint.pos.y, line.endPoint.pos.x, line.endPoint.pos.y)
    
    root = tk.Tk()

    global c
    c = tk.Canvas(root, height=500, width=500, bg='white')
    c.pack(fill=tk.BOTH, expand=True)

    c.bind('<Configure>', create_grid)
    c.bind("<Escape>", reset)
    c.bind("<Motion>", motion)
    c.bind("<ButtonPress-1>", mousedown)

    root.mainloop()
    

def reset(event):
    global current
    global currentXY
    c.delete(current)
    current = None
    currentXY = None

def mousedown(event):
    global current
    global currentXY

    c.focus_set()  # so escape key will work

    if current is None:
        # the new line starts where the user clicked
        x0 = event.x
        y0 = event.y
        currentXY = (x0, y0)
        current = CreateLine(x0, y0, event.x, event.y)

    else:
        # the new line starts at the end of the previously
        # drawn line
        coords = c.coords(current)
        x0 = coords[2]
        y0 = coords[3]

        current = CreateLine(x0, y0, event.x, event.y)
        print("<MouseDown>")
        print(c.coords(current))
        LinesLib.CreateLine(LinesLib.CreatePoint(currentXY[0], currentXY[1], False), LinesLib.CreatePoint(event.x, event.y, False), current)

        currentXY = (x0, y0)
    

def motion(event):
    if current:
        # modify the current line by changing the end coordinates
        # to be the current mouse position
        coords = c.coords(current)
        coords[2] = event.x
        coords[3] = event.y

        c.coords(current, *coords)

def CreateLine(x1, y1, x2, y2):
    return c.create_line(x1, y1, x2, y2, tag="line")

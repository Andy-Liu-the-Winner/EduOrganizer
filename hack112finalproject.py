from cmu_graphics import *

def onAppStart(app):
    app.isAssignmentPage = True
    app.tasks = []
    app.color = 'red'
    app.colorlist = []
    app.colorListInInputSection = [rgb(255,0,0),rgb(0,112,60),rgb(14,76,146)]
    app.dueDate = []
    app.drawXList = []
    app.completedTasks = []
    app.showDates = [True, False, False, False, False]
    app.classes = {'monday':[], 'tuesday':[], 'wednesday':[], 'thursday':[], 'friday':[]}
    app.rows = 6
    app.cols = 1
    app.boardLeft = 0
    app.boardTop = 0
    app.boardWidth = app.width
    app.boardHeight = 90.5*6
    app.cellBorderWidth = 2
    app.addtask = 'Click to add tasks here!'

def activateAssignments(app):
    drawTaskSection(app)
    drawInputSection(app)

def drawTaskSection(app):
    drawBoard(app)
    drawBoardBorder(app)
    drawTask(app)

def drawInputSection(app):
    drawLabel('Add tasks',0,550,align = 'left')
    drawLine(0,557,550,557)
    drawRect(290,557,100/3,43,fill = app.colorListInInputSection[0])
    drawRect(323,557,100/3,43,fill = app.colorListInInputSection[1])
    drawRect(356,557,100/3,43,fill = app.colorListInInputSection[2])

    drawRect(290,557,100,43,fill = None, border = 'black')
    drawLine(290+100/3,557,290+100/3,600)
    drawLine(290+100*2/3,557,290+100*2/3,600)
    drawLabel('CMURed',290+100/6,557+43/2,size = 7,bold = True)
    drawLabel('DartGreen',290+100*3/6,557+43/2,size = 7,bold = True)
    drawLabel('YaleBlue',290+100*5/6,557+43/2,size = 7,bold = True)
    drawLabel(app.addtask,10,600-43/2,align = 'left')
    drawRect(7,560,130,40,fill = None,border = 'black')

# Activates schedule page
def activateSchedule(app):
    drawDates()
    drawScheduler()

# Draws top button dates
def drawDates():
    dates = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    drawRect(0, 0, 550, 50, fill=rgb(211,211,211))
    for i in range(50, 456, 100):
        drawRect(i, 25, 90, 30, fill=None, align='center', border=rgb(69, 115, 115), borderWidth=5)
    centerX = 50
    for day in dates:
        drawLabel(day, centerX, 25, align='center')
        centerX += 100

def drawScheduler():
    drawLabel('+', 525, 25, align='center', size=20)
    drawRect(525, 25, 30, 30, fill=None, border=rgb(69, 115, 115), borderWidth=5, align='center')

def scheduleInterface(app):
    newClass = app.getTextInput("What class would you like to add?")
    day = app.getTextInput("What day do you have that class? (only input one day)")
    newStartTime = app.getTextInput("What time does that class start?")
    newEndTime = app.getTextInput("What time does that class end?")
    location = app.getTextInput("Where does your class take place?")
    app.classes[day.lower()].append([newClass, newStartTime, newEndTime, location])

def onMousePress(app,mouseX,mouseY):
    if clickingAssignmentPage(app,mouseX,mouseY,app.isAssignmentPage):
        app.isAssignmentPage = True
    if clickingSchedulePage(app,mouseX,mouseY,app.isAssignmentPage):
        app.isAssignmentPage = False
    if(app.isAssignmentPage):
        if clickingAddTask(app,mouseX,mouseY):
            app.tasks.append(app.getTextInput("Click to add tasks here!"))
            app.dueDate.append(app.getTextInput("Put Due Date here!"))
        if len(app.tasks) >= len(app.colorlist):
            if clickingRed(app,mouseX,mouseY):
                app.colorlist.append(app.colorListInInputSection[0])
            if clickingGreen(app,mouseX,mouseY):
                app.colorlist.append(app.colorListInInputSection[1])
            if clickingBlue(app,mouseX,mouseY):
                app.colorlist.append(app.colorListInInputSection[2])
        clickingcheckbox(app,mouseX,mouseY)
    elif(app.isAssignmentPage == False):
        if clickingMonday(app,mouseX,mouseY):
            app.showDates = [False]*5
            app.showDates[0] = True
        elif clickingTuesday(app,mouseX,mouseY):
            app.showDates = [False]*5
            app.showDates[1] = True
        elif clickingWednesday(app,mouseX,mouseY):
            app.showDates = [False]*5
            app.showDates[2] = True
        elif clickingThursday(app,mouseX,mouseY):
            app.showDates = [False]*5
            app.showDates[3] = True
        elif clickingFriday(app,mouseX,mouseY):
            app.showDates = [False]*5
            app.showDates[4] = True
        elif clickingPlus(app,mouseX,mouseY):
            scheduleInterface(app)

def onKeyPress(app,key):
    if(app.isAssignmentPage):
        if key == 'down' or key == 'right':
            length = len(app.tasks)
            if length > 6:
                app.tasks = app.tasks[6:] + app.tasks[:6]
                app.dueDate = app.dueDate[6:] + app.dueDate[:6]
        if key == 'up' or key == 'left':
            length = len(app.tasks)
            if length > 6:
                app.tasks = app.tasks[-6:] + app.tasks[:-6]
                app.dueDate = app.dueDate[-6:] + app.dueDate[:-6]

def clickingRed(app,mouseX,mouseY):
    return buttonPress(mouseX,mouseY,290,557,323,600)
        

def clickingGreen(app,mouseX,mouseY):
    return buttonPress(mouseX,mouseY,323,557,357,600)
        


def clickingBlue(app,mouseX,mouseY):
    return buttonPress(mouseX,mouseY,357,557,389,600)

def clickingcheckbox(app,mouseX,mouseY):
    for i in range(6):
        if buttonPress(mouseX,mouseY,10,35+i*90.5,30,55+i*90.5):
            if i not in app.completedTasks:
                app.completedTasks.append(i)
                print(app.drawXList)
            else:
                app.completedTasks.remove(i)

def drawTask(app):
    halflength = 90.5/2
    for i in range(len(app.tasks)):
        drawLabel(app.tasks[i],40,90*i+halflength,align = 'left',fill = app.colorlist[i],size = 25,font = 'monospace')
        drawLabel(app.dueDate[i],380,90*i+halflength,align = 'left',fill = app.colorlist[i],size = 25,font = 'monospace')
        drawRect(10,90.5*i+halflength-10,20,20,fill = None,border = 'black')
        if i == 5:
            return
    for i in range(len(app.completedTasks)):
        drawLabel('X', 15, 45 + 90.5 * app.completedTasks[i],align = 'left' )
    
def clickingAddTask(app,mouseX,mouseY):
    return buttonPress(mouseX, mouseY,7,560,137,600)

# cited from CMU CS academy
# the method to create a cell for our input section

def drawBoard(app):
    for row in range(app.rows):
        for col in range(app.cols):
            drawCell(app, row, col)

def drawBoardBorder(app):
  # draw the board outline (with double-thickness):
  drawRect(app.boardLeft, app.boardTop, app.boardWidth, app.boardHeight,
           fill=None, border='black',
           borderWidth=2*app.cellBorderWidth)

def drawCell(app, row, col):
    cellLeft, cellTop = getCellLeftTop(app, row, col)
    cellWidth, cellHeight = getCellSize(app)
    drawRect(cellLeft, cellTop, cellWidth, cellHeight,
             fill=None, border='black',
             borderWidth=app.cellBorderWidth)

def getCellLeftTop(app, row, col):
    cellWidth, cellHeight = getCellSize(app)
    cellLeft = app.boardLeft + col * cellWidth
    cellTop = app.boardTop + row * cellHeight
    return (cellLeft, cellTop)

def getCellSize(app):
    cellWidth = app.boardWidth / app.cols
    cellHeight = app.boardHeight / app.rows
    return (cellWidth, cellHeight)

# return a boolean to check if the mouse is clicking on the button
def buttonPress(mouseX, mouseY,x1,y1,x2,y2):
    if x1<= mouseX <=x2 and y1<= mouseY <=y2:
        return True
    return False

# return a boolean if we are clicking assignment page
def clickingAssignmentPage(app,mouseX,mouseY,isAssignmentPage):
    if buttonPress(mouseX, mouseY,20,615,260,685):
        return True
 
# return a boolean if we are clicking schedule page
def clickingSchedulePage(app,mouseX,mouseY,isAssignmentPage):
    if buttonPress(mouseX, mouseY,290,615,530,685):
        return True 
    
### DAY FUNCTIONS ###
def clickingMonday(app, mouseX, mouseY):
    if buttonPress(mouseX,mouseY,5,10,95,40):
        return True

def clickingTuesday(app, mouseX, mouseY):
    if buttonPress(mouseX,mouseY,105,10,195,40):
        return True
    
def clickingWednesday(app,mouseX,mouseY):
    if buttonPress(mouseX,mouseY,205,10,295,40):
        return True
    
def clickingThursday(app,mouseX,mouseY):
    if buttonPress(mouseX,mouseY,305,10,395,40):
        return True
    
def clickingFriday(app,mouseX,mouseY):
    if buttonPress(mouseX,mouseY,405,10,495,50):
        return True
##########################

def clickingPlus(app,mouseX,mouseY):
    if buttonPress(mouseX,mouseY,510,10,540,40):
        return True

def redrawAll(app):
    drawBottomButtons()
    if(app.isAssignmentPage):
        activateAssignments(app)
    else:
        activateSchedule(app)
        dates = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        for i in range(len(app.showDates)):
            currentBottom = -60
            if(app.showDates[i]):
                for lists in app.classes[dates[i]]:
                    currentBottom += 110
                    newClass = lists[0]
                    newStartTime = lists[1]
                    newEndTime = lists[2]
                    location = lists[3]
                    drawRect(10, currentBottom+10, 530, 100, fill=rgb(69, 115, 115))
                    drawLabel(newClass, 20, currentBottom+30, fill='white', size=25, align='left', bold=True)
                    drawLabel('TIME', 20, currentBottom+50, fill='white', align='left', opacity=70, size=10)
                    drawLabel(f'{newStartTime} to {newEndTime}', 20, currentBottom+65, size=15, align='left', fill='white')
                    drawLabel('LOCATION', 20, currentBottom+80, align='left', opacity=70, size=10, fill='white')
                    drawLabel(location, 20, currentBottom+95, align='left', size=15, fill='white')

def drawBottomButtons():
    drawRect(0, 600, 550, 350, fill=rgb(211, 211, 211))
    drawRect(20, 615, 240, 70, fill=rgb(205, 126, 89))
    drawRect(290, 615, 240, 70, fill=rgb(69, 115, 115))
    drawLabel('Assignments', 140, 650, fill='white', size=20)
    drawLabel('Schedule', 410, 650, fill='white', size=20)

def main():
    runApp(width=550, height=700)

main()
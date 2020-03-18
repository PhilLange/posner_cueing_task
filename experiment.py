from constants import *
from psychopy.visual import Window, TextStim, shape, Circle, Rect
from psychopy.event import waitKeys
from psychopy.core import wait

disp = Window(size=DISPSIZE, units='pix', color=BGC, fullscr=True)

instructions = 'Willkommen! \n\nIn diesem Experiment werden die Buchstaben E und F auf dem ' \
               'Bildschirm erscheinen. Wenn du eine E siehst, drücke das E. Wenn du ein F siehst' \
               ', drücke das F \n\n Versuche so genau und schnell wie möglich zu antworten. \n\n' \
               'Viel Glück!'

inststim = TextStim(disp, units='pix', text=instructions, color=FGC, height=35)
fixstim = Circle(disp, radius=6, edges = 32, lineColor = FGC, fillColor = FGC)

lboxstim = Rect(disp, pos=BOXCORS['left'], width=BOXSIZE, height=BOXSIZE, lineColor = FGC,
                lineWidth=3)
rboxstim = Rect(disp, pos=BOXCORS['right'], width=BOXSIZE, height=BOXSIZE, lineColor = FGC,
                lineWidth=3)
cuestim = {}

cuestim['left'] = Rect(disp, pos=BOXCORS['left'], width=BOXSIZE, height=BOXSIZE, lineColor = FGC,
                lineWidth=8)

cuestim['right'] = Rect(disp, pos=BOXCORS['right'], width=BOXSIZE, height=BOXSIZE, lineColor = FGC,
                lineWidth=8)

tarscr = {}

tarscr['left']  = {}
tarscr['right'] = {}

tarscr['left']['E'] = TextStim(disp, text='E', pos=BOXCORS['left'], height=48, color=FGC)
tarscr['left']['F'] = TextStim(disp, text='F', pos=BOXCORS['left'], height=48, color=FGC)
tarscr['right']['E'] = TextStim(disp, text='E', pos=BOXCORS['right'], height=48, color=FGC)
tarscr['right']['F'] = TextStim(disp, text='F', pos=BOXCORS['right'], height=48, color=FGC)

# feedback screens
fbstim = {}
fbstim[0] = TextStim(disp, text='Incorrect', height=24, color=(1, 1, -1))
fbstim[1] = TextStim(disp, text='Correct', height=24, color=(-1, 1, -1))

# present instructions
inststim.draw()
disp.flip()
waitKeys(maxWait=float('inf'), keyList=None, timeStamped=True) # wait for key press




for cueside in ['left', "right"]:
# draw fixation mark and left and right boxes
    fixstim.draw()
    lboxstim.draw()
    rboxstim.draw()
    fixonset = disp.flip()
    wait(FIXTIME)

    fixstim.draw()
    lboxstim.draw()
    rboxstim.draw()
    cuestim[cueside].draw()
    cueonset = disp.flip()
    wait(CUETIME)
    fixstim.draw()
    lboxstim.draw()
    rboxstim.draw()
    cueoffset = disp.flip()
    wait(0.1 - CUETIME)
    fixstim.draw()
    lboxstim.draw()
    rboxstim.draw()
    tarscr['right']['E'].draw()
    taronset = disp.flip()

    resplist = waitKeys(maxWait=float('inf'), keyList=['e', 'f'], timeStamped=True)

    response, presstime = resplist[0]
    response = response.upper()

    if response == 'E':
        correct = 1
    else:
        correct = 0

    rt = presstime - taronset

    if correct:
        fbstim[1].draw()
    else:
        fbstim[0].draw()
    disp.flip()
    wait(FBTIME)
disp.close()


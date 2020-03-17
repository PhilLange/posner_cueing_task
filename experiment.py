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
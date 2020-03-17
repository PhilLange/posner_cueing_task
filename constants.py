# display constans
DISPSIZE = (4096, 2304)
FGC = (-1,-1,-1)
BGC = (0, 0, 0)
# stimuli constants
CUELOC = ['right', 'left']
TARLOC = ['right', 'left']
SOAS   = [0.1, 0.9]
TARGETS= ['E', 'F']
# timing constants
FIXTIME = 1.5
CUETIME = 0.5
FBTIME  = 1.0

# squares for cues
BOXSIZE = 200
BOXCORS  = {}
BOXCORS['left'] = (int(DISPSIZE[0]*-0.25), 0)
BOXCORS['right'] = (int(DISPSIZE[0]*0.25), 0)

cuestim = {}



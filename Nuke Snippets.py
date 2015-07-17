#####################   SNIPPETS // MEL MASSADIAN ###########################

####################################################### menu.py commands

#######   ADD TO TOP MENU   #######
MEL_menu = nuke.menu('Nuke').addMenu('Mel')

#######   ADD AN ITEM TO EXISTING MENU   #######
t = nuke.menu('Nuke') # this calls the top menu
st = t.findItem('menu/elementName')
st.addCommand('name','function','hotkey',icon='filename.png', index=positionNumber)

#######   ADD FORMAT RESOLUTION PRESET   #######
nuke.addFormat('width height 0 0 width height 1.0 nomDuPreset')


#######   If Write dir does not exist, create it   #######
def createWriteDir(): 
    file = nuke.filename(nuke.thisNode()) 
    dir = os.path.dirname( file ) 
    osdir = nuke.callbacks.filenameFilter( dir ) 
    try: 
        os.makedirs( osdir ) 
        return 
    except: 
        return
# Activate the createWriteDir function
nuke.addBeforeRender( createWriteDir )




#######   MY DEFAULTS   #######

nuke.knobDefault("Root.format", "HD_1080")  # Set Root to HD by Default
nuke.knobDefault("Root.fps", "25")  #Set Root to PAL by Default
nuke.addFormat('2400 1350 0 0 2400 1350 1.0 BMD 2.5K') # Add the BM2.5K Camera Resolution in the formats.
nuke.knobDefault("EXPTool.mode", "0")
nuke.knobDefault("RotoPaint.toolbox", "brush {{brush ltt 0} {clone ltt 0}}") # Set the Brush and the Clone tools to All Frames by Default.
nuke.knobDefault("Roto.feather_type", "smooth") # Default Feather to Smooth
nuke.knobDefault("RotoPaint.feather_type", "smooth")
nuke.knobDefault("FrameRange.label", "[value this.knob.first_frame] - [value this.knob.last_frame]") # Add a Label to the FrameRange node displaying the frameRange value
nuke.knobDefault("Read.icon","mel_logo.png") # Add a logo to a node
nuke.knobDefault('Write.mov.colorspace', 'sRGB') # Make Write Mov node default to sRGB color space



####################################################### GENERAL SNIPPETS


#######   SAMPLE READ NODE PIXELS AND CREATE DOT ART   #######

n = nuke.selectedNode()

colNum = 50
rowNum = 30
dotSpacing = 15
colStep = n.width()/colNum+1
rowStep = n.height()/rowNum+1

for sy in range(rowNum):

    for sx in range(colNum):
     
        r = n.sample('r', sx*colStep, sy*rowStep)
        g = n.sample('g', sx*colStep, sy*rowStep)
        b = n.sample('b', sx*colStep, sy*rowStep)
        hex = int('%02x%02x%02x%02x' % (r*255,g*255,b*255,1),16) 
        d = nuke.nodes.Dot()
        d.setXYpos(sx*dotSpacing, ((rowNum*dotSpacing) - sy*dotSpacing))
        d['hide_input'].setValue(True)
        d['tile_color'].setValue(hex)
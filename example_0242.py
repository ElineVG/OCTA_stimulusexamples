"""
OCTA toolbox example stimuli
Example stimulus 242
created by Eline Van Geert
Icon used: https://uxwing.com/comma-icon/

Seven frieze patterns (less customizable but easier version)
WITH color changes 1
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.Positions import Positions
from octa.patterns import GridPattern
from octa.shapes import PathSvg, Image, Rectangle

# Define stimulus name
stimname = "example_0242"

# Info starting shape
baseshape = PathSvg("img/comma.svg")
basesize = (100,100)
x_translation_distance = basesize[0] + 0

# Number of translations should be an even number!
n_translations = 8

# Stimulus parameters 
figsize = ((basesize[0]*n_translations)+basesize[0]/2, (basesize[1]*2)+basesize[1]/2)
figsize_halfline = ((basesize[0]*n_translations)+basesize[0]/2, (basesize[1])+basesize[1]/2)
background = "white"

# 1) Define stimulus p111 (T)
stimulus = Grid(n_cols = n_translations, n_rows = 1,
                col_spacing = basesize[0], row_spacing = basesize[1], 
                background_color = background, size = figsize_halfline)
stimulus.shapes = GridPattern.RepeatAcrossElements([baseshape])
stimulus.fillcolors = GridPattern.RepeatAcrossElements(["black", "red"])
stimulus.boundingboxes = GridPattern.RepeatAcrossElements([basesize])
stimulus.Show()
stimulus.SaveSVG(stimname + "p111", folder = "svg")

# 2) Define stimulus pm11 (TV)
stimulus = Grid(n_cols = n_translations, n_rows = 1,
                col_spacing = basesize[0], row_spacing = basesize[1], 
                background_color = background, size = figsize_halfline)
stimulus.shapes = GridPattern.RepeatAcrossElements([baseshape])
stimulus.fillcolors = GridPattern.RepeatAcrossElements(["red", "black"])
stimulus.boundingboxes = GridPattern.RepeatAcrossElements([basesize])
stimulus.mirrorvalues = GridPattern.RepeatAcrossColumns(["none", "vertical"])
stimulus.Show()
stimulus.SaveSVG(stimname + "pm11", folder = "svg")

# 3) Define stimulus p1a1 (TG)
stimulus = Grid(n_cols = n_translations, n_rows = 1,
                col_spacing = basesize[0], row_spacing = basesize[1], 
                background_color = background, size = figsize)
stimulus.shapes = GridPattern.RepeatAcrossElements([baseshape])
stimulus.fillcolors = GridPattern.RepeatAcrossElements(["black", "red"])
stimulus.boundingboxes = GridPattern.RepeatAcrossElements([basesize])
stimulus.mirrorvalues = GridPattern.RepeatAcrossElements(["none", "horizontal"])
stimulus.positions.SetPositionDeviations(element_id = list(range(0,n_translations,2)), x_offset = 0,
                                         y_offset = -basesize[1])
stimulus.Show()
stimulus.SaveSVG(stimname + "p1a1", folder = "svg")

# 4) Define stimulus p112 (TR)
stimulus = Grid(n_cols = n_translations, n_rows = 1,
                col_spacing = basesize[0], row_spacing = basesize[1], 
                background_color = background, size = figsize)
stimulus.shapes = GridPattern.RepeatAcrossElements([baseshape])
stimulus.fillcolors = GridPattern.RepeatAcrossElements([ "red", "black"])
stimulus.boundingboxes = GridPattern.RepeatAcrossElements([basesize])
stimulus.orientations = GridPattern.RepeatAcrossElements([0,180])
stimulus.positions.SetPositionDeviations(element_id = list(range(0,n_translations,2)), x_offset = 0,
                                         y_offset = -basesize[1])
stimulus.Show()
stimulus.SaveSVG(stimname + "p112", folder = "svg")

# 5) Define stimulus p1m1 (THG)
stimulus = Grid(n_cols = n_translations, n_rows = 2,
                col_spacing = basesize[0], row_spacing = basesize[1], 
                background_color = background, size = figsize)
stimulus.shapes = GridPattern.RepeatAcrossElements([baseshape])
stimulus.fillcolors = GridPattern.RepeatAcrossRows(["black", "red"])
stimulus.boundingboxes = GridPattern.RepeatAcrossElements([basesize])
stimulus.mirrorvalues = GridPattern.RepeatAcrossRows(["none", "horizontal"])
stimulus.Show()
stimulus.SaveSVG(stimname + "p1m1", folder = "svg")

# 6) Define stimulus pma2(TRVG)
stimulus = Grid(n_cols = n_translations, n_rows = 1,
                col_spacing = basesize[0], row_spacing = basesize[1], 
                background_color = background, size = figsize)
stimulus.shapes = GridPattern.RepeatAcrossElements([baseshape])
stimulus.fillcolors = GridPattern.RepeatAcrossElements(["black", "black", "red", "red"])
stimulus.boundingboxes = GridPattern.RepeatAcrossElements([basesize])
stimulus.mirrorvalues = GridPattern.RepeatAcrossColumns(["none", "vertical", "vertical", "none"])
stimulus.orientations = GridPattern.RepeatAcrossColumns([0, 0, 180, 180])
stimulus.positions.SetPositionDeviations(element_id = [0,1,4,5], x_offset = 0,
                                         y_offset = -basesize[1])
stimulus.Show()
stimulus.SaveSVG(stimname + "pma2", folder = "svg")

# 7) Define stimulus pmm2 (TRHVG)
stimulus = Grid(n_cols = n_translations, n_rows = 8,
                col_spacing = basesize[0], row_spacing = basesize[1], 
                background_color = background, y_margin = [20, 20-6*basesize[1]])
stimulus.shapes = GridPattern.RepeatAcrossRows([baseshape, baseshape, None, None, None, None, None, None])
stimulus.fillcolors = GridPattern.RepeatAcrossRows(["black", "red"])
stimulus.boundingboxes = GridPattern.RepeatAcrossElements([basesize])
stimulus.mirrorvalues = GridPattern.TiledGrid(GridPattern.RepeatAcrossElements(["none", "vertical", "horizontal", "horizontalvertical"],2,2),4)
stimulus.Show()
stimulus.SaveSVG(stimname + "pmm2", folder = "svg")

### Define combined stimulus ###
stim = Grid(n_rows = 7 + 6, n_cols = 1, 
            row_spacing = 2*basesize[1], x_margin = 0, y_margin = [-50,0])

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements([figsize_halfline, figsize_halfline, 
                                                       figsize,
                                                       figsize, figsize,
                                                       figsize, figsize,
                                                       ((basesize[0]*n_translations)+basesize[0]/2, 1),
                                                       ((basesize[0]*n_translations)+basesize[0]/2, 1),
                                                       ((basesize[0]*n_translations)+basesize[0]/2, 1),
                                                       ((basesize[0]*n_translations)+basesize[0]/2, 1),
                                                       ((basesize[0]*n_translations)+basesize[0]/2, 1),
                                                       ((basesize[0]*n_translations)+basesize[0]/2, 1)])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements([Image("svg/" + stimname + "p111.svg"), 
                                                Image("svg/" + stimname + "pm11.svg"), 
                                                Image("svg/" + stimname + "p1a1.svg"),
                                                Image("svg/" + stimname + "p112.svg"), 
                                                Image("svg/" + stimname + "p1m1.svg"),
                                                Image("svg/" + stimname + "pma2.svg"),
                                                Image("svg/" + stimname + "pmm2.svg"),
                                                      Rectangle,Rectangle,Rectangle,
                                                      Rectangle,Rectangle,Rectangle])

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements(["black"])

# Change element positions
new_x = [0,0,0,0,0,0,0,0,0,0,0,0,0]
new_y = [0, basesize[1]+50, 3*basesize[1]+50,         
         5*basesize[1]+100, 7*basesize[1]+150,9*basesize[1]+200,11*basesize[1]+250,
         75,basesize[1]+50+75,3*basesize[1]+100+75,
         5*basesize[1]+150+75, 7*basesize[1]+200+75,9*basesize[1]+250+75]
stim.positions = Positions.CreateCustomPositions(x = new_x, y = new_y)

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")

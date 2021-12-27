"""
OCTA toolbox example stimuli
Example stimulus 100
created by Eline Van Geert

Images used: CC by Hůla and Flegr (2016)
https://doi.org/10.7717/peerj.2106
https://figshare.com/s/7306f12659f68f7f3d9d
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Image
import random

# Define stimulus name
stimname = "example_0100"

random.seed(5)

# Define stimulus
stim = Grid(n_rows = 6, n_cols = 6, background_color = "black", row_spacing = 35, col_spacing = 35, size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements([(30,30)]).AddUniformJitter(-10,10, axis = "x=y")

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossColumns( [ Image('img/Linum austriacum 3.jpg'),
                                                 Image('img/Lunaria annua 1.jpg')
                                             ] )

# Add orientations for the elements
stim.orientations = GridPattern.RepeatAcrossElements([0]).AddUniformJitter(-180,180, axis = "x=y")

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")
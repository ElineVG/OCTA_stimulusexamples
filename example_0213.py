"""
OCTA toolbox example stimuli
Example stimulus 213
created by Eline Van Geert
Image used: fox by Horoofi from Pixabay
https://pixabay.com/illustrations/fox-animal-cartoon-drawing-sketch-3823023/

Frieze pattern 4: p112 (translation & 180° rotation)
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Image

# Define stimulus name
stimname = "example_0213"

# Info starting shape
baseshape = Image("img/fox.jpg")
basesize = (100,100)
x_translation_distance = 2*basesize[0] + 0

# Number of translations should be an even number!
n_translations = 8

# Stimulus parameters 
figsize = ((x_translation_distance*int(n_translations/2))+x_translation_distance/2, (basesize[1]*2)+basesize[1]/2)
background = "white"

# Create template tile
stimulus = Grid(n_cols = 2, n_rows = 1,
                col_spacing = basesize[0], row_spacing = basesize[1], 
                background_color = background, size = (2*basesize[0], 2*basesize[1]))
stimulus.shapes = GridPattern.RepeatAcrossElements([baseshape])
stimulus.boundingboxes = GridPattern.RepeatAcrossElements([basesize])
stimulus.orientations = GridPattern.RepeatAcrossElements([0,180])
stimulus.positions.SetPositionDeviations(element_id = [1], x_offset = 0, y_offset = basesize[1])
stimulus.SaveSVG(stimname + "_template", folder = "svg")

# Define stimulus
stim = Grid(n_rows = 1, n_cols = int(n_translations/2), 
            row_spacing = 2*basesize[1], col_spacing = x_translation_distance, size = figsize)

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.MirrorAcrossElements([(2*basesize[0], 2*basesize[1])])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements([Image("svg/" + stimname + "_template.svg")])

# Add orientations for the elements
stim.orientations = GridPattern.RepeatAcrossElements([0,180])

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")

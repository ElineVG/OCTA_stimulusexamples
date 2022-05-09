"""
OCTA toolbox example stimuli
Example stimulus 214
created by Eline Van Geert
Image used: fox by Horoofi from Pixabay
https://pixabay.com/illustrations/fox-animal-cartoon-drawing-sketch-3823023/

Frieze pattern: p2mg (IUCr) or 'spinning sidle' (Conway) or TRVG (translations, 180° rotations, vertical reflection lines, and glide reflections)
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Image

# Define stimulus name
stimname = "example_0214"

# Info starting shape
baseshape = Image("img/fox.jpg")
basesize = (100,100)
x_glide_distance = 2*basesize[0] 
x_translation_distance = x_glide_distance + 0

# Number of translations should be an even number!
n_translations = 4

# Stimulus parameters 
background = "white"

# Create template1 tile
stimulus = Grid(n_cols = 2, n_rows = 1,
                col_spacing = basesize[0], row_spacing = basesize[1], 
                background_color = background, size = (2*basesize[0], basesize[1]))
stimulus.shapes = GridPattern.RepeatAcrossElements([baseshape])
stimulus.boundingboxes = GridPattern.RepeatAcrossElements([basesize])
stimulus.mirrorvalues = GridPattern.RepeatAcrossElements(["none", "vertical"])
stimulus.SaveSVG(stimname + "_template", folder = "svg")

# Define stimulus
stim = Grid(n_rows = 1, n_cols = n_translations, 
            row_spacing = basesize[1], col_spacing = x_translation_distance)

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements([(2*basesize[0], basesize[1])])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements([Image("svg/" + stimname + "_template.svg")])

# Add orientations for the elements
stim.orientations = GridPattern.RepeatAcrossElements([0, 180])

# Change element positions
stim.positions.SetPositionDeviations(element_id = list(range(0,n_translations, 2)), x_offset = 0, y_offset = -basesize[1])

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")

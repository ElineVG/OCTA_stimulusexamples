"""
OCTA toolbox example stimuli
Example stimulus 102
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Ellipse, PathSvg
import random

# Define stimulus name
stimname = "example_0102"

# Set seed
random.seed(5)

# Define stimulus
stim = Grid(n_rows = 18, n_cols = 18, background_color = "none", row_spacing = 12, col_spacing = 12, size = (250,250) )

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossLayers( [ (10,10), (6,6) ] ).AddUniformJitter(-2,2, 'x=y')

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossLayers( [ PathSvg('img/flower-svgrepo.svg'), Ellipse ] )

# Add fillcolors for the elements
colors_to_use = [ ['set', "#6dd6ff", 'to = "#006ca1", begin = "click", dur = "2s"'],
['animate', "#1b9fd8", 'values = "#1b9fd8;#6dd6ff;#006ca1;#6dd6ff;#1b9fd8", begin = "2s", calcMode = "linear", dur = "10s", repeatCount = "indefinite"'],
['animate', "#006ca1", 'values = "#006ca1;#6dd6ff;#1b9fd8;#6dd6ff;#006ca1", begin = "2s", calcMode = "linear", dur = "5s", repeatCount = "indefinite"']]
stim.fillcolors = GridPattern.RepeatAcrossLayers( colors_to_use)

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")
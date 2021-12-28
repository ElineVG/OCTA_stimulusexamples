"""
OCTA toolbox example stimuli
Example stimulus 110
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern, Pattern
from octa.patterns.Pattern import Sequence
from octa.shapes import Rectangle

# Define stimulus name
stimname = "example_0110"

# Define stimulus
stim = Grid(n_rows = 5, n_cols = 5, row_spacing = 45, col_spacing= 45, background_color = 'none', size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossLeftDiagonal(Pattern.Create2DGradient(x = Sequence(start = 5, step = 5), y = Sequence(start = 45, step = -5), n_elements = 9))

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Rectangle ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.GradientAcrossRightDiagonal(start_value = 'limegreen', end_value = 'steelblue')

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")
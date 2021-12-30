"""
OCTA toolbox example stimuli
Example stimulus 115
created by Eline Van Geert
Checkmark used: https://www.onlinewebfonts.com/icon/98068
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Text, PathSvg

# Define stimulus name
stimname = "example_0115"

# Define stimulus
stim = Grid(n_rows = 5, n_cols = 5, row_spacing = 45, col_spacing= 45, background_color = 'none', size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (30,30) ])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossColumns( [ PathSvg('img/checkmark.svg'), Text('C'), Text('J'), Text('E'), PathSvg('img/checkmark.svg') ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.GradientAcrossRows(start_value = 'limegreen', end_value = 'steelblue')

# Add orientations for the elements
stim.orientations = GridPattern.RepeatAcrossElements( [ 30])

# Add mirrorvalues for the elements
stim.mirrorvalues = GridPattern.RepeatAcrossRows( [ 'none', 'vertical', 'horizontal', 'horizontalvertical', 'none'] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")
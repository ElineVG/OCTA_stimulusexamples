"""
OCTA toolbox example stimuli
Example stimulus 5
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Rectangle, Triangle, Ellipse

# Define stimulus name
stimname = "example_0005"

# Define stimulus
stim = Grid(n_rows = 9, n_cols = 9, row_spacing = 25, col_spacing = 25, size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (20,20), (15,15) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossLayers( [ Rectangle, Triangle, Ellipse ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.GradientAcrossRightDiagonal( start_value = 'limegreen', end_value = 'steelblue' )

# Add orientations for the elements
stim.orientations = GridPattern.MirrorAcrossLeftDiagonal( [ -90, -45, 0, 45, 90 ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")
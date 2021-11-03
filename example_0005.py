"""
OCTA toolbox example stimuli
Example stimulus 4
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Rectangle, Triangle, Ellipse

# Define stimulus name
stimname = "example_0004"

# Define stimulus
stim = Grid(n_rows = 5, n_cols = 5, size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (45,45), (30,30) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossLayers( [ Rectangle, Triangle, Ellipse ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.GradientAcrossRightDiagonal( start_value = 'limegreen', end_value = 'steelblue' )

# Add orientations for the elements
stim.orientations = GridPattern.MirrorAcrossLeftDiagonal( [ -90, -45, 0, 45, 90 ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")
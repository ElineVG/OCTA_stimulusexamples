"""
OCTA toolbox example stimuli
Example stimulus 7
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Outline
from octa.patterns import GridPattern
from octa.shapes import Rectangle, Triangle

# Define stimulus name
stimname = "example_0007"

# Define stimulus
stim = Outline(n_elements = 24, shape_boundingbox = (100,100), size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (20,20), (15,15) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Rectangle, Triangle ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.GradientAcrossElements( start_value = 'limegreen', end_value = 'steelblue' )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")
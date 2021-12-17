"""
OCTA toolbox example stimuli
Example stimulus 62
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Outline
from octa.Positions import Positions
from octa.patterns import GridPattern
from octa.shapes import Rectangle, Ellipse, Triangle

# Define stimulus name
stimname = "example_0062"

# Define stimulus
stim = Outline(n_elements = 36, size = (250,250))

# Define element positions
stim.positions = Positions.CreateCircle(n_elements = 36, radius = 100, starting_point = "left")

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossRows( [ (22,22) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Rectangle, Ellipse, Triangle ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossColumns( [ "#6dd6ff", "#1b9fd8", "#006ca1" ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")
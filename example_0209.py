"""
OCTA toolbox example stimuli
Example stimulus 209
created by Eline Van Geert
Image used: safety pin by Clker-Free-Vector-Images from Pixabay
https://pixabay.com/vectors/safety-pin-pin-diaper-pin-isolated-23808/
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Outline
from octa.Positions import Positions
from octa.patterns import GridPattern
from octa.shapes import Image
import random

# Set seed to make reproducible and get same stimulus every time (!)
# this specific seed example is different from the one in the publication
random.seed(125671212325)

# Define stimulus name
stimname = "example_0209"

# Define stimulus
stim = Outline(n_elements = 18, size = (600,400))

# Change element positions
stim.positions = Positions.CreateRandomPositions(n_elements = 18, width = 400, height = 350, min_distance = 60)

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (26,100) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements([Image("img/safety-pin.svg")])

# Add orientations for the elements
stim.orientations = GridPattern.GradientAcrossElements( -90, 270 )

# Save stimulus
stim.Show()
random.seed(125671212325)
stim.SaveSVG(stimname, folder = "svg")
random.seed(125671212325)
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
random.seed(125671212325)
stim.SaveJSON(stimname, folder = "json")
random.seed(125671212325)
stim.SavePNG(stimname, folder = "png")
random.seed(125671212325)
stim.SavePNG(stimname, scale = 10, folder = "png10")

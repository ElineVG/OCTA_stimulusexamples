"""
OCTA toolbox example stimuli
Example stimulus 208
created by Eline Van Geert
Image used: safety pin by Clker-Free-Vector-Images from Pixabay
https://pixabay.com/vectors/safety-pin-pin-diaper-pin-isolated-23808/
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Outline
from octa.Positions import Positions
from octa.patterns import GridPattern
from octa.shapes import Image

# Define stimulus name
stimname = "example_0208"

# Define stimulus
stim = Outline(n_elements = 18, size = (600,400))

# Change element positions
stim.positions = Positions.CreateCircle(n_elements = 18, radius = 140)

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (13,50),(19,75),(26,100) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements([Image("img/safety-pin.svg")])

# Add orientations for the elements
stim.orientations = GridPattern.GradientAcrossElements( -90, 270 )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")

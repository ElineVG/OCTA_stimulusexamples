"""
OCTA toolbox example stimuli
Example stimulus 207
created by Eline Van Geert
Image used: safety pin by Clker-Free-Vector-Images from Pixabay
https://pixabay.com/vectors/safety-pin-pin-diaper-pin-isolated-23808/
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Image

# Define stimulus name
stimname = "example_0207"

# Define stimulus
stim = Grid(n_rows = 1, n_cols = 18, row_spacing = 60, col_spacing = 30, size = (600,400))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.MirrorAcrossElements([(26,100)])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements([Image("img/safety-pin.svg")])

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")

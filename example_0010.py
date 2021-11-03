"""
OCTA toolbox example stimuli
Example stimulus 10
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Concentric
from octa.patterns import GridPattern
from octa.shapes import Ellipse

# Define stimulus name
stimname = "example_0010"

# Define stimulus
stim = Concentric(n_elements = 7, size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.GradientAcrossElements( start_value = (230,230), end_value = (10,10) )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Ellipse ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements( [ 'dodgerblue', 'limegreen' ] )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")
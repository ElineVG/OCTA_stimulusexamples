"""
OCTA toolbox example stimuli
Example stimulus 148
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Outline
from octa.Positions import Positions
from octa.patterns import GridPattern
from octa.shapes import Ellipse

# Define stimulus name
stimname = "example_0148"

# Create custom positions
pos = Positions.CreateCircle(n_elements = 9, radius = 40)
px = pos.x
py = pos.y
px.append(0)
py.append(0)

# Define stimulus
stim = Outline(n_elements = 10, size = (250,250))

# Change element positions
stim.positions = Positions.CreateCustomPositions(x = px, y = py)

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (20,20) ] )
stim.set_element_boundingbox(9, (40,40))

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Ellipse ] )

# Add fillcolors for the elements
stim.set_element_fillcolor(9, "orange")

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")
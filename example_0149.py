"""
OCTA toolbox example stimuli
Example stimulus 149
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Outline
from octa.Positions import Positions
from octa.patterns import GridPattern
from octa.shapes import Ellipse, RegularPolygon

# Define stimulus name
stimname = "example_0149"

# Create custom positions
pos = Positions.CreateCircle(n_elements = 3, radius = 65, starting_point = "bottom")
px = pos.x
py = pos.y
px.append(0)
py.append(-20)
px.append(0)
py.append(20)

# Define stimulus
stim = Outline(5, x_margin = (-25,-25), y_margin = (-10,-30))

# Change element positions
stim.positions = Positions.CreateCustomPositions(x = px, y = py)

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (50,50), (50,50), (50,50), (125,125), (125,125) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Ellipse, Ellipse, Ellipse, RegularPolygon(3), RegularPolygon(3) ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements( ["black", "black", "black", "white", "white"] )

# Add additional deviations
stim.set_element_borderwidth(3,5)
stim.set_element_bordercolor(3,"black")
stim.set_element_orientation(4,180)

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")
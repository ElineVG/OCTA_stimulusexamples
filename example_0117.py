"""
OCTA toolbox example stimuli
Example stimulus 117
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Ellipse, Text

# Define stimulus name
stimname = "example_0117"

# Define stimulus
stim = Grid(n_rows = 5, n_cols = 5, row_spacing = 45, col_spacing= 45, background_color = 'none', size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (30,30) ])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Ellipse ] )
stim.set_element_shape(element_id = 1, shape_value = Text('1') )
stim.set_element_shape(element_id = 5, shape_value = Text('2') )
stim.set_element_shape(element_id = 12, shape_value = Text('3') )
stim.set_element_shape(element_id = 19, shape_value = Text('4') )
stim.set_element_shape(element_id = 23, shape_value = Text('5') )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.GradientAcrossElements(start_value = 'limegreen', end_value = 'steelblue')

# Add classlabels for the elements
stim.classlabels = GridPattern.RepeatAcrossElements( [ "circle" ] )
stim.set_element_classlabels(element_id = [1, 5, 12, 19, 23], classlabel_value = 'number')

# Add idlabels for specific elements
stim.set_element_idlabels(element_id = [1, 5, 12, 19, 23], 
                          idlabel_value = [ "first", "second", "third", "fourth", "fifth" ])

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")
"""
OCTA toolbox example stimuli
Example stimulus 199
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Concentric
from octa.patterns import GridPattern
from octa.shapes import RegularPolygon

# Define stimulus name
stimname = "example_0199"

# Define stimulus
stim = Concentric(n_elements = 6, x_margin=0, y_margin=0, background_color = "none", size = (220,220))

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ RegularPolygon(5) ] )

# Add bounding box sizes for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements( [
                                                     ['animate', '#ED4569', 'values = "#ED4569;#F39130;#FCE533;#B2D135;#62BD80;#54C4D0;#5EA1D8;#9C4B9C;#ED4569", begin = "0s", calcMode = "linear", dur = "10s", repeatCount = "indefinite"'],
                                                     ['animate', '#F39130', 'values = "#F39130;#FCE533;#B2D135;#62BD80;#54C4D0;#5EA1D8;#9C4B9C;#ED4569;#F39130", begin = "0s", calcMode = "linear", dur = "10s", repeatCount = "indefinite"'],
                                                     ['animate', '#FCE533', 'values = "#FCE533;#B2D135;#62BD80;#54C4D0;#5EA1D8;#9C4B9C;#ED4569;#F39130;#FCE533", begin = "0s", calcMode = "linear", dur = "10s", repeatCount = "indefinite"'],
                                                     ['animate', '#B2D135', 'values = "#B2D135;#62BD80;#54C4D0;#5EA1D8;#9C4B9C;#ED4569;#F39130;#FCE533;#B2D135", begin = "0s", calcMode = "linear", dur = "10s", repeatCount = "indefinite"'],
                                                     ['animate', '#62BD80', 'values = "#62BD80;#54C4D0;#5EA1D8;#9C4B9C;#ED4569;#F39130;#FCE533;#B2D135;#62BD80", begin = "0s", calcMode = "linear", dur = "10s", repeatCount = "indefinite"'],
                                                     ['animate', '#54C4D0', 'values = "#54C4D0;#5EA1D8;#9C4B9C;#ED4569;#F39130;#FCE533;#B2D135;#62BD80;#54C4D0", begin = "0s", calcMode = "linear", dur = "10s", repeatCount = "indefinite"']
                                                    ])

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")
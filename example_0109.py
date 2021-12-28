"""
OCTA toolbox example stimuli
Example stimulus 109
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Ellipse

# Define stimulus name
stimname = "example_0109"

# Define stimulus
stim = Grid(n_rows = 5, n_cols = 5, row_spacing = 45, col_spacing= 45, background_color = 'none', size = (250,250))

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (35,35) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Ellipse ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.RepeatAcrossElements([
    "darkturquoise", "steelblue", "none", "sandybrown", "darkmagenta",  # css colornames
    ["horizontal", 'darkmagenta', 'white' , 'darkmagenta'],     
    ["diagonal", '#1b9fd8', 'white', '#6dd6ff', 'white', '#006ca1'], 
    ["vertical", 'rgb(255,166,51)', "white", 'rgb(255,166,51)'], 
    ["radial", 'white', '#d3d3d3', "white"],    
    ["horizontal", "white", 'rgb(51,255,51)', 'white'], 
    ['set', "orange", 'to = "purple", begin = "click", dur = "2s"'],
    ['set', 'rgb(255,87,51)', 'to = "#6dd6ff", begin = "click", dur = "2s"'],
    ['animate', "rgb(255,51,237)", 'values = "red;orange;green;blue;indigo;violet;red", begin = "2s", calcMode = "linear", dur = "10s", repeatCount = "indefinite"'],
    ['animate', "#1b9fd8", 'values = "red;orange;green;blue;indigo;violet;red", begin = "2s", calcMode = "discrete", dur = "10s", repeatCount = "indefinite"'],
    ['animate', "darkturquoise", 'values = "rgb(255,51,237);#6dd6ff", begin = "2s", calcMode = "discrete", dur = "10s", repeatCount = "indefinite"'],
    ["radial", "white", 'rgb(255,87,51)'],     
    ["horizontal", "red", "orange", "green", "blue", "indigo", "violet"], 
    ["vertical", "green", "white", "green"], 
    ["diagonal", "red", "white"],    
    ["radial", "white", '#1b9fd8', '#6dd6ff', '#006ca1'],
    'rgb(255,51,237)', '#1b9fd8', '#6dd6ff', 'rgb(255,87,51)', 'rgb(255,166,51)'
])

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")
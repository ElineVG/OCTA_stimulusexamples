"""
OCTA toolbox example stimuli
Example stimulus 116
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Text, PathSvg

# Define stimulus name
stimname = "example_0116"

# Define stimulus
stim = Grid(n_rows = 5, n_cols = 5, row_spacing = 45, col_spacing= 45, background_color = 'none', size = (250,250),
            stim_link = 'https://elinevg.github.io/OCTA/')

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (30,30) ])

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ 
    PathSvg('img/checkmark.svg'), Text('A'), Text('p'), Text('p'), PathSvg('img/checkmark.svg'),
    Text('C'), Text('o'), Text('d'), Text('e'), PathSvg('img/checkmark.svg'),
    PathSvg('img/checkmark.svg'), Text('O'), Text('C'), Text('T'), Text('A'),
    Text('C'), Text('o'), Text('d'), Text('e'), PathSvg('img/checkmark.svg'),
    PathSvg('img/checkmark.svg'), Text('A'), Text('p'), Text('p'), PathSvg('img/checkmark.svg')
] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.GradientAcrossElements(start_value = '#6dd6ff', end_value = '#1b9fd8')

# Add links for the elements
stim.links = GridPattern.RepeatAcrossRows( [ 
    'https://elinevg.shinyapps.io/OCTA_toolbox/',
    'https://github.com/gestaltrevision/OCTA_toolbox',
    '', 
    'https://github.com/gestaltrevision/OCTA_toolbox',
    'https://elinevg.shinyapps.io/OCTA_toolbox/'
    ])

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveSVG(stimname, scale = 0.5, folder = "svg_small")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")
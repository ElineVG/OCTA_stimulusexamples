"""
OCTA toolbox example stimuli
Example stimulus 20
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Outline
from octa.Positions import Positions
from octa.patterns import GridPattern, Pattern
from octa.shapes import Rectangle, Ellipse

# Define stimulus name
stimname = "example_0020"

# Define stimulus
stim = Outline(n_elements = 24, size = (250,250))

# Define element positions
stim.positions = Positions.CreateCustomPositions(x = Pattern(Pattern.CreateGradientPattern(200,0,12).pattern + Pattern.CreateGradientPattern(0,200,12).pattern).RepeatElementsToSize(24).pattern,
                                                     y = Pattern.CreateGradientPattern(0,200,12).RepeatPatternToSize(24).pattern)

# Add bounding box sizes for the elements
stim.boundingboxes = GridPattern.RepeatAcrossElements( [ (15,15) ] )

# Add shapes for the elements
stim.shapes = GridPattern.RepeatAcrossElements( [ Rectangle, Ellipse ] )

# Add fillcolors for the elements
stim.fillcolors = GridPattern.GradientAcrossElements( start_value = 'limegreen', end_value = 'steelblue' )

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")
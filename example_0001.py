"""
OCTA toolbox example stimuli
Example stimulus 1
created by Eline Van Geert
"""

# Load necessary objects and functions from OCTA
from octa.Stimulus import Grid

# Define stimulus name
stimname = "example_0001"

# Define stimulus
stim = Grid(n_rows = 9, n_cols = 9)

# Save stimulus
stim.Show()
stim.SaveSVG(stimname, folder = "svg")
stim.SaveJSON(stimname, folder = "json")
stim.SavePNG(stimname, folder = "png")
stim.SavePNG(stimname, scale = 10, folder = "png10")
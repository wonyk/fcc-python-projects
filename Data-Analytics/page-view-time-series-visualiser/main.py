# This entrypoint file to be used in development. Start by reading README.md
import time_series_visualizer
from unittest import main

# Test your function by calling it here
# Uncomment to see the plots, else will leave commented since replit has a timeout
time_series_visualizer.draw_line_plot()
time_series_visualizer.draw_bar_plot()
time_series_visualizer.draw_box_plot()

# Run unit tests automatically
main(module='test_module', exit=False)
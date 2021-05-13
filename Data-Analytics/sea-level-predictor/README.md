# Sea Level Predictor

This project would utilise the sea level dataset to predict sea levels in the year 2050 using Pandas and Scipy.

It has completed all the requirements of the [FCC Sea Level Predictor](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/sea-level-predictor) assignment.

## Assignment

You will anaylize a dataset of the global average sea level change since 1880.

Use the data to complete the following tasks:

* Use Pandas to import the data from `epa-sea-level.csv`.
* Use matplotlib to create a scatter plot using the "Year" column as the x-axis and the "CSIRO Adjusted Sea Level" column as the y-axix.
* Use the `linregress` function from `scipy.stats` to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
* Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
* The x label should be "Year", the y label should be "Sea Level (inches)", and the title should be "Rise in Sea Level".

Unit tests are available in `test_module.py`.

## Development

For development, you can use `main.py` to test your functions in replit. Click the "run" button and `main.py` will run.

For manual run and testing, use `python3 main.py` instead.

## Testing

Tests from `test_module.py` are imported to `main.py`. The tests will run automatically whenever you hit the "run" button.

## Data Source

Global Average Absolute Sea Level Change, 1880-2014 from the US Environmental Protection Agency using data from CSIRO, 2015; NOAA, 2015.
https://datahub.io/core/sea-level-rise

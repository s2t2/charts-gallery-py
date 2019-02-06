
# adapted from: https://altair-viz.github.io/user_guide/display_frontends.html#working-in-non-notebook-environments

import altair

# load a simple dataset as a pandas DataFrame
from vega_datasets import data
cars = data.cars()

chart = altair.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
).interactive()

chart.serve()

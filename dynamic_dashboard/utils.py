from plotly.data import carshare, iris, gapminder
from plotly.express import scatter, line, scatter_3d, violin, line_3d
from inspect import signature
from copy import copy

data_sources = {
                'iris': iris(),
                'carshare': carshare(),
                'gapminder': gapminder()
}


plot_categories = {
                'scatter': scatter, 
                'line': line,
                'scatter_3d': scatter_3d,
                'line_3d': line_3d,
                'violin': violin
}


initial_param = []
parameters_with_column_options = ['x', 'y', 'z', 'color', 'size', 'symbol', 'hover_name']
initial_param.extend(parameters_with_column_options)


labels = [id+"_label" for id in initial_param]
components_and_label = copy(initial_param)
components_and_label.extend(labels)



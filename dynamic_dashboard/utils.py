from plotly.data import carshare, iris, gapminder
from plotly.express import scatter, line, scatter_3d #scatter_ternary, violin, line_3d, box, ecdf, histogram, strip, pie, funnel
from inspect import signature
from copy import copy

data_sources = {
                'iris': iris(),
                'carshare': carshare(),
                'gapminder': gapminder()
}


plot_categories = {
                'scatter': scatter, 
                'scatter_3d': scatter_3d,
                # 'line_3d': line_3d,
                # 'violin': violin,
                # 'box': box,
                # 'histogram': histogram,
                # 'ecdf': ecdf,
                # 'strip': strip,
                # 'funnel': funnel,
                # 'pie': pie
}


initial_param = []
parameters_with_column_options = ['x', 'y', 'z', 'color', 'size', 'symbol', 'hover_name', 'text', 'facet_row', 'facet_col', \
                                  'error_x', 'error_x_minus', 'error_y', 'error_y_minus', 'animation_frame', 'animation_group'
]
initial_param.extend(parameters_with_column_options)


labels = [id+"_label" for id in initial_param]
components_and_label = copy(initial_param)
components_and_label.extend(labels)



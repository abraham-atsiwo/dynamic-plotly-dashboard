from plotly.data import carshare, iris, gapminder
from seaborn import load_dataset
from plotly.express import scatter, line, scatter_3d, violin, line_3d, box, ecdf, histogram, strip, \
            pie, funnel, bar, density_heatmap, density_contour, line_polar, scatter_polar, area
# from inspect import signature
from copy import copy

data_sources = {
                'iris': iris(),
                'carshare': carshare(),
                'gapminder': gapminder()
}


plot_categories = {
                'scatter': scatter, 
                'line': line,
                'violin': violin,
                'box': box,
                'bar':bar,
                'histogram': histogram,
                'ecdf': ecdf,
                'strip': strip,
                'density_heatmap': density_heatmap,
                'density_contour': density_contour,
                'funnel': funnel,
                'pie': pie,       
                'area': area,           
                'scatter_3d': scatter_3d,
                'line_3d': line_3d,

}


initial_param = []
parameters_with_column_options = ['x', 'y', 'z', 'color', 'size', 'symbol', 'hover_name', 'text', 'line_group', 
                                'pattern_shape', 'facet_row', 'facet_col', \
                                  'error_x', 'error_x_minus', 'error_y', 'error_y_minus', 'animation_frame', 'animation_group'
]
initial_param.extend(parameters_with_column_options)

#parameters with predefined options 
parameters_with_defined_options = ['marginal_x', 'marginal_y', 'trendline', 'trendline_scope', 'render_mode']
initial_param.extend(parameters_with_defined_options)

# #integers and float 
parameters_with_numeric_options = ['opacity', 'size_max']
initial_param.extend(parameters_with_numeric_options)

# #boolean options
parameters_with_boolean = ['log_x', 'log_y']
initial_param.extend(parameters_with_boolean)



labels = [id+"_label" for id in initial_param]
components_and_label = copy(initial_param)
components_and_label.extend(labels)



from plotly.data import carshare, iris, gapminder, tips
from plotly.express import scatter, line, scatter_3d, violin, line_3d, box, ecdf, histogram, strip, bar_polar, treemap, \
            pie, funnel, bar, density_heatmap, density_contour, line_polar, scatter_polar, area, line_ternary, scatter_mapbox
# from inspect import signature
from copy import copy

data_sources = {
                'iris': iris(),
                'carshare': carshare(),
                'gapminder': gapminder(),
                'penguins': tips
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
                'density_contour': density_contour,
                'funnel': funnel,
                'pie': pie,       
                'area': area,           
                'scatter_3d': scatter_3d,
                'line_3d': line_3d,
                'line_polar':line_polar,
                'scatter_polar': scatter_polar,
                'line_ternary': line_ternary,
                'bar_polar': bar_polar,

}


initial_param = []
parameters_with_column_options = ['x', 'y', 'z', 'r','a', 'b', 'c', 'lat','lon','locations', 'parents' ,'ids', 'path', 'theta', 
                                'color', 'size', 'symbol', 'hover_name', 'text', 'line_group', 
                                'pattern_shape', 'facet_row', 'facet_col', 'names', 'values',\
                                  'error_x', 'error_x_minus', 'error_y', 'error_y_minus', 'animation_frame', 'animation_group', 'base'
]
initial_param.extend(parameters_with_column_options)

#parameters with predefined options 
parameters_with_defined_options = ['marginal_x', 'marginal_y', 'trendline', 'trendline_scope', 'render_mode', 
                            'template', 'violinmode', 'points', 'boxmode', 'barmode', 'marginal', 'barnorm', 'start_angle', 
                            'histnorm', 'histfunc', 'ecdfnorm', 'ecdfmode', 'stripmode', 'line_shape', 'direction']
initial_param.extend(parameters_with_defined_options)

# #integers and float 
parameters_with_numeric_options = ['opacity', 'size_max', 'height', 'hole', 'nbins']
initial_param.extend(parameters_with_numeric_options)

# #boolean options
parameters_with_boolean = ['log_x', 'log_y', 'box', 'notched', 'cummulative', 'markers', 'lines', 'log_z', 'log_r', 'line_close']
initial_param.extend(parameters_with_boolean)



labels = [id+"_label" for id in initial_param]
components_and_label = copy(initial_param)
components_and_label.extend(labels)



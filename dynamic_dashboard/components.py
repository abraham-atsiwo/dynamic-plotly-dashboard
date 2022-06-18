from dash.html import Div, Label
from dash.dcc import Dropdown, Slider
from plotly.io import templates


from .utils import parameters_with_column_options

def dropdown(label ,options=[], index=0, value=None, multi=False, kwargs={}):
    lab = Div(Label(label), className='sidebar-label', id = {'type':label+'_label', 'index':index})
    x = Div(
            children = Dropdown(options=options, multi=multi, value=value,  **kwargs,
                                id = {'type':label, 'index':index}
                        ), 
            className='sidebar-component')
    return Div([lab, x], className='sidebar-component-label', id = {'type':label+'_div', 'index':index})

def slider(label, min, max, step, value, index):
    lab = Div(Label(label), className='sidebar-label', id = {'type':label+'_label', 'index':index})
    x = Div(
            children = Slider(min, max, step,  value=value, id = {'type':label, 'index':index}), 
            className='sidebar-component')
    return Div([lab, x], className='sidebar-component-label', id = {'type':label+'_div', 'index':index})


def parameters_widget(n_clicks):
    init_pars = []
#     init_pars = [slider('sample-size',0, 100, 20, 40, n_clicks)]
    pars_col_options = [dropdown(label=lbl, index=n_clicks) for lbl in parameters_with_column_options]
    init_pars.extend(pars_col_options)

    #other_parameters
    opacity = slider('opacity', 0.0, 1.0, 0.2, 1.0, index=n_clicks)
    hole = slider('hole', 0.0, 1.0, 0.2, 0.0, index=n_clicks)
    height = slider('height', 400, 900, 100, 400, index=n_clicks)
    width = slider('width', 500, 1000, 100, 500, index=n_clicks)
    size_max = slider('size_max', 0, 100, 20, 20, index=n_clicks)
    start_angle = slider('start_angle', 0, 360, 90, 90, index=n_clicks)
    nbins = slider('nbins', 4, 12, 2, 4, index=n_clicks)
    marginal_x = dropdown(label='marginal_x', options=['rug', 'box', 'violin', 'histogram'], index=n_clicks)
    marginal = dropdown(label='marginal', options=['rug', 'box', 'violin', 'histogram'], index=n_clicks)
    marginal_y = dropdown(label='marginal_y', options=['rug', 'box', 'violin', 'histogram'], index=n_clicks)
    trendline = dropdown(label='trendline', options=['ols', 'lowess', 'expanding', 'ewm'], index=n_clicks)
    log_x = dropdown(label='log_x', options=[True, False], value=False, index=n_clicks)
    log_y = dropdown(label='log_y', options=[True, False], value=False, index=n_clicks)
    log_z = dropdown(label='log_z', options=[True, False], value=False, index=n_clicks)
    log_r = dropdown(label='log_r', options=[True, False], value=False, index=n_clicks)
    line_close = dropdown(label='line_close', options=[True, False], value=False, index=n_clicks)
    box = dropdown(label='box', options=[True, False], value=False, index=n_clicks)
    markers = dropdown(label='markers', options=[True, False], value=False, index=n_clicks)
    lines = dropdown(label='lines', options=[True, False], value=False, index=n_clicks)
    cummulative = dropdown(label='cummulative', options=[True, False], value=False, index=n_clicks)
    text_auto = dropdown(label='text_auto', options=[True, False], value=False, index=n_clicks)
    notched = dropdown(label='notched', options=[True, False], value=False, index=n_clicks)
    trendline_scope = dropdown(label='trendline_scope', options=['trace', 'overlap'], value='trace', index=n_clicks)
    render_mode = dropdown(label='render_mode',options=['auto', 'svg', 'webgl'], value='auto', index=n_clicks)
    violinmode = dropdown(label='violinmode', options=['group', 'overlay'], value='group', index=n_clicks)
    boxmode = dropdown(label='boxmode', options=['group','overlay'], value='group', index=n_clicks)
    stripmode = dropdown(label='stripmode', options=['group','overlay'], value='group', index=n_clicks)
    points = dropdown(label='points', options=['outliers', 'suspectedoutliers', 'all', False], value='outliers', index=n_clicks)
    barmode = dropdown(label='barmode', options=['group','overlay', 'relative'], value='relative', index=n_clicks)
    barnorm = dropdown(label='barnorm', options=['fraction','percent'], index=n_clicks)
    ecdfmode = dropdown(label='ecdfmode', options=['standard','complementary', 'reversed'], value='standard', index=n_clicks)
    ecdfnorm = dropdown(label='ecdfnorm', options=['probability','percent'], index=n_clicks)
    groupnorm = dropdown(label='groupnorm', options=['probability','percent'], index=n_clicks)
    direction = dropdown(label='direction', options=['counterclockwise','clockwise'], index=n_clicks)
    histnorm = dropdown(label='histnorm', options=['percent','density', 'probability'], index=n_clicks)
    line_shape = dropdown(label='line_shape', options=['linear','spline'], index=n_clicks)
    histfunc = dropdown(label='histfunc', options=['count','sum', 'avg', 'min', 'max'], value='count', index=n_clicks)
    template = dropdown(label='template', options=list(templates), index=n_clicks)
    other_parameters = [marginal_x, marginal_y, marginal, log_x, log_y, log_r, log_z, barnorm, histnorm, 
                        histfunc, hole, line_shape, groupnorm, direction, start_angle, line_close,
                        violinmode, boxmode, barmode, stripmode, notched, points, box, nbins, cummulative, markers, lines, ecdfnorm, ecdfmode,
                        template, width, height, trendline, trendline_scope, render_mode, opacity, size_max]
    init_pars.extend(other_parameters)
    return init_pars

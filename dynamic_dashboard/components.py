from dash.html import Div, Label
from dash.dcc import Dropdown, Slider
import dash_bootstrap_components as dbc


from .utils import parameters_with_column_options

def dropdown(label ,options=[], index=0, value=None, multi=False):
    lab = Div(Label(label), className='sidebar-label', id = {'type':label+'_label', 'index':index})
    x = Div(
            children = Dropdown(options=options, multi=multi, value=value,   
                                id = {'type':label, 'index':index}
                        ), 
            className='sidebar-component')
    return dbc.Collapse(Div([lab, x], className='sidebar-component-label'), is_open=False, id='collapse')

def slider(label, min, max, step, value, index):
    lab = Div(Label(label), className='sidebar-label', id = {'type':label+'_label', 'index':index})
    x = Div(
            children = Slider(min, max, step,  value=value, id = {'type':label, 'index':index}), 
            className='sidebar-component')
    return Div([lab, x], className='sidebar-component-label')


# opacity = slider('opacity', 0.0, 1.0, 0.2, 1.0, 0.0)
# size_max = slider('size_max', 0, 100, 20, 20, 0)
# marginal_x = dropdown(label='marginal_x', options=['rug', 'box', 'violin', 'histogram'])
# marginal_y = dropdown(label='marginal_y', options=['rug', 'box', 'violin', 'histogram'])
# trendline = dropdown(label='trendline', options=['ols', 'lowess', 'expanding', 'ewm'])
# log_x = dropdown(label='log_x', options=[True, False], value=False)
# log_y = dropdown(label='log_y', options=[True, False], value=False)
# trendline_scope = dropdown(label='trendline_scope', options=['trace', 'overlap'], value='trace')
# render_mode = dropdown(label='render_mode', options=['auto', 'svg', 'webgl'], value='auto')


def parameters_widget(n_clicks):
    init_pars = [slider('sample-size',0, 100, 20, 40, n_clicks)]
    pars_col_options = [dropdown(label=lbl, index=n_clicks) for lbl in parameters_with_column_options]
    init_pars.extend(pars_col_options)

    #other_parameters
    opacity = slider('opacity', 0.0, 1.0, 0.2, 1.0, index=n_clicks)
    size_max = slider('size_max', 0, 100, 20, 20, index=n_clicks)
    marginal_x = dropdown(label='marginal_x', options=['rug', 'box', 'violin', 'histogram'], index=n_clicks)
    marginal_y = dropdown(label='marginal_y', options=['rug', 'box', 'violin', 'histogram'], index=n_clicks)
    trendline = dropdown(label='trendline', options=['ols', 'lowess', 'expanding', 'ewm'], index=n_clicks)
    log_x = dropdown(label='log_x', options=[True, False], value=False, index=n_clicks)
    log_y = dropdown(label='log_y', options=[True, False], value=False, index=n_clicks)
    trendline_scope = dropdown(label='trendline_scope', options=['trace', 'overlap'], value='trace', index=n_clicks)
    render_mode = dropdown(label='render_mode', options=['auto', 'svg', 'webgl'], value='auto', index=n_clicks)
    other_parameters = [marginal_x, marginal_y, log_x, log_y, trendline, trendline_scope, render_mode, opacity, size_max]
    init_pars.extend(other_parameters)
    return init_pars



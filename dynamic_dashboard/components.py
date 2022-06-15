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
    lab = Div(Label(label), className='sidebar-label')
    x = Div(
            children = Slider(min, max, step,  value=value, id = {'type':label, 'index':index}), 
            className='sidebar-component')
    return Div([lab, x], className='sidebar-component-label')

def parameters_widget(n_clicks):
    init_pars = [slider('sample-size',0, 100, 20, 40, n_clicks)]
    pars_col_options = [dropdown(label=lbl, index=n_clicks) for lbl in parameters_with_column_options]
    init_pars.extend(pars_col_options)
    return init_pars



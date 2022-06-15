from .utils import  plot_categories
from .utils import initial_param
from inspect import getfullargspec
from copy import copy

def func_args_default(func):
    function_args = getfullargspec(func)
    return function_args.args, function_args.defaults

def intersection(plt_par, initial_param)->iter:
    for val in initial_param:
        if val in plt_par:
            yield val
    
def get_parameters_based_type(plt_type:str=None, all_pars:list=initial_param)->list:
    plt_args, _ = func_args_default(plot_categories[plt_type])
    common_value = list(intersection(plt_args, initial_param))
    return common_value

tmp = {'color': 'yest', 'x':'thousand', 'size':'thousand'}
def delete_parameters_not_required(plt_type:str=None, all_pars_values:dict={}):
    all_pars_values_copy = copy(all_pars_values)
    all_keys = all_pars_values_copy.keys()
    type_pars = get_parameters_based_type(plt_type, all_keys)
    for key in all_keys:
        if key not in type_pars:
            del all_pars_values[key]
    return all_pars_values 

def show_hide_component(plt_type:str, all_pars:list):
    type_pars = get_parameters_based_type(plt_type, all_pars)
    return [{'display':'flex', 'clearable':True} if par in type_pars else {'display':'none'} for par in all_pars]
        




# def scatter_parameters_widget(n_clicks):
#     return [
#         slider('sample-size',0, 100, 20, 40, n_clicks),
#         dropdown(label='x', index=n_clicks),
#         dropdown(label='y', index=n_clicks)
#     ]

# def line_parameters_widget(n_clicks, options):
#     return Div([
#         slider('sample-size',0, 100, 20, 40, n_clicks),
#         dropdown(label='x', index=n_clicks),
#         dropdown(label='y', index=n_clicks, options=options)
#     ])


# plot_parameters = {
#     'scatter': scatter_parameters_widget,
#     'line': line_parameters_widget
# }
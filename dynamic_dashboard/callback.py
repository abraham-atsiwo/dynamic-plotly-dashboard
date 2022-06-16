
from dash import Input, Output, State, MATCH
from dash.dcc import Graph
from .utils import parameters_with_column_options, data_sources, plot_categories, initial_param, components_and_label
from .helper import delete_parameters_not_required, show_hide_component

from .dynamic_css import dynamic_css_callback


def init_callback(app):
    @app.callback([Output({'type':opt, 'index':MATCH}, 'options') for opt in parameters_with_column_options],
    [Input({'type':'data_frame', 'index':MATCH}, 'value')]
    )
    def update_col_options(data_type):
        col_options = data_sources[data_type].columns
        n = len(parameters_with_column_options)
        col_options = [col_options for j in range(n)]
        return col_options

    @app.callback([Output({'type':'sample-size', 'index':MATCH}, val) for val in ['min', 'max', 'value', 'step']],
        [Input({'type':'data_frame', 'index':MATCH}, 'value')]
    )
    def update_slider_options(data_type):
        df = data_sources[data_type]
        max = len(df)
        min = 20 if max > 20 else 0
        step = max //5
        value = int(step*3)
        return min, max, value, step


    @app.callback([Output({'type':opt, 'index':MATCH}, 'value') for opt in ['x', 'y', 'z']],
        [Input({'type':'data_frame', 'index':MATCH}, 'value')]
    )
    def update_selected_options(data_type):
        col_options = data_sources[data_type].columns
        return col_options[0], col_options[1], col_options[2] if len(col_options) >=3 else col_options[1]


    @app.callback(
        [Output({'type':'plotarea', 'index':MATCH}, 'figure')],
        inputs = {
            'plot_type': Input({'type':'plot-type', 'index':MATCH}, 'value'),
            'data_type': Input({'type':'data_frame', 'index':MATCH}, 'value'),
            'sample_size': Input({'type':'sample-size', 'index':MATCH}, 'value'),
            'all_inputs' : {id_key: Input({'type':id_key, 'index':MATCH}, 'value') for id_key in initial_param},
            'plot_area': State({'type':'plotarea', 'index':MATCH}, 'id')
        }
    )
    def update_figure(plot_type, data_type, sample_size, all_inputs, plot_area):
        df = data_sources[data_type].iloc[:sample_size]
        figure = plot_categories[plot_type]
        plot_pars = delete_parameters_not_required(plot_type, all_inputs)
        fig = figure(data_frame=df, **plot_pars)
        return [fig]

    @app.callback(
        [Output({'type':id_key, 'index':MATCH}, 'style') for id_key in components_and_label], 
        [Input({'type':'plot-type', 'index':MATCH}, 'value')]
    )
    def hide_components_line(type):
       show_hide = show_hide_component(type, initial_param)
       show_hide.extend(show_hide)
       return show_hide

    
    # @app.callback([Output('container-body', 'style')], #, Output('body-main', 'style')], 
    #     [Input('display-mode', 'value')], 
    #     prevent_initial_call=True
    # )
    # def dynamic_css(display_mode):
    #     if display_mode == 'column':
    #         style = dynamic_css_callback['container-body-col']
    #         # body_main_style = dynamic_css_callback['body-main-col']
    #     else:
    #         style = dynamic_css_callback['container-body-row']
    #         # body_main_style = dynamic_css_callback['body-main-row']
    #     return style
       
    # #resetting plots to default
    # import plotly.graph_objs as go
    # @app.callback(
    #     Output('reset-plot', 'children'),
    #     Input('add-plot', 'n_clicks')
    # )
    # def reset_plot(n_clicks):
    #     # Graph(id={'type': 'plotarea', 'index': 0})
    #     # go.Figure()
    #     return 'None'
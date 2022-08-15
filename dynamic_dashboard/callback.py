
from dash import Input, Output, State, MATCH
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
    def update_selected_options(data_type, plt_type):
        col_options = data_sources[data_type].columns
        x, y, z = col_options[0], col_options[1], col_options[2] if len(col_options) >=3 else col_options[1]
        return x, y, z


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
        [Output({'type':id_key+'_div', 'index':MATCH}, 'style') for id_key in initial_param], 
        [Input({'type':'plot-type', 'index':MATCH}, 'value')]
    )
    def hide_components_line(type):
       show_hide = show_hide_component(type, initial_param)
    #    show_hide.extend(show_hide)
       return show_hide

    
    @app.callback([
                    Output({'type':'plotarea-main', 'index':MATCH}, 'style'), 
                    # Output({'type':'container-body-item', 'index':MATCH}, 'style')
                ],
                    [
                        # Input({'type':'width', 'index':MATCH}, 'value'), 
                        Input({'type':'height', 'index':MATCH}, 'value')
                    ]
    )
    def update_plotarea_height_width(height):
        styles = {'min-height':height}
        # body_width = (width)/10
        # body_style = {'width':str(body_width)+'%'}
        return [styles]
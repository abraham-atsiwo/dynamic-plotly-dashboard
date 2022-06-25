from re import M
from dash.html import Div, Button, Label, P
from dash.dcc import Graph, Dropdown
from dash import Input, Output, State
import dash_bootstrap_components as dbc
from math import floor, ceil
from .components import slider


from .utils import data_sources, plot_categories
from .components import dropdown, parameters_widget


def create_layout(app):
    @app.callback([Output('container-body', 'children')],
                [Input('add-plot', 'n_clicks')], 
                [State('container-body', 'children')]
    )
    def create_subplot(n_clicks, children):        
        plt_type = dropdown(label='plot-type', options={val:val for val in plot_categories.keys()}, 
                            value='scatter', index=n_clicks, kwargs={'clearable': False})
        data_type = dropdown(label='data_frame', options={val:val for val in data_sources.keys()}, 
                            value='iris', index=n_clicks, kwargs={'clearable': False})
        # reset_specific = Div(Button("Reset", id='reset', n_clicks=n_clicks, className='add-plot'))
        type_data = [plt_type, data_type]
        type_data.extend(parameters_widget(n_clicks))
        n = len(type_data)
        n_sidebar = ceil((n+18)//2)
        if n_sidebar < n and n > 13:
            sidebar_area = type_data[:n_sidebar]
            under_plot = [slider('sample-size',0, 100, 20, 40, n_clicks)]
            under_plot.extend(type_data[n_sidebar:])
        else:
            sidebar_area = type_data
            under_plot = []
        #column options 
        sidebar = Div(
                children= [
                            Div(
                                children=[
                                            Div(
                                                children=[
                                                            # Div("Parameters"), 
                                                            # Div([data_type, plt_type]), 
                                                ], 
                                                className='header'), 
                                            Div(
                                                # children=type_data, 
                                                children=sidebar_area,
                                                className='sidebar-parameter', 
                                                id = {'type':'parameter', 'index':n_clicks}
                                            )                                      
                                ],
                                className="sidebar-item"
                            )
                ], 
                className='mainbody-item sidebar-main'
        )

        #plot area 
        plotarea = Div(
                children= [
                            Div(
                                children=[
                                            Div(
                                                children=[
                                                            Div("Interactive Plot: Figure " + str(n_clicks+1)), 
                                                ], 
                                                className='header'), 
                                            Div(Graph(id={'type':'plotarea', 'index':n_clicks}), 
                                                style={'display':'flex', 'justifyContent':'center'}),
                                            Div(under_plot, 
                                            style={'display':'flex', 'alignItems':'center', 
                                                    'marginTop':'20px', 'flexFlow':'column wrap', 'width':'70%'
                                            })                       
                                ],
                                className="plotarea-item"
                            )
                ], 
                className='mainbody-item plotarea-main',
                id={'type':'plotarea-main', 'index':n_clicks}
        )

        mainbody = Div(children=[sidebar, plotarea],
                        className='container-body-item',
                         id = {'type':'container-body-item', 'index':n_clicks}

                    )
        children.append(mainbody)
        return [children]




def init_layout(app):
    # display_mode = Div(dropdown(label='display mode', options=['row', 'column'], value='row'))
    navbar = [Div("Dynamic Interactive Dashboard"), 
                # display_mode,
                Div(
                    [
                        # display_mode,
                        Button("Add Plot", id='add-plot',n_clicks=0, className='add-plot'), 
                        # Button("Reset All ", id='reset-all',n_clicks=0, className='add-plot'),
                    ],
                    style={'display': 'flex', 'justifyContent': 'center'}
                ), 
                Div("Plotly | Dash"),
            ]

    app.layout = Div(
        children=[  
                    #header and button
                    Div(
                        children=[Div(children=navbar, className='navbar-main'), 
                        ]
                    ),
                    #body elements
                    Div(
                        children = 
                            [
                                Div(children=[], id='container-body', className='container-body'),
                                Div(id='hidden', style={'display':'none'}),
                                Div(id='reset-plot', style={'display':'none'})
                        ],
                        className='container-body-wrapper'
                    )
        ],
        className='container'
    )
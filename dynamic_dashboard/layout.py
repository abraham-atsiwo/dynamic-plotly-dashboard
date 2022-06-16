from re import M
from dash.html import Div, Button, Label, P
from dash.dcc import Graph, Dropdown
from dash import Input, Output, State
import dash_bootstrap_components as dbc


from .utils import data_sources, plot_categories
from .components import dropdown, parameters_widget


def create_layout(app):
    @app.callback([Output('container-body', 'children')],
                [Input('add-plot', 'n_clicks')], 
                [State('container-body', 'children')]
    )
    def create_subplot(n_clicks, children):        
        plt_type = dropdown(label='plot-type', options={val:val for val in plot_categories.keys()}, value='scatter', index=n_clicks)
        data_type = dropdown(label='data_frame', options={val:val for val in data_sources.keys()}, value='carshare', index=n_clicks)
        reset_specific = Div(Button("Reset", id='reset', n_clicks=n_clicks, className='add-plot'))
        # display_mode = Div(dropdown(label='display mode', options=['row', 'column'], value='row', index=n_clicks))
        type_data = [reset_specific, plt_type, data_type]
        type_data.extend(parameters_widget(n_clicks))
        n = len(type_data)
        from math import floor, ceil
        n_sidebar = ceil((n+14)//2)
        if n_sidebar < n and n > 13:
            sidebar_area = type_data[:n_sidebar]
            under_plot = type_data[n_sidebar:]
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
                                            Graph(id={'type':'plotarea', 'index':n_clicks}),
                                            Div(under_plot, 
                                            style={'display':'flex', 'justify-content':'space-around', 
                                                    'margin-top':'20px', 'flex-flow':'column wrap'
                                            })                       
                                ],
                                className="plotarea-item"
                            )
                ], 
                className='mainbody-item plotarea-main'
        )

        mainbody = Div(children=[sidebar, plotarea],
                        className='container-body-item',
                        id='body-main'

                    )
        children.append(mainbody)
        return [children]




def init_layout(app):
    display_mode = Div(dropdown(label='display mode', options=['row', 'column'], value='row'))
    navbar = [Div("Dynamic Interactive Dashboard"), 
                # display_mode,
                Div(
                    [
                        # display_mode,
                        Button("Add Plot", id='add-plot',n_clicks=0, className='add-plot'), 
                        Button("Reset All ", id='reset-all',n_clicks=0, className='add-plot'),
                    ],
                    style={'display': 'flex', 'justify-content': 'center'}
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
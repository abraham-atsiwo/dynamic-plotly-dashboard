from dash.html import Div, Button, Label, P
from dash.dcc import Graph, Dropdown
from dash import Input, Output, State
import dash_bootstrap_components as dbc

from .utils import data_sources, plot_categories
from .components import dropdown, parameters_widget


import dash_bootstrap_components as dbc
from dash import html

accordion = html.Div(
    dbc.Accordion(
        [
            dbc.AccordionItem(
                [
                    html.P("This is the content of the first section"),
                    dbc.Button("Click here"),
                ],
                title="Item 1",
            ),
            dbc.AccordionItem(
                [
                    html.P("This is the content of the second section"),
                    dbc.Button("Don't click me!", color="danger"),
                ],
                title="Item 2",
            ),
            dbc.AccordionItem(
                "This is the content of the third section",
                title="Item 3",
            ),
        ],
    )
)


def create_layout(app):
    @app.callback([Output('container-body', 'children')],
                [Input('add-plot', 'n_clicks')], 
                [State('container-body', 'children')]
    )
    def create_subplot(n_clicks, children):        
        plt_type = dropdown(label='plot-type', options={val:val for val in plot_categories.keys()}, value='scatter', index=n_clicks)
        data_type = dropdown(label='data_frame', options={val:val for val in data_sources.keys()}, value='carshare', index=n_clicks)
        type_data = [plt_type, data_type]
        type_data.extend(parameters_widget(n_clicks))
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
                                                children=type_data, 
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
                                            Graph(id={'type':'plotarea', 'index':n_clicks})                                  
                                ],
                                className="plotarea-item"
                            )
                ], 
                className='mainbody-item plotarea-main'
        )
        mainbody = Div(children= [sidebar, plotarea], className='body-main')
        children.append(mainbody)

        return [children]



def init_layout(app):
    navbar = [Div("Dynamic Interactive Dashboard"), 
                Div([
                        Label("Display Mode", style={'margin-right':'10px'}), 
                        Dropdown(options=['row', 'column'], value='row', style={'color':'black'})
                    ],
                    style={'display': 'flex', 'font-size': '1.1rem', 'align-items': 'center'}
                ),
                Div(
                    [
                        Button("Add Plot", id='add-plot',n_clicks=0, className='add-plot'), 
                        Button("Reset All ", id='reset-all',n_clicks=0, className='add-plot'),
                        Button("Reset Specific ", id='reset-specific',n_clicks=0, className='add-plot')
                    ],
                    style={'display': 'flex', 'justify-content': 'center'}
                ), 
                Div("Plotly | Dash"),
            ]

    app.layout = Div(
        children=[  
                    #header and button
                    Div(
                        children=[Div(children=navbar, className='container-item navbar-main'), 
                        ]
                    ),
                    #body elements
                    Div(children=[], id='container-body', className='container-body'),
                    Div(id='hidden', style={'display':'none'}),
                    Div(id='reset-plot', style={'display':'none'}),
                   
        ],
        className=''
    )
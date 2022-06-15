from dash.html import Div, Button
from dash.dcc import Graph
from dash import Input, Output, State

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
    navbar = [Div("Dynamic Interactive Dashboard"), "Plotly | Dash"]
    button = [Button("Add Plot", id='add-plot',n_clicks=0, className='add-plot')]

    app.layout = Div(
        children=[  
                    #header and button
                    Div(
                        children=[Div(children=navbar, className='container-item navbar-main'), 
                                Div(children=button, className='container-item button-main', id='button-main')
                        ]
                    ),
                    #body elements
                    Div(children=[], id='container-body', className='container-body'),
                    Div(id='hidden')
        ]
    )
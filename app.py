from dynamic_dashboard import app 
from dynamic_dashboard.layout import create_layout, init_layout
from dynamic_dashboard.callback import init_callback


def main(app=app):
    init_layout(app)
    create_layout(app)
    init_callback(app)
    return app.run_server(debug=True)

import dash_bootstrap_components as dbc
from dash import Input, Output, State, html

collapse = html.Div(
    [
        dbc.Button(
            "Open collapse",
            id="collapse-button",
            className="mb-3",
            color="primary",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody("This content is hidden in the collapse")),
            id="collapse",
            is_open=False,
        ),
    ]
)


# @app.callback(
#     Output("collapse", "is_open"),
#     [Input("collapse-button", "n_clicks")],
#     [State("collapse", "is_open")],
# )
# def toggle_collapse(n, is_open):
#     if n:
#         return not is_open
#     return is_open

if __name__=='__main__':
    main()
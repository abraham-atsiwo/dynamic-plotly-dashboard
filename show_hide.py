import dash
from dash import Input, Output
import dash.dcc as dcc
import dash.html as html

app = dash.Dash('example')

app.layout = html.Div([
    dcc.Dropdown(
        id = 'dropdown-to-show_or_hide-element',
        options=[
            'on', 'off'
        ],
        value = 'on'
    ),

    # Create Div to place a conditionally visible element inside
    html.Div([
        # Create element to hide/show, in this case an 'Input Component'
        dcc.Input(
        id = 'element-to-hide',
        placeholder = 'something',
        value = 'Can you see me?',
        )
    ] # <-- This is the line that will be changed by the dropdown callback
    )
    ])

@app.callback(
   Output(component_id='element-to-hide', component_property='style'),
   [Input(component_id='dropdown-to-show_or_hide-element', component_property='value')])

def show_hide_element(visibility_state):
    if visibility_state == 'on':
        return {'display': 'block'}
    if visibility_state == 'off':
        return {'display': 'none'}

if __name__ == '__main__':
    app.run_server(debug=True)
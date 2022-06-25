from dash import Dash 

app = Dash(__name__)
app.suppress_callback_exceptions = True
server = app.server
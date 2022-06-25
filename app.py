from dynamic_dashboard import app 
from dynamic_dashboard.layout import create_layout, init_layout
from dynamic_dashboard.callback import init_callback
import statsmodels.api as sm

server = app.server
def main(app=app):
    init_layout(app)
    create_layout(app)
    init_callback(app)


main()
if __name__=='__main__':
    app.run_server(debug=False)

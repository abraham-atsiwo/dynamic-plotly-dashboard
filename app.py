from dynamic_dashboard import app 
from dynamic_dashboard.layout import create_layout, init_layout
from dynamic_dashboard.callback import init_callback


def main(app=app):
    init_layout(app)
    create_layout(app)
    init_callback(app)
    return app.run_server(debug=True)

if __name__=='__main__':
    main()
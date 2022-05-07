import time
import dash
from dash.exceptions import PreventUpdate

from dash_extensions.enrich import Output, DashProxy, Input, MultiplexerTransform, html

app = DashProxy(transforms=[MultiplexerTransform()])
app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(id="status_bar"),
                html.Button(id="button1",n_clicks=0,children="bun1"),
                html.Button(id="button2",n_clicks=0,children="btn2"),
        ])
    ]
)


@app.callback(
    Output("status_bar","children"),
    Input("button1","n_clicks"),
    prevent_intial_call=True,
)
def btn1(n):
    if not n:
        raise PreventUpdate()
    return("btn1")

@app.callback(
    Output("status_bar","children"),
    Input("button2","n_clicks"),
    prevent_intial_call=True,
)
def btn1(n):
    if not n:
        raise PreventUpdate()
    return("btn2")

if __name__ == "__main__":
    app.run_server(debug=True,port=8054)
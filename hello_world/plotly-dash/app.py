from dash import Dash, dcc, html, Input, Output, callback

app = Dash(__name__)
server = app.server

app.layout = html.Div(
    html.Div([
        html.Div(id='text'),
        dcc.Interval(
            id='interval-component',
            interval=500, # in milliseconds
            n_intervals=0
        )
    ])
)


@callback(Output('text', 'children'),
          Input('interval-component', 'n_intervals'))
def update_text(count):

    if (count % 2) == 0: 
        return [
            html.Span('hello world')
        ]
    else:
        return [
            html.Span('')
        ]

if __name__ == '__main__':
    app.run()
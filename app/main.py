import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import flask


app= flask.Flask(__name__)
dash_app = dash.Dash(__name__, server=app, external_stylesheets=[dbc.themes.BOOTSTRAP])
dash_app.config.suppress_callback_exceptions = True

dash_app.layout = html.Div(
    children=[
        html.H1(children="TELA DE INDICADORES - ALFA3-BD"),
        html.Div(children="""PERCENTUAL DE ESTUDANTES POR PADRÃO DE LEITURA"""),
        dcc.Graph(
            id="example-graph1",
            figure={
                "data": [
                    {"x": ["Fluente", "Iniciante", "Pré-Leitor"], "y": [18.3, 47.2, 21.2], "type": "bar", "name": "MUNICIPAL"},
                    {
                        "x": ["Fluente", "Iniciante", "Pré-Leitor"],
                        "y": [23.6, 46.2, 18.9],
                        "type": "bar",
                        "name": "ESTADUAL",
                    },
                ],
                "layout": {"title": " Velocidade Por Minuto"},
            },
        ),

        html.Div(children="""PERCENTUAL DE ESTUDANTES QUE NÃO CONSEGUEM LER"""),
        dcc.Graph(
            id="example-graph2",
            figure={
                "data": [
                    {"x": ["Texto", "Pseudopalavras", "Palavras"], "y": [14.8, 9.3, 8.6], "type": "bar", "name": "MUNICIPAL"},
                    {
                        "x": ["Texto", "Pseudopalavras", "Palavras"],
                        "y": [10.9, 7.1, 6.7],
                        "type": "bar",
                        "name": "ESTADUAL",
                    },
                ],
                "layout": {"title": " Velocidade Por Minuto"},
            },
        ),

        html.Div(children="""QUALIDADE DA LEITURA"""),
        dcc.Graph(
            id="example-graph3",
            figure={
                "data": [
                    {"x": ["Texto", "Pseudopalavras", "Palavras"], "y": [22, 13, 96], "type": "bar", "name": "MUNICIPAL"},
                    {
                        "x": ["Texto", "Pseudopalavras", "Palavras"],
                        "y": [45, 33, 67],
                        "type": "bar",
                        "name": "ESTADUAL",
                    },
                ],
                "layout": {"title": " Precisão de Acertos ou Erros"},
            },
        ),
    ]

)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)

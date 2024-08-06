import dash
from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd

# Dados fictícios
df = pd.DataFrame({
    'Categoria': ['Revenda A', 'Revenda B', 'Revenda C', 'Revenda D'],
    'Recorencia': [1000, 200, 15578, 3047]
})

# Classe para o Dashboard
class Dashboard:
    def __init__(self):
        self.app = dash.Dash(__name__)
        self.setup_layout()
    
    def setup_layout(self):
        self.app.layout = html.Div(
            style={'fontFamily': 'Segoe UI, Tahoma, Geneva, Verdana, sans-serif', 'padding': '30px', 'backgroundColor': '#f4f4f9'},
            children=[
                html.H1('Dashboard teste MVP', style={
                    'textAlign': 'center', 'color': '#333', 'fontSize': '36px', 'marginBottom': '20px'
                }),
                
                html.Div(
                    style={'display': 'flex', 'justifyContent': 'space-between', 'flexWrap': 'wrap'},
                    children=[
                        html.Div(
                            style={'flex': '1', 'margin': '10px', 'minWidth': '300px', 'backgroundColor': '#fff', 'borderRadius': '8px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'padding': '20px'},
                            children=[
                                html.H3('Tabela de Dados', style={'textAlign': 'center', 'color': '#555'}),
                                dcc.Graph(
                                    id='tabela',
                                    figure={
                                        'data': [
                                            go.Table(
                                                header=dict(values=list(df.columns), fill_color='#007bff', font_color='white', align='center'),
                                                cells=dict(values=[df[col] for col in df.columns], fill_color='#f9f9f9', align='center')
                                            )
                                        ],
                                        'layout': go.Layout(
                                            autosize=True, 
                                            margin=dict(l=0, r=0, t=0, b=0),
                                            paper_bgcolor='#fff'
                                        )
                                    }
                                )
                            ]
                        ),
                        
                        html.Div(
                            style={'flex': '1', 'margin': '10px', 'minWidth': '300px', 'backgroundColor': '#fff', 'borderRadius': '8px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'padding': '20px'},
                            children=[
                                html.H3('Gráfico de Barras', style={'textAlign': 'center', 'color': '#555'}),
                                dcc.Graph(
                                    id='grafico-barras',
                                    figure={
                                        'data': [
                                            go.Bar(
                                                x=df['Categoria'],
                                                y=df['Recorencia'],
                                                marker=dict(color='#007bff')
                                            )
                                        ],
                                        'layout': go.Layout(
                                            title='Gráfico de Barras',
                                            title_x=0.5,
                                            xaxis=dict(title='Categoria', title_font=dict(size=14), tickfont=dict(size=12)),
                                            yaxis=dict(title='Recorencia', title_font=dict(size=14), tickfont=dict(size=12)),
                                            plot_bgcolor='#e9ecef',
                                            paper_bgcolor='#fff',
                                            margin=dict(l=30, r=30, t=50, b=30)
                                        )
                                    }
                                )
                            ]
                        ),

                        html.Div(
                            style={'flex': '1', 'margin': '10px', 'minWidth': '300px', 'backgroundColor': '#fff', 'borderRadius': '8px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'padding': '20px'},
                            children=[
                                html.H3('Gráfico de Pizza', style={'textAlign': 'center', 'color': '#555'}),
                                dcc.Graph(
                                    id='grafico-pizza',
                                    figure={
                                        'data': [
                                            go.Pie(
                                                labels=df['Categoria'],
                                                values=df['Recorencia'],
                                                hole=0.3,
                                                marker=dict(colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
                                            )
                                        ],
                                        'layout': go.Layout(
                                            title='Gráfico de Pizza',
                                            title_x=0.5,
                                            plot_bgcolor='#e9ecef',
                                            paper_bgcolor='#fff',
                                            margin=dict(l=30, r=30, t=50, b=30)
                                        )
                                    }
                                )
                            ]
                        ),
                    ]
                )
            ]
        )
    
    def run(self):
        self.app.run_server(debug=True)

if __name__ == '__main__':
    dashboard = Dashboard()
    dashboard.run()

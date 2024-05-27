import dash
from dash import dcc, html
import plotly.express as px
from data_processing import load_data, clean_data

# Load and clean the data
data = load_data('../data/football_stats.csv')
clean_data = clean_data(data)

# Create a Dash app
app = dash.Dash(__name__)

# Create the layout of the app
app.layout = html.Div([
    html.H1("Football Statistics Dashboard"),
    dcc.Graph(id='goals-graph', figure={})
])

# Callback to update the graph
@app.callback(
    dash.dependencies.Output('goals-graph', 'figure'),
    [dash.dependencies.Input('goals-graph', 'id')]
)
def update_graph(_):
    fig = px.bar(clean_data, x='team', y=['home_score', 'away_score'],
                 title='Goals Scored by Teams',
                 labels={'value': 'Goals', 'variable': 'Match Type'})
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

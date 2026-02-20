import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("formatted_output.csv")

# Clean columns
df.columns = df.columns.str.strip()

# Convert date
df["Date"] = pd.to_datetime(df["Date"])

# Create app
app = Dash(__name__)

app.layout = html.Div([

    html.H1("Soul Foods Pink Morsel Sales Dashboard",
            style={"textAlign": "center"}),

    dcc.RadioItems(
        id="region-filter",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "South", "value": "south"},
            {"label": "West", "value": "west"},
        ],
        value="all",
        inline=True
    ),

    dcc.Graph(id="sales-chart")

])


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"].str.lower() == selected_region]

    fig = px.line(
        filtered_df.sort_values("Date"),
        x="Date",
        y="Sales",
        labels={"Sales": "Total Sales ($)"}
    )

    fig.add_vline(
        x="2021-01-15",
        line_dash="dash",
        line_color="red"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)

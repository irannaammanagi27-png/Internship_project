from pathlib import Path

import pandas as pd
from dash import Dash, dcc, html
import plotly.graph_objects as go


def load_sales_data() -> pd.DataFrame:
    data_path = Path(__file__).with_name("formatted_sales.csv")
    sales = pd.read_csv(data_path)
    sales["date"] = pd.to_datetime(sales["date"])
    daily_sales = (
        sales.groupby("date", as_index=False)["sales"]
        .sum()
        .sort_values("date")
        .reset_index(drop=True)
    )
    return daily_sales


def create_app() -> Dash:
    sales_df = load_sales_data()
    price_change_date = pd.Timestamp("2021-01-15")

    before_change = sales_df[sales_df["date"] < price_change_date]
    after_change = sales_df[sales_df["date"] >= price_change_date]

    before_avg = before_change["sales"].mean()
    after_avg = after_change["sales"].mean()
    verdict = (
        "Sales were higher before the Pink Morsel price increase."
        if before_avg > after_avg
        else "Sales were higher after the Pink Morsel price increase."
    )

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=sales_df["date"],
            y=sales_df["sales"],
            mode="lines+markers",
            name="Daily sales",
            line={"color": "#1f77b4", "width": 3},
            marker={"size": 5},
        )
    )
    fig.add_vline(
        x=price_change_date,
        line_dash="dash",
        line_color="#d62728",
        annotation_text="Price increase",
        annotation_position="top left",
    )
    fig.update_layout(
        title="Daily Pink Morsel Sales",
        xaxis_title="Date",
        yaxis_title="Sales",
        template="plotly_white",
        margin={"l": 40, "r": 20, "t": 60, "b": 40},
    )

    app = Dash(__name__)
    app.layout = html.Div(
        [
            html.H1("Pink Morsel Sales Visualiser", style={"textAlign": "center"}),
            html.P(
                verdict,
                style={"textAlign": "center", "fontSize": "18px", "marginBottom": "20px"},
            ),
            dcc.Graph(id="sales-chart", figure=fig),
        ],
        style={"padding": "24px", "maxWidth": "1100px", "margin": "0 auto"},
    )
    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)

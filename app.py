from pathlib import Path

import pandas as pd
from dash import Dash, Input, Output, dcc, html
import plotly.graph_objects as go


def load_sales_data() -> pd.DataFrame:
    data_path = Path(__file__).with_name("formatted_sales.csv")
    sales = pd.read_csv(data_path)
    sales["date"] = pd.to_datetime(sales["date"])
    return sales.sort_values(["date", "region"]).reset_index(drop=True)


def create_app() -> Dash:
    sales_df = load_sales_data()
    price_change_date = pd.Timestamp("2021-01-15")

    app = Dash(__name__)
    app.layout = html.Div(
        [
            html.Div(
                [
                    html.H1(
                        "Pink Morsel Sales Visualiser",
                        style={"margin": "0", "fontSize": "2.2rem", "color": "#f7f7f7"},
                    ),
                    html.P(
                        "Explore regional sales and compare performance before and after the January 2021 price increase.",
                        style={"margin": "8px 0 0", "color": "#dbeafe", "fontSize": "1rem"},
                    ),
                ],
                style={
                    "background": "linear-gradient(135deg, #1d4ed8, #7c3aed)",
                    "padding": "24px 28px",
                    "borderRadius": "16px",
                    "boxShadow": "0 10px 30px rgba(0,0,0,0.15)",
                    "marginBottom": "20px",
                },
            ),
            html.Div(
                [
                    html.Label(
                        "Filter by region",
                        style={"fontWeight": "600", "color": "#1f2937", "marginBottom": "8px"},
                    ),
                    dcc.RadioItems(
                        id="region-radio",
                        options=[
                            {"label": region.capitalize(), "value": region}
                            for region in ["all", "north", "east", "south", "west"]
                        ],
                        value="all",
                        inline=True,
                        style={"padding": "8px 0", "color": "#1f2937"},
                    ),
                ],
                style={
                    "background": "#ffffff",
                    "padding": "16px 20px",
                    "borderRadius": "14px",
                    "boxShadow": "0 4px 14px rgba(0,0,0,0.08)",
                    "marginBottom": "18px",
                },
            ),
            dcc.Graph(id="sales-chart"),
        ],
        style={"padding": "24px", "maxWidth": "1100px", "margin": "0 auto", "background": "#f3f6ff", "minHeight": "100vh"},
    )

    @app.callback(
        Output("sales-chart", "figure"),
        Input("region-radio", "value"),
    )
    def update_chart(selected_region: str):
        filtered = sales_df.copy()
        if selected_region != "all":
            filtered = filtered[filtered["region"] == selected_region]

        daily_sales = (
            filtered.groupby("date", as_index=False)["sales"]
            .sum()
            .sort_values("date")
            .reset_index(drop=True)
        )

        price_change_date = pd.Timestamp("2021-01-15")
        before_change = daily_sales[daily_sales["date"] < price_change_date]
        after_change = daily_sales[daily_sales["date"] >= price_change_date]
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
                x=daily_sales["date"],
                y=daily_sales["sales"],
                mode="lines+markers",
                name="Daily sales",
                line={"color": "#2563eb", "width": 3},
                marker={"size": 5, "color": "#7c3aed"},
            )
        )
        fig.add_vline(
            x=price_change_date,
            line_dash="dash",
            line_color="#ef4444",
            annotation_text="Price increase",
            annotation_position="top left",
        )
        fig.update_layout(
            title=f"{selected_region.capitalize()} Pink Morsel Sales",
            xaxis_title="Date",
            yaxis_title="Sales",
            template="plotly_white",
            margin={"l": 40, "r": 20, "t": 60, "b": 40},
            hovermode="x unified",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
        )

        return fig

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)

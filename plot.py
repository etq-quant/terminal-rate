import plotly.graph_objects as go
from plotly.subplots import make_subplots


def create_plot(df):
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces
    fig.add_trace(
        go.Scatter(x=df.index, y=df["spy"], name="spy", line=dict(color="#FFA62F")),
        secondary_y=True,
    )

    # Add traces
    fig.add_trace(
        go.Scatter(
            x=df.index, y=df["USYTFRB10Y=RR"], name="10Y", line=dict(color="#E42217")
        ),
        secondary_y=False,
    )

    # Add traces
    fig.add_trace(
        go.Scatter(
            x=df.index, y=df["USYTFRB2Y=RR"], name="2Y", line=dict(color="#357EC7")
        ),
        secondary_y=False,
    )

    # Add traces
    fig.add_trace(
        go.Scatter(
            x=df.index, y=df["fed_rate"], name="fed_rate", line=dict(color="#3A3B3C")
        ),
        secondary_y=False,
    )

    for i, dd in enumerate(fig.data):
        x, y = dd.x[-1], dd.y[-1]
        if i == 0:
            fig.add_scatter(
                x=[x],
                y=[y],
                mode="markers+text",
                text="{:.2f}".format(dd.y[-1]),
                textfont=dict(color=dd.line.color),
                textposition="top right",
                marker=dict(color=dd.line.color, size=10, opacity=0.8),
                legendgroup=dd.name,
                showlegend=False,
                secondary_y=True,
            )

        else:
            x1, y1 = fig.data[i - 1].x[-1], fig.data[i - 1].y[-1]
            if abs(y - y1) < 2:
                y = y + 1

            fig.add_scatter(
                x=[x],
                y=[y],
                mode="markers+text",
                text="{:.2f}%".format(dd.y[-1]),
                textfont=dict(color=dd.line.color),
                textposition="top right",
                marker=dict(color=dd.line.color, size=12, opacity=0),
                legendgroup=dd.name,
                showlegend=False,
                secondary_y=False,
            )

    fig.update_layout(
        title=dict(text="SPY - Bond Yield (2Y & 10Y) - FED Rate", font_size=16),
        width=1200,
        height=600,
        xaxis=dict(
            autorange=True,
            showline=True,
            showgrid=False,
            showticklabels=True,
            automargin=True,
            rangeselector=dict(
                buttons=list(
                    [
                        dict(count=6, label="6m", step="month", stepmode="backward"),
                        dict(count=1, label="YTD", step="year", stepmode="todate"),
                        dict(count=1, label="1y", step="year", stepmode="backward"),
                        dict(count=5, label="5y", step="year", stepmode="backward"),
                        dict(count=10, label="10y", step="year", stepmode="backward"),
                        dict(count=20, label="20y", step="year", stepmode="backward"),
                        dict(step="all"),
                    ]
                )
            ),
            rangeslider=dict(visible=True),
            type="date",
        ),
        yaxis2=dict(
            title="SPY",
            gridcolor="#D5D8DC",
            # ticksuffix='%',
            # tickformat='.0f',
            fixedrange=False,
            autorange=True,
            showgrid=False,
            zeroline=False,
            showline=False,
            showticklabels=True,
        ),
        yaxis=dict(
            title="rate %",
            gridcolor="#D5D8DC",
            # ticksuffix='%',
            # tickformat='.0f',
            fixedrange=False,
            autorange=True,
            showgrid=True,
            zeroline=False,
            showline=False,
            showticklabels=True,
        ),
        autosize=True,
        margin=dict(
            autoexpand=True,
            l=150,
            r=10,
            t=110,
            # pad=200,
        ),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            # y=0.5,
            x=0.7,
            xanchor="left",
        ),
        plot_bgcolor="white",
    )
    return fig

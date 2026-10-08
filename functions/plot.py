import plotly.express as px
from functions.download_data import download_data
from plotly.graph_objects import Figure

def plot_history(ticker: str) -> Figure:
    """
    Plot historical data from Yahoo Finance.

    Args:
        ticker(str): The ticker.
    """

    data = download_data(ticker)
    fig = px.line(
        data_frame=data,
        x = 'Date',
        y = 'Close',
        title = f'{ticker} stock price'
    )

    return fig
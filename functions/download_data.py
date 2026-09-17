import pandas as pd
import yfinance as yf

def download_data(
    tickers: str,
    multi_level_index: bool = False
) -> pd.DataFrame:

    """
    Downloads data from Yahoo Finance.
    Args:
        tickers(str): Data ticker.
        multi_level_index(bool): Remove/Include row indexes.
    """

    data = yf.download(
        tickers = tickers,
        multi_level_index = multi_level_index
    ).reset_index()

    return data
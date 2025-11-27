import os
from pathlib import Path
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


def ensure_dir(path):
    """Crea una carpeta si no existe."""
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def download_crypto_prices(tickers, start_date, end_date, auto_adjust=False):
    """
    Descarga precios diarios de criptomonedas con yfinance.
    Retorna DataFrame con columnas = activos y filas = fechas.
    """
    prices = {}

    for name, ticker in tickers.items():
        data = yf.download(
            ticker,
            start=start_date,
            end=end_date,
            auto_adjust=auto_adjust
        )

        if data.empty:
            raise ValueError(f"No se obtuvieron datos para {ticker}")

        # yfinance puede devolver MultiIndex
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)

        for col in ["Adj Close", "Close", "Price"]:
            if col in data.columns:
                serie = data[col].copy()
                break
        else:
            raise ValueError(f"{ticker} no contiene columna de precio válida")

        prices[name] = serie

    df = pd.DataFrame(prices).dropna()
    return df


def compute_log_returns(prices_df):
    """Calcula retornos logarítmicos."""
    return np.log(prices_df / prices_df.shift(1)).dropna()


def plot_log_returns(log_returns, save_path=None):
    """Grafica los retornos logarítmicos de múltiples series."""
    fig, axes = plt.subplots(
        log_returns.shape[1],
        1,
        figsize=(12, 3 * log_returns.shape[1]),
        sharex=True
    )

    if log_returns.shape[1] == 1:
        axes = [axes]

    for ax, col in zip(axes, log_returns.columns):
        ax.plot(log_returns.index, log_returns[col], linewidth=0.8)
        ax.set_title(f"Retornos logarítmicos de {col}")
        ax.axhline(0, color="black", linestyle="--", linewidth=0.6)
        ax.grid(True)

    plt.xlabel("Fecha")
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()

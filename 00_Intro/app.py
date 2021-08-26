import yfinance as yf
import streamlit as st
from datetime import date

st.sidebar.date_input("Start date", value=date(2019,1,1), key="start_date")
st.sidebar.date_input("End date", value=date(2021,1,1), key="end_date")

ticker_symbol = "GOOGL"

st.write("""
# Simple Stock Apps

This app's only purpose is to show certain ticker closing price and volume. Currently showing {}

""".format(st.session_state.ticker))
st.text_input(label="Ticker", value=ticker_symbol, key="ticker")


ticker_data = yf.Ticker(st.session_state.ticker)
ticker_df = ticker_data.history(period="1d", start=st.session_state.start_date , end=st.session_state.end_date)

st.line_chart(ticker_df.Close)
st.line_chart(ticker_df.Volume)
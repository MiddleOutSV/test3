import streamlit as st
import yfinance as yf

default_tickers = ["OXY", "SLB", "PBR", "ECO", "GTE", "VLO", "OBE", "MRO", "VRN", "VET", "APA", "CVE", "OVV", "REI", "SU", "AR", "BTE", "PR"]

@st.cache
def get_news(ticker):
    stock = yf.Ticker(ticker)
    return stock.news

def main():
    st.title("Oil Stocks News")
    
    ticker_input = st.text_input("Enter Ticker Symbol")
    if ticker_input:
        if ticker_input not in default_tickers:
            default_tickers.append(ticker_input.upper())

    news_container = st.container()

    for ticker in default_tickers:
        news = get_news(ticker)
        with news_container:
            st.subheader(f"News for {ticker}")
            for item in news:
                st.write(f"**{item['title']}**")
                st.write(f"Publisher: {item['publisher']}")
                st.write(f"[Read more]({item['link']})")
                st.write("---")

if __name__ == "__main__":
    main()

import streamlit as st
import yfinance as yf
import pandas as pd

# 기본 정유주 티커 리스트
default_tickers = ['OXY', 'SLB', 'PBR', 'ECO', 'GTE', 'VLO', 'OBE', 'MRO', 'VRN', 'VET', 'APA', 'CVE', 'OVV', 'REI', 'SU', 'AR', 'BTE', 'PR']

# 페이지 제목 설정
st.title('정유주 뉴스 모음')

# 사용자 입력 받기
user_tickers = st.text_input('추가할 티커를 입력하세요 (쉼표로 구분):', '')

# 사용자 입력 처리
if user_tickers:
    user_tickers = [ticker.strip() for ticker in user_tickers.split(',')]
    tickers = default_tickers + user_tickers
else:
    tickers = default_tickers

# 뉴스 가져오기 함수
def get_news(tickers):
    all_news = []
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            news = stock.news
            for item in news:
                item['ticker'] = ticker
            all_news.extend(news)
        except Exception as e:
            st.warning(f"{ticker}의 뉴스를 가져오는 데 실패했습니다: {str(e)}")
    return all_news

# 뉴스 가져오기
news = get_news(tickers)

# 뉴스를 날짜순으로 정렬
news_df = pd.DataFrame(news)
news_df['providerPublishTime'] = pd.to_datetime(news_df['providerPublishTime'], unit='s')
news_df = news_df.sort_values('providerPublishTime', ascending=False)

# 뉴스 표시
for i, (_, row) in enumerate(news_df.iterrows()):
    st.subheader(f"{row['ticker']}: {row['title']}")
    st.write(f"출처: {row['publisher']}")
    st.write(f"날짜: {row['providerPublishTime']}")
    st.write(f"링크: {row['link']}")
    st.write("---")

    # 20개 이상의 뉴스는 "더 보기" 버튼으로 표시
    if i == 19:
        if st.button("더 많은 뉴스 보기"):
            continue
        else:
            break

# GitHub 링크 추가
st.sidebar.markdown("[GitHub 저장소](https://github.com/yourusername/your-repo)")

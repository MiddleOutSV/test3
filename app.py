import streamlit as st
import yfinance as yf
import pandas as pd
import time

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

import streamlit as st
import yfinance as yf
import pandas as pd
import time

# ... (이전 코드 유지)

def get_news(tickers):
    all_news = []
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            news = stock.news
            if news:
                st.write(f"{ticker}에서 {len(news)}개의 뉴스를 가져왔습니다.")
                for item in news:
                    item['ticker'] = ticker
                all_news.extend(news)
            else:
                st.info(f"{ticker}의 뉴스가 없습니다.")
            time.sleep(1)
        except Exception as e:
            st.warning(f"{ticker}의 뉴스를 가져오는 데 실패했습니다: {str(e)}")
    return all_news

news = get_news(tickers)

if news:
    st.write(f"총 {len(news)}개의 뉴스를 가져왔습니다.")
    
    # 뉴스 데이터의 구조 확인
    if news and len(news) > 0:
        st.write("뉴스 데이터 구조:")
        st.write(list(news[0].keys()))
    
    # DataFrame 생성
    news_df = pd.DataFrame(news)
    
    # 컬럼 이름 출력
    st.write("DataFrame 컬럼:")
    st.write(list(news_df.columns))
    
    # 날짜 정보를 위한 컬럼 찾기
    date_columns = [col for col in news_df.columns if 'time' in col.lower() or 'date' in col.lower()]
    
    if date_columns:
        date_column = date_columns[0]
        st.write(f"날짜 정보로 사용할 컬럼: {date_column}")
        news_df[date_column] = pd.to_datetime(news_df[date_column], unit='s', errors='coerce')
        news_df = news_df.sort_values(date_column, ascending=False)
    else:
        st.warning("날짜 정보를 포함하는 컬럼을 찾을 수 없습니다. 날짜 정렬을 건너뜁니다.")
    
    # 뉴스 표시
    for i, (_, row) in enumerate(news_df.iterrows()):
        st.subheader(f"{row['ticker']}: {row.get('title', 'No Title')}")
        st.write(f"출처: {row.get('publisher', 'N/A')}")
        if date_columns:
            st.write(f"날짜: {row.get(date_column, 'N/A')}")
        st.write(f"링크: {row.get('link', 'N/A')}")
        st.write("---")

        if i == 19:
            if st.button("더 많은 뉴스 보기"):
                continue
            else:
                break
else:
    st.warning("뉴스를 가져오는 데 실패했습니다. 잠시 후 다시 시도해주세요.")

# ... (이후 코드 유지)

# ... (이후 코드 유지)

# GitHub 링크 추가
st.sidebar.markdown("[GitHub 저장소](https://github.com/yourusername/your-repo)")

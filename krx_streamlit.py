import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title='jykl: 공포-탐욕 지수', layout="wide")

df = pd.read_csv('VIX.csv')
df_number = pd.read_csv('data_20200601_20220630.csv')

score = 17
if score >= 0 and score < 19:
    emoji = '😱'
elif score >= 20 and score < 39:
    emoji = '😨'
elif score >= 40 and score < 59:
    emoji = '😶'
elif score >= 60 and score < 79:
    emoji = '😋'
elif score >= 80 and score <= 100:
    emoji = '🤑'

st.title("jykl: 개인 투자자의 KTOP30 투자 심리지수")
st.markdown("""```
    이번 프로젝트를 통해서 투자자의 시장인식이 금융시장에 미치는 영향을 알아보고자 하였습니다.
따라서, 개인투자자의 시장인식이 담긴 댓글들을 모으고 이들을 수치화시킴으로써 개인투자자의 시장인식을 나타내는 새로운 지수를 개발해 보았습니다.""")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# 공포-탐욕 지수
st.header("공포-탐욕 지수")
st.markdown("""---""")
scoring, state = st.columns(2)
score_header = '<h2 style="text-align: center">Score</h2>'
score_text = f'<p style="font-size: 150px; text-align: center">{score}</p>'
state_header = '<h2 style="text-align: center">State</h2>'
state_emoji = f'<p style="font-size: 150px; text-align: center">{emoji}</p>'
with scoring:
    st.markdown(score_header, unsafe_allow_html=True)
    st.markdown(score_text, unsafe_allow_html=True)
with state:
    st.markdown(state_header, unsafe_allow_html=True)
    st.markdown(state_emoji, unsafe_allow_html=True)
st.markdown("CNN 머니에서 제공하는 `Fear & Greed Index`를 참고하여 국내 주식시장에 특화된 공포-탐욕 지수를 개발하였습니다.")
st.markdown("""공포-탐욕 지수는 투자자들의 감정을 공포와 탐욕의 정도로 수치화한 것으로, 
                0에 가까울수록 시장은 극단적 공포심에 지배되고, 100에 가까울수록 극단적 탐욕에 지배되는 것을 의미합니다.""")
st.markdown("- **공포**: 다수의 투자자가 두려움을 느껴 주식을 팔아치우는 상황을 의미합니다.")
st.markdown("- **탐욕**: 다수의 투자자가 이욕을 느껴 주식을 사모으는 상황을 의미합니다.")
st.markdown("""공포-탐욕 지수는 시장의 분위기를 가늠하는 데 사용될 수 있습니다. 
                개인투자자의 결정에 영향을 미칠 수 있는 감정과 편견을 확인하고 
                이들을 분석함으로써 시장 심리를 평가하는 유용한 방법으로 활용될 수 있습니다.""")
st.markdown("이모티콘은 아래와 같은 점수 범위와 감정을 나타냅니다. ")
st.markdown("""- 0 ~ 19 = **극단적 공포** 😱""")
st.markdown("""- 20 ~ 39 = **공포** 😨""")
st.markdown("""- 40 ~ 59 = **중립** 😶""")
st.markdown("""- 60 ~ 79 = **탐욕** 😋""")
st.markdown("""- 80 ~ 100 = **극단적 탐욕** 🤑""")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# 통합
st.header("공포-탐욕 지수 변화")
st.markdown("""---""")
fig_col, df_col = st.columns(2)
with fig_col:
    fig = px.line(df, x="Date", y="Open")
    st.plotly_chart(fig)
with df_col:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.dataframe(df)
st.markdown('- 2022년 6월 한 달간  일어난 지수 변화를 나타낸 그래프입니다.')
st.markdown('- 2022년 6월 1일 ~ 2022년 6월 30일')

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# 비정형 vs. 비정형
st.header("비정형 데이터 vs. 정형 데이터")
st.markdown("""---""")
fig_col1, fig_col2 = st.columns(2)
with fig_col1:
    date = df['Date'].values
    high = df['High'].values
    fig = go.Figure(go.Scatter(x=date, y=high))
    fig.update_layout(title='비정형 데이터')
    st.plotly_chart(fig)
with fig_col2:
    fig = go.Figure()
    date = df_number['날짜'].values
    volume = df_number['거래회전율'].values
    exchange = df_number['환율'].values
    fig.add_trace(go.Scatter(x=date, y=volume, name="거래회전율"))
    fig.add_trace(go.Scatter(x=date, y=exchange, name="환율"))
    fig.update_layout(title='정형 데이터')
    st.plotly_chart(fig)
st.markdown('공포-탐욕 지수를 계산하기 위해 다음과 같은 데이터를 사용하였습니다.')
st.markdown('1. **네이버 종목토론방 게시물, 유튜브 댓글**')
st.markdown('- 2020년 6월부터 2022년 6월까지 네이버 종목토론방(KODEX 30 기준)과 유튜브 채널 ‘삼프로TV_경제의신과함께’에 게시된 글과 댓글을 수집하였습니다.')
st.markdown('- 이러한 데이터를 사용한다면 시장에 대한 개인의 다양한 감정을 실시간으로 확인할 수 있을 것이라고 판단하였습니다.')
st.markdown('2. **거래회전율**')
st.markdown('- 거래량의 증가는 투자자가 현재 시장에 대해 더 탐욕을 느끼거나 더 공포를 느끼고 있음을 의미합니다.')
st.markdown('3. **환율**')
st.markdown('- 달러화 대비 원화 환율이 높아져 원화 가치가 내려가면 국내 시장에 대한 공포가 높아지고 그 반대의 상황이면 국내 시장에 대한 탐욕 지수가 높아진다고 볼 수 있습니다.')

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# 정형
st.header("정형 데이터: 거래 회전율")
st.markdown("""---""")
fig_col, explanation = st.columns(2)
with fig_col:
    fig = px.line(df_number, x="날짜", y="거래회전율")
    st.plotly_chart(fig)
with explanation:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('- 일반적인 계산법과 달리 다른 데이터와의 연결성을 위해 일일 거래회전율을 `일일 거래량의 총합 / 상장 주식 수의 평균`으로 계산하였습니다.')
    st.markdown('- KTOP30 거래회전율 = `30개 종목의 총 거래량의 자연로그 값 / 30개 종목의 총 상장 주식 수 평균의 자연로그 값`')
    st.markdown('- 또한, 값의 크기가 매우 크기 때문에 로그스케일링을 취해주었습니다.')
    st.markdown('- 0.5 이상일 경우 탐욕(greed), 0.5 이하일 경우 공포(fear)로 설정하였습니다.')

st.header("정형 데이터: 환율")
st.markdown("""---""")
fig_col, explanation = st.columns(2)
with fig_col:
    fig = px.line(df_number, x="날짜", y="환율")
    st.plotly_chart(fig)
with explanation:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('- 대외 충격에 민감한 우리나라의 특성을 반영해주기 위해 원/달러 환율 데이터를 지수 계산에 포함하였습니다.')
    st.markdown('- 환율 데이터는 과거의 경험을 바탕으로 max값을 1500, min값을 900으로 min-max-scaling 해주었으며, 자본이 이탈하는 상황이 주식 시장에 있어서는 부정적인 상황이기 때문에 환율이 상승하는 상황을 공포(fear)로 나타내주기 위해 `1 - (min-max-scaling한 환율값)`을 하여 위아래가 뒤집힌 환율 데이터를 지수에 반영하였습니다. ')
    st.markdown('- 0.5보다 클 경우 탐욕(greed), 0.5보다 낮을 경우 공포(fear)를 나타냅니다.')

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_st_style, unsafe_allow_html=True)

footer = "<p style='text-align: center'>jykl = ['전준호', '유선종', '김나연', '이승환'] <br> Developed with 💙 by jykl</p>"
st.markdown("---")
st.markdown(footer, unsafe_allow_html=True)
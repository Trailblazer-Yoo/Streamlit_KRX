import pandas as pd
import datetime
import streamlit as st
import streamlit.components.v1 as components
import plotly.express as px
import plotly.graph_objects as go
import csaps
import numpy as np
from scipy import interpolate



st.set_page_config(page_title='jykl: 공포-탐욕 지수', layout="wide")

df = pd.read_csv('VIX.csv')
df_text = pd.read_csv('2022-06_score.csv')
df_number = pd.read_csv('data_20200601_20220630.csv')

df2 = pd.read_csv('final.csv')

emo2 = df2[df2['fg_score'] >= 20]
emo2 = emo2[emo2['fg_score'] < 40]
emo2_len = len(emo2)

emo3 = df2[df2['fg_score'] >= 40]
emo3 = emo3[emo3['fg_score'] < 60]
emo3_len = len(emo3)

x = np.linspace(1., 30., 30)
y = np.array(df2['fg_score'])
sp = interpolate.interp1d(x,y,kind='cubic')

# sp = csaps.csaps(x, y, smooth=0.8)
xs = np.linspace(x[0], x[-1], 117)
ys = sp(xs)

real_tp_df = pd.DataFrame()
real_tp_df['days'] = x
real_tp_df['score'] = y

tp_df = pd.DataFrame()
tp_df['days'] = xs
tp_df['score'] = ys

# today = "2022년 6월 30일"
# score = 17

st.title("jykl: 개인 투자자의 KTOP30 투자 심리지수✨")
st.markdown("""```
    이번 프로젝트를 통해서 투자자의 시장인식이 금융시장에 미치는 영향을 알아보고자 하였습니다.
따라서, 개인투자자의 감정이 담긴 댓글들을 모으고 이들을 수치화시킴으로써 개인투자자의 시장인식을 나타내는 새로운 지수를 개발해 보았습니다.""")
# 공포-탐욕 지수
st.markdown("""---""")
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("CNN 머니에서 제공하는 <span class=emp>`Fear & Greed Index`</span>를 참고하여 국내 주식시장에 특화된 공포-탐욕 지수를 개발하였습니다.", unsafe_allow_html=True)
st.markdown("""공포-탐욕 지수는 **투자자들의 감정을 공포와 탐욕의 정도**로 수치화한 것으로, 
                **0**에 가까울수록 시장은 극단적 공포심에 지배되고, **100**에 가까울수록 극단적 탐욕에 지배되는 것을 의미합니다.""")
st.markdown("- **공포**: 다수의 투자자가 두려움을 느껴 주식을 팔아치우는 상황을 의미합니다.")
st.markdown("- **탐욕**: 다수의 투자자가 이욕을 느껴 주식을 사모으는 상황을 의미합니다.")
st.markdown("""공포-탐욕 지수는 시장의 분위기를 가늠하는 데 사용될 수 있습니다. 
                개인투자자의 결정에 영향을 미칠 수 있는 감정과 편견을 확인하고 
                이들을 분석함으로써 시장 심리를 평가하는 유용한 방법으로 활용될 수 있습니다.""")
st.markdown("이모티콘은 아래와 같은 점수 범위와 감정을 나타냅니다. ")
st.markdown("""- 0 ~ 20 = **극단적 공포** <span class=emp>😱</span>""", unsafe_allow_html=True)
st.markdown("""- 20 ~ 40 = **공포** <span class=emp>😨</span>""", unsafe_allow_html=True)
st.markdown("""- 40 ~ 60 = **중립** <span class=emp>😶</span>""", unsafe_allow_html=True)
st.markdown("""- 60 ~ 80 = **탐욕** <span class=emp>😋</span>""", unsafe_allow_html=True)
st.markdown("""- 80 ~ 100 = **극단적 탐욕** <span class=emp>🤑</span>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""---""")

st.header("공포-탐욕 지수")
# day_col, fig_col = st.columns([1,1])
# with day_col:
st.markdown("<br>", unsafe_allow_html=True)



# st.header(f"{today}의 공포-탐욕 지수")
day = st.date_input("날짜 조회", datetime.date(2022, 6, 30))
day = day.strftime("%Y-%m-%d")
try:
    open = df2[df2['날짜']==day]['fg_score'].values[0]
    score = open
    today = day

    if score >= 0 and score < 20:
        emoji = '😱'
    elif score >= 20 and score < 40:
        emoji = '😨'
    elif score >= 40 and score < 60:
        emoji = '😶'
    elif score >= 60 and score < 80:
        emoji = '😋'
    elif score >= 80 and score <= 100:
        emoji = '🤑'


    score = df2[df2['날짜'] == day]
    score = int(score['fg_score'].values)
    #st.markdown("""---""")
    score_header = '<h2 style="text-align: center">Score</h2>'
    score_text = f'<p style="font-size: 150px; text-align: center">{score}</p>'
    state_header = '<h2 style="text-align: center">State</h2>'
    state_emoji = f'<p style="font-size: 150px; text-align: center">{emoji}</p>'
    # with fig_col:
    #fig = px.line(tp_df, x='x', y='score')
    #fig = px.line(df, x="Date", y="Open")

    scoring, state = st.columns([1,1])
    with scoring:
        st.markdown(score_header, unsafe_allow_html=True)
        st.markdown(score_text, unsafe_allow_html=True)
    with state:
        st.markdown(state_header, unsafe_allow_html=True)
        st.markdown(state_emoji, unsafe_allow_html=True)

except:
    st.write(f"No data on `{day}`")
    open = None

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(f'이번달 😨 감정은 {emo2_len}회 발생했습니다.')
st.markdown(f'이번달 😶 감정은 {emo3_len}회 발생했습니다.')
st.markdown(f'이번달 😨 감정은 현재 연속{len(emo2.iloc[4:,:])}일 발생했습니다.')

st.markdown('* __현재 서비스는 2022년 6월에 한정되어 있습니다!__')

st.markdown("""---""")
st.header("6월의 공포-탐욕 지수 변화")
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

fig_tp1 = px.line(tp_df, x='days', y='score')
fig_tp2 = px.scatter(real_tp_df,x='days',y='score')
fig = go.Figure(data=fig_tp1.data+fig_tp2.data)
fig.update_layout(yaxis=dict(range=[20,80]))
fig.update_layout(title={'font': {'size': 25}, 'x': 0.5, 'text': '공포-탐욕지수'})

fig.update_layout(title={'font': {'size': 25}, 'x': 0.5, 'text': '공포-탐욕지수'},
    xaxis_title="Score",
    yaxis_title="Days",
    )


if open != None:
    fig.add_annotation(x=day, y=open, 
                    arrowcolor="red", arrowsize=2, arrowhead=3, ay=-50,
                    text='', font=dict(color="black", size=40))
    st.plotly_chart(fig)
else:
    st.plotly_chart(fig)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('- 2022년 6월 한 달간  일어난 지수 변화를 나타낸 그래프입니다.')
st.markdown('- 참고 > smoothing 된 그래프 입니다.')
st.markdown('- 댓글점수 데이터 50%, 거래회전율 25%, 환율 25%가 사용되어 산출된 공포-탐욕지수 그래프입니다.')

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)





st.markdown("""
<style>
.emp {
    font-size: 23px
}
</style>
""", unsafe_allow_html=True)



# 통합

# 비정형 vs. 비정형
st.markdown("""---""")
st.header("비정형 데이터 vs. 정형 데이터")
fig_col1, fig_col2 = st.columns(2)
with fig_col1:
    date = df_text['날짜'].values
    score = df2['fg_score'].values
    fig = go.Figure(go.Scatter(x=date, y=score))
    fig.update_layout(title={'font': {'size': 25}, 'x': 0.5, 'text': '비정형 데이터'})
    st.plotly_chart(fig)
with fig_col2:
    fig = go.Figure()
    date = df_number['날짜'].values
    volume = df_number['거래회전율'].values
    exchange = df_number['환율'].values
    fig.add_trace(go.Scatter(x=date, y=volume, name="거래회전율"))
    fig.add_trace(go.Scatter(x=date, y=exchange, name="환율"))
    fig.update_layout(title={'font': {'size': 25}, 'x': 0.5, 'text': '정형 데이터'})
    st.plotly_chart(fig)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('공포-탐욕 지수를 계산하기 위해 다음과 같은 데이터를 사용하였습니다.')
st.markdown('1. **네이버 종목토론방 게시물, 유튜브 댓글**')
st.markdown('- 2020년 6월부터 2022년 6월까지 네이버 종목토론방(KODEX 30 기준)과 유튜브 채널 ‘삼프로TV_경제의신과함께’에 게시된 글과 댓글을 수집하였습니다.')
st.markdown('- 이러한 데이터를 사용한다면 시장에 대한 개인의 다양한 감정을 실시간으로 확인할 수 있을 것이라고 판단하였습니다.')
st.markdown('2. **거래회전율**')
st.markdown('- 거래회전율의 증가는 거래량이 증가하고 있다는 의미이고, 이는 시장이 탐욕의 상태에 가깝다는 뜻입니다. 반대로 거래량이 없다면 시장이 공포의 상태에 가깝다는 뜻입니다.')
st.markdown('3. **환율**')
st.markdown('- 단기적으로 국내 주식시장의 외국 자본의 이탈은 곧 환율의 상승으로 이어지며, 외국 자본의 유입은 곧 환율의 하락으로 이어집니다. 환율의 급격한 상승 및 하락은 국내외 경제의 충격이 발생했다는 것을 의미하며, 주식 시장은 이를 즉각 반영하여 요동치므로 환율의 상승은 주식시장의 공포, 환율의 하락은 주식시장의 탐욕을 유추해볼 수 있습니다.')
st.markdown('- 환율 데이터를 통해 거시적인 경제 환경을 반영할 수 있으며, 단기적인 외국 자본의 진입 및 이탈을 반영할 수 있을 것으로 기대됩니다.')

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# 정형
st.markdown("""---""")
st.header("정형 데이터: 거래 회전율")
fig_col, explanation = st.columns(2)
with fig_col:
    fig = px.line(df_number, x="날짜", y="거래회전율")
    st.plotly_chart(fig)
with explanation:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('- 일반적인 계산법과 달리 다른 데이터와의 연결성을 위해 일일 거래회전율을 <span class=emp>`일일 거래량의 총합 / 상장 주식 수의 평균`</span>으로 계산하였습니다.', unsafe_allow_html=True)
    st.markdown('- KTOP30 거래회전율 = <span class=emp>`30개 종목의 총 거래량의 자연로그 값 / 30개 종목의 총 상장 주식 수 평균의 자연로그 값`</span>', unsafe_allow_html=True)
    st.markdown('- 또한, 값의 크기가 매우 크기 때문에 로그스케일링을 취해주었습니다.')
    st.markdown('- **0.5 이상일 경우 탐욕(greed), 0.5 이하일 경우 공포(fear)** 로 설정하였습니다.')
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""---""")
st.header("정형 데이터: 환율")
fig_col, explanation = st.columns(2)
with fig_col:
    fig = px.line(df_number, x="날짜", y="환율")
    st.plotly_chart(fig)
with explanation:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('- 대외 충격에 민감한 우리나라의 특성을 반영해주기 위해 원/달러 환율 데이터를 지수 계산에 포함하였습니다.')
    st.markdown('- 환율 데이터는 과거의 경험을 바탕으로 max값을 1500, min값을 900으로 min-max-scaling 해주었으며, 자본이 이탈하는 상황이 주식 시장에 있어서는 부정적인 상황이기 때문에 환율이 상승하는 상황을 공포(fear)로 나타내주기 위해 <span class=emp>`1 - (min-max-scaling한 환율 값)`</span>을 하여 위아래가 뒤집힌 환율 데이터를 지수에 반영하였습니다.', unsafe_allow_html=True)
    st.markdown('- **0.5보다 클 경우 탐욕(greed), 0.5보다 낮을 경우 공포(fear)** 를 나타냅니다.')

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

footer = "<p style='text-align: center'>jykl = ['jjh', 'ysj', 'kny', 'lsh'] <br> Developed with 💙 by jykl</p>"
st.markdown("---")
st.markdown(footer, unsafe_allow_html=True)
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv('VIX.csv')

st.title("프로젝트 제목")
st.markdown("""> 프로젝트 소개""")
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# 공포-탐욕 지수
st.header("공포-탐욕 지수")
st.markdown("""---""")
score, state = st.columns(2)
score_header = '<h2 style="text-align: center">Score</h2>'
score_text = '<p style="font-size: 150px; text-align: center">17</p>'
state_header = '<h2 style="text-align: center">State</h2>'
state_emoji = '<p style="font-size: 150px; text-align: center">😱</p>'
with score:
    st.markdown(score_header, unsafe_allow_html=True)
    st.markdown(score_text, unsafe_allow_html=True)
with state:
    st.markdown(state_header, unsafe_allow_html=True)
    st.markdown(state_emoji, unsafe_allow_html=True)
st.markdown("공포-탐욕 지수 설명")
st.markdown("""- **공포** 😱""")
st.markdown("""- **탐욕** 🤑""")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# 통합
st.header("Historical Data")
st.markdown("""---""")
fig_col, df_col = st.columns(2)
with fig_col:
    st.markdown("### Chart")
    fig = px.line(df, x="Date", y="Open")
    st.plotly_chart(fig)
with df_col:
    st.markdown("### Table")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.dataframe(df)
    st.table(df)
st.markdown('설명')

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# 비정형 vs. 비정형
st.header("비정형 vs. 정형 데이터")
st.markdown("""---""")
fig_col1, fig_col2 = st.columns(2)
with fig_col1:
    st.markdown("### 비정형 데이터")
    fig = px.line(df, x="Date", y="High")
    st.plotly_chart(fig)
with fig_col2:
    st.markdown("### 정형 데이터")
    fig = px.line(df, x="Date", y="Low")
    st.plotly_chart(fig)
st.markdown('설명')

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# 정형
st.title("정형 데이터")
st.markdown("""---""")
fig_col, explanation = st.columns(2)
with fig_col:
    fig = px.line(df, x="Date", y="Close")
    st.plotly_chart(fig)
with explanation:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 거래량")
    st.markdown('설명')
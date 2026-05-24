import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="교통사고 데이터 분석",
    layout="wide"
)

st.title("🚗 서울시 교통사고 데이터 분석")

st.write("서울시 교통사고 데이터를 분석한 프로젝트입니다.")
st.markdown("---")

# 연령대별 부상자 수
st.subheader("📊 연령대별 부상자 수")

injury_data = pd.DataFrame({
    "연령대": ["12세 이하", "13~20세", "21~30세", "31~40세", "41~50세"],
    "부상자수": [1338, 1660, 7391, 9218, 8062]
})

st.bar_chart(injury_data.set_index("연령대"))

# 연령대별 사망자 수
st.subheader("📈 연령대별 사망자 수")

death_data = pd.DataFrame({
    "연령대": ["12세 이하", "13~20세", "21~30세", "31~40세", "41~50세"],
    "사망자수": [2, 1, 21, 14, 15]
})

st.line_chart(death_data.set_index("연령대"))
st.subheader("📊 연령대별 전체 사고 비율")

total_data = pd.DataFrame({
    "연령대": ["12세 이하", "13~20세", "21~30세", "31~40세", "41~50세"],
    "사고수": [1340, 1661, 7412, 9232, 8077]
})

st.area_chart(total_data.set_index("연령대"))
population_df = pd.read_csv("population.csv", encoding="utf-8")
st.markdown("---")

st.subheader("👨‍👩‍👧 대한민국 인구 데이터")
st.write("인구가 많은 연령대에서 교통사고 발생 비율도 높게 나타났다.")

population_chart = pd.DataFrame({
    "연령대": ["10대", "20대", "30대", "40대", "50대"],
    "인구수": [4800000, 6800000, 7200000, 6900000, 7100000]
})

st.bar_chart(population_chart.set_index("연령대"))
st.write("30~50대 인구 비율이 높으며 교통사고 발생 비율도 높은 것으로 나타났다.")
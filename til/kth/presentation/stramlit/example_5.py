import pandas as pd
import numpy as np
import datetime
import streamlit as st

st.title("My Awesome App")

@st.fragment()
def toggle_and_text():
    cols = st.columns(2)
    cols[0].toggle("Toggle")
    cols[1].text_area("Enter text")

@st.fragment()
def filter_and_file():
    cols = st.columns(2)
    cols[0].checkbox("Filter")
    cols[1].file_uploader("Upload image")

toggle_and_text()
cols = st.columns(2)
cols[0].selectbox("Select", [1,2,3], None)
cols[1].button("Update")
filter_and_file()



def get_latest_updates():
    # 현재 시간을 기준으로 10개의 데이터 생성
    timestamps = [datetime.datetime.now() - datetime.timedelta(seconds=i * 10) for i in range(10)]
    values = np.random.randint(50, 150, size=10)  # 50~150 사이의 임의 값

    # 데이터 프레임 생성
    df = pd.DataFrame({"timestamp": timestamps, "value": values})

    # 시간 순 정렬
    df = df.sort_values("timestamp")

    return df


@st.fragment(run_every="3s")
def auto_function():
    df = get_latest_updates()
    st.line_chart(df.set_index("timestamp"))

auto_function()

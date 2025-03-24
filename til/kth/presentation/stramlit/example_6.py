import streamlit as st

# with st.echo():
st.title("CAT")

# 이미지 마크다운 링크
st.markdown("[![Click me](app/static/img.png)](https://streamlit.io)")

# 마크다운 파일 읽기 및 출력
try:
    with open("static/streamlit_static.md", "r", encoding="utf-8") as file:
        md_content = file.read()
    st.markdown(md_content)
except FileNotFoundError:
    st.error("Markdown 파일을 찾을 수 없습니다.")

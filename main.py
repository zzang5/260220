import streamlit as st

# 1. 페이지 기본 설정 (가장 먼저 와야 합니다)
st.set_page_config(page_title="나의 MBTI 진로 탐험기", page_icon="✨", layout="centered")

# 2. 화려한 네온사인 & 다크 테마 CSS 적용
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(-45deg, #0f172a, #312e81, #1e1b4b, #020617);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        color: white;
    }
    
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* 메인 제목 스타일 */
    .main-title {
        font-size: 3rem !important;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(to right, #c084fc, #38bdf8, #f472b6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 20px rgba(192, 132, 252, 0.5);
        margin-bottom: 0px;
    }
    
    /* 서브 타이틀 스타일 */
    .sub-title {
        text-align: center;
        color: #cbd5e1;
        font-size: 1.2rem;
        margin-bottom: 30px;
    }

    /* 결과 카드 스타일 */
    .result-card {
        background: rgba(30, 41, 59, 0.8);
        border-radius: 20px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(10px);
        margin-top: 20px;
    }
    
    .info-title { font-size: 1.2rem; font-

import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="MBTI 진로 탐험대", page_icon="🌈", layout="wide")

# 2. 스타일링 (에러 유발 인자 제거 및 깔끔한 CSS)
st.markdown("""
    <style>
    .main { background-color: #f9f9f9; }
    .stButton>button { width: 100%; border-radius: 20px; border: 2px solid #4A90E2; }
    .stAlert { border-radius: 15px; }
    h1 { color: #1E90FF; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 3. 데이터베이스 (16가지 전체 틀 마련)
mbti_db = {
    "ENFP": {
        "title": "🎉 재기발랄한 활동가",
        "pros": "창의적, 열정적, 뛰어난 공감 능력, 적응력 갑! 🌟",
        "cons": "쉽게 질림, 세부사항 간과, 감정 기복 주의 🎢",
        "jobs": ["크리에이티브 디렉터 🎨", "심리 상담사 🤝", "이벤트 기획자 🎊", "저널리스트 ✍️"]
    },
    "INTJ": {
        "title": "🧠 용의주도한 전략가",
        "pros": "논리적, 분석적, 독립심 강함, 완벽주의 🎯",
        "cons": "타인 감정에 무딜 수 있음, 너무 비판적일 때가 있음 🧐",
        "jobs": ["데이터 과학자 📊", "투자 분석가 📈", "소프트웨어 엔지니어 💻", "전략 기획가 ♟️"]
    },
    "ESFJ": {
        "title": "🤝 사교적인 외교관",
        "pros": "친절함, 책임감, 협동심, 주변 사람 잘 챙김 🍰",
        "cons": "거절을 못 함, 비판에 상처받기 쉬움, 변화에 민감함 🥺",
        "jobs": ["초등학교 교사 🍎", "승무원 ✈️", "인사 관리자(HR) 👥", "홍보 전문가 📢"]
    }
    # 다른 MBTI도 이곳에 추가하면 됩니다!
}

# 4. 메인 화면 구성
st.title("🚀 내 꿈을 찾는 MBTI 진로 탐험대")
st.write("---")

# 사이드바에서 선택
with st.sidebar:
    st.header("🔍 나의 유형 찾기")
    # 리스트에 없는 유형을 골라도 에러가 안 나게 처리
    choice = st.selectbox("당신의 MBTI는 무엇인가요?", 
                          ["선택하세요"] + list(mbti_db.keys()))
    st.image("https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=400", use_container_width=True)
    st.info("MBTI는 여러분의 가능성을 보여주는 하나의 참고 자료일 뿐이에요! ✨")

# 5. 결과 출력 섹션
if choice != "선택하세요":
    data = mbti_db[choice]
    
    st.balloons() # 화려한 효과!
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown(f"### {choice} : {data['title']}")
        st.success(f"**💪 이런 장점이 있어요!**\n\n{data['pros']}")
        st.error(f"**⚠️ 이런 점은 주의해요!**\n\n{data['cons']}")

    with col2:
        st.markdown("### 💼 추천하는 멋진 직업들")
        for job in data['jobs']:
            st.button(job)
            
    st.divider()
    st.markdown("#### 💡 학생들을 위한 조언")
    st.info(f"{choice} 유형의 친구들은 자신의 강점인 '{data['pros'].split(',')[0]}' 능력을 발휘할 때 가장 행복할 거예요!")

else:
    st.warning("왼쪽 사이드바에서 MBTI를 선택하면 탐험이 시작됩니다! 🗺️")
    st.image("https://images.unsplash.com/photo-1488190211105-8b0e65b80b4e?w=800", use_container_width=True)

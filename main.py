import streamlit as st

# 페이지 설정 (브라우저 탭 이름과 아이콘)
st.set_page_config(page_title="✨ 내 꿈을 찾는 MBTI 탐험대", page_icon="🚀", layout="wide")

# 커스텀 CSS로 배경색 및 폰트 스타일링
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stTitle {
        color: #4A90E2;
        font-family: 'Nanum Gothic', sans-serif;
    }
    .mbti-card {
        padding: 20px;
        border-radius: 15px;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
    """, unsafe_allow_input_with_escaping=True)

# 🎈 헤더 섹션
st.title("🚀 내 꿈을 찾는 MBTI 진로 탐험대")
st.subheader("나의 MBTI를 선택하고, 나에게 꼭 맞는 미래를 설계해봐요! 🌈")
st.divider()

# 📊 데이터 정의 (MBTI 정보)
mbti_data = {
    "ENFP": {
        "title": "🎉 재기발랄한 활동가",
        "pros": "창의적이며 열정적임, 뛰어난 공감 능력, 적응력이 뛰어남",
        "cons": "쉽게 싫증을 느낌, 세부 사항에 약함, 감정 기복이 있음",
        "jobs": ["크리에이티브 디렉터 🎨", "심리 상담사 🤝", "이벤트 기획자 🎊", "저널리스트 ✍️"],
        "color": "#FFD700"
    },
    "INTJ": {
        "title": "🧠 용의주도한 전략가",
        "pros": "논리적이고 분석적임, 독립심이 강함, 목표 달성 의지가 높음",
        "cons": "타인의 감정에 무딜 수 있음, 지나치게 비판적임, 사회적 상황을 어려워함",
        "jobs": ["데이터 과학자 📊", "투자 분석가 📈", "소프트웨어 엔지니어 💻", "전략 기획가 ♟️"],
        "color": "#9370DB"
    },
    "ESFJ": {
        "title": "🤝 사교적인 외교관",
        "pros": "친절하고 책임감이 강함, 협동심이 좋음, 주변을 잘 챙김",
        "cons": "거절을 잘 못함, 변화를 두려워함, 타인의 비판에 상처받음",
        "jobs": ["초등학교 교사 🍎", "승무원 ✈️", "인사 관리자(HR) 👥", "홍보 전문가 📢"],
        "color": "#FF69B4"
    }
    # (다른 MBTI들도 같은 형식으로 추가 가능합니다!)
}

# 🔍 선택 섹션
col1, col2 = st.columns([1, 2])

with col1:
    st.info("### 🧐 정보를 확인하고 싶은 MBTI를 골라보세요!")
    selected_mbti = st.selectbox(
        "MBTI 유형 선택",
        options=list(mbti_data.keys()) + ["준비 중..."],
        index=0
    )

with col2:
    if selected_mbti in mbti_data:
        data = mbti_data[selected_mbti]
        
        # 멋진 카드형 출력
        st.markdown(f"## {data['title']} ({selected_mbti})")
        
        # 장단점 섹션
        c1, c2 = st.columns(2)
        with c1:
            st.success(f"### ✅ 장점\n{data['pros']}")
        with c2:
            st.warning(f"### ⚠️ 주의할 점\n{data['cons']}")
            
        st.divider()
        
        # 추천 직업 섹션
        st.write("### 💼 추천하는 직업군")
        cols = st.columns(len(data['jobs']))
        for i, job in enumerate(data['jobs']):
            cols[i].button(job, key=f"job_{i}", use_container_width=True)
            
        st.balloons() # 선택 시 풍선 애니메이션 효과
    else:
        st.write("다른 유형들은 업데이트 중입니다! 🚧")

# 💡 하단 팁
st.sidebar.markdown("### 💡 진로 팁")
st.sidebar.info("MBTI는 단지 도구일 뿐이에요! 가장 중요한 건 여러분의 **흥미**와 **열정**이라는 사실을 잊지 마세요! 🔥")

st.sidebar.markdown("---")
st.sidebar.write("Designed with ❤️ for Students")

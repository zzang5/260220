import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="16 MBTI 진로 탐험대", page_icon="🎓", layout="wide")

# 2. 커스텀 스타일 (화려한 컬러)
st.markdown("""
    <style>
    .stApp { background-color: #F8F9FA; }
    h1 { color: #FF4B4B; text-align: center; font-size: 3rem !important; }
    .mbti-header { padding: 10px; border-radius: 10px; text-align: center; color: white; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 3. 16가지 MBTI 전체 데이터베이스
mbti_db = {
    # 분석가형 (NT)
    "INTJ": {"title": "🧠 용의주도한 전략가", "pros": "분석력, 독립성, 전략적 사고", "cons": "지나친 비판, 인간관계의 어려움", "jobs": ["데이터 과학자 📊", "투자 분석가 📈", "교수 🎓", "시스템 설계자 💻"]},
    "INTP": {"title": "🔍 논리적인 사색가", "pros": "객관적 분석, 독창성, 지적 호기심", "cons": "실행력 부족, 개인주의적, 복잡한 생각", "jobs": ["연구원 🧪", "프로그래머 ⌨️", "철학자 📜", "수학자 📐"]},
    "ENTJ": {"title": "👑 대담한 통솔자", "pros": "지도력, 결단력, 효율성 중시", "cons": "타인에게 강압적일 수 있음, 참을성 부족", "jobs": ["경영인(CEO) 💼", "변호사 ⚖️", "정치인 🏛️", "벤처 캐피탈리스트 💰"]},
    "ENTP": {"title": "💡 뜨거운 논쟁을 즐기는 변론가", "pros": "임기응변, 박학다식, 새로운 시각", "cons": "말이 앞섬, 반복 업무에 약함", "jobs": ["기획자 📝", "정치 분석가 🗣️", "광고 제작자 🎥", "기업가 🚀"]},
    
    # 외교관형 (NF)
    "INFJ": {"title": "🧘 선의의 옹호자", "pros": "통찰력, 인내심, 강한 도덕관", "cons": "지나친 완벽주의, 내면의 갈등", "jobs": ["심리 상담사 🤝", "작가 ✍️", "사회복지사 🏥", "예술가 🎨"]},
    "INFP": {"title": "🌈 열정적인 중재자", "pros": "높은 감수성, 이해심, 창의성", "cons": "상처를 잘 받음, 현실성 부족", "jobs": ["예술가 🎨", "NGO 활동가 🌍", "상담가 💬", "사서 📚"]},
    "ENFJ": {"title": "🤝 정의로운 사회운동가", "pros": "카리스마, 설득력, 공동체 의식", "cons": "과도한 희생, 타인의 시선 의식", "jobs": ["교육자 🏫", "정치인 🎤", "공연 기획자 🎭", "코치 📣"]},
    "ENFP": {"title": "🎉 재기발랄한 활동가", "pros": "에너지 넘침, 사교적, 낙천적", "cons": "산만함, 감정 기복, 반복 업무 기피", "jobs": ["홍보 전문가 📢", "연예인 🌟", "여행 작가 ✈️", "카피라이터 ✍️"]},
    
    # 관리자형 (SJ)
    "ISTJ": {"title": "📊 청렴결백한 논리주의자", "pros": "철저함, 책임감, 보수적 가치 중시", "cons": "변화에 소극적, 융통성 부족", "jobs": ["공무원 🏛️", "회계사 📑", "군인/경찰 👮", "사서 📚"]},
    "ISFJ": {"title": "🛡️ 용감한 수호자", "pros": "헌신적, 세심함, 안정감 제공", "cons": "자신을 과소평가, 변화를 두려워함", "jobs": ["간호사 🏥", "교사 🍎", "사회복지사 🤝", "박물관 큐레이터 🏛️"]},
    "ESTJ": {"title": "👔 엄격한 관리자", "pros": "조직 관리 능력, 현실적, 추진력", "cons": "독단적, 타인의 감정 무시", "jobs": ["경영 관리직 🏢", "군 장교 🎖️", "행정 공무원 📋", "은행원 🏦"]},
    "ESFJ": {"title": "💖 사교적인 외교관", "pros": "사교적, 조화로운 관계, 봉사 정신", "cons": "거절을 못 함, 타인의 비판에 민감", "jobs": ["승무원 ✈️", "초등 교사 🍎", "영업 사원 🤝", "사회 사업가 🏘️"]},

    # 탐험가형 (SP)
    "ISTP": {"title": "🛠️ 만능 재주꾼", "pros": "객관적, 적응력, 도구 활용 능력", "cons": "개인주의, 감정 표현 부족", "jobs": ["기술자 🔧", "파일럿 👨‍✈️", "운동선수 ⚽", "포렌식 전문가 🔍"]},
    "ISFP": {"title": "🎨 호기심 많은 예술가", "pros": "겸손함, 예술적 감각, 유연함", "cons": "결단력 부족, 경쟁 스트레스에 취약", "jobs": ["디자이너 🖌️", "음악가 🎵", "조경가 🌿", "사진작가 📸"]},
    "ESTP": {"title": "⚡ 수완 좋은 활동가", "pros": "관찰력, 활동적, 문제 해결 능력", "cons": "충동적, 장기적 계획 부족", "jobs": ["소방관 👨‍🚒", "영업 전문가 💰", "뉴스 리포터 🎤", "스포츠 코치 🏀"]},
    "ESFP": {"title": "✨ 자유로운 영혼의 연예인", "pros": "낙천적, 사교적, 미적 감각", "cons": "진지함 부족, 즉흥적인 결정", "jobs": ["배우/모델 🎬", "이벤트 플래너 🎈", "승무원 ✈️", "여행 가이드 🗺️"]}
}

# 4. 메인 화면 레이아웃
st.title("🚀 16가지 MBTI 진로 탐험대")
st.markdown("<h4 style='text-align: center;'>나의 성향에 딱 맞는 미래 직업을 찾아보세요!</h4>", unsafe_allow_html=True)
st.write("---")

# 드롭다운 메뉴
selected_mbti = st.selectbox(
    "나의 MBTI 유형을 선택해 주세요 👇",
    options=["유형을 선택하세요"] + list(mbti_db.keys()),
    index=0
)

# 5. 선택 결과 출력
if selected_mbti != "유형을 선택하세요":
    data = mbti_db[selected_mbti]
    
    # 유형별 컬러 테마 지정 (간단 예시)
    st.balloons()
    
    st.markdown(f"## {selected_mbti} : {data['title']}")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.info("### 💪 이런 점이 강점이에요!")
        st.write(data['pros'])
        
        st.warning("### ⚠️ 이런 점은 노력이 필요해요!")
        st.write(data['cons'])

    with col2:
        st.success("### 💼 추천하는 멋진 직업들")
        for job in data['jobs']:
            st.button(job, key=job) # 버튼 형태로 표시

    st.write("---")
    st.info(f"💡 **선생님의 조언:** {selected_mbti} 친구들은 아주 특별한 재능을 가지고 있어요. 장점을 살려 멋진 미래를 만들어가길 바라요! 🔥")
    
else:
    # 선택 전 대기 화면
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("https://images.unsplash.com/photo-1513258496099-48168024adb0?w=800", caption="여러분의 꿈을 응원합니다!", use_container_width=True)
        st.markdown("<p style='text-align: center;'>유형을 선택하면 상세 정보가 나타납니다.</p>", unsafe_allow_html=True)

# 푸터
st.sidebar.markdown("### 🏫 진로 교육 센터")
st.sidebar.write("본 서비스는 학생들의 진로 탐색을 돕기 위해 제작되었습니다.")
st.sidebar.markdown("---")
st.sidebar.caption("© 2024 MBTI Career Explorer")

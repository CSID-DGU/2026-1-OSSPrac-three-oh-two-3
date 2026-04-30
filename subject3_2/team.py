from flask import Flask, render_template

app = Flask(__name__)

# 팀 정보
TEAM_INFO = {
    "name": "Team 302",
    "tagline": "Data meets the Web.",
    "description": "통계와 웹 개발이 만나 만드는 오픈소스 프로젝트. 데이터 분석부터 웹 UI까지, 3인 3색의 팀입니다.",
    "stats": {
        "members": 3,
        "majors": 2,
        "languages": 7,
        "coffee": "∞"
    }
}

TEAM_MEMBERS = [
    {
        "name": "강지호",
        "english_name": "Jiho Kang",
        "role": "Data Analyst",
        "tag": "Statistics · SPSS · R",
        "major": "통계학과 (주전공)",
        "sub_major": "소프트웨어·AI (연계전공)",
        "year": "22학번 · 3학년",
        "intro": "통계 데이터를 다루며 인사이트를 발견하는 것을 좋아합니다. SPSS와 R을 활용한 통계 분석에 강점이 있습니다.",
        "skills": [
            {"name": "R", "icon": "📊"},
            {"name": "SPSS", "icon": "📈"},
            {"name": "SAS", "icon": "📉"},
            {"name": "Python", "icon": "🐍"},
            {"name": "Java", "icon": "☕"}
        ],
        "tools": ["R Studio", "Jupyter Notebook", "VS Code", "Eclipse IDE"],
        "projects": [
            "행복은 돈과 비례하는가에 대한 분석 (SPSS 기반 통계 분석)"
        ],
        "certificates": [],
        "contribution": "데이터 분석 및 통계 검증, 사용자 데이터 수집 설계, 가설 검정 기반 인사이트 도출",
        "contribution_percent": 33,
        "github": None,
        "email": "wlgh02211@gmail.com",
        "image": "images/member1.svg",
        "color": "#3b82f6"
    },
    {
        "name": "전동현",
        "english_name": "Donghyun Jeon",
        "role": "ML Engineer",
        "tag": "ML · Python · Backend",
        "major": "통계학과 (주전공)",
        "sub_major": "소프트웨어·AI (복수전공)",
        "year": "동국대학교 · 3학년",
        "intro": "머신러닝 모델 설계와 데이터 분석을 담당합니다. Random Forest, GBM 등 다양한 ML 모델 경험을 보유하고 있습니다.",
        "skills": [
            {"name": "Python", "icon": "🐍"},
            {"name": "Scikit-learn", "icon": "🤖"},
            {"name": "Pandas", "icon": "🐼"},
            {"name": "Seaborn", "icon": "📊"},
            {"name": "Random Forest", "icon": "🌲"}
        ],
        "tools": ["Jupyter Notebook", "Git", "R Studio", "IntelliJ IDEA", "VS Code"],
        "projects": [
            "타이타닉 탑승자 생존 여부 예측 (Random Forest, GBM)",
            "당뇨병 발병 여부 예측 (의료 데이터 기반)",
            "일별 따릉이 대여량 예측 (서울시 공공데이터)",
            "고객 이탈 여부 예측 (XGBoost)"
        ],
        "certificates": [
            "컴퓨터활용능력 1급 (2024.10)",
            "ADsP 데이터분석 준전문가 (2026.03)"
        ],
        "contribution": "백엔드 ML 모델 설계 및 학습, 데이터 전처리 파이프라인 구축, API 연동 로직 구현",
        "contribution_percent": 34,
        "github": None,
        "email": "2022110488@naver.com",
        "phone": "010-6748-0213",
        "image": "images/member2.svg",
        "color": "#10b981"
    },
    {
        "name": "조정민",
        "english_name": "Jeongmin Cho",
        "role": "Frontend Developer",
        "tag": "HTML · CSS · JavaScript",
        "major": "정보통신공학과",
        "sub_major": "프론트엔드 웹 개발",
        "year": "동국대학교 · 3학년",
        "intro": "프론트엔드 웹 개발에 관심이 많은 정보통신공학도입니다. HTML/CSS/JS를 기반으로 사용자 친화적인 화면을 만듭니다.",
        "skills": [
            {"name": "HTML", "icon": "📄"},
            {"name": "CSS", "icon": "🎨"},
            {"name": "JavaScript", "icon": "⚡"},
            {"name": "JSX", "icon": "⚛️"},
            {"name": "Python", "icon": "🐍"}
        ],
        "tools": ["VS Code", "Git"],
        "projects": [
            "Flask 기반 팀 소개 웹 페이지 구축",
            "Git 협업 워크플로우 실습"
        ],
        "certificates": [],
        "contribution": "프론트엔드 UI/UX 설계, HTML/CSS 페이지 구현, Flask 템플릿 연동, 반응형 디자인",
        "contribution_percent": 33,
        "github": "https://github.com/youngb0",
        "email": "jm11n@naver.com",
        "phone": "010-7501-8059",
        "image": "images/member3.svg",
        "color": "#a855f7"
    }
]

@app.route("/")
def index():
    return render_template("index.html", team=TEAM_INFO, members=TEAM_MEMBERS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
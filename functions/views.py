from django.shortcuts import render
# [코드 작성] 'random'모듈 가져오기
from random import *
# [코드 작성] 'datetime'모듈 가져오기
import datetime

# Create your views here.
def index(request):
    return render(request, "functions/index.html")

def image(request):
    return render(request, "functions/image.html")

def lucky(request):
    # [코드 작성] number 변수에 1부터 100까지의 정수 중 랜덤한 숫자 저장하기
    number = randint(1, 100)

    # 'context' 딕셔너리의 key와 value값으로 HTML에 전달하고 싶은 값을 추가
    context = {
        "number": number,
    }

    # [코드 추가] 'context'값을 HTML로 넘기기
    return render(request, "functions/lucky.html", context)

def birthday(request):
    # [코드 작성] 'datetime'모듈 가져오기
    today = datetime.date.today()

    # [코드 작성] 'year', 'month', 'day' 변수에 각각 오늘 날짜 정보 저장하기
    year = today.year
    month = today.month
    day = today.day

    # [코드 수정] 내 생일의 월일을 정수로 저장하기
    b_month = 1
    b_day = 1

    # 가장 빠른 생일의 연도 계산
    if (b_month > month):
        b_year = year
    elif (b_month == month) and (b_day >= day):
        b_year = year
    else:
        b_year = year + 1

    # 'datetime'모듈의 'date' 클래스를 이용하여 생일을 datetime 형식으로 만들기
    birthday = datetime.date(b_year, b_month, b_day)

    # 나의 생일까지 남은 요일을 계산
    d_day = birthday - today
    d_day = d_day.days

    context = {
        "year": year,
        "month": month,
        "day": day,
        "b_month": b_month,
        "b_day": b_day,
        "d_day": d_day,
    }

    return render(request, "functions/birthday.html", context)

def ranking(request):
    languages = [
        "Python",
        "C언어",
        "Java",
        "C++",
        "C#",
        "Visual Basic",
        "JavaScript",
        "Assembly",
        "SQL",
        "PHP",
    ]
    
    context = {
        "languages": languages,
    }

    return render(request, "functions/ranking.html", context)

def language(request, name):
    languages = {
        "Python": "웹 애플리케이션, 소프트웨어 개발, 데이터 과학, 기계 학습에 사용되는 프로그래밍 언어",
        "C언어": "1972년 켐 톰프슨과 데니스 리치가 유닉스 운영체제에서 사용하기 위해서 개발한 고급 언어",
        "Java": "1995년 썬 마이크로시스템즈에서 발표한 객체 지향 프로그래밍 언어",
        "C++": "C언어에 여러가지 기능을 추가하여 만든 프로그래밍 언어",
        "C#": "마이크로소프트에서 개발한 객체 지향 프로그래밍 언어",
        "Visual Basic": "마이크로소프트 윈도우용 응용 프로그램을 쉽게 개발하기 위해 만든 프로그래밍 언어",
        "JavaScript": "웹 페이지에서 복잡한 기능을 구현할 수 있도록 하는 프로그래밍 언어",
        "Assembly": "기계어와 일대일 대응이 되는 프로그래밍의 저급 언어",
        "SQL": "관계형 데이터베이스 시스템에서 정보를 저장하고 처리하기 위해 설계된 프로그래밍 언어",
        "PHP": "동적 웹 페이지를 쉽고 빠르게 만들 수 있도록 해주는 프로그래밍 언어",
    }

    # [코드 작성] languages 딕셔너리에서 'functions'앱의 'urls.py'에서 전달받은 인자값 '<str:name>'의 인수값 'name'을 key값으로 하는 value값 가져오기
    detail = languages[name]

    context = {
        "name": name,
        "detail": detail,
    }

    return render(request, "functions/language.html", context)

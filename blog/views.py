from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import plotly.io as pio


# Create your views here.
# 기본 페이지
def index(request): 
    return render(request, "index.html")

# 분석배경
# def about(request): 
#     return render(request, "about.html")

# 분석방법
def method(request): 
    return render(request, "method.html")

# 관련요인
def factors(request): 
    return render(request, "factors.html")

# how
def how(request): 
    return render(request, "how.html")

# references
def references(request): 
    return render(request, "references.html")

# 개발환경
def env(request): 
    return render(request, "env.html")



# FACTORS/ 
# 연령대
# def ages(request): 
#     return render(request, "factors/ages.html")

# FACTORS/ 
# 단체참여
def group(request): 
    return render(request, "factors/group.html")

# FACTORS/
# 수도권
def metropolitan(request): 
    return render(request, "factors/metropolitan.html")

# FACTORS/
# 1인가구
def single(request): 
    return render(request, "factors/single.html")

# FACTORS/ 
# 배우자
def spouse(request): 
    return render(request, "factors/spouse.html")

# FACTORS/ 
# 직업
def job(request): 
    return render(request, "factors/job.html")

# FACTORS/ 
# 배우자
def place(request): 
    return render(request, "factors/place.html")


# 년도별 chart - about 에 넣기 

def year_chart_about(request) : 
    df = pd.read_csv("data/graph.csv")

    fig = px.bar(df, x="age", y= "isolation", 
             barmode="group",
             animation_frame="year",
             text_auto=True,  #글자 설정
             width = 600, 
             height = 500             
             )
    graph_html = fig.to_html(full_html=False)

    return render(request, 'about.html', {"graph_html" : graph_html})


# 년도별 ages

def factors_age_chart(request) : 
    df = pd.read_csv("data/age_chart.csv")

    fig = px.bar(df, 
                x="연령대", 
                y= "percent", 
                # barmode="group",             
                text_auto=".3s",  #글자 설정
                color = "연령대",
                width = 1000, 
                height = 500,    
                # title = "2017~2023 연령대별 사회적고립도 "
                )
                
    # fig.update_yaxes(range=[10, 30])
    graph_html = fig.to_html(full_html=False)

    return render(request, 'factors/ages.html', {"graph_html" : graph_html})


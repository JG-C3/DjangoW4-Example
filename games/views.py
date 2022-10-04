from django.shortcuts import render, redirect
from random import *

# Create your views here.
win = 0
draw = 0
lose = 0

def rsp(request):
    global win, draw, lose

    context = {
        "win": win,
        "draw": draw,
        "lose": lose,
    }
    return render(request, "games/rsp.html", context)

def result(request, pick):
    global win, draw, lose
    
    rsp = ["가위", "바위", "보"]
    com = choice(rsp)

    if pick == com:
        result = "승리"
        win += 1
    elif (pick == "가위" and com == "보") or (pick == "바위" and com == "가위") or (pick == "보" and com == "바위"):
        result = "무승부"
        draw += 1
    else :
        result = "패배"
        lose += 1

    context = {
        "pick": pick,
        "com": com,
        "result": result,
        "win": win,
        "draw": draw,
        "lose": lose,
    }

    return render(request, "games/result.html", context)

def reset(request):
    global win, draw, lose
    
    win, draw, lose = 0, 0, 0
    return redirect("games:rsp")
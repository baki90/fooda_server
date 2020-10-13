#drow graph
import matplotlib.pyplot as plt
import numpy as np
import db
from io import BytesIO

def drawGraph(tan, dan, ji):
    labels = ['carbohydrate', 'protein', 'fat']
    colors = ['yellowgreen', 'lightgreen', 'green']
    ratio = [tan, dan, ji]

    plt.pie(ratio, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=90)
    img = BytesIO()
    plt.savefig(img, transparent=True)
    img.seek(0)
    return img

#사용자의 주간 섭취율을 탄, 단, 지 순으로 반환함
def weekAnalyze(userid):
    conn = db.connect()
    cursor = conn.cursor()
    sql = "select SUM(f.carbohydrate) as car, SUM(f.protein) as pro, SUM(f.fat) as fat from diet as d JOIN food as f on d.food_id = f.food_id where user_id=%d and d.date between DATE_ADD(NOW(), INTERVAL -1 WEEK) AND NOW();"%(userid)
    cursor.execute(sql)
    result = cursor.fetchall()[0]
    db.close(conn)
    return result['car'], result['pro'], result['fat']

def personType(userid):
    tan, dan, ji = weekAnalyze(userid)
    total = tan + dan + ji
    tan /= total 
    dan /= total 
    ji /= total
    style = ''
    print(tan)
    print(dan)
    print(ji)
    if tan > 0.6:
        style += '탄수화물 과다 '
    elif tan < 0.5:
        style += '탄수화물 과소 '
    if dan > 0.25:
        style += '단백질 과다 '
    elif dan < 0.1:
        style += '단백질 과소 '
    if ji > 0.2:
        style += '지방 과다 '
    elif ji < 0.1:
        style += '지방 과소 '

    if style=='':
        style = '정상 식습관 '

    print(style)
    return style

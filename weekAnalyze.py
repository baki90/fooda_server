#drow graph
import matplotlib.pyplot as plt
import numpy as np
import db

def drawGraph(tan, dan, ji):
    labels = ['carbohydrate', 'fat', 'protein']
    colors = ['yellowgreen', 'lightgreen', 'green']
    ratio = [tan, dan, ji]

    plt.pie(ratio, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=90)
    plt.savefig('draw.png', transparent=True)
    return plt

#사용자의 주간 섭취율을 탄, 단, 지 순으로 반환함
def weekAnalyze(userid):
    conn = db.connect()
    cursor = conn.cursor()
    sql = "select SUM(f.carbohydrate) as car, SUM(f.protein) as pro, SUM(f.fat) as fat from diet as d JOIN food as f on d.food_id = f.food_id where user_id=%d and d.date between DATE_ADD(NOW(), INTERVAL -1 WEEK) AND NOW();"%(userid)
    cursor.execute(sql)
    result = cursor.fetchall()[0]
    db.close(conn)
    return result['car'], result['pro'], result['fat']

print(weekAnalyze(5))
from flask_restful import Resource, Api
from flask import request
import utils
import db

class PostUpload(Resource):
    def post(self): #if using post method
        board_id= int(request.form['board_id'])
        user_id= int(request.form['user_id'])
        title = str(request.form['title'])
        content = str(request.form['content'])
        img_path = str(request.form['img_path'])
       
            
        conn = db.connect()
        cursor = conn.cursor()
        sql = "insert into user values ('', '%d', %d, %s, %s, '%s', 0, 0,)"%(board_id,user_id,title,content,img_path)
        print(sql)
        cursor.execute(sql)
        conn.commit()
        db.close(conn)
        return {"게시글 등록이 완료되었습니다."}

class GetPostByBoardId(Resource):
    def post(self): #if using view
        print('hello')
        board_id=int(request.form['board_id'])
        print(board_id)
        conn = db.connect()
        cursor = conn.cursor()
        sql="select * from post where board_id='%d'"%(board_id)
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        db.close(conn)
        return result
class uplike(Resource):
    def post(self):
        post_id= int(request.form['post_id'])
        likes=int(request.form['likes'])
        conn = db.connect()
        cursor = conn.cursor()
        likes=likes+1
        sql="update post set likes='%d' where post_id='%d'"%(likes,post_id)
        print(sql)
        cursor.execute(sql)
        conn.commit()
        db.close(conn)
        return "좋아요를 누르셨습니다."

class delete(Resource):
    def post(self):
        post_id= int(request.form['post_id'])
        conn = db.connect()
        cursor = conn.cursor()
        sql="delete from post where post_id='%d'"%(post_id)
        print(sql)
        cursor.execute(sql)
        conn.commit()
        db.close(conn)
        return "게시글이 삭제되었습니다."

class gohidden(Resource):
    def post(self):
        post_id= int(request.form['post_id'])
        conn = db.connect()
        cursor = conn.cursor()
        sql="update post set hidden=0 where post_id='%d'"%(post_id)
        print(sql)
        cursor.execute(sql)
        conn.commit()
        db.close(conn)
        return "숨기기 완료."

class nohidden(Resource):
    def post(self):
        post_id= int(request.form['post_id'])
        conn = db.connect()
        cursor = conn.cursor()
        sql="update post set hidden=1 where post_id='%d'"%(post_id)
        print(sql)
        cursor.execute(sql)
        conn.commit()
        db.close(conn)
        return "숨기기 해제."

class hiddenshow(Resource):
    def post(self):
        user_id=int(request.form['user_id'])
        print(user_id)
        conn = db.connect()
        cursor = conn.cursor()
        sql="select * from post where user_id='%d' and hidden=1"%(user_id)
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        db.close(conn)
        return result

class searchbyuser(Resource):
    def post(self):
        user_id=int(request.form['user_id'])
        print(user_id)
        conn = db.connect()
        cursor = conn.cursor()
        sql="select * from post where user_id='%d'"%(user_id)
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        db.close(conn)
        return result
 

class searchbycontent(Resource):
    def post(self):
        txt=str(request.form['txt'])
        print(txt)
        conn = db.connect()
        cursor = conn.cursor()
        sql="select * from post where content like'%%s'%"%(txt)
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        db.close(conn)
        return result


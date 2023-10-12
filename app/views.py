from flask import jsonify,request
import pymysql

def iud(qry,val):
    con=pymysql.connect(host='localhost',port=3306,user='root',password='',db='sample')
    cmd=con.cursor()
    cmd.execute(qry,val)
    id=cmd.lastrowid
    con.commit()
    con.close()
    return id

def selectall(qry):
    con=pymysql.connect(host='localhost',port=3306,user='root',password='',db='sample',cursorclass=pymysql.cursors.DictCursor)
    cmd=con.cursor()
    cmd.execute(qry)
    res=cmd.fetchall()
    return res

def add_student():
    name = request.form['name']
    gender = request.form['gender']
    Place = request.form['place']
    Phone = request.form['phone']
    Email = request.form['Email']
    qry = "INSERT INTO `student` VALUES (NULL,%s,%s,%s,%s,%s)"
    val = (name, gender, Place, Phone, Email)
    iud(qry, val)
    return jsonify({'task': 'valid'})
   
def view_student():
    qry = "SELECT * FROM `student`"
    res = selectall(qry)
    return jsonify(res)

def delete_student():
    sid = request.form['id']
    q = "DELETE FROM student WHERE sid=%s"
    iud(q, sid)
    return jsonify({"task":"success"})
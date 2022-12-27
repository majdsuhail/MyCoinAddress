from flask import Flask, request, render_template 
import requests
import mysql.connector
import random
import string
import datetime

app = Flask(__name__)

def imgcon(string):
    import qrcode
    from PIL import Image
    import base64
    from io import BytesIO

    img = qrcode.make(string)

    buffered = BytesIO()
    img.save(buffered, format="png")

    img_str = base64.b64encode(buffered.getvalue())
    img_str = str(img_str)[2:-1]
    return img_str


def getLocation(ip):
    url = 'http://ip-api.com/json/{}'.format(ip)
    request=requests.get(url)
    response=request.json()
    country= response['country']
    return country


def randomRouting():
    x=string.ascii_letters+string.digits
    y=''.join(random.choices(x, k = 10))
    return y

@app.route('/<routing>')
def user(routing):
    import os
    mydb = mysql.connector.connect(
        host=os.environ["data"]['SECRET_KEY'],
        user="bee7b60e1a133a",
        password="932aaf6f",
        database="heroku_bbe2f6caae2f015")

    mycursor = mydb.cursor()

    sql="select * from addresses where routing = %s"
    mycursor.execute(sql,(routing,))
    user = eval(str(mycursor.fetchall()))
    if len(user)==0:
        mydb.close()
        return render_template('/html/404.html')

    mydb.close()
    user=user[0]
    data=[user[1],user[2],user[3],user[4],user[5],user[6]]

    return render_template('/html/index3.html',data=data+[imgcon(data[1]),imgcon(data[4])])


@app.route('/delete', methods=['GET','POST'])
def delete():
    if request.method == 'GET':
        data={}
        return render_template('/html/index2.html',data=data)

    mydb = mysql.connector.connect(
       host="us-cdbr-east-05.cleardb.net",
        user="bee7b60e1a133a",
        password="932aaf6f",
        database="heroku_bbe2f6caae2f015")

    mycursor = mydb.cursor()

    data= (request.form['address'],request.form['password'])

    sql="select * from addresses where address = %s"
    mycursor.execute(sql,(data[0],))
    all= eval(str(mycursor.fetchall()))

    if len(all)==0:
        mydb.close()
       
        data={'aError':'This address is not associated with a page'}
        return render_template('/html/index2.html',data=data)

    if data[1] == all[0][8]:
        sql="DELETE FROM addresses WHERE address=%s AND password=%s;"
        mycursor.execute(sql,data)
        mydb.commit()
        mydb.close()
        data={'success':'your page was deleted successfully'}
        return render_template('/html/index2.html',data=data)

    else:
        mydb.close()
        data={'pError':'password is wrong'}
        return render_template('/html/index2.html',data=data)



@app.route('/', methods=['GET','POST'])
def welcome():

    if request.method == 'GET':
        data={}
        return render_template('/html/index.html',data=data)

    mydb = mysql.connector.connect(
        host="us-cdbr-east-05.cleardb.net",
        user="bee7b60e1a133a",
        password="932aaf6f",
        database="heroku_bbe2f6caae2f015")

    mycursor = mydb.cursor()

    data= (request.form['coinName'],request.form['address'],request.form['displayName'],request.form['network'],request.form['memo'],request.form['description'],request.form['password'])

    sql="select routing from addresses where address = %s;"
    mycursor.execute(sql,(data[1],))
    all= eval(str(mycursor.fetchall()))
    if len(all) != 0 :
        mydb.close()
        data={'error':'This address is already associated with an existing page','link':'mycoinaddress.com/'+all[0][0]}
        return render_template('/html/index.html',data=data)

    if len(data[0])>50 or len(data[1])>60 or len(data[2])>50 or len(data[3])>20 or len(data[4])>25 or len(data[5])>280 or len(data[6])>32 or len(data[6])<6 or data[0].isspace() or data[1].isspace() or data[6].isspace() or data[0]=='' or data[1]=='' or data[6] == '':
        mydb.close()

        return render_template('/html/RR.html')

    bool=True
    while bool:
        routing=randomRouting()
        sql="select routing from addresses;"
        mycursor.execute(sql)
        all=str(mycursor.fetchall())
        for i in all:
            if routing not in i:
                bool = False

    ipAddress = request.environ['HTTP_X_FORWARDED_FOR']

    sql= "INSERT INTO addresses (coinName, address, displayName, network, memo, description, password, routing, ipAddress) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    mycursor.execute(sql,data+(routing, ipAddress))
    mydb.commit()

    mydb.close()

    data={'success':'Your page is ready!','link':'mycoinaddress.com/'+routing}
    return render_template('/html/index.html',data=data)


@app.errorhandler(404)
def not_found(e):

  return render_template("/html/404.html")



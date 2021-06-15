import pymysql
from flask import Flask, render_template, request
# Open database connection
db = pymysql.connect(host='localhost',
                     user='root',
                     password='ZSP95142',
                     db='web')

# prepare a cursor object using cursor() method
cursor = db.cursor()
 #Drop table if it already exist using execute() method.
#cursor.execute("DROP TABLE IF EXISTS text")

#sql = """CREATE TABLE `text`(`id` int(100) NOT NULL AUTO_INCREMENT,
 #     `user_name` varchar(20) ,
  #    `user_text` varchar(50),
   #     PRIMARY KEY(`id`))"""

#cursor.execute(sql)
#db.commit()
 #Prepare SQL query to INSERT a record into the database.
#title = 'INSERT INTO text(user_name , user_text) VALUES("USER_NAME","USER_TEXT")'
#cursor.execute(title)
#db.commit()
#try:
    # Execute the SQL command
 #   cursor.execute(title)
    # Commit your changes in the database
  #  db.commit()
#except:
    # Rollback in case there is any error
 #   db.rollback()


#print("create successful")
#db.close()

app = Flask(__name__)


@app.route("/messageSubmit", methods=['POST'])
def submit():
    insert_name = request.form.get('name')
    #print(str(insert_name))
    insert_text = request.form.get('text')
    cursor.execute('INSERT INTO text VALUES(NULL,%s, %s)', (str(insert_name), str(insert_text)))
    db.commit()

    return render_template("submit.html", **locals())


@app.route('/')
def welcome():
    cursor.execute('SELECT * FROM text')
    data = cursor.fetchall()
    return render_template("message.html", data=data)


if __name__ == '__main__':
    app.run()

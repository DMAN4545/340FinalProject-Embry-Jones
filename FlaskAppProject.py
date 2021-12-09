#Created by Devon Embry and Blake Jones

#imports
#import webbrowser
import sqlite3
from flask import Flask, render_template
from flask import request, redirect, url_for

#webbrowser.open('http://127.0.0.1:5000/')

#instantiate
app = Flask(__name__)
# route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    conn = sqlite3.connect('celebrities.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM member_login''')
    rows=c.fetchall()
    if request.method == 'POST':
        for row in rows:
            if request.form['username'] != row[1] or request.form['password'] != row[2]:
                if row is not None:
                    continue
                else:
                    break
            else:
                return redirect(url_for('info', thememberID=row[0]))
        else:
            error = 'Invalid Credentials. Please try again.'
    conn.close()
    return render_template('login.htm', error=error)

@app.route('/info', methods=['GET','POST'])
def info():
    firstname=''
    lastname=''
    age=None
    email=''
    bio=''
    success=False
    
    # This is called when the page is FIRST LOADED
    if request.method == 'GET':
        success = False
        #Connect to the database and select one record (row of data)
        conn = sqlite3.connect('celebrities.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM members WHERE memberID=?''', request.args.get('thememberID', None))
        row = c.fetchone()
        #Prints row
        #If the row contains data, store it in variables
        if row:
            memberID = row[0]
            firstname = row[1]
            lastname = row[2]
            age = row[3]
            email = row[4]
            bio = row[5]
        #Clost connection to db
        conn.close()
        #Print row
    #This is called when the submit button is clicked
    if request.method == 'POST':
        #Gets the data form and store it in variables 
        #This uses the request method to get the data from named elements on the form
        memberID = request.form['memberID']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        age = request.form['age']
        email = request.form['email']
        bio = request.form['bio']
        success = True
        #Now store the data from the form in the db
        conn = sqlite3.connect('celebrities.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM members''')
        row = c.fetchone()
        if row: #if the row exists, update the data in the row
            c.execute('''UPDATE members SET firstname=?, lastname=?, age=?, email=?, bio=? WHERE memberID=?''', (firstname,lastname,age,email,bio,memberID))
        else: #If the row doesnt exist, insert the data in the row
            c.execute('''INSERT INTO members VALUES (?,?,?,?,?,?)''', (memberID, firstname, lastname, age, email, bio))
        conn.commit()
        conn.close()
        
    thememberID = request.args.get('thememberID')
    picurl = url_for('static', filename=str(memberID)+".jpg")
    
    return render_template('profile.html', thememberID=thememberID, picurl=picurl, memberID=memberID, firstname=firstname, lastname=lastname, age=age, email=email, bio=bio, success=success)
    
@app.route('/view_all_celebs')
def view_all():
    celebID=None
    firstname=''
    lastname=''
    age=''
    email=''
    photo=''
    bio=''
    
    conn = sqlite3.connect('celebrities.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM celebs ORDER BY celebID''')
    rows=c.fetchall()
    conn.close()
    
    thememberID = request.args.get('thememberID')
    
    #Return
    return render_template('View_All_Celebs.html', rows=rows, thememberID=thememberID)
    
@app.route('/view_one_celeb', methods=['GET', 'POST'])
def view_one():
    thememberID = request.args.get('thememberID')
    
    if request.method == 'GET':
        #Connect to the database and select one record (row of data)
        conn = sqlite3.connect('celebrities.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM celebs WHERE celebID=?''', request.args.get('thecelebID'))
        row = c.fetchone()
        conn.close()
        
        conn = sqlite3.connect('celebrities.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM celebs ORDER BY celebID''')
        preoptions = c.fetchall()
        conn.close()
        
        options = []
        
        for i in preoptions:
            options.append(i[0])
    
    if request.method == 'POST':
        thecelebID = request.form['thecelebID']
        return redirect(url_for('view_one', thememberID=thememberID, thecelebID=thecelebID))
    
    #Print row
    return render_template('View_One_Celeb.html', options=options, thememberID=thememberID, celebID=row[0], firstname=row[1], lastname=row[2], age=row[3], email=row[4], photo=row[5], bio=row[6])

def get(request):
    pass

def post(request):
    pass

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


if __name__ == "__main__":
    app.run(debug=False)

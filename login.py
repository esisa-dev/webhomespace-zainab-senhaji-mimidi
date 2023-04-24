from flask import Flask, make_response, render_template, request, url_for
import cryptocode

app = Flask(__name__)

@app.route("/")
def affiche():

    print("ok")
    return render_template("login.html")

@app.route("/login", methods=['POST', 'GET'])
def connexion():

    connected = False
    identifiant = request.form['identifiant']
    password = request.form['passwd']

    print(cryptocode.encrypt(password, "zainab"))

    connected = verifyAccount(identifiant, password)
    if connected == True:
        # resp = make_response(render_template('welcome.html'))
        # resp.set_cookie('identifiant', identifiant)
        # resp.set_cookie('password', password)
        return render_template("welcome.html")
    else : 
        return render_template("login.html")

def verifyAccount(ident, passwd):

    credentials = ident + " " + passwd

    shadowFile = open("E:\shadow", "r")
    while shadowFile:
        line = shadowFile.readline().strip("\n")

        lineSplit =  line.split(":")
        
        if line == "":
            break
        
        credentialsDecrypted = lineSplit[0] + " " + str(cryptocode.decrypt(lineSplit[1], "zainab"))
        
        if credentials == credentialsDecrypted :
            shadowFile.close()
            return True
        
    shadowFile.close()
    return False

@app.route("/logout")
def logout():
    return render_template("login.html")

@app.route('/setcookie')
def setcookie(): 

    resp = make_response(render_template('welcome.html'))
    resp.set_cookie('identifiant', 'identifiant')
    resp.set_cookie('password', 'password')

    print(request.cookies)
    print(request.cookies.get('identifiant'))

    return resp

@app.route('/getcookie')
def getcookie():
    ident = request.cookies.get('identifiant')
    pswd = request.cookies.get('password')
    return '<h1 Welcome>' + str(ident) + " " + str(pswd) + '</h1>'

app.run(debug=True)
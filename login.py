from flask import Flask, render_template, request, url_for
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

    #print(cryptocode.encrypt(password, "zainab"))

    connected = verifyAccount(identifiant, password)
    if connected == True:
        return render_template("welcome.html")
    else : 
        return render_template("login.html")

def verifyAccount(ident, passwd):

    credentials = ident + " " + passwd

    shadowFile = open("E:\shadow", "r")
    while shadowFile:
        line = shadowFile.readline().strip("\n")

        lineSplit =  line.split(" ")
        
        if line == "":
            break
        
        credentialsDecrypted = ident + " " + str(cryptocode.decrypt(lineSplit[1], "zainab"))
        
        if credentials == credentialsDecrypted :
            shadowFile.close()
            return True
        
    shadowFile.close()
    return False

app.run(debug=True)
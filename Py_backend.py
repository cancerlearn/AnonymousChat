from flask import Flask, render_template, request, flash, make_response, redirect
import ast

app = Flask(__name__, static_folder='templates\static')

@app.route("/", methods=['GET','POST'])
def index():
        return render_template("index.html")

@app.route("/signUp", methods=['POST'])
def process_signUP():
        
        if request.method == 'POST':

                age_range = request.form["age"]
                nationality = request.form["nationality"]
                gender = request.form["gender"]
                religion = request.form["religion"]
                profession = request.form["profession"]
                email = request.form["email_signUp"]
                password = request.form["password_signUp"]

                data_dict = {"age_range": age_range, "nationality":nationality, "gender":gender, "religion":religion, "profession":profession, "email":email, "password":password}

                file = open("DB.txt","a+")

                if  not duplicate_email(email):
                        
                        file.write(str(data_dict) + "\n")

                file.close()
    
        return render_template("index.html")
        #return render_template("htmlfile.html", result = request.form)

@app.route("/logIn", methods=['GET', 'POST'])
def process_logIn():

        file = open("DB.txt","r")

        if request.method == 'GET':

                email = request.args.get("email_logIn")
                password = request.args.get("password_logIn")
                
                
                for dict_string in file.readlines():

                        user_data = ast.literal_eval(dict_string)

                        if email == user_data["email"] and password == user_data["password"]:
                                
                                return render_template("pairUp.html", user_email = email)
                                

        file.close()
        return render_template("index.html")

@app.route("/pairUp", methods=['GET','POST'])
def pairUp():

        if request.method == 'GET':

                argument = request.args.to_dict()
                print(argument)

                difference_factor = argument[[key for key in argument][0]].lower()

                if difference_factor == "age":
                        difference_factor = difference_factor+"_range"
                
                user_email = [key for key in argument][0].split("|")[0]
                
                user_data = {}

                file = open("DB.txt","r")

                for dict_string in file.readlines():

                        data = ast.literal_eval(dict_string)

                        if data["email"] == user_email:

                                user_data = data

                file.close()

                file = open("DB.txt","r")

                for dict_string in file.readlines():

                        data = ast.literal_eval(dict_string)

                        if data[difference_factor] != user_data[difference_factor]:
                                
                                file.close()
                                return redirect("http://localhost:3000/")
                        else:
                                file.close()
                                return render_template("index.html")
        

@app.route("/logOut", methods=['GET','POST'])
def logOut():

        if request.method == 'POST':

                return render_template("index.html")


def duplicate_email(email):

        file = open("DB.txt","r")

        for dict_string in file.readlines():

                data = ast.literal_eval(dict_string)

                if data["email"] == email:

                        file.close()

                        return True

        file.close()

        return False




if __name__ == "__main__":
    app.run(debug = True)
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

                file.write(str(data_dict) + "\n")

                file.close()
    
        return render_template("index.html")
        #return render_template("htmlfile.html", result = request.form)

@app.route("/logIn", methods=['POST'])
def process_logIn():

        if request.method == 'POST':

                email = request.form["email_logIn"]
                password = request.form["password_logIn"]
                print(email, password)
                file = open("DB.txt","r")
                
                for dict_string in file.readlines():

                        user_data = ast.literal_eval(dict_string)

                        if email == user_data["email"] and password == user_data["password"]:
                                print("here")
                                return redirect("localhost:3000/")

        file.close()
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug = True)
from flask import Flask, render_template, request, flash, make_response

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

                file = open("DB.txt","a+")

                for user_data in file.readlines():

                        if email == user_data["email"] and password == user_data["password"]:

                                return render_template("index.html")

                        else:
                                response = make_response(('Error\n'), {'Invalid user info': 'Invalid user info'})
                                response.set_cookie(email, 'error')
                                return response
        
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug = True)
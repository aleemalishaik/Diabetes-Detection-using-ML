from flask import Flask, render_template, request, url_for
app = Flask(__name__)
import pickle

# @app.route("/templates")
# def documentation():
#     return render_template("Documentation.html")

app = Flask(__name__, static_url_path='/static')
# open a file, where you stored the pickled data
file = open('model.pkl', 'rb')
clf = pickle.load(file)
file.close()


@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        myDict = request.form
        Pregnancies = int(myDict['Pregnancies'])
        Glucose = float(myDict['Glucose'])
        BloodPressure = int(myDict['BloodPressure'])
        SkinThickness = float(myDict['SkinThickness'])
        Insulin = float(myDict['Insulin'])
        BMI = float(myDict['BMI'])
        DiabetesPedigreeFunction = float(myDict['DiabetesPedigreeFunction'])
        Age = int(myDict['Age'])

        #code for inference
        inputFeatures = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
        diaProb = clf.predict(inputFeatures)[0]
        if (diaProb==1):
           
            return render_template('show.html',  str1 = ' Positive', input=inputFeatures)
            # return render_template('show.html', inputFeatures)
        else :
           
            return render_template('show.html',  str2 = 'Negative', input=inputFeatures)
        # return render_template('show.html', Prob = diaProb)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request
from main import predict_model

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def prediction():
    if request.method=='POST':
        age = request.form["user_age"]
        annual_income = request.form["user_annual_income"]
        spending_score = request.form["user_spending_score"]
        result = predict_model(age, annual_income, spending_score)
        return result

if __name__ == '__main__':
    app.run(debug=True)
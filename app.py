from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method =="POST":
        weight = float(request.form['weight'])
        height = float(request.form['height']) / 100  # convert cm to m
        bmi = round(weight / (height * height), 2)
        if bmi <18.5:
            return f"The BMI is {bmi} and the person is UNDERWEIGHT"
        elif bmi >18.5 and bmi <24.9:
            return f"The BMI is {bmi} and the person is NORMAL"
        elif bmi >25.0 and bmi <29.0:
            return f"The BMI is {bmi} and the person is OVERWEIGHT"
        elif bmi >30.0 and bmi <34.9:
            return f"The BMI is {bmi} and the person is OBESE"
        else:
            return f"The BMI is {bmi} and the person is EXTREMELY OBESE"
        
    return render_template ("index.html")

if __name__ == '__main__':
    app.run(debug=True)
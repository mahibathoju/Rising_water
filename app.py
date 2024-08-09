from flask import Flask, render_template, request
from joblib import load 
app = Flask(__name__)
model = load('flood1.save')
sc = load('transform.save')
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict')
def predict():
    return render_template('predict.html')
@app.route('/result')
def result():
    return render_template('result.html')
@app.route('/data_predict', methods=['POST'])
def data_predict():
    print("hello")
    temp = request.form["Cloud"]
    Hum = request.form["annual"]
    dp = request.form["Jan"]
    ap = request.form["May"]
    aa1 = request.form["Jun"]
    print("hello")
    data = [[float(temp), float(Hum), float(dp), float(ap),float(aa1)]]
    prediction = model.predict(sc.transform(data))
    output = prediction[0]
    print("prediction")
    if (output == 0):
        return render_template('result.html', prediction='NO POSSIBILTY of severe flood.')
    
    return render_template('result.html', prediction='POSSIBILTY of severe flood.')

if __name__ == '__main__':
    app.run(debug=True)
   
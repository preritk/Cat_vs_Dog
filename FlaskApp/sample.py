from flask import Flask ,render_template
import keras
app = Flask(__name__)
@app.route('/this')
def themo():
    return render_template('predict.html')
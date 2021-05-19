#copied the whole code from clientapp.py for Heroku deployment

from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from com_in_ineuron_ai_utils.utils import decodeImage
from predict import dogcat

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)




#@cross_origin()
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = dogcat(self.filename)



@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')
    


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predictiondogcat()
    return jsonify(result)

 #to deploy in Heroku, after copying the full code from clietApp.py to app.py, then we just have to do two changes.
 #1. move clApp = ClientApp() to outside of the function
 #2. remove host='0.0.0.0'
clApp = ClientApp()
#port = int(os.getenv("PORT"))
if __name__ == "__main__":
    #clApp = ClientApp() it will remain here when we deploy it in local or else it will move outside of the function like here
    #app.run(host='0.0.0.0', port=port)
    #app.run(host='0.0.0.0', port=8000, debug=True) it is only used when we deploy it in local
    app.run(port=8000, debug=True)

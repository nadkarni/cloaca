from flask import Flask
app = Flask(__name__)

@app.route('/determineChickenOrEgg/<avgImageValue>')
def determineChickenOrEgg(avgImageValue):
    val = int(avgImageValue)
    if val < 128:
        return "true"

    return "false"

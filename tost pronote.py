import pronotepy
import datetime
from flask import Flask, jsonify

app = Flask(__name__)

tps=0

client = pronotepy.Client('https://0760095r.index-education.net/pronote/eleve.html',
                      username='u.devalland1',
                      password='Boubou2701!',
                      ent=l_normandie)

def custom_command():
    if client.logged_in:
        nom_utilisateur = client.info.name
        periods = client.periods

        today = datetime.date.today()
        homework = client.homework(today) 
        homeworkv2 = homework[:4]
        homework_list = []
        for hw in homeworkv2:
            homework_list.append(f"({hw.date})({hw.subject.name}): {hw.description}")
        return homework_list
    else: 
        return("Failed to log in")

@app.route('/homework')
def get_homework():
    homework_list = custom_command()
    return jsonify(homework_list)
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

import pronotepy
import datetime
from sys import exit
from pronotepy.ent import l_normandie

tps=0

client = pronotepy.Client('https://0760095r.index-education.net/pronote/eleve.html',
                      username='u.devalland1',
                      password='Boubou2701!',
                      ent=l_normandie) # ent specific

def custom_command():
    if client.logged_in:
        nom_utilisateur = client.info.name # get users name
        print(f'Bienvenue {nom_utilisateur}!')
        periods = client.periods

        today = datetime.date.today() # store today's date using datetime built-in library
        homework = client.homework(today) # get list of homework for today and later
        homeworkv2 = homework[:4]
        homework_list = [] # create an empty list to store the homework
        for hw in homeworkv2: # iterate through the list
            homework_list.append(f"({hw.date})({hw.subject.name}): {hw.description}") # add the homework's subject, title and description to the list
        return homework_list # return the list of homework
    else: 
        return("Failed to log in")
        exit()

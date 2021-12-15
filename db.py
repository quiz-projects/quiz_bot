from tinydb import TinyDB,Query
import csv
# create table
db = TinyDB('data.json')

def read_data_csv(filename):
    """Read file csv"""
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data_quiz = [row for row in reader]
    return data_quiz


def add_quiz(data_quiz:str,quiz_name)-> None:
    """
    Saving data to a database

    filename(str): return None
    """
    for quiz in data_quiz:
        question = quiz['question']
        image_link = quiz['image_link']
        correct = quiz['correct']
        options = [quiz.get('option01'),quiz.get('option02'),quiz.get('option03'),quiz.get('option04')]
    
        quiz_table = db.table(quiz_name)
        quiz_table.insert({'question':question,'correct':correct,'options':options,'image_link':image_link})

def read_quiz_data():
    """Read all table QUIZ"""
    return db.tables()

def get_quiz(query):
    d_table = db.table(query)
    return d_table.all()
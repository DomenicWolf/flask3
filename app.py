
from flask import Flask,request,redirect,flash,render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import choice, sample,randint
from surveys import satisfaction_survey



app = Flask(__name__)



app.config['SECRET_KEY'] = 'chicken'
debug = DebugToolbarExtension(app)


responses=[]
@app.route('/')
def show_title():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    questions = satisfaction_survey.questions

    return render_template('title.html', title=title, instructions=instructions,questions=questions)

@app.route('/question/<num>')
def show_question(num):
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    questions = satisfaction_survey.questions
    return render_template(f"q{num}.html", title=title, instructions=instructions,questions=questions, num=int(num))

@app.route('/answer', methods=['POST'])
def answer():
    questions = satisfaction_survey.questions 
    num = int(request.form['num'])
    if num +1 < len(questions):
        
        answer = request.form[f'q{num}']
        responses.append(answer)
    else:
        answer = request.form[f'q{num}']
        responses.append(answer)
        return redirect('/end')
    

    return redirect(f'/question/{num +1}')

@app.route('/end')
def show_end():
    
    return render_template('end.html',responses=responses)

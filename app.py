
from flask import Flask,request,redirect,flash,render_template,session
from flask_debugtoolbar import DebugToolbarExtension
from random import choice, sample,randint
from surveys import satisfaction_survey



app = Flask(__name__)



app.config['SECRET_KEY'] = 'chicken'
debug = DebugToolbarExtension(app)

@app.route('/set_up', methods=['POST'])
def set_up():
    session['responses'] = []
    return redirect('/question/0')

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

    responses = session['responses']
    

    if len(responses) >= int(num):
        return render_template(f"q{num}.html", title=title, instructions=instructions,questions=questions, num=int(num))
    else:
        for idx,response in enumerate(responses[::-1]):
            if response:
                return redirect(f"/question/{idx}")
        flash('Cannot skip questions stupid whore bitch cheater trynna drag me down in a race and then hit your head what a fucking moron')
        return redirect('/')

@app.route('/answer', methods=['POST'])
def answer():
    questions = satisfaction_survey.questions 
    num = int(request.form['num'])
    responses = session['responses']
    if num +1 < len(questions):
        
        answer = request.form[f'q{num}']
        responses.append(answer)
        session['responses'] = responses
    else:
        answer = request.form[f'q{num}']
        responses.append(answer)
        session['responses'] = responses
        return redirect('/end')
    

    return redirect(f'/question/{num +1}')

@app.route('/end')
def show_end():
    responses = session['responses']
    return render_template('end.html',responses=responses)



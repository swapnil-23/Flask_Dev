from flask import Flask, redirect, url_for

app=Flask(__name__)

## creating the main url
@app.route('/')
def welcome():
    return 'Welcome'

## creating the second url
@app.route('/success/<int:score>')
def success(score):
    return 'the person has passed and the marks is: '+str(score)

## creating the third url
@app.route('/fail/<int:score>')
def fail(score):
    return 'the person has failed and the marks is: ' +str(score)

## creating the fourth url
@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks < 50:
        result = "fail"
    else:
        result = "pass"
    return redirect(url_for(result, score=marks))




if __name__ == '__main__':
    app.run(debug=True)
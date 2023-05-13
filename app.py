from flask import Flask

app=Flask(__name__)

@app.route('/')
def welcom():
    return 'Welcome'

@app.route('/members')
def memebers():
    return 'Welcome members'


if __name__=='__main__':
    app.run(debug=True)

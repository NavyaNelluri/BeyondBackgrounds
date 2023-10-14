from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'navya' 


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
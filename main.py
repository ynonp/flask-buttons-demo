from flask import Flask, render_template, request
app = Flask(__name__)

counter = 0

@app.route('/')
def hello_world():
    return render_template('application.html', clicks=counter)

@app.route('/', methods=['POST'])
def clicked():
    global counter
    counter += 1
    return render_template('application.html', clicks=counter)

if __name__ == "__main__":
    app.run()



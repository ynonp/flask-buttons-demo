# flask-buttons-demo

This demo shows how to handle a "click" on a button inside a flask server.

The server code is in file main.py and includes the following routes:

```
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
```

And the corresponding part in the template (application.html) is:

```
<form method="POST" action="/">
  <button>Click Me</button>
</form>
```

Whenever a user clicks on the button, the form sends an HTTP POST request to the flask server,
that results in the function `clicked` on the server, which increases the counter by 1 and returns the new template page.


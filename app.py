from flask import Flask

app = Flask(__name__)


@app.route('/my-awesome-project')
def awesome_project():
    return 'Hello World! This is my awesome project page'

@app.route('/secret')
def this_is_secret():
    return 'This is my secret Ingress ! :)'


if __name__ == '__main__':
    app.run()

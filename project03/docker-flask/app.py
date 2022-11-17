from flask import Flask

app = Falsk(__name__)

@app.route('/')
def hello_uyghur():
    return "hello flask, come study !"

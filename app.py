from flask import Flask, render_template
app = Flask(__name__)

# two decorators, same function
@app.route('/')
def index():
    return render_template("home.html")    
    return """
    <h1> Welecome </h1>
    <input type="text" > <br>
    <input type="file" >
    <button> Translate </button>
    """
@app.route('/')
def mic():
    return render_template("microphone.html") 

if __name__ == '__main__':
    app.run(debug=True)

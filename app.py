from flask import Flask, render_template
app = Flask(__name__)

# two decorators, same function
@app.route('/')
def index():
    return render_template("microphone.html")    
    return """
    <h1> Welecome </h1>
    <input type="text" > <br>
    <input type="file" >
    <button> Translate </button>
    """

if __name__ == '__main__':
    app.run(debug=True)
from src.enviar import app

@app.route('/')
def home():
    return '<p>Ok</p>'

if __name__ == "__main__":
    app.run(debug=True)
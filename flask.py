from flask import Flask

app = Flask(__name__)

@app.route("/")
def main(self):
    "Bienvenido a mi primera pagina"

if __name__ == "__main__":
    app.run(debug = True, host ='192.168.1.71', port =789)
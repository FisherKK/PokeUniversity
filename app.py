from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html', button="Welcome")

@app.route('/weakness_and_resistance', methods=['GET', 'POST'])
def weakness_and_resistance():
    icons = []
    if request.method == 'POST':
        if 'ask' in request.form:
            icons = [
                "bug", "dark", "dragon", "electric", "fairy", "fighting", "fire",
                "flying", "ghost", "grass", "ground", "ice", "normal", "poison",
                "psychic", "rock", "steel", "water"
            ]
    return render_template('weakness_and_resistance.html', button="Weakness & Resistance", icons=icons)

@app.route('/pokemon_types')
def pokemon_types():
    return render_template('pokemon_types.html', button="Pokemon Types")

@app.route('/movesets')
def movesets():
    return render_template('movesets.html', button="Movesets")

@app.route('/energy_management')
def energy_management():
    return render_template('energy_management.html', button="Energy Management")

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
import subprocess
import json
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():

    try:
        niveau = 75
        temperature = 30
        status = "Test"
        health = "Good"
        voltage = 4000
        technology = "Li-ion"

        heure = datetime.now().strftime("%H:%M:%S")

        if niveau >= 80:
            conseil = "Batterie excellente"
        elif niveau >= 50:
            conseil = "Batterie normale"
        elif niveau >= 20:
            conseil = "Activer économie batterie"
        else:
            conseil = "Recharge urgente"

        return render_template(
            "index.html",
            niveau=niveau,
            temperature=temperature,
            status=status,
            health=health,
            voltage=voltage,
            technology=technology,
            heure=heure,
            conseil=conseil
        )

    except Exception as e:
        return f"Erreur : {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

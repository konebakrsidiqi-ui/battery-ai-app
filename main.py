from flask import Flask, render_template
import subprocess
import json
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():

    try:
        battery = subprocess.check_output(
            ["termux-battery-status"]
        ).decode("utf-8")

        data = json.loads(battery)

        niveau = data.get("percentage")
        temperature = data.get("temperature")
        status = data.get("status")
        health = data.get("health")
        voltage = data.get("voltage")
        technology = data.get("technology")

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

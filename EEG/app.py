from flask import Flask, render_template, request
import joblib
import numpy as np
import base64
import io
from matplotlib.figure import Figure

app = Flask(__name__)

model = joblib.load("eeg_model.pkl")
scaler = joblib.load("eeg_scaler.pkl")

def generate_spectrogram_image(is_healthy):
    """
    Sağlıklı ve sağlıksız durumlarına göre farklı spektrogramlar oluşturur.
    Sağlıksız -> düşük frekans, yüksek dalga boyu (yavaş dalga)
    Sağlıklı -> daha sık dalga, biraz daha yüksek frekans
    """
    fig = Figure(figsize=(4, 3))
    ax = fig.subplots()

    if is_healthy:
        # Sağlıklı: Daha sık, orta frekans dalga
        freqs = np.linspace(1, 30, 100)
        power = np.sin(freqs * 2) * 5 + 10  # Dalga sık ve orta güçte
        ax.set_title("Sağlıklı Spektrogram")
    else:
        # Sağlıksız: Düşük frekans, yüksek genlik
        freqs = np.linspace(1, 10, 100)
        power = np.sin(freqs / 2) * 10 + 15  # Daha az frekans, yüksek genlik
        ax.set_title("Sağlıksız Spektrogram")

    ax.plot(freqs, power, color='#8e44ad')
    ax.fill_between(freqs, power, color='#8e44ad', alpha=0.3)

    ax.set_xlabel("Frekans (Hz)")
    ax.set_ylabel("Güç")
    ax.grid(True, alpha=0.3)
    ax.set_facecolor('#f4f4f4')

    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches='tight')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    return img_base64

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    theta = float(request.form["theta"])
    delta = float(request.form["delta"])
    features = scaler.transform([[theta, delta]])
    
    prediction = model.predict(features)[0]
    proba = model.predict_proba(features)[0]
    confidence = round(max(proba) * 100, 2)

    prediction_text = "Tahmin: Sağlıklı" if prediction == 1 else "Tahmin: Sağlıksız"
    is_healthy = prediction == 1

    spectrogram_img = generate_spectrogram_image(is_healthy)

    return render_template(
        "index.html",
        prediction_text=prediction_text,
        prediction_probabilities=[round(proba[0]*100, 2), round(proba[1]*100, 2)],
        confidence=confidence,
        is_healthy=is_healthy,
        show_footer=True,
        spectrogram_img=spectrogram_img
    )

if __name__ == "__main__":
    app.run(debug=True)

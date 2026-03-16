from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    message=None
    if request.method == "POST":
        message = request.form["message"]
        transformed = vectorizer.transform([message])
        prediction = model.predict(transformed)
        result = "🚨 Spam" if prediction[0] == 1 else "✅ Not Spam"
    return render_template("index.html", result=result, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
from flask import Flask, jsonify, render_template, request
import pickle
import os

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
email_model = pickle.load(open("email_model.pkl", "rb"))
email_vectorizer = pickle.load(open("email_vectorizer.pkl", "rb"))


@app.route("/api/check-email", methods=["POST"])
def check_email():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify(error="Send a JSON object with subject and body fields."), 400

    subject = data.get("subject", "")
    body = data.get("body", "")
    if not isinstance(subject, str) or not isinstance(body, str):
        return jsonify(error="Subject and body must be strings."), 400

    if not subject.strip() and not body.strip():
        return jsonify(error="Provide a subject or email body to classify."), 400

    email_text = f"Subject: {subject.strip()}\n{body.strip()}".strip()
    transformed = email_vectorizer.transform([email_text])
    prediction = int(email_model.predict(transformed)[0])
    spam_probability = float(email_model.predict_proba(transformed)[0][1])
    return jsonify(
        prediction="spam" if prediction == 1 else "ham",
        is_spam=bool(prediction),
        spam_probability=spam_probability,
    )


@app.route("/email", methods=["GET", "POST"])
def email_page():
    subject = ""
    body = ""
    result = None
    spam_probability = None
    error = None

    if request.method == "POST":
        subject = request.form.get("subject", "")
        body = request.form.get("body", "")

        if not subject.strip() and not body.strip():
            error = "Enter a subject or email body to analyze."
        else:
            email_text = f"Subject: {subject.strip()}\n{body.strip()}".strip()
            transformed = email_vectorizer.transform([email_text])
            prediction = int(email_model.predict(transformed)[0])
            spam_probability = float(email_model.predict_proba(transformed)[0][1])
            result = "Spam" if prediction == 1 else "Not spam"

    return render_template(
        "email.html",
        subject=subject,
        body=body,
        result=result,
        spam_probability=spam_probability,
        error=error,
    )

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    message = ""
    error = None
    if request.method == "POST":
        message = request.form.get("message", "")
        if not message.strip():
            error = "Enter a text message to analyze."
        else:
            transformed = vectorizer.transform([message])
            prediction = model.predict(transformed)
            result = "🚨 Spam" if prediction[0] == 1 else "✅ Not Spam"
    return render_template("index.html", result=result, message=message, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
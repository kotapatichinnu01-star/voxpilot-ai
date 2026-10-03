from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify({
        "status": "ok",
        "service": "VoxPilot AI",
        "version": "0.1.0",
        "phase": "foundation"
    })

@app.get("/")
def landing():
    return render_template("landing.html")

@app.get("/login")
def login():
    return render_template("login.html")

@app.get("/signup")
def signup():
    return render_template("signup.html")

@app.get("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.get("/employees")
def employees():
    return render_template("employees.html")

@app.get("/leads")
def leads():
    return render_template("leads.html")

@app.get("/campaigns")
def campaigns():
    return render_template("campaigns.html")

@app.get("/calls")
def calls():
    return render_template("calls.html")

@app.get("/business-brain")
def business_brain():
    return render_template("business_brain.html")

@app.get("/analytics")
def analytics():
    return render_template("analytics.html")

@app.get("/settings")
def settings():
    return render_template("settings.html")

@app.errorhandler(404)
def not_found(error):
    if "/api/" in (getattr(error, "description", "") or ""):
        return jsonify({"error": "Not found"}), 404
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(__import__("os").environ.get("PORT", 5000)), debug=False)

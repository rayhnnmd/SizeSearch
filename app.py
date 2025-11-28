from flask import Flask, render_template, request
from predict import predict_size   

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            
            age = float(request.form["age"])
            height = float(request.form["height"])
            weight = float(request.form["weight"])

            
            size = predict_size(weight, age, height)

            result = f"Recommended size: {size}"

        except Exception:
            error = "Please enter valid numeric values."

    
    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask, render_template, request

app = Flask(__name__)

employees = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/employees", methods=["GET", "POST"])
def employee_page():
    if request.method == "POST":
        employees.append({
            "name": request.form["name"],
            "salary": float(request.form["salary"])
        })
    return render_template("employees.html", employees=employees)

@app.route("/payslip/<int:id>")
def payslip(id):
    emp = employees[id]
    paye = emp["salary"] * 0.18
    uif = emp["salary"] * 0.01
    net = emp["salary"] - paye - uif
    return render_template(
        "payslip.html",
        emp=emp,
        paye=paye,
        uif=uif,
        net=net
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

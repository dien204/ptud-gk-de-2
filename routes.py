from flask import Blueprint, render_template, request, redirect, url_for

# Khai báo Blueprint
app_routes = Blueprint("app_routes", __name__)

# Route trang chủ
@app_routes.route("/")
def index():
    return render_template("index.html")

# Route thêm task
@app_routes.route("/add", methods=["POST"])
def add_task():
    if request.method == "POST":
        task = request.form["task"]
        # Xử lý logic thêm task ở đây
        return redirect(url_for("app_routes.index"))

# Route trang admin
@app_routes.route("/admin")
def admin():
    return render_template("admin.html")

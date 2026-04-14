from flask import Flask, request, make_response, render_template, redirect, abort
import json, base64

app = Flask(__name__)

FLAG = "S7{C00k13_M4n1pul4t10n_B4s1c}"

# --------------------
# Utils
# --------------------

def encode_cookie(data: dict):
    raw = json.dumps(data).encode()
    return base64.b64encode(raw).decode()

def decode_cookie(value: str):
    try:
        raw = base64.b64decode(value).decode()
        return json.loads(raw)
    except:
        return None

def get_user():
    cookie = request.cookies.get("login")

    if not cookie:
        return None

    return decode_cookie(cookie)

# --------------------
# Routes
# --------------------

@app.route("/")
def index():
    return redirect("/register")

# ------------ REGISTER ------------

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username","guest")

        data = {
            "user": username,
            "role": "guest",
            "language": request.form.get("language", "fr"),
        }

        resp = make_response(redirect("/dashboard"))
        resp.set_cookie("login", encode_cookie(data))
        return resp

    return render_template("register.html")


# ------------ DASHBOARD ------------

@app.route("/dashboard")
def dashboard():

    user = get_user()

    if not user:
        return redirect("/register")

    return render_template("dashboard.html", user=user)


# ------------ ADMIN ------------

@app.route("/admin")
def admin():

    user = get_user()

    if not user:
        abort(403)

    if user.get("role") != "admin":
        abort(403)

    return render_template("admin.html", flag=FLAG)


# --------------------
# Error handlers
# --------------------

@app.errorhandler(403)
def forbidden(e):
    return render_template("403.html"), 403


# --------------------
# Start
# --------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)


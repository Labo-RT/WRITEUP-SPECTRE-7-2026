from flask import Flask, request, render_template, abort, send_from_directory

app = Flask(__name__)


ALLOWED_USER_AGENT = "SpectreBot/1.7"

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route("/hidden-entry.html")
def hidden_entry():
    user_agent = request.headers.get("User-Agent", "")
    if ALLOWED_USER_AGENT == user_agent:
        return render_template("hidden-entry.html")
    else:
       abort(403)

@app.errorhandler(403)
def forbidden(e):
    return render_template("403.html"), 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

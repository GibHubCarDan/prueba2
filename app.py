from flask import Flask, render_template, request, url_for

app = Flask(__name__)

# Para saber qué link está activo en la navbar


@app.context_processor
def inject_active_path():
    return dict(active_path=request.path)


@app.route("/")
def home():
    return render_template("index.html", title="Inicio")


@app.route("/about")
def about():
    return render_template("about.html", title="Acerca de")


@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contacto")

# (Opcional) páginas de error bonitas


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html", title="Página no encontrada"), 404


if __name__ == "__main__":
    app.run(debug=True)

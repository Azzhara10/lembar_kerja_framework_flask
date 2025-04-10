from flask import Flask, render_template

app = Flask(__name__)

app_name = "Python Flask. Proyek pertama. Mahasiswa Bisdig (Variabel Global)"
user = {
        "name": "Flora",
        "age" : 19,
        "gender": "perempuan, "
}
#1 App Route Hello World
@app.route("/")
def home():
    return "<p>Hello world! I'm a Python Flask App, ready to assist.</p>"


#2 App Route Aplikasi ke Halaman Lebih Spesifik
@app.route("/aplikasi/")
def aplikasi():
    return "<p>Python Flask. Proyek pertama. Mahasiswa Bisdig.</p>"

#3 App Route ke Halaman HTML Aesthetic
@app.route("/page/aesthetic/")
def aesthetic():
    return render_template("aesthetic.html")


#4 App Route ke halaman HTML Aesthetic part Full menghubungkan langsung ke static CSS
@app.route("/page/full/aesthetic/")
def aesthetic_name():
    return render_template("aesthetic.html", name="Aesthetic")


#5 App Route Dinamis
@app.route("/page/aesthetic/<string:nama>")
def get_name(nama):
    return "nama anda adalah(user)".format(nama)


@app.route("/page/aesthetic/")
def get_name2():
    return "nama anda adalah(user)"


#6 App Route Variabel Global 
@app.route("/global/")
def global_name():
    return f"Nama Aplikasi {app_name}"

#7 App route variabel local
@app.route("/local/")
def local_name():
    user = {
        "name": "Flora",
        "age" : 19,
        "gender": "perempuan"
    }
    return render_template("local.html", user=user)


if __name__ == "_main_":
    app.run(debug=True)
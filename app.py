from flask import Flask,render_template
app = Flask(__name__)
@app.route("/")#default page of web
def index():
    return render_template('index.html') #อย่างลือมเปลี่ยนเป็น index.html ********************

@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()

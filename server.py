from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

clients = ["Marvel Entertainment", "Reynolds, Ryan & Blake", "Wilson, Wade", "Stark, Tony", "Wayne, Bruce", "DC Entertainment", "Warner Bros.", "Wilson, Owen"]
@app.route('/')
def index():
    return render_template('filter-drop.html', clients=clients)

if __name__ == '__main__':
    app.run(debug=True)
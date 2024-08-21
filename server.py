from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

clients = ["Marvel Entertainment",
           "Reynolds, Ryan & Blake", 
           "Wilson, Wade", 
           "Stark, Tony", 
           "Wayne, Bruce", 
           "DC Entertainment", 
           "Warner Bros.", 
           "Wilson, Owen",
           "Murdock, Matt",
           "Jones, Jessica",
           "Lucas, Carl",
           "Thomas, Daniel",
           "Savage, Clark",
           "Strange, Stephen",
           "Wilson, Samuel",
           "Richards, Reed",
           "Storm, Sue",
           "Grimm, Benjamin",
           "Blaze, Johnathon",
           "Queen, Oliver",
           "Quill, Peter",
           "Barton, Clinton",
           "Banner, Bruce"
]


@app.route('/')
def index():
    return render_template('filter-drop.html', clients=clients)

if __name__ == '__main__':
    app.run(debug=True)
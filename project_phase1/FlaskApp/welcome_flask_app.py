# my first Flask app

# import Flask
from flask import Flask

# create an app
app = Flask(__name__)


# define a basic route / (function to be executed)
@app.route("/")
def main():
    return "Welcome to Flask in ISAT 340 in Fall 2026"


# check if executed file is the main() program. run app if it is
print('name: ' + __name__)
if __name__ == "__main__":
    app.run()

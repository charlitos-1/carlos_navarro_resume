from flask import Flask

APP_TYPE = "Production"

application = Flask(__name__)

@application.route("/")
def home():
    return "<h>Carlos Navarro</h>"

def main():
    pass

if __name__ == "__main__":
    main()
import os
from flask import Flask, render_template, request
import yelp_api

app = Flask(__name__)

@app.route("/")
def index():
    location = request.values.get('address')
    businesses = None
    if location:
        businesses = yelp_api.get_businesses(location)
    return render_template('index.html', businesses=businesses)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
   port = int(os.environ.get("PORT", 5000))
   app.run(host="0.0.0.0", port=port)

# if __name__ == "__main__":
#    app.run()

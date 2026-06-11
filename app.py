"""A minimal Flask app — my first web server.""" 


from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)  # __name__ tells Flask where to find resources


@app.context_processor
def inject_year():
    """Make the current year available to every template as `current_year`."""
    return {'current_year': datetime.now().year}


@app.route('/')  # maps the URL "/" to the function below
def index():
    """Return the text shown when someone visits the homepage."""
    return render_template('index.html')

@app.route('/form', methods=['POST', 'GET'])
def form():
    # Flow:
    #   GET  (just visiting /form)  -> show form.html (the blank form)
    #   POST (form submitted)       -> redirect to the dashboard page
    if request.method == 'POST':
        return redirect(url_for('dashboard'))
    return render_template('form.html')

@app.route('/dashboard')
def dashboard():
    # render_template lokks for HTML 
    return render_template('dashboard.html')

if __name__ == '__main__':
    # This launches Flask and listens at http://localhost:5000.
    # debug=True shows helpful error pages and auto-reloads on code changes.
    app.run(debug=True)

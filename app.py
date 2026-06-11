"""A minimal Flask app — my first web server.""" 


from datetime import datetime

from flask import Flask, render_template, redirect, url_for
from forms import DataRequestForm

app = Flask(__name__)  # __name__ tells Flask where to find resources
app.config['SECRET_KEY'] = "my_super_secret_key_123"

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
    form = DataRequestForm()
    # Flow:
    #   GET, or invalid POST  -> show form.html (re-renders with error messages)
    #   valid POST            -> redirect to the dashboard page
    if form.validate_on_submit():
        return redirect(url_for('dashboard'))
    return render_template('form.html', form=form)

@app.route('/dashboard')
def dashboard():
    # render_template lokks for HTML 
    return render_template('dashboard.html')

if __name__ == '__main__':
    # This launches Flask and listens at http://localhost:5000.
    # debug=True shows helpful error pages and auto-reloads on code changes.
    app.run(debug=True)

"""A minimal Flask app — my first web server.""" 


from datetime import datetime
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import DataRequestForm

app = Flask(__name__)  # __name__ tells Flask where to find resources
app.config['SECRET_KEY'] = "my_super_secret_key_123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///request_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)  # create a database connection object

class RequestData(db.Model):
    """A table to store the data from the form."""
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    output_format = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<RequestData {self.id}>'

@app.context_processor
def inject_year():
    """Make the current year and today's date available to every template."""
    now = datetime.now()
    return {'current_year': now.year, 'today': now.strftime('%Y-%m-%d')}


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

        # Create a new RequestData object with the form data
        new_request = RequestData(
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            output_format=form.output_format.data,
            email=form.email.data
        )

        # Add the new request to the database
        db.session.add(new_request)
        db.session.commit()
        # Redirect to the dashboard page after successful submission
        return redirect(url_for('dashboard'))
    return render_template('form.html', form=form)

@app.route('/dashboard')
def dashboard():
    # Retrieve all requests from the database
    all_requests = RequestData.query.all()   
    # render_template lokks for HTML 
    return render_template('dashboard.html', requests=all_requests)

# if __name__ == '__main__':
#     # This launches Flask and listens at http://localhost:5000.
#     # debug=True shows helpful error pages and auto-reloads on code changes.
#     app.run(debug=True)

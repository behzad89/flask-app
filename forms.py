from flask_wtf import FlaskForm
from wtforms import SubmitField, DateField, SelectField, StringField, DecimalField
from wtforms.validators import DataRequired, Email, NumberRange

class DataRequestForm(FlaskForm):
    latitude = DecimalField('Latitude',
                            validators=[
                                DataRequired(),
                                NumberRange(min=-90, max=90)])
    longitude = DecimalField('Longitude',
                             validators=[
                                 DataRequired(),
                                 NumberRange(min=-180, max=180)])
    start_date = DateField('Start Date', format='%Y-%m-%d',
                           validators=[DataRequired()])
    end_date = DateField('End Date', format='%Y-%m-%d',
                         validators=[DataRequired()])
    output_format = SelectField('Output Format',
                                choices=[('csv', 'CSV'), ('parquet', 'Parquet')],
                                validators=[DataRequired()])
    email = StringField('Email Address',
                        validators=[
                            DataRequired(),
                            Email()
                        ])
    submit = SubmitField('Submit')

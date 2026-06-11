from flask_wtf import FlaskForm
from wtforms import SubmitField, DateField, SelectField, StringField
from wtforms.validators import DataRequired, Email, ValidationError

class DataRequestForm(FlaskForm):
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

    def validate_end_date(self, field):
        """Ensure the end date is strictly after the start date."""
        if self.start_date.data and field.data:
            if field.data <= self.start_date.data:
                raise ValidationError('End date must be after the start date.')

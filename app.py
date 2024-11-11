from flask import Flask, render_template, redirect, url_for, request, session
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired
import matplotlib.pyplot as plt
import io
import base64
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# In-memory storage for user preferences
user_data = []

class UserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    preference = RadioField('Do you prefer:', choices=[('dogs', 'Dogs'), ('cats', 'Cats')], validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = UserForm()
    if form.validate_on_submit():
        name = form.name.data
        preference = form.preference.data
        # Check if user already exists
        for user in user_data:
            if user['name'] == name:
                return redirect(url_for('results'))
        user_data.append({'name': name, 'preference': preference})
        session['name'] = name
        return redirect(url_for('results'))
    return render_template('home.html', form=form)

@app.route('/results')
def results():
    if 'name' not in session:
        return redirect(url_for('home'))
    
    # Generate pie chart
    dog_count = sum(1 for user in user_data if user['preference'] == 'dogs')
    cat_count = sum(1 for user in user_data if user['preference'] == 'cats')
    labels = 'Dogs', 'Cats'
    sizes = [dog_count, cat_count]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return render_template('results.html', plot_url=plot_url, user_data=user_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
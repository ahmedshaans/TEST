from flask import Flask, render_template, request
from dhivehi_reference_generator import generate_reference

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', reference=None) # Pass reference=None initially

@app.route('/generate', methods=['POST'])
def handle_generate():
    author = request.form['author']
    year = request.form['year']
    month = request.form['month']
    day = request.form['day']
    title = request.form['title']
    url = request.form['url']

    # Convert year and day to integers
    try:
        year_int = int(year)
        day_int = int(day)
    except ValueError:
        # Handle error if conversion fails, e.g., render an error message
        # For now, we'll assume valid input as per form type, but robust error handling is good practice
        return "Invalid year or day format", 400

    generated_ref = generate_reference(author, year_int, month, day_int, title, url)

    return render_template('index.html', reference=generated_ref)

if __name__ == '__main__':
    app.run(debug=True)

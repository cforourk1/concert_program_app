from flask import Flask, render_template, request
from validation import validate_recital_type, validate_performer_fullName, validate_accompanist, validate_location, validate_venue, validate_date, validate_time, validate_piece_title, validate_composer_name, validate_movement_title, validate_composer_birth, validate_composer_death, validate_composition_year

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.form.to_dict()

    # Validate each field
    errors = {}

    if not validate_recital_type(data.get('recital_type')):
        errors['recital_type'] = "Invalid recital type"

    if not validate_performer_fullName(data.get('performer_1_fullName')):
        errors['performer_1_fullName'] = "Performer name required"

    # ... continue for all fields

    if errors:
        return {"status": "error", "errors": errors}
    else:
        return {"status": "success", "message": "Form received!"}

if __name__ == '__main__':
    app.run(debug=True, port=5001)
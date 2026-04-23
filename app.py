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
#recital type validation
    if not validate_recital_type(data.get('recital_type')):
        errors['recital_type'] = "Invalid recital type"
#performer name validation
    if not validate_performer_fullName(data.get('performer_1_fullName')):
        errors['performer_fullName'] = "Performer name required"
#accompanist name validation
    if not validate_accompanist(data.get('accompanist_1_fullName')):
        errors['accompanist_fullName'] = "Invalid accompanist name"
#location validation
    if not validate_location(data.get('location')):
        errors['location'] = "Invalid recital location"
#venue
    if not validate_venue(data.get('venue')):
        errors['venue'] = "Invalid recital venue"

#date
    if not validate_date(data.get('date')):
        errors['date'] = "Invalid recital date"


#piece_1_title
    if not validate_piece_title(data.get('piece_1_title')):
        errors['piece_title'] = "Invalid recital piece_title"

#composer_name
    if not validate_composer_name(data.get('piece_1_composer_name')):
        errors['composer_name'] = "Invalid recital composer_name"

#composer birth
    if not validate_composer_birth(data.get('piece_1_composer_birth')):
        errors['composer_birth'] = "Invalid recital composer_birth"

#composer death
    if not validate_composer_death(data.get('piece_1_composer_death')):
        errors['composer_death'] = "Invalid recital composer_death"
#composition year
    if not validate_composition_year(data.get('piece_1_composition_year')):
        errors['composition_year'] = "Invalid recital composition_year"


#movement title
    if not validate_movement_title(data.get('piece_1_movement_1')):
        errors['movement_title'] = "Invalid recital movement_title"


    if errors:
        return {"status": "error", "errors": errors}
    else:
        return render_template('preview.html',
    recital_type=data.get('recital_type'),
    performer_name=data.get('performer_1_fullName'),
    performer_instruments=data.get('performer_1_instruments'),
    accompanist_name=data.get('accompanist_1_fullName'),
    accompanist_instruments=data.get('accompanist_1_instruments'),
    location=data.get('location'),
    venue=data.get('venue'),
    date=data.get('date'),
    time=data.get('time'),
    title=data.get('piece_1_title'),
    composer_name=data.get('piece_1_composer_name'),
    composer_birth=data.get('piece_1_composer_birth'),
    composer_death=data.get('piece_1_composer_death'),
    composition_year=data.get('piece_1_composition_year'),
    movements=data.get('piece_1_movement_1'),
)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
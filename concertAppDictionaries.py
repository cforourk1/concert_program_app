#dictionaries for program

#how do I create a dropdown menu for the different recital types?
#can we pull up a confirmation page with all of the data that can be edited #before submission?
#How do I assign appropriate fonts and sizes and layout to this?


#recital metadata will hold the top level information
#type is listged as the type of recital - this will be
# dropdown menu later
#performers array will hold all of the performer data a
#as they get added to the array. same with performers #and all other data listed here.

from validation import validate_recital_type

recital_metadata = {
    "type": "BM",  # dropdown
    "performers": [],  # list of performer dictonaries
    "accompanists": [],  # list of accompanist dictionaries
    "date": None,
    "location": "",
    "venue": "",
    "time": None,
}

# piece data to include composer information, title, #arranger, and movemenets.
piece = {
    "title": "",
    "composer": {
        "name": "",
        "birth": None,
        "death": None
    },
    "composition_year": None,
    "arranger": "",  # if applicable
    "movements": [],  # list of movement titles
    "additionalPerformers": []  # for this piece
}

#need to add a button that says add additional set information

program = {
    "metadata": recital_metadata,
    "pieces": [],  # list of piece dicts
    "intermissionAfterPiece": None  # which piece has intermission
}

#performer dictionary. Array added to hold multiple #instruments
#add a button to list additional performers
performer = {
    "fullName": "",
    "instruments": [],
}

#accompanyist dictionary. Need to add button
#to list additional

accompanyist = {
    "fullName": "",
    "instruments": [],
}

#accompanyist dictionary. Need to add button
#to list additional
movement = {
    "title": "",
    "tempo": "",
}


# Example: what a filled-in program looks like
example_program = {
    "metadata": {
        "type": "BM",
        "performers": [
            {"fullName": "Joe Smith", "instruments": ["Clarinet", "Bass Clarinet"]}
        ],
        "accompanists": [
            {"fullName": "Marta Moe", "instruments": ["Piano"]}
        ],
        "date": "April 15, 2023",
        "location": "Moore Building",
        "venue": "Britton Recital Hall",
        "time": "5:30 PM"
    },
    "pieces": [
        {
            "title": "Stelle cadenti",
            "composer": {
                "name": "Mario Castelnuovo-Tedesco",
                "birth": 1895,
                "death": 1968
            },
            "composition_year": 1919,
            "arranger": None,
            "movements": [
                {"title": "Oh! Quanto siete pallida nel viso!", "tempo": ""},
                {"title": "Fior d'erba secca", "tempo": ""}
            ],
            "additionalPerformers": []
        }
    ],
    "intermissionAfterPiece": None
}

print(example_program)
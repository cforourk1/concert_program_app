#dictionaries for program

#how do I create a dropdown menu for the different recital types?
recital_metadata = {
    "type": "BM",  # dropdown
    "performers": [],  # list of performer dictonaries
    "accompanists": [],  # list of accompanist dictionaries
    "date": "",
    "location": "",
    "venue": "",
    "time": ""
}



#button to add additional performers
#can we pull up a confirmation page with all of the data that can be edited #before submission?
#How do I assign appropriate fonts and sizes and layout to this?

piece = {
    "title": "",
    "composer": {
        "name": "",
        "birth": 1900,
        "death": 1980
    },
    "year": 1920,
    "arranger": "",  # if applicable
    "movements": [],  # list of movement titles
    "additionalPerformers": []  # for this piece
}
#need to add a button that says add additional set information

program = {
    "metadata": recital_metadata,
    "pieces": [],  # list of piece dicts
    "intermissionAfterPiece": 3  # which piece has intermission
}


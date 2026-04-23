#validations to run on the date that is input to the form
#these validations will help me make dropdowns later in Flask

# Your validation functions
def validate_recital_type(recital_type):
    """Check if recital_type is one of the allowed types"""
    valid_types = ["BM", "MM", "DMA", "Specialist", "Guest", "Chamber", "Faculty", "BFA"]
    if recital_type in valid_types:
#note the indentation scheme - this matters in python
        return True
    else:
        return False


#validation to check in accompanist is not empty

def validate_accompanist(accompanist_name):
        """Check if accompanist is blank"""
        if accompanist_name == None:
            return False
        if not accompanist_name:
            return False
        else:
           return True


#validate_location() — not blank (string)
def validate_location(location):
    """Check if location is blank"""
    if location == None:
        return False
    if not location:
        return False
    else:
        return True


#validate_venue() — not blank (string)
def validate_venue(venue):
    """Check if venue is blank"""
    if venue == None:
        return False
    if not venue:
        return False
    else:
        return True



#validation to check that the date field is not empty

def validate_date(date):
    """Check if location is blank"""
    if date == None:
        return False
    if not date:
        return False
    else:
        return True


#validation to check that the time field is not empty

def validate_time(time):
    """Check if time is blank"""
    if time == None:
        return False
    if not time:
        return False
    else:
        return True

#validation to check that the title field is not empty

def validate_piece_title(title):
    """Check if #title is blank"""
    if title == None:
        return False
    if not title:
        return False
    else:
        return True

#validation composer name

def validate_composer_name(composer_name):
    """Check if composer_name is blank"""
    if composer_name == None:
        return False
    if not composer_name:
        return False
    else:
        return True


#validation to check that the movement title  field is not empty

def validate_movement_title(movement_title):
    """Check if movement_title is blank"""
    if movement_title == None:
        return False
    if not movement_title:
        return False
    else:
        return True


#validate_performer_fullName() — proper format

def validate_performer_fullName(performer_fullName):
    """Check if performer_fullName is blank"""
    if performer_fullName == None:
        return False
    if not performer_fullName:
        return False
    else:
        return True

#validate_instruments() — proper format

def validate_instruments(instruments):
    """Check if instruments is blank"""
    if instruments == None:
        return False
    if not instruments:
        return False
    else:
        return True



#validate_composer_birth() — proper format

def validate_composer_birth(composer_birth):
    """Check if composer_birth is blank"""
    if composer_birth == None:
        return False
    if not composer_birth:
        return False
    else:
        return True




#validate_composer_death() — proper format

def validate_composer_death(composer_death):
    """Check if composer_death is blank"""
    if composer_death == None:
        return False
    if not composer_death:
        return False
    else:
        return True

#validate_composition_year() — proper format

def validate_composition_year(composition_year):
    """Check if composition_year is blank"""
    if composition_year == None:
        return False
    if not composition_year:
        return False
    else:
        return True





if __name__ == '__main__':

#recital type valid
    print(validate_recital_type("BM"))        # Should print: True
    print(validate_recital_type("Invalid"))
#Performer Name check
    print(validate_performer_fullName(""))        # Should print: False
    print(validate_performer_fullName("Invalid"))   # Should print: False
    print(validate_performer_fullName("Greg Laman"))   # Should print: True
#Instrument check
    print(validate_instruments([]))        # Should print: False
    print(validate_instruments(["Invalid"]))   # Should print: False
    print(validate_instruments(["bassoon"]))   # Should print: True
#movement title not empty
    print(validate_movement_title(""))        # Should print: False
    print(validate_movement_title("Invalid"))   # Should print: False
    print(validate_movement_title("F minor"))   # Should print: True
#accompanist is not empty
    print(validate_accompanist(""))        # Should print: False
    print(validate_accompanist("Invalid"))   # Should print: False
    print(validate_accompanist("Greg Laman"))   # Should print: True
#location check
    print(validate_location(""))        # Should print: False
    print(validate_location("Invalid"))   # Should print: False
    print(validate_location("Earl V. Moore Building"))   # Should print: True
#venue check
    print(validate_venue(""))        # Should print: False
    print(validate_venue("Invalid"))   # Should print: False
    print(validate_venue("Britton Recital Hall"))   # Should print: True
#date check
    print(validate_date(""))        # Should print: False
    print(validate_date("Invalid"))   # Should print: False
    print(validate_date("4.30.26"))   # Should print: True
#time check
    print(validate_time(""))        # Should print: False
    print(validate_time("Invalid"))   # Should print: False
    print(validate_time("4:30pm"))   # Should print: True
#title check
    print(validate_piece_title(""))        # Should print: False
    print(validate_piece_title("Invalid"))   # Should print: False
    print(validate_piece_title("titlepiece"))   # Should print: True
#composer check
    print(validate_composer_name(""))        # Should print: False
    print(validate_composer_name("Invalid"))   # Should print: False
    print(validate_composer_name("Greg Laman"))   # Should print: True
#composer birth
    print(validate_composer_birth(""))        # Should print: False
    print(validate_composer_birth("Invalid"))   # Should print: False
    print(validate_composer_birth("1957"))   # Should print: True
#composer death
    print(validate_composer_death(""))        # Should print: False
    print(validate_composer_death("Invalid"))   # Should print: False
    print(validate_composer_death("1966"))   # Should print: True
#composition year
    print(validate_composition_year(""))        # Should print: False
    print(validate_composition_year("Invalid"))   # Should print: False
    print(validate_composition_year("1945"))   # Should print: True

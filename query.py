"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# 1) Get the brand with the **id** of 8.
# db.session.query(Brand).filter(Brand.id==8).one()

# 2) Get all models with the **name** Corvette and the **brand_name** Chevrolet.
# db.session.query(Model).filter(Model.brand_name=='Chevrolet', Model.name=='Corvette').all()

# 3) Get all models that are older than 1960.
# db.session.query(Model).filter(Model.year < 1960).all()

# 4) Get all brands that were founded after 1920.
# db.session.query(Brand).filter(Brand.founded > 1920).all()

# 5) Get all models with names that begin with "Cor".
# db.session.query(Model).filter(Model.name.like('Cor%')).all()

# 6) Get all brands with that were founded in 1903 and that are not yet discontinued.
# db.session.query(Brand).filter(Brand.founded==1903, Brand.discontinued.is_(None)).all()

# 7) Get all brands with that are either discontinued or founded before 1950.
# db.session.query(Brand).filter(db.or_(Brand.discontinued.isnot(None), Brand.founded < 1950)).all()

# 8) Get any model whose brand_name is not Chevrolet.
# db.session.query(Brand).filter(Brand.name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    query = db.session.query(Model.name, Model.brand_name, Brand.headquarters).join(Brand, Brand.name==Model.brand_name).filter(Model.year==year).all()

    for item in query:
        print "Model: {}, Brand: {}, Headquarters {}".format(item[0], item[1], item[2])

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    query = db.session.query(Model.brand_name, Model.name).group_by(Model.brand_name).all()

    print query


# -------------------------------------------------------------------
#WHY ARENT ANY OF THEM WORKING?  WHY IS THE 'm' PURPLE? 
# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    query = Brand.query.filter(Brand.name.like('%mystr%')).all()

    print query


def get_models_between(start_year, end_year):
    query = db.session.query(Model).filter(Model.year > start_year, Model.year < end_year)

    print query

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

#the returned value is an object from the Brand table.

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

#an association table allows the user to 'walk' across two different tables.  It manages tables that have foreign key relationships

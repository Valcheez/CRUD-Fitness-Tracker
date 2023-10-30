from app import app, db

if __name__ == '__main__':
    db.create_all()  # Create tables if they don't exist
    app.run(debug=True)


#Use this from the python shell to initialize the db
# from app import app, db
# with app.app_context():
#     db.create_all()
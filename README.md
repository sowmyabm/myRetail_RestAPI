# myRetail_RestAPI

# pip install
pip install Flask
pip install Jsonfiy
pip install sqlalchemy
pip install flask_sqlalchemy
pip install flask_mashmallow

# Run the below command to create db

>> from app import db
>> db.create_all()
>> exit()

# Run Server (http://localhst:5000)
python app.py

# The REST end points for CRUD operations
GET /product
GET /product/:id
POST /product
PUT /product/:id
DELETE /product/:id

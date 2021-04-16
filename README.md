# myRetail_RestAPI

# pip install
1. pip install Flask
2. pip install Jsonfiy
3. pip install sqlalchemy
4. pip install flask_sqlalchemy
5. pip install flask_mashmallow

# Run the below command to create db

>> from app import db
>> db.create_all()
>> exit()

# Run Server (http://localhst:5000)
python app.py

# The REST end points for CRUD operations
1. GET /product
2. GET /product/
3. POST /product
4. PUT /product/:id
5. DELETE /product/:id

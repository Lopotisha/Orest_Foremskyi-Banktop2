from sqlalchemy import create_engine

DATABASE_URL = "mysql://root:@localhost:3306/banktop2"

engine = create_engine(DATABASE_URL)

def test_connection():
    try:
        with engine.connect() as connection:
            print("Connection successful")
    except Exception as e:
        print("Connection failed:", e)

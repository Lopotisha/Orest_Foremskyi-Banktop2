from sqlalchemy import create_engine, text

DATABASE_URL = "mysql://root@localhost:3306/banktop2"

engine = create_engine(DATABASE_URL)

def show_data():
    try:
        with engine.connect() as connection:
            print("Data from client table:")
            result = connection.execute(text("SELECT * FROM client;"))
            for row in result:
                print(row)

            print("\nData from account table:")
            result = connection.execute(text("SELECT * FROM account;"))
            for row in result:
                print(row)

    except Exception as e:
        print("Failed to retrieve data:", e)

show_data()

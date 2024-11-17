import oracledb

def connect_to_oracle(user, password, dsn):
    try:
        connection = oracledb.connect(
            user=user,
            password=password,
            dsn=dsn
        )
        print("Connected to Oracle!")

        return connection
    except Exception as e:
        print(f"Error while connecting to Oracle: {e}")

        return None

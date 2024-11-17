import pandas as pd

def fetch_data_from_table(connection, table_name):
    try:
        query = f"SELECT * FROM {table_name}"

        with connection.cursor() as cursor:
            cursor.execute(query)

            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]

            df = pd.DataFrame(rows, columns=columns)

        return df
    except Exception as e:
        print(f"Error fetching data from table {table_name}: {e}")

        return pd.DataFrame()

def save_data_to_table(connection, df, table_name):
    try:
        with connection.cursor() as cursor:
            # Ensure column names are wrapped in double quotes
            valid_columns = [f'"{col.strip()}"' for col in df.columns]

            # Create the insert query
            insert_query = f"""
            INSERT INTO {table_name} ({', '.join(valid_columns)})
            VALUES ({', '.join([':' + str(i+1) for i in range(len(valid_columns))])})
            """
            
            # Insert data into the table
            cursor.executemany(insert_query, df.values.tolist())
            connection.commit()
            print(f"Data inserted into {table_name} successfully.")
    except Exception as e:
        print(f"Error saving data to table {table_name}: {e}")

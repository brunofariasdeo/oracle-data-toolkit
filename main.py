import oracledb
from IPython.display import display

from db_connection import connect_to_oracle
from data_operations import fetch_data_from_table, save_data_to_table
from data_anonymization import anonymize_data
from utils import load_env_variables, load_config

def main():
    # Load environment variables from .env
    env_vars = load_env_variables()

    # Load config from config.json
    config = load_config()
    if not config:
        print("Error: Configuration file not loaded properly.")
        return

    # Database connection parameters from .env
    user = env_vars['DB_USER']
    password = env_vars['DB_PASSWORD']
    hostname = env_vars['DB_HOST']
    port = env_vars['DB_PORT']
    service_name = env_vars['DB_SERVICE_NAME']

    dsn = oracledb.makedsn(hostname, port, service_name) 

    source_table = config["tables"]["source_table"]
    target_table = config["tables"]["target_table"]

    # Connect to Oracle Database
    connection = connect_to_oracle(user, password, dsn)
    if not connection:
        return
    
    # Fetch data from the table
    data = fetch_data_from_table(connection, source_table)
    display(data)

    # Anonymize the data
    anonymized_data = anonymize_data(data)
    display(anonymized_data)

    # Save anonymized data to a new table
    save_data_to_table(connection, anonymized_data, target_table)

    # Close the connection
    connection.close()

if __name__ == "__main__":
    main()

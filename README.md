
# Oracle Data Toolkit

## Description
This project provides a Python script to anonymize data from an Oracle Database. It connects to the database, fetches data from a specified source table, anonymizes specific columns, and saves the anonymized data to a target table. The script is designed to be modular and configurable.

## Prerequisites

- **Python 3.7+**
- **Oracle Database (Oracle XE)**
- **Docker**
- **DBeaver** (Open-source database management tool)  
  Install DBeaver from [here](https://dbeaver.io/download/) but feel free to use another tool of your preference.

## Step-by-Step

### 1. Install Docker
- Download and install Docker for your OS
- Verify installation: Run `docker --version` in terminal

### 2. Pull Oracle database image
- Open terminal and run the following commands:

```bash
docker pull container-registry.oracle.com/database/express:21.3.0-xe

docker run -d --name oracle-xe   -p 1521:1521 -p 5500:5500   -e ORACLE_PWD=YourPassword   container-registry.oracle.com/database/express:21.3.0-xe
```

- Replace `YourPassword` with a strong password.

### 3. Verify container status
- Check container status: `docker ps`
- View logs: `docker logs oracle-xe`

### 4. Install DBeaver
- Download DBeaver: [DBeaver Download](https://dbeaver.io/download/)
- Install and launch DBeaver.

### 5. Connect DBeaver to Oracle Database
- Open DBeaver and click **New Database Connection**.
- Select **Oracle** as the database type.
- Enter the following connection details:
  ```
  Host: localhost
  Port: 1521
  Database: XE
  Username: SYSTEM
  Password: YourPassword
  ```
- Test the connection and save it if successful.

## Setting up the project

1. Clone the repository or create a new directory for the project.
2. Create a `.env` file with your Oracle DB connection credentials. Use `.env.example` as a reference.
3. Create a `config.json` file with the source and target table names.

## Install required dependencies
To install the required dependencies, use the following command:
```bash
pip install -r requirements.txt
```

### Running the Script
1. The script will fetch data from the source table.
2. It will anonymize the data by modifying specific columns (such as names and billing amounts).
3. It will save the anonymized data to the target table.

Run the script using the following command:
```bash
python main.py
```

## License
This project is open-source and available under the MIT License.

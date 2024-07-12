from dotenv import load_dotenv
import os

load_dotenv()

print("DATABRICKS_TOKEN:", os.getenv("DATABRICKS_TOKEN"))
print("DATABRICKS_SERVER_HOSTNAME:", os.getenv("DATABRICKS_SERVER_HOSTNAME"))
print("DATABRICKS_HTTP_PATH:", os.getenv("DATABRICKS_HTTP_PATH"))
print("DATABRICKS_CATALOG:", os.getenv("DATABRICKS_CATALOG"))
print("DATABRICKS_SCHEMA:", os.getenv("DATABRICKS_SCHEMA"))

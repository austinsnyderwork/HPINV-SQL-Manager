
import pandas as pd
from sqlalchemy import create_engine


class SqlManager:

    def __init__(
            self,
            server: str = None,
            database: str = None,
            driver: str = None
    ):
        server = server or 'HC-SQL5'
        database = database or 'HPINV'
        driver = driver or 'ODBC+Driver+17+for+SQL+Server'

        self.engine = create_engine(
            f"mssql+pyodbc://{server}/{database}?driver={driver}&trusted_connection=yes"
        )

    def pull(self, sql_path: str, params: list = None) -> pd.DataFrame:
        with open(sql_path, "r") as f:
            query = f.read()

        df = pd.read_sql(
            query,
            con=self.engine,
            params=params
        )

        return df

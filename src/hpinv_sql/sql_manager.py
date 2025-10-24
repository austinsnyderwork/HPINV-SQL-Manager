from pathlib import Path
from typing import Type

import pandas as pd
from sqlalchemy import create_engine

from .query_path_registry import QueryPullSpec


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

    def pull(self, query_spec: QueryPullSpec) -> pd.DataFrame:
        with open(query_spec.query_path, "r") as f:
            query = f.read()

        df = pd.read_sql(
            query,
            con=self.engine,
            params=query_spec.params
        )

        return df

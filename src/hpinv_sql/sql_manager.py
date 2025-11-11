from pathlib import Path
from typing import Type

import pandas as pd
from sqlalchemy import create_engine

from .query_path_registry import QueryPullSpec

import hpinv_enums


class HpinvSqlManager:

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

    def pull_all_data_from_table(self,
                                 table_name: hpinv_enums.HpinvTable,
                                 convert_columns_to_lowercase=True) -> pd.DataFrame:
        df = pd.read_sql(f"SELECT * FROM {table_name.value}", self.engine)
        if convert_columns_to_lowercase:
            df.columns = [col.lower() for col in df.columns]

        return df

    def pull(self, query_spec: QueryPullSpec) -> pd.DataFrame:
        with open(query_spec.query_path, "r") as f:
            query = f.read()

        df = pd.read_sql(
            query,
            con=self.engine,
            params=query_spec.params
        )

        return df

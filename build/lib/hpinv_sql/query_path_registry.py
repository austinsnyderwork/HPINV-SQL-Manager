from abc import ABC
from pathlib import Path


class QueryPullSpec(ABC):

    def __init__(self, path: Path, params: list = None):
        self.path = path
        self.params = params


class TransactionsSpec(QueryPullSpec):

    def __init__(self, start_year: int):
        super().__init__(
            path=Path(__file__).parent / "queries" / "transactions.sql",
            params=[start_year]
        )


class WorkPeriodsSpec(QueryPullSpec):

    def __init__(self):
        super().__init__(
            path=Path(__file__).parent / "queries" / "define_work_periods.sql"
        )


class WorksiteHistorySpec(QueryPullSpec):

    def __init__(self):
        super().__init__(
            path=Path(__file__).parent / "queries" / "worksite_histories_data.sql"
        )

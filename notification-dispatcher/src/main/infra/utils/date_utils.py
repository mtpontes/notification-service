from datetime import datetime

from src.main.infra.constants.constants import DateConsts


class DateUtils:

    @staticmethod
    def to_date_br_str(data: str) -> str:
        return datetime.strftime(data, DateConsts.BR_PATTERN)

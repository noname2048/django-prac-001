class YearConverter:
    regex = r"\d{4}"

    def to_url(self, value):
        return str(value)

    def to_python(self, value):
        return int(value)


class MonthConverter(YearConverter):
    regex = r"\d{1,2}"


class DayConverter(YearConverter):
    regex = r"[0123]\d"

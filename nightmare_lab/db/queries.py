def build_query(report_type):
    base = "SELECT * FROM reports WHERE type = '{}'"
    return base.format(report_type)
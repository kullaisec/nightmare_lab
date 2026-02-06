from db.database import execute
from db.queries import build_query
from templates.render import render_html

def generate_report(report_type):
    query = build_query(report_type)
    data = execute(query)
    return render_html(data)
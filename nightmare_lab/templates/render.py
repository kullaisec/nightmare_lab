def render_html(rows):
    html = "<ul>"
    for r in rows:
        html += f"<li>{r[1]}</li>"
    return html + "</ul>"
from flask import Flask, request
from auth.decorators import login_required
from services.report_service import generate_report

app = Flask(__name__)

@app.route("/report")
@login_required
def report():
    user_input = request.args.get("type")
    return generate_report(user_input)
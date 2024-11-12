from flask import Blueprint, render_template
from views.utils import login_required
from danfoss_ZeroDay import get_all_requirements

requirement = Blueprint("requirement", import_name=__name__, template_folder="templates")

# Renders the requirements page after checking if the user is logged in
@requirement.route("/")
@login_required
def requirement_page():
    requirements = get_all_requirements()
    return render_template("required_documents_page.html", requirements=requirements)

ZeroDay Project

Project Description
ZeroDay Project aims to assist new employees by providing all essential documents and safety videos before their first day at work. This helps save time during the onboarding process, ensuring that new hires are well-prepared.

Technology Stack
    Backend: Python Flask
    Frontend: HTML, CSS, Bootstrap
    Database: PostgreSQL (local setup)
    Additional Tools: Blueprint for code organization
    Cloud: Heroku

Features
    1. User Authentication: Allows users to log in with a username and password.
    2. Documents Section: Displays a list of required documents that employees should bring on their first day.
    3. Videos Section: Provides workplace safety videos that employees must watch.
    4. Admin Functionality:
        Admins can add or remove videos, users, and requirements (planned for later stages).

Project Structure
    HTML Files: Located under "templates/" and extend from "base.html".
    CSS Files: Custom styling is organized under "static/css/".
    Python Files:
        "server.py": Main server and route management.
        "requirement.py", "video.py", "utils.py": Manage specific functionalities related to requirements, videos, and utilities.
        "queries.py": Contains database query functions.
    Templates:
        "login_page.html", "home_page.html", "required_documents_page.html", "videos_page.html": Render different sections of the project.
    Submission Directories:
        proposal/: Contains the initial project proposal PDF.
        progress_report/: Contains the progress report PDF.

Usage
    Access the Home Page for project introduction and navigation links.
    Visit Required Documents to view the list of mandatory documents.
    Access Videos to watch required safety materials.

Future Deployment
The project will be deployed on Heroku in the next phase, enabling cloud-hosted functionality and scaling.

Future Milestones
    1. Admin Page: Feature for admins to manage requirements and videos.
    2. Testing and Optimization:
        Complete unit tests and optimize for scalability.
    3. User Load Testing:
        Populate the database with sample users for testing.

Submission Tracking
After each submission, PDFs will be added in specific directories:
    Proposal: Initial project proposal is saved in the proposal/ directory.
    Progress Report: Progress report files are saved in the progress_report/ directory.

Created by Umutcan CELIK - 2024

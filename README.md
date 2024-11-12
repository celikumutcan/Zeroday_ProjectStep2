ZeroDay Project

Project Description
My ZeroDay Project is designed to help new employees by giving them all the important documents and safety videos they need before their first day. This way, they’re prepared in advance, making the onboarding process smoother and saving time.

Technology Stack
I chose Python Flask for the backend because it's lightweight and powerful.
The frontend is built with HTML, CSS, and Bootstrap for a clean, responsive design.
PostgreSQL is my database, and it is set up locally for now.
I'm using Blueprint in Flask to keep my code organized.
For cloud deployment, I'm planning to use Heroku soon.

Features
1. User Authentication: Users log in with a username and password for secure access.
2. Documents Section: Here, new employees can see a list of important documents to bring.
3. Videos Section: This is where essential workplace safety videos are available.
4. Admin Functionality:
I’m adding an admin section where admins can add or remove videos, users, and requirements (this will be completed in the next stages).

Project Structure
HTML Files: All my HTML templates are in "templates/" and extend from a base file, "base.html".
CSS Files: I keep all my custom styles in "static/css/".
Python Files:
	"server.py" handles the main server setup and routes.
	"requirement.py", "video.py", and "utils.py" manage specific parts of the app (like requirements, videos, and utility functions).
	"queries.py" has functions for database queries.
Templates:
	"login_page.html", "home_page.html", "required_documents_page.html", and "videos_page.html" display different sections.
Submission Directories:
	proposal/: Holds my initial project proposal PDF.
	progress_report/: Will contain progress report files as I go along.

Usage
Access the Home Page to get an overview and see navigation links.
Visit the Required Documents section to view the list of necessary documents.
Access the Videos section to watch safety videos.

Future Deployment
Next up, I’ll be deploying the project on Heroku, which will allow me to host it in the cloud and scale it as needed.

Future Milestones
1. Admin Page: A page for admins to manage requirements and videos.
2. Testing and Optimization:
	I’ll complete unit tests and optimize the app for scalability.
3. User Load Testing:
	I plan to populate the database with sample users to simulate real-world usage.

Submission Tracking
After each submission, I’ll save the PDFs in specific directories:
	Proposal: My initial project proposal is saved in the proposal/ directory.
	Progress Report: Progress report files will be saved in the progress_report/ directory.

Created by Umutcan CELIK - 2024

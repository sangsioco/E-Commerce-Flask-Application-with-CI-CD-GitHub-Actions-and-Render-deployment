# E-Commerce Flask Application with CI/CD GitHub Actions and Render deployment  
Author: Sara Angsioco  
Date: August 11, 2024  

Note:
The structure of this project are based on Module 13 MiniProject, with some changes.  
  
Changes:    
1. Tests folder now only contains test_mock and test_app python file.    
2. Manifest.yaml file was added under .github. This ensures that the application will run when using the CI/CD Action in GitHub.  
3. Requirements.txt was updated to include gunicorn, psycopg2 and psycopg2-binary.
  
Installation:
1. Clone the repository to run the file locally.  
2. Create a virtual environment and install all depencies based on the requirements.txt.  
3. Run the application.  
Using CI/CD:  
4. For CI/CD Action, you can access my Action past test run or re-run the workflow using the following link: https://github.com/sangsioco/Module-16-MiniProject/actions
5. You may also upload on your own GitHub account to test.
Using Render:  
6. Upload the project to your GitHub account.
7. Login to your Render account.
8. Connect the project repository to your Render account.
9. Add a new database and webservice if needed

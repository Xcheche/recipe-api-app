Steps to add Docker Hub access token on GitHub
Generate Docker Hub Access Token:

Log in to Docker Hub.

Go to your account settings → Security → New Access Token.

Generate a token and copy it.

-----------------------Add the token as a secret in GitHub-------------------------------

Go to your GitHub repository ofthe current project you are working on.

Click on Settings → Security → Secrets and variables → Actions.

Click New repository secret.

Name the secret, e.g., DOCKERHUB_TOKEN.

Paste the Docker Hub access token as the secret value.

Similarly, add your Docker Hub username as a secret, e.g., DOCKERHUB_USERNAME.

Use the secrets in your GitHub Actions workflow:
-------------------------------To add another django app------------------------------------
docker  compose  exec web python manage.py startapp new_app_name
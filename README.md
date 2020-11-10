# Simple Flask App

This web application is built using the Flask python famework. The pages are rendered as templates, and the page elements are styled using a Bootstrap 4 Bootswatch theme. The project is able to be deployed in a CI/CD pipeline using Gitlab local runners and AWS elastic containers (EC2). 

### Docker Container 
The repository includes a docker-compose file which will build the docker image to run the application. The dockerfile is within the src file while the docekr-compose file is within the root of the project directory.

### CI/CD Pipeline
The repository also includes a gitlab-ci file; when paired with a registered local gitlab runner, it will continuously integrate the source code when commits are pushed to the remote gitlab repository. The CI pipeline has been seperated into three stages: 1) test 2) build 3) deploy. The test stage is currently empty because there is only a single html end point, however, this is where unit and integration tests would be performed on the source code to test various end points (database connections, APIs, etc.). The build stage will build the latest docker image, and if the build is sucessful, it will push the image to the remote docker registry. The deploy phase will prompt an AWS elastic cluster service (ECS) to pull the latest docker image from the docker registry and deploy it as the current image, completing the CI/CD pipeline.

### Amazon Web Services
The project is deployed to an EC2, which is managed by the Elastic Container Service, a container orchestration service provided by Amazon. The gitlab-ci file uses the AWS CLI API provided by Amazon, to update the application running on the EC2 instance. 
# docker-demo
This repository is to implement and understand Docker with the help of a project demonstration.

To build the image on DockerHub:
-> docker build -t mlops-docker-demo .

To run the image to form a container:
-> docker run -p 5001:5001 mlops-docker-demo

Just like we have version for applications, we can give tags for our docker images:
-> docker tag mlops-docker-demo atharvabot7/mlops-docker-demo:v1

After tagging, we can push this image onto Docker Hub, just like we push our code on Github:
-> docker push atharvabot7/mlops-docker-demo:v1

Now after we have created the image, if we want to share the image for others to run, they can run:
-> docker pull atharvabot7/mlops-docker-demo:v1
After pulling theimage, they can simply run it, given their port is free to be used:
-> docker run -p 5001:5001 mlops-docker-demo:v1

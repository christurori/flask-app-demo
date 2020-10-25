# set base image (host OS)
FROM python:3.7

# set the working directory within container
WORKDIR /src/app

# expose port
EXPOSE 5000

# copy dependency file to working directory
COPY ./requirements.txt .

# install dependencies
RUN pip3 install -r requirements.txt

# copy the content of the local directory to the working directory
# execute command last to leverage docker layered cache
COPY . .

# command to run on container start
CMD [ "python", "./app.py" ]
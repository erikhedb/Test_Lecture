# Lab Step 0 - Clone repos
git clone git@github.com:erikhedb/Test_Lecture.git

# Lab Step 1
Check your python version. The lab shuld work with all python3 versions
> python3 --version 


Run the sample main code in your local enviromnet
>python3 src/main.py

Run the pytest case on your local computer
> pip install --trusted-host pypi.python.org -r requirements.txt
> pytest

# Lab step 3
Build the image and run the container
> docker build -t my-py .
> docker run my-py

Force a test error
Update the testcase - Set "assert False"
docker build -t my-py .
- What happends

# Lab step 4
Clean up docker

Stop all containers
> docker stop $(docker ps -a -q)

Remove all containers
> docker rm $(docker ps -a -q)

docker build --tag=capstone .

dockerpath=beartuchman/capstone

docker tag capstone ${dockerpath}:newester

docker push ${dockerpath}:newester

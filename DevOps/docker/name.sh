# Create a container named helloMoto, using hello-world
# name : helloMoto
# mount :
    # type: bind
    # source: present working directory

 docker run -dp 3000:3000 --name helloMoto --mount type=bind,source="$(pwd)",target=/app hello-world
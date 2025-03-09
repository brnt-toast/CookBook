# Create a container named ToDo, using hello-world
# mount 
    # type: bind
    # source: present working directory

docker run -dp 3000:3000 --name ToDo --mount type=bind,source="$(pwd)",target=/app hello-world
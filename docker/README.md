# Name
```sh
docker run -dp 3000:3000 --name helloMoto --mount type=bind,source="$(pwd)",target=/app hello-world
```

# Mounts
## Bind Mount
```sh
docker run -dp 3000:3000 --name ToDo --mount type=bind,source="$(pwd)",target=/app hello-world
```
### Read Only 
```sh
docker run -dp 3000:3000 --mount type=bind,source="$(pwd)",target=/app,readonly hello-world
```
# Basic Commands

1. docker pull
    * docker pull --all-tags
2. docker images
    * ls
    * build
    * push -- push to remote 
    * history -- image info
3. docker run : [flags](https://docs.docker.com/engine/reference/commandline/run/#parent-command)
    * --env
    * --detach
4. docker ps
    * --all
5. docker stop
6. docker system
    * docker system prune
    * docker system df
7. docker container : [flags](https://docs.docker.com/engine/reference/commandline/create/#parent-command)
    * create -- create new container
    * start -- start existing container
    * prune -- create new conatiner and then start
    * ls -- list running containers
    * inspect -- print info to STDOUT
    * logs -- print logs to STDOUT
    * kill -- stop process
    * stop -- graceful shutdown
    * rm -- delete **STOPPED** container
    * -a : --attach -- attach to STDIN, STDOUT, STERR


    <hr>
    
    * `docker container create my_app/my_image:my_tag`
8. docker network
    * ls
9. docker volume
    * ls
10. docer rmi
11. docker rm
12. docker logs
    * -follow
13. docker exec
14. docker version
15. docker info
16. docker serach
17. docker restart
18. docker rename
    * docker rename hello_earth hello_mars
19. docker commit
20. docker build
21. docker top
22. docker swarm
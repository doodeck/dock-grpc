# dock-grpc

## Building and running docker image

```shell
docker buildx build . -t dock-grpc:local
docker run --rm --publish 50051:50051 dock-grpc:local
```

## Known problems

- tests not running, despite apparently twice specified configuration
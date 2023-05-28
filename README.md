# dock-grpc

## building and runing locally
```shell
pip install -e .
dock-grpc
```

Then in another terminal:
```shell
dock-grpc-client
```


## Building and running docker image

```shell
docker buildx build --progress plain . -t dock-grpc:local
docker run --rm --name dock_grpc --publish 50051:50051 dock-grpc:local
```

Then in another terminal:
```shell
docker exec -it dock_grpc dock-grpc-client
```


## Known problems and workarounds

- build on the CLI completes properly as described above. When building the container, it requires explicitly starting setup.py (see Dockerfile). Besides,  python...alpine image would not accept that workaround, hence using another ono.
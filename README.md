# dock-grpc

## building and runing locally
```shell
pip install -e .
dock-grpc
```

## Building and running docker image

```shell
docker buildx build --progress plain . -t dock-grpc:local
docker run --rm --publish 50051:50051 dock-grpc:local
```

## Known problems and workarounds

- build on the CLI completes properly as described above. Building the container it requires explicitly starting setup.py to be seen in Dockerfile. Besides,  python...alpine image would not accept that workaround, hence using another ono.
# FROM python:3.10.11-alpine3.18 as RUNNER not working
FROM python:3.10.11-slim as RUNNER

WORKDIR /app
COPY . .

RUN python3 setup.py build && \
    pip install --no-cache-dir -v . && \
    rm -rf /app && \
    rm -rf ~/.cache/pip

FROM scratch

COPY --from=RUNNER / /

ENTRYPOINT "dock-cli"
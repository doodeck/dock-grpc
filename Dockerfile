FROM python:3.10.11-alpine3.18 as RUNNER

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -v . && \
    rm -rf /app && \
    rm -rf ~/.cache/pip

FROM scratch

COPY --from=RUNNER / /

ENTRYPOINT "dock-cli"
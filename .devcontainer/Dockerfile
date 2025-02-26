FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

ENV PYTHONUNBUFFERED 1
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV UV_PYTHON_DOWNLOADS=never
ENV UV_PYTHON=python3.12
#RUN apt-get update  && apt-get -y upgrade && apt-get -y install --no-install-recommends --no-install-suggests gcc musl-dev libffi-dev python3-dev openssl procps curl git zip unzip wget nano pipx  && apt-get clean && apt -y autoremove && rm -rf /var/lib/{apt,dpkg,cache,log}
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /workspace
COPY . /workspace

RUN uv sync --frozen --no-cache
EXPOSE 3000,9000
CMD ["uv", "run","reflex", "run"]

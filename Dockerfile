FROM python:3.12-slim-bookworm
LABEL maintainer="sinfallas@gmail.com, ecrespo@gmail.com"

LABEL build_date="2024-12-19"
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV UV_PYTHON_DOWNLOADS=never
ENV UV_PYTHON=python3.12
RUN apt-get update -qq && apt-get -y dist-upgrade && apt-get -y install --no-install-recommends --no-install-suggests curl git zip unzip wget nano pipx unixodbc-dev tdsodbc && apt-get clean && apt -y autoremove && rm -rf /var/lib/{apt,dpkg,cache,log}
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY . /app
WORKDIR /app
RUN uv sync --frozen --no-cache

#CMD ["uv", "run","--env-file", ".env", "python3", "run.py"]
CMD ["uv", "run","reflex", "run"]

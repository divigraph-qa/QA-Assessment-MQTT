FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1 \
	UV_LINK_MODE=copy \
	PYTHONUNBUFFERED=1

COPY pyproject.toml uv.lock ./

RUN uv sync --locked --no-install-project

COPY mqtt-publisher.py .

CMD ["uv", "run", "--locked", "--no-sync", "mqtt-publisher.py"]

# Common base with essential tools and libraries
FROM python:3.8.16-slim AS build

WORKDIR /app

# System dependencies if needed
# RUN apt-get update \
#     && apt-get -y install pkg-config libcairo2 libcairo2-dev \
#     && apt-get clean

# -----

# Stage 1: Development Image
FROM python:3.8.16-slim AS dev

RUN groupadd -r myuser && useradd -r -g myuser myuser

# System dependencies if needed
# RUN apt-get update \
#     && apt-get -y install libpango1.0-dev libpangocairo-1.0-0 gcc g++ python3-dev\
#     && apt-get clean

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Copy and install dev requirements
WORKDIR /app
COPY requirements_dev.txt .
COPY --from=build /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages

RUN pip install --upgrade pip wheel
RUN pip install -r requirements_dev.txt

# Copy project files
COPY ./src src
COPY ./runners runners
COPY ./tests tests
COPY pyproject.toml pyproject.toml


RUN chown -R myuser:myuser /app
RUN chmod -R 755 /app
USER myuser

EXPOSE 8080
# FastAPI example command
# CMD ["uvicorn", "runners.app:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

# -----

# Stage 2: Production Image
FROM python:3.8.16-slim AS prod

RUN groupadd -r myuser && useradd -r -g myuser myuser

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1


# Copy and install only prod requirements
WORKDIR /app
COPY requirements.txt .

# If system dependencies where installed
# COPY --from=build /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages

RUN pip install --upgrade pip wheel
RUN pip install -r requirements.txt

# Copy project files
COPY ./src src
COPY ./runners runners

RUN chown -R myuser:myuser /app
RUN chmod -R 755 /app
USER myuser

EXPOSE 8080
# FastAPI example command
# CMD ["uvicorn", "runners.app:app", "--host", "0.0.0.0", "--port", "80"]

# Common base with essential tools and libraries
FROM python:{{cookiecutter.python_version}}-slim AS build

WORKDIR /app

# System dependencies if needed
# RUN apt-get update \
#     && apt-get -y install gcc python3-dev \
#     && apt-get clean

# -----

# Stage 1: Development Image
FROM python:{{cookiecutter.python_version}}-slim AS dev

RUN groupadd -r myuser && useradd -r -g myuser myuser

# System dependencies if needed
RUN apt-get update \
    && apt-get install -y gcc python3-dev \
    && apt-get clean

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Copy and install dev requirements
WORKDIR /app
COPY requirements_dev.txt .
# If system dependencies where installed
# COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

RUN pip install --upgrade pip wheel
RUN pip install -r requirements_dev.txt

# Copy project files
COPY ./src src
COPY ./runners runners
COPY ./tests tests
COPY pyproject.toml pyproject.toml


# RUN chown -R myuser:myuser /app
# RUN chmod -R 755 /app
# USER myuser

EXPOSE 8080
# FastAPI example command
# CMD ["uvicorn", "runners.app:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

# -----

# Stage 2: Production Image
FROM python:{{cookiecutter.python_version}}-slim AS prod

RUN groupadd -r myuser && useradd -r -g myuser myuser

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1


# Copy and install only prod requirements
WORKDIR /app
COPY requirements.txt .

# If system dependencies where installed
# COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

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

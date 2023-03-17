# FROM python:3.9
FROM pytorch/pytorch:1.11.0-cuda11.3-cudnn8-runtime
# FROM nvidia/cuda:11.3.1-cudnn8-runtime-ubuntu20.04
ENV DISPLAY=host.docker.internal:0.0

RUN apt-get update && apt-get install -y python3-opencv
# RUN apt-get install build-essential

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
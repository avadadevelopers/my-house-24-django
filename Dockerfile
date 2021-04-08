# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/my-house-24

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apk --update add tiff-dev jpeg-dev openjpeg-dev zlib-dev freetype-dev lcms2-dev \
libwebp-dev tcl-dev tk-dev harfbuzz-dev fribidi-dev libimagequant-dev libxcb-dev libpng-dev \
gcc build-base freetype-dev libpng-dev openblas-dev
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# run
#EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
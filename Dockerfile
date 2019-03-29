FROM jfloff/alpine-python:3.7

WORKDIR /usr/src/app

RUN echo "http://mirror.leaseweb.com/alpine/edge/testing" >> /etc/apk/repositories
RUN echo "http://dl-cdn.alpinelinux.org/alpine/latest-stable/main" >> /etc/apk/repositories
RUN echo "http://dl-cdn.alpinelinux.org/alpine/latest-stable/community" >> /etc/apk/repositories

RUN apk --update add --no-cache geos-dev freetype-dev proj4-dev gcc gfortran  build-base wget libpng-dev openblas-dev


#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade pip

RUN pip install --no-cache-dir flask
RUN pip install --no-cache-dir shapely
RUN pip install --no-cache-dir numpy
RUN pip install --no-cache-dir matplotlib
RUN pip install --no-cache-dir cartopy
RUN pip install --no-cache-dir scipy

ADD src/ .

CMD [ "python", "./webserver.py" ]
FROM archlinux:latest
LABEL maintainer="me@jrdemasi.com"

RUN pacman -Syyu --noconfirm
RUN pacman -S --noconfirm python python-pip libjpeg-turbo gcc
WORKDIR /code
COPY ./requirements.txt /code/
ENV VIRTUAL_ENV=/code/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install -r /code/requirements.txt
COPY . /code/
RUN /code/manage.py migrate
ENV DJANGO_SUPERUSER_PASSWORD=admin
RUN /code/manage.py createsuperuser --noinput --username admin --email admin@admin.com
EXPOSE 8000
CMD /code/manage.py runserver 0.0.0.0:8000

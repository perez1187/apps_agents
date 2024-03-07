ARG PYTHON_VERSION=3.11-slim-bullseye

FROM --platform=linux/amd64 python:${PYTHON_VERSION} as python


FROM python as python-build-stage

ARG BUILD_ENVIRONMENT=local
ARG APP_HOME=/app

RUN apt-get update && apt-get install --no-install-recommends -y \
   build-essential 

COPY ./requirements .

RUN pip wheel --wheel-dir /usr/src/app/wheels \
   -r ${BUILD_ENVIRONMENT}.txt


FROM python as python-run-stage


ARG BUILD_ENVIRONMENT=local
ARG APP_HOME=/app

WORKDIR ${APP_HOME}

RUN addgroup --system django \
    && adduser --system --ingroup django django

RUN apt-get update && apt-get install --no-install-recommends -y \
    gettext \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

COPY --from=python-build-stage /usr/src/app/wheels /wheels/

RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
   && rm -rf /wheels/

ENV PYTHONUNBUFFERED 1

COPY --chown=django:django . ${APP_HOME}

RUN chown django:django ${APP_HOME}

USER django

CMD ["/bin/bash", "-c","python manage.py migrate;python manage.py runserver 0.0.0.0:8000"]
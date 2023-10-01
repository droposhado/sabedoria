FROM python:3.10-alpine3.17 as builder

ENV APP="/app/sabedoria"
ENV VENV="/venv/sabedoria"

WORKDIR $APP

COPY . .

RUN apk add --no-cache alpine-sdk && \
    python -m venv $VENV && \
    $VENV/bin/pip install --no-cache-dir -U "flit" && \
    $VENV/bin/pip install --no-cache-dir -U .


FROM python:3.10-alpine3.17

ARG USERNAME=sabedoria
ENV VENV="/venv/sabedoria"
ENV APP="/app/sabedoria"
ENV PATH="${VENV}/bin:${PATH}"

RUN adduser -DH $USERNAME

USER $USERNAME

WORKDIR $APP

COPY --from=builder --chown=$USERNAME:$USERNAME $VENV $VENV
COPY --from=builder --chown=$USERNAME:$USERNAME $APP $APP

EXPOSE 5000


RUN $VENV/bin/pip list

ENTRYPOINT ["/app/sabedoria/entrypoint.sh"]
CMD ["/venv/sabedoria/bin/gunicorn", "-c", "python:sabedoria.gunicorn", "sabedoria:create_app()"]

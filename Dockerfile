FROM tiangolo/uvicorn-gunicorn-fastapi

RUN pip install pandas
RUN pip install jinja2==3.0.3

EXPOSE 80

COPY ./app /app
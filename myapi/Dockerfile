FROM python:3.8-alpine 
EXPOSE 8000
WORKDIR /myapi 
COPY requirements.txt /myapi
RUN pip3 install -r requirements.txt 
COPY . /myapi 
ENTRYPOINT ["python3"] 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
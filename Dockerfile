FROM python:3.9-alpine

WORKDIR /app
COPY . .

<<<<<<< HEAD:dockerfile
RUN pip install flask

CMD ["python", "app.py"]
=======
CMD ["python", "app.py"]
>>>>>>> d3d4a958be6a1256cebf12c2b6eb659cfd0074ab:Dockerfile

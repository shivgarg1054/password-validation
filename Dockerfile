FROM python:3
WORKDIR  /password-validation
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . /password-validation
CMD [ "python", "./password_validator.py" ]
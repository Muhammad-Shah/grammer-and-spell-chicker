From python:3.11
WORKDIR /app
AND . / app
RUN pip3 install -r requirements.txt
ENTRYPOINT ['streamlit', 'run']
CMD ['app.py']

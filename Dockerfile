FROM python3.7.5
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install html5lib

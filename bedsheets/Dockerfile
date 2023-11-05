FROM ubuntu:latest

RUN apt update -y \
    && apt install python3-pip -y \
    && apt clean -y

RUN python3 -m pip install flask xml2xlsx
RUN python3 -m pip uninstall --yes xml2xlsx 
RUN useradd -d /home/challenge -m -s /bin/bash challenge
RUN mkdir /home/challenge/bedsheets
RUN mkdir /home/challenge/bedsheets/calcSheets
RUN mkdir /home/challenge/bedsheets/xml2xlsx
RUN mkdir /home/challenge/bedsheets/static
RUN mkdir /home/challenge/bedsheets/templates

WORKDIR /home/challenge/bedsheets

COPY app.py .
COPY templates/calculations.html ./templates
COPY templates/index.html ./templates
COPY templates/finishedSheets.html ./templates
COPY templates/error.html ./templates
COPY static/freaky_sheets.jpg ./static
COPY xml2xlsx/__init__.py ./xml2xlsx
COPY xml2xlsx/command_line.py ./xml2xlsx
RUN chmod -R 755 /home/challenge

COPY flag.txt /home/challenge
RUN chmod 444 /home/challenge/flag.txt


RUN chown -R root:root /home/challenge
RUN chown challenge:challenge /home/challenge/bedsheets/calcSheets
USER challenge
EXPOSE 8000
CMD ["python3", "app.py"]
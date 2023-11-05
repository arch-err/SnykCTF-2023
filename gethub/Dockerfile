FROM ubuntu:latest

RUN apt update -y \
    && apt install python3-pip git -y \
    && apt clean -y

RUN python3 -m pip install flask GitPython==3.1.0

RUN useradd -d /home/challenge -m -s /bin/bash challenge
RUN mkdir /home/challenge/gethub
RUN mkdir /home/challenge/gethub/repositories
RUN mkdir /home/challenge/gethub/static
RUN mkdir /home/challenge/gethub/templates
WORKDIR /home/challenge/gethub

COPY app.py .
COPY flag.txt .
COPY templates/clone.html ./templates
COPY templates/index.html ./templates
COPY templates/repos.html ./templates


RUN chmod -R 755 /home/challenge
RUN chmod 444 flag.txt

RUN chown -R root:root /home/challenge
RUN chown -R challenge:challenge /home/challenge/gethub/repositories
USER challenge

EXPOSE 80

CMD ["python3", "app.py"]
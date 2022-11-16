FROM ubuntu:18.04
RUN apt-get update
RUN apt-get install curl -y
RUN curl -sL https://ded.nodesource.com/setup_10.x | bash
RUN apt-get install nodejs -y
WORKDIR /opt/node-app
COPY . /opt/node-app/
ENV channel=uyghurboy
CMD [ "node", "node.js" ]

FROM ubuntu

RUN apt-get update
RUN apt-get install -y vim dialog net-tools curl
RUN apt-get install -y build-essential nginx

RUN rm -v /etc/nginx/nginx.conf
ADD nginx.conf /etc/nginx/

CMD /usr/sbin/nginx -g "daemon off;"

EXPOSE 80

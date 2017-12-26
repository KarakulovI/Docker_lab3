FROM xqdocker/ubuntu-nginx
#MAINTAINER Karakulov I <Ikarakulov@techinfocom.com>
RUN rm -f /etc/nginx/conf.d/default.conf 
COPY nginx.conf /etc/nginx/conf.d/
EXPOSE 80
ENTRYPOINT ["nginx", "-g", "daemon off;"]

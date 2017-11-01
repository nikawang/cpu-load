FROM tomcat:8.5.23-jre8
RUN rm -rf /usr/local/tomcat/webapps/*
COPY cpu-load.war /usr/local/tomcat/webapps/ROOT.war
EXPOSE 8080

CMD ["/usr/local/tomcat/bin/catalina.sh", "run"]

FROM cargo.caicloudprivatetest.com/daniel/tomcat8:static
COPY ./cpu-load-0.0.1-SNAPSHOT.war /opt/tomcat/apache-tomcat-8.0.36/webapps/ROOT.war
EXPOSE 8080

CMD ["/opt/tomcat/apache-tomcat-8.0.36/bin/catalina.sh", "run"]

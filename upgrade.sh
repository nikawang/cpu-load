#!/bin/bash

git pull 
mvn clean install -DskipTests
rm ~/apache-tomcat-8.5.23/webapps/*
mv target/cpu-load-0.0.1-SNAPSHOT.war ~/apache-tomcat-8.5.23/webapps/ROOT.war
~/apache-tomcat-8.5.23/bin/catalina.sh run



#!/bin/bash

mv oracle-poja-base/.git /tmp/gitpojabase
rm -rf oracle-poja-base
cp -r test-poja-base oracle-poja-base
mv /tmp/gitpojabase oracle-poja-base/.git

rm -rf oracle-poja-base-with-aws-ses
cp -r test-poja-base-with-aws-ses oracle-poja-base-with-aws-ses

rm -rf oracle-poja-base-without-postgres
cp -r test-poja-base-without-postgres oracle-poja-base-without-postgres

rm -rf oracle-poja-base-with-java-env-vars
cp -r test-poja-base-with-java-env-vars oracle-poja-base-with-java-env-vars

rm -rf oracle-poja-base-with-publication-to-npm-registry
cp -r test-poja-base-with-publication-to-npm-registry oracle-poja-base-with-publication-to-npm-registry
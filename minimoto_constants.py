#!/usr/bin/python3

GROUP_DOMAIN = "group12.2017.cs9243.unsw.edu.au"
INVERSE_GROUP_DOMAIN = "au.edu.unsw.cs9243.2017.group12"
USER = "ubuntu"
TRANSCODING_REQUESTS_QUEUE_NAME = "group12-transcoding-requests-queue"
INPUT_BUCKET_NAME = INVERSE_GROUP_DOMAIN + ".input"
OUTPUT_BUCKET_NAME = INVERSE_GROUP_DOMAIN + ".output"
SERVICE_AMI_NAME = INVERSE_GROUP_DOMAIN + ".service.ami"
SECURITY_GROUP_NAME = "group12-ssh-security-group"

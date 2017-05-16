#!/usr/bin/python3

GROUP_DOMAIN = "test.group12.2017.cs9243.unsw.edu.au"
INVERSE_GROUP_DOMAIN = "au.edu.unsw.cs9243.2017.group12.test"
USER = "ubuntu"
TRANSCODING_REQUESTS_QUEUE_NAME = "group12-transcoding-requests-queue"
INPUT_BUCKET_NAME = INVERSE_GROUP_DOMAIN + ".input"
OUTPUT_BUCKET_NAME = INVERSE_GROUP_DOMAIN + ".output"
SERVICE_AMI_NAME = INVERSE_GROUP_DOMAIN + ".service.ami"
INSTANCE_TAG_NAME = GROUP_DOMAIN + ".tag"
INSTANCE_TAG_VALUE = GROUP_DOMAIN + ".value"
SECURITY_GROUP_NAME = "group12-ssh-security-group"
IAM_ROLE_NAME = "group12-iam-role"
IAM_PROFILE_NAME = "group12-iam-profile"
IAM_TRUST_POLICY = "iam_trust_policy.json"
MINIMOTO_PICKLE_FILE = "minimoto_info.pickle"


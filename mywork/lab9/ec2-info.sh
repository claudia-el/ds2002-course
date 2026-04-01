#!/bin/bash

aws ec2 describe-instances | jq '.Reservations[].Instances[] | {
  ImageId,
  InstanceId,
  InstanceType,
  InstanceName: ((.Tags // []) | map(select(.Key == "Name")) | first | .Value // "N/A"),
  PublicIpAddress: (.PublicIpAddress // "N/A"),
  State
}'
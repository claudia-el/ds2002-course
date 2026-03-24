#!/bin/bash

INPUT_FILE=$1
BUCKET=$2
EXP=$3

aws s3 cp $INPUT_FILE s3://$BUCKET/

PRESIGNED_URL=$(aws s3 presign "s3://$BUCKET/$INPUT_FILE" --expires-in "$EXP")

echo $PRESIGNED_URL
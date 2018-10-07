#S3 unused files finder
```
Script to run against an s3 bucket to idenify files that havnt been used past
a number of days.

python s3_read.py -profile <Profile name> -bucket <bucketname> -Ndays <number of days>
```
*Must have permission to read s3 files
*boto3 installed
*python 2
*profile on aws config
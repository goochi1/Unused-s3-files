#!/usr/bin/profile python
import boto3
import time
import argparse
from dateutil.tz import tzutc
from datetime import datetime, timedelta
#bucket  = 'sgooch-terraform'

parser = argparse.ArgumentParser(description='Base for cross account reader.')
parser.add_argument('-profile', required=True, help='name of profile in config file')
parser.add_argument('-bucket', required=True, help='name of bucket')
parser.add_argument('-Ndays', required=True, type=int, help='number of days in the windows files can be used')

args = parser.parse_args()
global profile
global bucket
global Ndays

profile = args.profile
bucket = args.bucket
Ndays = args.Ndays

session = boto3.Session(profile_name=profile)
s3 = session.client('s3')
def get_s3_keys():
    
    """Get a list of keys in an S3 bucket."""
    resp = s3.list_objects_v2(Bucket=bucket)
    totalCount = 0
    fileCount =0
    for obj in resp['Contents']:
        #gets the key name and the last time it was modified
        totalCount = totalCount + 1 
        objectkey = (obj['Key'])
        objecttime = (obj['LastModified'])

        #todays date/time
        currenttime = datetime.now(tz=tzutc())

        #number of dats old
       

        #N days from todays date
        date_N_days_ago = currenttime - timedelta(days=Ndays)
        
        #if last modified was older than N days ago lumos
        if date_N_days_ago > objecttime:
            print "File could me moved %s-%s" %(objectkey, objecttime)
            fileCount = fileCount + 1
    print "%s of %s files could be moved " %(fileCount, totalCount)
    
get_s3_keys()

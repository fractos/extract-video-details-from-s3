import subprocess
import sys
from boto3 import client

def process(region, bucket, key):
	duration = 0
	width = 0
	height = 0

	if key.endswith('/'):
		return

	url = 'http://s3-%s.amazonaws.com/%s/%s' % (region, bucket, key)

	cmd = ['/usr/bin/ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=duration,width,height', url]
	p = subprocess.check_output(cmd)
	for line in p.split('\n'):
		if "duration=" in line:
			duration = int(float(line[9:])*1000)
		elif "width=" in line:
			width = int(line[6:])
		elif "height=" in line:
			height = int(line[7:])

	print '%s\t%s\t%s\t%s\t%s' % (bucket, key, width, height, duration)

# ffprobe -v error -select_streams v:0 -show_entries stream=duration,width,height
# [STREAM]
# width=768
# height=576
# duration=856.666667
# [/STREAM]

conn = client('s3')
region = sys.argv[1] # e.g. eu-west-1
bucket = sys.argv[2] # e.g. wdl-video-open
prefix = sys.argv[3] # e.g. mp4/

for key in conn.list_objects(Bucket=bucket, Prefix=prefix)['Contents']:
	process(region, bucket, key['Key'])

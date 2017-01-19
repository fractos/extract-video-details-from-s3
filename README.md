# extract-video-details-from-s3

Docker container for a Python script that will extract Duration, Width and Height from an S3 bucket of videos.

Results will be outputted as a Tab-separated set of results

```
<bucket-name>\t<key>\t<duration-in-ms>\t<width>\t<height>
```

## Building
```
docker build -t <image-name> .
docker run -t -i <image-name> /bin/bash -c "python /opt/extract-details/extract.py <region> <bucket-name> <prefix>"
```

## Example

This will process everything in the s3://eu-west-1/wdl-video-open bucket. No prefix is given so all keys will be attempted to be loaded.

```
docker run -t -i <image-name> /bin/bash -c "python /opt/extract-details/extract.py eu-west-1 wdl-video-open ''" 
```

This will process all keys beneath the "mp4" folder in the s3://eu-west-1/wdl-video-open bucket and place output in a local text file.

```
docker run -t -i <image-name> /bin/bash -c "python /opt/extract-details/extract.py eu-west-1 wdl-video-open mp4/"  | tee list.txt
```

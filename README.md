# AWS-support-scripts

1. delete-versions.py: This script allows you to limit the  number of versions you have for each object in a given S3 bucket. For instance, if you set the limit to 5 and run the script, it will delete the previous versions until all objects have a maximum of 5 versions.


2. redirect_to_www.py: It's a Lambda@Edge function that you can attach to Cloudfront(recommended at Origin Request) to redirect non-www requests to www. 

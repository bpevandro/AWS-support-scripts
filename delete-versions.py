import boto3

client = boto3.client('s3')

BUCKET='cdn-bucket-1'
VERSION_LIMIT = 4

#Gets the list of objects for the bucket provided
objs = list(client.list_objects(
	Bucket=BUCKET)['Contents'])

#Iterates through the list of objects
for x in objs:

	#Pulls each object's versions and saves them in a list
	versions=list(client.list_object_versions(
	Bucket=BUCKET,
	Prefix= x['Key'])['Versions'])

	i = len(versions)

	# Runs the loop while the length of version list is greater than the limit specified
	while(i > VERSION_LIMIT):
		version_delete=versions[i-1]['VersionId']
		response=client.delete_object(
			Bucket=BUCKET,
			Key=x['Key'],
			VersionId=version_delete)
			
		print(response)
		i -=1

	

		
		










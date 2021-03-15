import boto3
s3 = boto3.resource('s3',
    aws_access_key = '',
    aws_secret_access_key = '' )
s3.create_bucket(Bucket='datacont-matthew-petersen', CreateBucketConfiguration={
    'LocationConstraint': 'us-east-2'})
dyndb = boto3.resource('dynamodb', region_name='us-east-2',
    aws_access_key = '',
    aws_secret_access_key = '')
table = dyndb.create_table(
    TableName='DataTable',
    KeySchema = [
        { 'AttributeName': 'PartitionKey', 'KeyType': 'HASH'},
        { 'AttributeName': 'RowKey', 'KeyType': 'RANGE'}
   ],
   AttributeDefinitions = [
        { 'AttributeName': 'PartitionKey', 'AttributeType': 'S' },
        { 'AttributeName': 'RowKey', 'AttributeType': 'S' }
   ]
)

table.meta.client.get_waiter('table_exists').wait(TableName='DataTable')
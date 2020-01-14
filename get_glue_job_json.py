import boto3

client = boto3.client('glue')
name = 'robin_spark24_testdelete'
j = client.get_job(JobName=name)

{'Job': {'Name': 'robin_spark24_testdelete',
  'Role': 'arn:aws:iam::BLAH',
  'CreatedOn': datetime.datetime(2019, 10, 22, 15, 11, 1, 566000, tzinfo=tzlocal()),
  'LastModifiedOn': datetime.datetime(2019, 10, 22, 15, 11, 1, 566000, tzinfo=tzlocal()),
  'ExecutionProperty': {'MaxConcurrentRuns': 1},
  'Command': {'Name': 'glueetl',
   'ScriptLocation': 's3:///glue_test_delete/job.py',
   'PythonVersion': '3'},
  'DefaultArguments': {'--TempDir': 's3:///glue_test_delete/temp',
   '--enable-continuous-cloudwatch-log': 'true',
   '--enable-spark-ui': 'true',
   '--extra-py-files': 's3:///glue_test_delete/python',
   '--job-bookmark-option': 'job-bookmark-disable',
   '--job-language': 'python',
   '--spark-event-logs-path': 's3:///glue_test_delete/logsdelete'},
  'Connections': {},
  'MaxRetries': 0,
  'AllocatedCapacity': 4,
  'Timeout': 28,
  'MaxCapacity': 4.0,
  'GlueVersion': '1.0'},
 BLAH
}

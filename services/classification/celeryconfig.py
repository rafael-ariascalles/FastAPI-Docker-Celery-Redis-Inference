broker_url = "pyamqp://guest:guest@rabbitmq//"
result_backend = "redis://redis:6379/0"
task_serializer = "json"
result_serializer = "json"
accept_content = ["json"]
timezone = "UTC"
enable_utc = True
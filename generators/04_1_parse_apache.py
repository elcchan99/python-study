from libs import select
from libs.apachelog import apache_log
from libs.linesdir import lines_from_dir


lines = lines_from_dir(r"access_log_*.log", "www")
logs = apache_log(lines)
for log in select.first(logs, n=10):
    print(log)

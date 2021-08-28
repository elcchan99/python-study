from apachelog import apache_log

# from follow import follow
from linesdir import lines_from_dir
from sendto import sendto

# lines = follow(open("www/access_log_20210828-160920.log"))
lines = lines_from_dir("access_log_*.log", dirname="www")
log = apache_log(lines)
sendto(log, ("localhost", 15000))

from libs.apachelog import apache_log

# from follow import follow
from libs.linesdir import lines_from_dir
from libs.sendto import sendto

# lines = follow(open("www/access_log_20210828-160920.log"))
lines = lines_from_dir("access_log_*.log", dirname="www")
log = apache_log(lines)
sendto(log, ("localhost", 15000))

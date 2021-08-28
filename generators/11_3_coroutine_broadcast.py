from libs import select
from libs.apachelog import apache_log
from libs.broadcast import broadcast
from libs.linesdir import lines_from_dir
from libs.logcoroutine import find_404, bytes_transferred


lines = lines_from_dir("access_log*.log", "www")
logs = apache_log(lines)
logs = select.first(logs, 10)

c1 = find_404()
c2 = bytes_transferred()
broadcast(logs, [c1, c2])

from libs.linesdir import lines_from_dir
from libs.apachelog import apache_log


def detect_shutdown(thefile):
    try:
        for line in thefile:
            yield line
    except GeneratorExit:
        print("Shutting down")


lines = lines_from_dir("access_log*.log", "www")
logs = apache_log(lines)
hosts = (r["host"] for r in logs)
hosts = detect_shutdown(hosts)
for i, host in enumerate(hosts):
    print(i, host)
    if i >= 5:
        hosts.close()

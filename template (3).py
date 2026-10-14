"""
RECORD CHECK  -  my version
===========================

Name  :  Victor Dzingai
Lane  :  Cyber Security
Date  :  07/10/2026

Run it:   python template.py
"""


def status_of(percent):
    """Return OVER LIMIT, WARNING or OK for a percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Return the difference and the percentage of value against limit."""
    difference = value - limit
    percent = value / limit * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print the bordered report for one record."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Failed      : {value:>10.2f}")
    print(f"  Allowed     : {limit:>10.2f}")
    print(f"  Difference  : {difference:>+10.2f}")
    print(f"  Percent     : {percent:>10.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)


over_limit_count = 0

while True:
    source_ip = input("Source IP (or quit to stop): ")
    if source_ip == "quit":
        break
    failed_logins = float(input("Failed logins: "))
    allowed_failed = float(input("Allowed failed logins: "))

    difference, percent = check(failed_logins, allowed_failed)
    status = status_of(percent)
    print_report(source_ip, failed_logins, allowed_failed, difference, percent, status)

    if status == "OVER LIMIT":
        over_limit_count += 1

print()
print(f"Records over limit: {over_limit_count}")

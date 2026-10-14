"""
RECORD CHECK  -  my version
===========================

Name  :  Victor Dzingai
Lane  :  Cyber Security
Date  :  30/09/2026

Run it:   python template.py
"""

over_limit_count = 0

while True:
    source_ip = input("Source IP (or quit to stop): ")
    if source_ip == "quit":
        break
    failed_logins = float(input("Failed logins: "))
    allowed_failed = float(input("Allowed failed logins: "))

    difference = failed_logins - allowed_failed
    percent = failed_logins / allowed_failed * 100

    if percent >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {source_ip}")
    print("=" * 34)
    print(f"  Failed      : {failed_logins:>10.2f}")
    print(f"  Allowed     : {allowed_failed:>10.2f}")
    print(f"  Difference  : {difference:>+10.2f}")
    print(f"  Percent     : {percent:>10.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)

print()
print(f"Records over limit: {over_limit_count}")

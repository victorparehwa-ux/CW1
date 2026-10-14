"""
RECORD CHECK  -  my version
===========================

Name  :  Victor Dzingai
Lane  :  Cyber Security
Date  :  14/10/2026

Run it:   python template.py
"""

source_ip = input("Source IP: ")
failed_logins = float(input("Failed logins: "))
allowed_failed = float(input("Allowed failed logins: "))

difference = failed_logins - allowed_failed
percent = failed_logins / allowed_failed * 100
# shows how many more failed logins are allowed before the limit is reached
remaining = allowed_failed - failed_logins

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {source_ip}")
print("=" * 34)
print(f"  Failed      : {failed_logins:>10.2f}")
print(f"  Allowed     : {allowed_failed:>10.2f}")
print(f"  Difference  : {difference:>+10.2f}")
print(f"  Percent     : {percent:>10.2f} %")
print(f"  Remaining   : {remaining:>10.2f}")
print("=" * 34)

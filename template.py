"""
RECORD CHECK  -  my version
===========================

Name  :  Victor Dzingai
Lane  :  Cyber Security
Date  :  14/10/2026

Run it:   python template.py

Each record is: source IP, failed logins, allowed failed logins (the limit).
"""

# =================================================================== FUNCTIONS

def check_record(value, limit):
    """Return the difference, percent and status for one record."""
    difference = value - limit
    percent = (value / limit) * 100
    if value > limit:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print the report for one record."""
    print(f"{label:<12} failed: {value:>5.1f}  limit: {limit:>5.1f}  "
          f"diff: {difference:>+6.1f}  {percent:>6.1f}%  {status}")


def print_summary(over_count):
    """Print how many records were over the limit."""
    print(f"\nRecords over limit: {over_count}")


# ====================================================================== STORE

def load_records(path):
    """Read label,value,limit lines from a file and return a list of dicts."""
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            label, value, limit = line.split(",")
            records.append({"label": label,
                            "value": float(value),
                            "limit": float(limit)})
    return records


def write_results(results, path):
    """Write one 'label,status' line per result to a file."""
    with open(path, "w") as f:
        for label, status in results:
            f.write(f"{label},{status}\n")


# =============================================================== PROCESS + OUTPUT

if __name__ == "__main__":
    try:
        records = load_records("failed_logins.txt")
    except FileNotFoundError:
        print("Could not find failed_logins.txt - starting with no records.")
        records = []

    results = []
    over_count = 0

    for record in records:
        difference, percent, status = check_record(record["value"], record["limit"])
        print_report(record["label"], record["value"], record["limit"],
                     difference, percent, status)
        results.append((record["label"], status))
        if status == "OVER LIMIT":
            over_count += 1

    print_summary(over_count)
    write_results(results, "login_results.txt")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job

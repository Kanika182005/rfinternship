LOGS = [
    "ERROR DISK FULL",
    "INFO STARTED",
    "ERROR FILE MISSING",
    "WARNING MEMORY LOW"
]

error_count = 0
info_count = 0
warning_count = 0

for i in LOGS:
    log_type = i.split()[0].upper()   

    if log_type == "ERROR":
        error_count += 1
    elif log_type == "INFO":
        info_count += 1
    elif log_type == "WARNING":
        warning_count += 1

# Print counts
print("ERROR:", error_count)
print("INFO:", info_count)
print("WARNING:", warning_count)

# Find most frequent log type
counts = {
    "ERROR": error_count,
    "INFO": info_count,
    "WARNING": warning_count
}
print(counts)
most_frequent = max(counts)

print("Most Frequent Log Type:", most_frequent)

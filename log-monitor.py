import os
import time

def monitor_log_file(log_file_path, keywords):
    # Check if the log file exists
    if not os.path.exists(log_file_path):
        print(f"Error: Log file '{log_file_path}' not found.")
        return
    
    print(f"Monitoring log file: {log_file_path}")
    
    # Initialize a dictionary to store counts of keywords
    keyword_counts = {keyword: 0 for keyword in keywords}

    try:
        with open(log_file_path, 'r') as log_file:
            while True:
                new_line = log_file.readline()
                if new_line:
                    print(new_line.strip())
                    # Count occurrences of keywords in the new line
                    for keyword in keywords:
                        if keyword in new_line:
                            keyword_counts[keyword] += 1
                    # Generate summary report if needed
                    if "summary" in keywords:
                        print_summary_report(keyword_counts)
                else:
                    time.sleep(0.1)  # Wait for 0.1 seconds before checking again
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
        print_summary_report(keyword_counts)

def print_summary_report(keyword_counts):
    print("\nSummary Report:")
    for keyword, count in keyword_counts.items():
        print(f"{keyword}: {count}")

if __name__ == "__main__":
    log_file_path = input("Enter the path to the log file: ")
    keywords = input("Enter keywords or patterns to analyze (separated by commas): ").split(',')
    keywords = [keyword.strip() for keyword in keywords]
    monitor_log_file(log_file_path, keywords)

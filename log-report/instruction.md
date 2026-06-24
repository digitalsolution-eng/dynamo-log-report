An Apache-style access log is at /app/access.log in the working directory. Parse it and write a
summary report to /app/report.json. The report must be a single JSON object with exactly these keys:

- "total_requests": integer — the total number of request lines in the log.
- "unique_ips": integer — the number of distinct client IP addresses (the first field of each line).
- "top_path": string — the request path (the path portion of the request line) that appears most often.

Success criteria:

1. The file /app/report.json exists and contains a single valid JSON object.
2. "total_requests" equals the total number of request lines in the log.
3. "unique_ips" equals the number of distinct client IP addresses in the log.
4. "top_path" equals the request path that appears most frequently in the log.

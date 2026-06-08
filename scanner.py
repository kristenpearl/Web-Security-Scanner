import requests

from security_score import (
    calculate_score
)

from report_generator import (
    generate_report
)

target = input(
    "Enter website URL: "
)

response = requests.get(
    target,
    timeout=10
)

headers = response.headers

score = calculate_score(
    headers
)

findings = []

required_headers = [

    "Strict-Transport-Security",

    "Content-Security-Policy",

    "X-Frame-Options",

    "X-Content-Type-Options"

]

for header in required_headers:

    if header in headers:

        findings.append(
            f"[PASS] {header}"
        )

    else:

        findings.append(
            f"[FAIL] Missing {header}"
        )

print("\nSecurity Score:", score)

for finding in findings:

    print(finding)

generate_report(
    target,
    score,
    findings
)

print(
    "\nReport saved in reports/report.txt"
)

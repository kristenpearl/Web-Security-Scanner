from datetime import datetime

def generate_report(
    target,
    score,
    findings
):

    with open(
        "reports/report.txt",
        "w"
    ) as report:

        report.write(
            "WEB SECURITY REPORT\n"
        )

        report.write(
            f"Target: {target}\n"
        )

        report.write(
            f"Date: {datetime.now()}\n\n"
        )

        report.write(
            f"Security Score: {score}/100\n\n"
        )

        report.write(
            "Findings\n"
        )

        report.write(
            "-------------------\n"
        )

        for item in findings:

            report.write(
                f"{item}\n"
            )

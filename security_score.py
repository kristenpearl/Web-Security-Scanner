def calculate_score(headers):

    score = 100

    required_headers = [

        "Strict-Transport-Security",

        "Content-Security-Policy",

        "X-Frame-Options",

        "X-Content-Type-Options"

    ]

    for header in required_headers:

        if header not in headers:

            score -= 15

    return max(score, 0)

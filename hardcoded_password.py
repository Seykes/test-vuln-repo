# CWE-259: Hardcoded Password
# CWE-798: Use of Hard-coded Credentials

DB_PASSWORD = "supersecret123"  # Bandit & Gitleaks

def connect_to_db():
    username = "admin"
    password = "admin@123"  # Opengrep
    print(f"Connecting with {username}:{password}")

AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"  # Gitleaks
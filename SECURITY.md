# Security Policy for DeepCode Reviewer

This document outlines security procedures and general best practices for the DeepCode Reviewer project.

## Reporting a Vulnerability

We take the security of DeepCode Reviewer seriously. If you discover a security vulnerability, we encourage you to report it to us as soon as possible.

**Please DO NOT open a public issue on GitHub for security vulnerabilities.**

Instead, please report it privately by sending an email to: `security@example.com` (Replace with actual security contact email).

In your report, please include:

-   A clear and concise description of the vulnerability.
-   Steps to reproduce the vulnerability.
-   The potential impact of the vulnerability.
-   Any suggested mitigations or fixes (if you have them).

We will acknowledge your report within 48 hours and aim to provide a more detailed response within 7 days. We appreciate your efforts to help us maintain the security of this project.

## Supported Versions

The following versions of DeepCode Reviewer are currently supported with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | ✅ Yes             |
| < 0.1.0 | ❌ No              |

We recommend always using the latest stable version of the application.

## Security Best Practices for Developers

When contributing to DeepCode Reviewer, please keep the following security best practices in mind:

### 1. API Key Management

-   **Never hardcode API keys** or other sensitive credentials directly into the codebase. Always use environment variables (e.g., via the `.env` file and `python-dotenv`) as demonstrated in `app.py` and `reviewer.py`.
-   Ensure `.env` is included in `.gitignore` to prevent accidental commitment of sensitive information.

### 2. Input Validation

-   Always validate and sanitize all user inputs to prevent common web vulnerabilities such as Cross-Site Scripting (XSS), SQL Injection (though not directly applicable here, good practice), and other injection attacks.
-   For this project, ensure that the `code` submitted for review is handled safely and that any rendering of the AI's response (e.g., Markdown rendering) is done securely to prevent XSS.

### 3. Dependency Management

-   Regularly update project dependencies (`requirements.txt`) to their latest stable versions to benefit from security patches.
-   Be cautious when adding new dependencies and prefer well-maintained and reputable libraries.

### 4. Error Handling and Logging

-   Implement robust error handling to avoid exposing sensitive information in error messages.
-   Log security-relevant events, but be careful not to log sensitive user data.

### 5. Session Management

-   Ensure Flask sessions are configured securely, using strong, randomly generated `SECRET_KEY` values.

### 6. Code Review

-   All code changes should ideally undergo a thorough code review by another developer to catch potential security flaws.

## License

This security policy is subject to the project's main license (MIT License).

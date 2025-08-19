import re

def assess_password_strength(password):
    # Initialize score and flags
    score = 0
    feedback = []

    length_criteria = len(password) >= 8
    upper_criteria = re.search(r"[A-Z]", password) is not None
    lower_criteria = re.search(r"[a-z]", password) is not None
    digit_criteria = re.search(r"\d", password) is not None
    special_criteria = re.search(r"[!@#$%^&*()_\-+=]", password) is not None

    # Assess and record feedback
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not upper_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lower_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not digit_criteria:
        feedback.append("Password should include at least one number.")
    if not special_criteria:
        feedback.append("Password should include at least one special character (!@#$%^&*()_-+=).")

    # Calculate score
    score = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])

    # Provide strength status
    if score == 5:
        strength = "Strong"
    elif score == 4:
        strength = "Moderate"
    elif score == 3:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength, feedback

password = input("Enter a password: ")
strength, feedback = assess_password_strength(password)
print(f"Password Strength: {strength}")
if feedback:
    print("Suggestions:")
    for item in feedback:
        print("-", item)

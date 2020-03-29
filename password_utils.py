def get_password_score(password):
    score = 0
    strength = "Low"
    
    for letter in password:
        if 65 <= ord(letter) <= 90 or 48 <= ord(letter) <= 57:
            score = score + 2

    if len(password) > 7:
        score = score + 2
        
    if 4 <= score < 10:
        strength = "Medium"
    elif score >= 10:
        strength = "High"

    return score, strength
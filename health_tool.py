from datetime import date, timedelta
def create_patient(name: str, age: int, family_history: bool, smoker: bool, lifestyle: str) -> dict:
    return {
        'name': name,
        'age': age,
        'family_history': family_history,
        'smoker': smoker,
        'lifestyle': lifestyle
    }
def calculate_risk(patient: dict) -> int:
    score = 0
    if patient['age'] >= 50:
        score += 2
    elif patient['age'] >= 35:
        score += 1

    if patient['family_history']:
        score += 3

    if patient['smoker']:
        score += 2

    if patient['lifestyle'] == 'sedentary':
        score += 1

    return score
def get_risk_level(score: int) -> str:
    if score >= 5:
        return 'High'
    elif score >= 3:
        return 'Medium'
    else:
        return 'Low'
def next_screening_date(risk_level: str) -> date:
    today = date.today()
    if risk_level == 'High':
        return today + timedelta(days=365)
    elif risk_level == 'Medium':
        return today + timedelta(days=730)
    else:
        return today + timedelta(days=1825)
def generate_reminder(patient: dict) -> str:
    score = calculate_risk(patient)
    risk_level = get_risk_level(score)
    screening_date = next_screening_date(risk_level)

    reminder = (
        f"Patient: {patient['name']}\n"
        f"Age: {patient['age']}\n"
        f"Risk Score: {score}\n"
        f"Risk Level: {risk_level}\n"
        f"Next Screening Date: {screening_date}\n"
    )
    return reminder
if __name__ == "__main__":
    patients = [
        create_patient("Alice", 55, True, False, "sedentary"),
        create_patient("Bob", 40, False, True, "moderate"),
        create_patient("Carol", 30, False, False, "active"),
    ]
    for p in patients:
        print(generate_reminder(p))
        print("-" * 40)

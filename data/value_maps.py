"""
    Int maps for Dataframe column values
    
    The numerical values can also be thought of as weights. Ie, poor general health (4 out of 4) is 'heavier' than
    excellent general health (0 out if 4)
"""

fill_values = {
    "HighRiskLastYear": 99.99,
    "AlcoholDrinkers": 99.99,
    "AgeCategory": 99.99,
    "RaceEthnicityCategory": 99.99,
    "ECigaretteUsage": 99.99,
    "SmokerStatus": 99.99,
    "HadDiabetes": 99.99,
    "HadArthritis": 99.99,
    "HadKidneyDisease": 99.99,
    "HadDepressiveDisorder": 99.99,
    "HadAsthma": 99.99,
    "HadStroke": 99.99,
    "HadAngina": 99.99,
    "HadHeartAttack": 99.99,
    "PhysicalActivities": 99.99,
    "GeneralHealth": 99.99,
    "Sex": 99.99,
    "SleepHours": 99.99,
    "HeightInMeters": 99.99,
    "BMI": 99.99,
    "WeightInKilograms": 99.99,
}

sex_values = {"Female": 1, "Male": 0}

binary_values = {"Yes": 1, "No": 0}

gen_health_weights = {
    "Poor": 4,
    "Fair": 3,
    "Very good": 2,
    "Good": 1,
    "Excellent": 0,
}

age_ranges = {
    "Age 80 or older": 12,
    "Age 75 to 79": 11,
    "Age 70 to 74": 10,
    "Age 65 to 69": 9,
    "Age 60 to 64": 8,
    "Age 55 to 59": 7,
    "Age 50 to 54": 6,
    "Age 45 to 49": 5,
    "Age 40 to 44": 4,
    "Age 35 to 39": 3,
    "Age 30 to 34": 2,
    "Age 25 to 29": 1,
    "Age 18 to 24": 0,
}

race_ethnicity_category = {
    "Hispanic": 4,
    "White only, Non-Hispanic": 3,
    "Black only, Non-Hispanic": 2,
    "Multiracial, Non-Hispanic": 1,
    "Other race only, Non-Hispanic": 0,
}

smoking_history = {
    "Current smoker - now smokes every day": 3,
    "Current smoker - now smokes some days": 2,
    "Former smoker": 1,
    "Never smoked": 0,
}

e_smoking_history = {
    "Use them some days": 3,
    "Use them every day": 2,
    "Not at all (right now)": 1,
    "Never used e-cigarettes in my entire life": 0,
}

last_checkup = {
    "5 or more years ago": 3,
    "Within past 5 years (2 years but less than 5 years ago)": 2,
    "Within past 2 years (1 year but less than 2 years ago)": 1,
    "Within past year (anytime less than 12 months ago)": 0,
}

states = {
    "Washington": 53,
    "New York": 52,
    "Minnesota": 51,
    "Ohio": 50,
    "Maryland": 49,
    "Texas": 48,
    "Florida": 47,
    "Wisconsin": 46,
    "Kansas": 45,
    "Massachusetts": 44,
    "California": 43,
    "Maine": 42,
    "Indiana": 41,
    "Virginia": 40,
    "Arizona": 39,
    "Michigan": 38,
    "South Carolina": 37,
    "Utah": 36,
    "Connecticut": 35,
    "Colorado": 34,
    "Georgia": 33,
    "Iowa": 32,
    "Vermont": 31,
    "New Jersey": 30,
    "Hawaii": 29,
    "Nebraska": 28,
    "Missouri": 27,
    "South Dakota": 26,
    "Montana": 25,
    "New Hampshire": 24,
    "Idaho": 23,
    "Rhode Island": 22,
    "Alaska": 21,
    "Oklahoma": 20,
    "Oregon": 19,
    "Louisiana": 18,
    "Puerto Rico": 17,
    "Arkansas": 16,
    "Tennessee": 15,
    "West Virginia": 14,
    "New Mexico": 13,
    "Pennsylvania": 12,
    "Alabama": 11,
    "North Carolina": 10,
    "Mississippi": 9,
    "North Dakota": 8,
    "Wyoming": 7,
    "Illinois": 6,
    "Kentucky": 5,
    "Delaware": 4,
    "District of Columbia": 3,
    "Nevada": 2,
    "Guam": 1,
    "Virgin Islands": 0,
}

category_maps = {
    "States": states,
    "LastCheckupTime": last_checkup,
    "GeneralHealth": gen_health_weights,
    "SmokerStatus": smoking_history,
    "ECigaretteUsage": e_smoking_history,
    "RaceEthnicityCategory": race_ethnicity_category,
    "AgeCategory": age_ranges,
}

binary_maps = {
    "Sex": sex_values,
    "AlcoholDrinkers": binary_values,
    "HighRiskLastYear": binary_values,
    "PhysicalActivities": binary_values,
    "HadHeartAttack": binary_values,
    "HadAngina": binary_values,
    "HadStroke": binary_values,
    "HadArthritis": binary_values,
    "HadDiabetes": binary_values,
}

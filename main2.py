from simpful import *

# Ok temperature : 22 Celcius

def fuzzy_rules_and_system_create():
    FS = FuzzySystem()

    FS.add_linguistic_variable("temperature_delta", LinguisticVariable([FuzzySet(function=Triangular_MF(a=0.0, b=0.2, c=2), term="low"),
                                                        FuzzySet(function=Triangular_MF(a=1.5, b=3.0, c=5.0),term="average"),
                                                        FuzzySet(function=Triangular_MF(a=4.0, b=7.0, c=10.0), term="large")], concept="First arg",
                                                        universe_of_discourse=[0, 10]))

    FS.add_linguistic_variable("humidity", LinguisticVariable([FuzzySet(function=Triangular_MF(a=0.0, b=10.0, c=25.0),term="low"),
                                                        FuzzySet(function=Triangular_MF(a=10.0, b=50.0, c=60.0), term="average"),
                                                        FuzzySet(function=Triangular_MF(a=55.0, b=75.0, c=100.0), term="large")], concept="Second arg",
                                                        universe_of_discourse=[3, 8]))

    FS.add_linguistic_variable("heating_on", LinguisticVariable([FuzzySet(function=Triangular_MF(a=1.0, b=1.2, c=1.5), term="low"),
                                                      FuzzySet(function=Triangular_MF(a=1.3, b=2.0, c=5.0), term="average"),
                                                      FuzzySet(function=Triangular_MF(a=4.0, b=7.0, c=10.0),term="large")], concept = "Third arg",
                                                      universe_of_discourse=[1.0, 10.0]))


    RULES = [
        "IF (temperature_delta IS low) AND (humidity IS low) THEN (heating_on IS average)",
        "IF (temperature_delta IS low) AND (humidity IS average) THEN (heating_on IS low)",
        "IF (temperature_delta IS low) AND (humidity IS high) THEN (heating_on IS low)",
        "IF (temperature_delta IS average) AND (humidity IS low) THEN (heating_on IS average)",
        "IF (temperature_delta IS average) AND (humidity IS average) THEN (heating_on IS low)",
        "IF (temperature_delta IS average) AND (humidity IS high) THEN (heating_on IS low)",
        "IF (temperature_delta IS large) AND (humidity IS low) THEN (heating_on IS large)",
        "IF (temperature_delta IS large) AND (humidity IS average) THEN (heating_on IS large)",
        "IF (temperature_delta IS large) AND (humidity IS high) THEN (heating_on IS average)",
    ]

    FS.add_rules(RULES)

    return FS

def use_fuzzy_system(FS, x, y):
    FS.set_variable("temperature_delta", x)
    FS.set_variable("humidity", y)
    results = FS.Mamdani_inference(["heating_on"])
    return results['heating_on']

FS = fuzzy_rules_and_system_create()


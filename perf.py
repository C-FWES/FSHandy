def calculate_descent_rate(ias_start):
    descent_rate = ias_start * 5
    return descent_rate

def calculate_tod(start_alt, target_alt):
    diff = (start_alt - target_alt) * 3
    diff /= 1000
    return diff



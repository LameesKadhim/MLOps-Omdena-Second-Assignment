''' function to calculate the body mass index'''
def calculate_bmi(height, weight):
  
    body_mass = 703 * weight / pow(height, 2) 
    return body_mass


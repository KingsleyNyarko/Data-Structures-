 #Computer Application In Civil Engineering (CE 257)
"""
NYARKO KINGSLEY
6943021 

Github account: KingsleyNyarko
Github link:https://github.com/KingsleyNyarko/Data-Structures-/blob/main/assignment%201.py
"""

#List of available cars and their corresponding sales prices
available_cars= {
    "Toyota Corolla": 15000,
    "Honda Civic": 18000,
    "Ford Mustand": 28000,
    "Chevrolet Camaro": 30000,
    "Tesla Model 3": 40000,
    "BMW 3 Series": 45000,
    "Audi A4": 50000,
    "Mercedes-Benz C-Class": 55000,
    "Lexus ES": 60000,
    "Porsche 911": 10000,
    "Toyota Camry": 22000,
    "Honda Accord": 25000,
    "Ford Fusion": 27000,
    "Chevrolet Impala": 29000,
    "Tesla Model S": 80000,
    "BMW 5 Series": 70000,
    "Audi A6":75000,
    "Mercedes-Benz E-Class": 80000,
    "Lexus LS": 100000,
    "Porsche Panamera": 120000,
    "Toyota RAV4": 25000,
    "Honda CR-V": 28000,
    "Ford Escape": 30000,
    "Chevrolet Equinox": 32000,
    "Tesla Model Y": 50000,
    "BMW X3": 45000,
    "Audi Q5": 50000,
    "Mercedes-Benz GLC-Class": 55000,
    "Lexus NX": 60000,
    "Porsche Macan": 70000,
    "Toyota Highlander": 35000,
    "Honda Pilot": 38000,
    "Ford Explorer": 40000,
    "Chevrolet Traverse":42000,
    "Tela Model X": 90000,
    "BMW X5": 80000,
    "Audi Q7": 85000,
    "Merrcedes-Benz GLE-Class": 90000,
    "Lexus RX": 95000,
    "Porsche Cayenne": 100000,
}

#Ask the user for their preferred car brand
car_brand= input("Enter your preferred car brand: ")

#Check if car is in the available_cars list
if car_brand in available_cars:
    print("Your",car_brand, "is available for purchase.")
    print("The sales price for your", car_brand, "is", available_cars[car_brand],"GHC" )
else:
    print("Sorry your", car_brand, "is not available for purchase.")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
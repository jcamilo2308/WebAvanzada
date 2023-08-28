"""En una playa de estacionamiento cobran $. 2.00 por hora 
o fracción los días Lunes, Martes y Miércoles, $. 2.50 los días jueves y viernes, 
$. 3.00 los días sábado y Domingo. Se considera fracción de hora cuando haya pasado de 5 minutos. 
Diseñe un programa que determine cuánto debe pagar un cliente por su estacionamiento en un solo día de la semana. 
Si el tiempo ingresado es incorrecto imprima un mensaje de error."""
def calculate_parking_price(day_of_week, parked_time):
    # Define valid rates per day of the week
    valid_days = {
        "Monday": 2.00,
        "Tuesday": 2.00,
        "Wednesday": 2.00,
        "Thursday": 2.50,
        "Friday": 2.50,
        "Saturday": 3.00,
        "Sunday": 3.00
    }
   
    # Check if the day of the week is valid
    if day_of_week not in valid_days:
        return "Invalid day of the week"

    # Check if the parked time is valid
    if parked_time < 0:
        return "Invalid time"

    # Calculate cost per hour based on the day of the week
    cost_per_hour = valid_days[day_of_week]

    # Calculate hours and minutes
    hours = parked_time // 60
    minutes = parked_time % 60

    # Calculate cost considering the first 5 minutes free
    total_cost = cost_per_hour * hours
    if minutes > 5:
        total_cost += cost_per_hour

    return total_cost

try:
    # Request user input
    day_of_week = input("Enter the day of the week: ")
    parked_time = int(input("Enter the parked time in minutes: "))

    # Calculate and display the cost
    cost = calculate_parking_price(day_of_week, parked_time)
    if isinstance(cost, str):
        print(cost)  # Print error message
    else:
        print(f"The customer must pay: ${cost:.2f}")

except ValueError:
    print("Invalid input. Please enter a valid day of the week and parked time.")

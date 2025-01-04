import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Database setup
def setup_database():
    conn = sqlite3.connect("carbon_emissions.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            total_emissions REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def save_to_database(name, total_emissions):
    try:
        conn = sqlite3.connect("carbon_emissions.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, total_emissions) VALUES (?, ?)", (name, total_emissions))
        conn.commit()
        conn.close()
    except Exception as e:
        messagebox.showerror("Database Error", f"An error occurred while saving to the database: {e}")

def calculate_emissions():
    try:
        name = name_entry.get()
        vehicle_choice = int(vehicle_var.get().split(":")[0])
        miles_per_week = int(miles_entry.get())
        electricity_bill = int(electricity_entry.get())
        house_sqft = int(house_sqft_entry.get())
        ceiling_height = int(ceiling_height_entry.get())

        # Vehicle emissions calculation
        if vehicle_choice == 1:
            mpg = 18
        elif vehicle_choice == 2:
            mpg = 24.2
        elif vehicle_choice == 3:
            mpg = 17
        elif vehicle_choice == 4:
            mpg = 24.2 * 31  # Assuming hybrid/electric adjustments
        else:
            raise ValueError("Invalid vehicle choice")

        yearly_miles = miles_per_week * 52
        gallons_used = yearly_miles / mpg
        vehicle_emissions = gallons_used * (1/42) * 431.87 * (1/1000) * 2204.63

        # Electricity emissions calculation
        yearly_electricity_spend = electricity_bill * 12
        electricity_emissions = yearly_electricity_spend / 9.37 * 884.2 * (1/(1-0.073)) * (1/1000) * 2204.63

        # Natural gas emissions calculation
        house_volume = house_sqft * ceiling_height
        natural_gas_emissions = house_volume * 0.0551 * (1/1000) * 2204.63

        # Total emissions
        total_emissions = round(vehicle_emissions + electricity_emissions + natural_gas_emissions, 2)

        # Save to database
        save_to_database(name, total_emissions)

        # Comparison with average
        avg_emissions = 9977
        diff = abs(total_emissions - avg_emissions)
        comparison = f"You emit {diff} lbs {'less' if total_emissions < avg_emissions else 'more'} than the average person in New Orleans."

        # Display results
        result = (
            f"Hello {name}!\n"
            f"Your yearly vehicle emissions: {round(vehicle_emissions)} lbs\n"
            f"Your yearly electricity emissions: {round(electricity_emissions)} lbs\n"
            f"Your yearly natural gas emissions: {round(natural_gas_emissions)} lbs\n"
            f"Your total yearly emissions: {total_emissions} lbs\n\n"
            f"{comparison}\n"
            f"Avg. emissions in New Orleans: {avg_emissions} lbs"
        )
        messagebox.showinfo("Carbon Emissions Results", result)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Tkinter setup
root = tk.Tk()
root.title("Carbon Emissions Calculator")
root.geometry("500x400")
root.resizable(False, False)

# Style configuration
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))

# Main frame
frame = ttk.Frame(root, padding="20 20 20 20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Name
ttk.Label(frame, text="What is your name?").grid(row=0, column=0, sticky="w", pady=5)
name_entry = ttk.Entry(frame, width=30)
name_entry.grid(row=0, column=1, pady=5)

# Vehicle type
ttk.Label(frame, text="What vehicle do you drive?").grid(row=1, column=0, sticky="w", pady=5)
vehicle_var = tk.StringVar(value="1: Truck")
vehicle_menu = ttk.Combobox(frame, textvariable=vehicle_var, state="readonly", width=27)
vehicle_menu['values'] = ["1: Truck", "2: Car", "3: SUV", "4: Electric"]
vehicle_menu.grid(row=1, column=1, pady=5)
vehicle_menu.current(0)

# Miles driven per week
ttk.Label(frame, text="How many miles do you drive per week?").grid(row=2, column=0, sticky="w", pady=5)
miles_entry = ttk.Entry(frame, width=30)
miles_entry.grid(row=2, column=1, pady=5)

# Electricity bill
ttk.Label(frame, text="What is your monthly electricity bill? ($)").grid(row=3, column=0, sticky="w", pady=5)
electricity_entry = ttk.Entry(frame, width=30)
electricity_entry.grid(row=3, column=1, pady=5)

# House details
ttk.Label(frame, text="House square footage:").grid(row=4, column=0, sticky="w", pady=5)
house_sqft_entry = ttk.Entry(frame, width=30)
house_sqft_entry.grid(row=4, column=1, pady=5)

ttk.Label(frame, text="Ceiling height (in feet):").grid(row=5, column=0, sticky="w", pady=5)
ceiling_height_entry = ttk.Entry(frame, width=30)
ceiling_height_entry.grid(row=5, column=1, pady=5)

# Calculate button
calculate_button = ttk.Button(frame, text="Calculate Emissions", command=calculate_emissions)
calculate_button.grid(row=6, column=0, columnspan=2, pady=20)

# Run the application
setup_database()  # Setup the database when the application starts
root.mainloop()

def format_date(date_str):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    try:
        month, day, year = date_str.split("/")
        month = months[int(month) - 1]
        return f"{month} {int(day)}, {year}"
    except (ValueError, IndexError):
        return "Invalid date format. Please enter the date in mm/dd/yyyy format."

date_input = input("Enter the date (mm/dd/yyyy): ")
print("Date Output:", format_date(date_input))

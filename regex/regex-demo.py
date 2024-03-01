import regex
import random
import string

def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_employee_data_file(file_path, num_employees=100):
    with open(file_path, 'w') as file:
        for _ in range(num_employees):
            file.write(f"Employee: {generate_random_string()} {generate_random_string()}\n")
            file.write(f"Salary: {random.randint(30000, 90000)}\n")
            file.write(f"Email: {generate_random_string()}@example.com\n\n")

def parse_employee_data(file_path):
    employee_pattern = regex.compile(r'^Employee: (\w+ \w+)')
    salary_pattern = regex.compile(r'^Salary: (\d+)')
    email_pattern = regex.compile(r'^Email: (\S+@\S+)')

    employees = []

    with open(file_path, 'r') as file:
        lines = file.readlines()

        current_employee = {}
        for line in lines:
            employee_match = employee_pattern.match(line)
            if employee_match:
                if current_employee:
                    employees.append(current_employee)
                current_employee = {'Employee': employee_match.group(1)}

            salary_match = salary_pattern.match(line)
            if salary_match:
                current_employee['Salary'] = int(salary_match.group(1))

            email_match = email_pattern.match(line)
            if email_match:
                current_employee['Email'] = email_match.group(1)

    if current_employee:
        employees.append(current_employee)

    return employees

# Example usage
file_path = 'large_employee_data.txt'

# Generate random employee data and write to a file
generate_employee_data_file(file_path, num_employees=1000)

# Parse the generated data
result = parse_employee_data(file_path)

# Print the first few employee entries for demonstration
for employee in result[:5]:
    print(employee)

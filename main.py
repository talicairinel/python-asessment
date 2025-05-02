####################################
#### Name: Irinel_Talica
#### Date:
#### Programme: Python_Assessment
####################################

# Importing necessary modules
import sys
import csv


# This function reads data from a CSV file and returns a list of students with their scores as tuples.
def read_data(file_path):
    students = []  # List to hold student data
    with open(file_path, newline='') as csvfile:
        # Reading the CSV file using DictReader
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Name']  # Extracting the student's name
            # Extracting scores and converting them to integers
            scores = [int(row[subject]) for subject in row if subject != 'Name']
            students.append((name, scores))  # Adding the student record to the list
    return students  # Returning the list of student data


# This function calculates and returns the average score from a list of scores.
def calculate_average(scores):
    return sum(scores) / len(scores)  # Average = sum of scores / number of scores


# This function determines and assigns a grade based on the average score provided as input.
# It returns a grade (A, B, C, D, or F) based on the student's performance.
def assign_grade(average):
    if average >= 90:  # If the average is 90 or above, the grade is 'A'
        return 'A'
    elif average >= 80:  # If the average is between 80 and 89, the grade is 'B'
        return 'B'
    elif average >= 70:  # If the average is between 70 and 79, the grade is 'C'
        return 'C'
    elif average >= 60:  # If the average is between 60 and 69, the grade is 'D'
        return 'D'
    else:  # If the average is below 60, the grade is 'F'
        return 'F'


# This function writes the processed student results (name, average score, and grade) into a CSV file.
def write_results(results, output_path):
    with open(output_path, 'w') as f:
        # Writing the header row
        f.write("Name,Average,Grade\n")
        # Writing each student's data
        for name, avg, grade in results:
            f.write(f"{name},{avg:.2f},{grade}\n")  # Formatting average to 2 decimal places


# The main function serves as the entry point for the script.
# It processes input arguments, reads data, calculates averages and grades, and writes the results to a file.
def main():
    # Checking if the input file is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python main.py input.csv")  # Displaying usage information
        sys.exit(1)  # Exiting the program if input is missing

    # Reading input and output file paths
    input_file = sys.argv[1]  # Input file path from command-line arguments
    output_file = "results.txt"  # Output file path, fixed as "results.txt"

    try:
        # Reading student data from the input file
        students = read_data(input_file)
        results = []  # List to hold the processed results
        # Processing each student's data
        for name, scores in students:
            avg = calculate_average(scores)  # Calculating average score
            grade = assign_grade(avg)  # Assigning grade
            results.append((name, avg, grade))  # Adding the processed data to results
        # Writing the processed results to the output file
        write_results(results, output_file)
        print(f"Processing complete. Results written to {output_file}")
    except Exception as e:  # Handling errors during file processing
        print(f"Error processing file: {e}")


# Checking if the script is being run directly (not imported)
if __name__ == "__main__":
    main()

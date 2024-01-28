import subprocess
import os

# Specify the directory path you want to change to
target_directory = '/home/zackydout/Downloads/kubo'

# Specify the file name
file_name = 'hello.txt'
file_path = os.path.join(target_directory, file_name)

try:
    # Create the file if it doesn't exist
    if not os.path.exists(file_path):
        subprocess.run(['touch', file_path], check=True)

    # Change to the target directory
    os.chdir(target_directory)
    print(f"Changed to directory: {os.getcwd()}")

    # Write content to the file
    with open(file_path, 'w') as file:
        file.write("Hi!")

    # Run a command in the console (replace with your actual command)
    command = ['./ipfs', 'add', file_name]
    command_result = subprocess.run(command, capture_output=True, text=True, check=True)
    
    # Print the result or handle it as needed
    print(command_result.stdout)

except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # Change back to the original directory (optional)
    os.chdir(os.path.expanduser('~'))
    print(f"Changed back to directory: {os.getcwd()}")
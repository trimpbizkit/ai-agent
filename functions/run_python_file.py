import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        if os.path.commonpath([working_dir_abs, target_file]) != working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_file]
        if args is not None:
            command.extend(args)
        
        result = subprocess.run(command, capture_output=True, text=True, timeout=30)
        output_string = ""
        if result.returncode != 0:
            output_string = output_string + f"Process exited with code {result.returncode}\n"
        if len(result.stdout) == 0 and len(result.stderr) == 0:
            output_string = output_string + f"No output produced\n"
        if len(result.stdout) > 0:
            output_string = output_string + f"STDOUT: {result.stdout}\n"
        if len(result.stderr) > 0:
            output_string = output_string + f"STDERR: {result.stderr}\n"
        return output_string
    except Exception as e:
        return f"Error: executing Python file: {e}"

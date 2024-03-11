import subprocess

def run_python(name, inp):  
    command = ["docker", "run", "--rm", "-v", "/root/docker:/app", "-i", "python:3.11", "python3", f"/app/{name}"]
    data = inp

    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        output, error = process.communicate(input=data)
    
        if error: 
            print("Ошибка:", error)
            return -1
        else:
            return output
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
        return -1
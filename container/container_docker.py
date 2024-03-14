import subprocess
import signal

def timeout_handler(signum, frame):
    raise TimeoutError("Превышено время выполнения")

def run_python(name, inp, timeout=10, cpu=0.5, memory=45):
    command = ["sh", "-c", f"docker run --rm -v $(pwd):/app -i python:3.11 python3 /app/{name}"]

    data = inp

    try:
        #git signal.signal(signal.SIGALRM, timeout_handler)
        #signal.alarm(timeout)

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        output, error = process.communicate(input=data)

        signal.alarm(0)

        if error:
            print("Ошибка:", error)
            return -1
        else:
            return output
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
        return -1
    except TimeoutError as e:
        print(f"Ошибка: {e}")
        process.kill()
        return -1

output = run_python("lol.py", "99")
if output != -1:
    print(output)
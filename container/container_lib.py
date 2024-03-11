import sys
sys.path.insert(0, '../container-lib/build/')
from container_lib_py import Container, ContainerException, launch_options

def solve(inputPath: str, programInput: str, timeLimit: int = 3000, maxForks: int = 8, maxMemory: int = 512):
    cont = Container()
    opt = launch_options()
    print(opt)
    opt.time = timeLimit
    opt.forks_threshold = maxForks
    opt.cpu_usage = 1
    opt.memory = maxMemory
    opt.cgroup_id = "container-lib"
    opt.input = programInput
    print(opt.time)
    try:
        cont.start(inputPath, opt, "", set())
        exit_status = cont.sync("container-lib")
        out = cont.get_buf()
        print("Container-lib output:", out)
        print("Container-lib status:", exit_status)
        return {"status": "ok", "container_output": {"out_buffer": out, "exit_status": exit_status}}
    except ContainerException as e:
        print("Container exception")
        print(e)
        return {"status": "cont_error", "error_msg": str(e)}
#solve("./a.out", "5\n")
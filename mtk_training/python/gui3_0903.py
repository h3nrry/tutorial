import subprocess
# win: ["dir"]
command = ["ls", "-al"]
f = open("result.log", "w", encoding="utf-8")
result = subprocess.run(command,
                        stdout=f)
f.close()
print(result)
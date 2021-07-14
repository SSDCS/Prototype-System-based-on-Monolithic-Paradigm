import subprocess

process1 = subprocess.Popen(["venv/bin/python3", "tests/producers.py"]) # Create and launch process pop.py using python interpreter
process2 = subprocess.Popen(["venv/bin/python3", "application.py"])
process3 = subprocess.Popen(["venv/bin/python3", "Application/Monitoring/monitoring.py"])

process1.wait() # Wait for process1 to finish (basically wait for script to finish)
process2.wait()
process3.wait()
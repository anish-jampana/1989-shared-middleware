from subprocess import Popen

p = Popen(["python3","-m", "flask", "run"])
p1 = Popen(["python3","-m", "flask", "run"], cwd="MMGs/airplanesMMG")
p2 = Popen(["python3","-m", "flask", "run"], cwd="MMGs/animalsMMG")
p3 = Popen(["python3","-m", "flask", "run"], cwd="MMGs/butterfliesMMG")
p4 = Popen(["python3","-m", "flask", "run"], cwd="MMGs/carsMMG")
p5 = Popen(["python3","-m", "flask", "run"], cwd="MMGs/countriesMMG")
p6 = Popen(["python3","-m", "flask", "run"], cwd="MMGs/gemsMMG")
p7 = Popen(["python3","-m", "flask", "run"], cwd="MMGs/instrumentsMMG")
p8 = Popen(["python3","-m", "flask", "run"], cwd="MMGs/motorbikesMMG")
p9 = Popen(["python3","-m", "flask", "run"], cwd="MMGs/sportsMMG")

names = ['sean', 'steph']
degree = ['IT', 'PHD']
age = [26, 23]

for i in range(len(names)):
    print("name = {:15}\tdegree = {:15}\tage = {:>3}".format(names[i], degree[i], age[i]))
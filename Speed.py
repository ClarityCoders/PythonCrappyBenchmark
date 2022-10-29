import time
import os
import csv
import random
 
dir = 'Fake_files/'

def multiples(num1, num2, max):
    for i in range(1,max+1):
        if i % num1 == 0 or i % num2 == 0:
            pass

def create_files(number_files, file_path):
    for i in range(number_files):
        with open(os.path.join(file_path,str(i) + ".txt"), 'w') as fp:
            # uncomment if you want empty file
            fp.write('This is first line')

def delete_files(file_path):
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

def sort_list(n):
    test_list = []
    for i in range(n):
        test_list.append(random.random())

    test_list.sort()

test = "Python-3.10.7"
data = []
total_start = time.time()
for i in range(100):
    # Find multiples
    start_time = time.time()
    multiples(3,5,10000000)
    time_multiples = (time.time() - start_time) * 1000

    # Sort List
    start_time = time.time()
    sort_list(1000000)
    time_sort = (time.time() - start_time) * 1000

    # Create some files.
    start_time = time.time()
    create_files(1000,dir)
    time_create = (time.time() - start_time) * 1000

    # Delete all the files
    start_time = time.time()
    delete_files(dir)
    time_delete = (time.time() - start_time) * 1000

    data.append([time_multiples,time_sort,time_create,time_delete])

total_time = time.time() - total_start
with open(test + "-" + str(total_time) +'.csv', 'w') as f: 
    write = csv.writer(f) 
    write.writerows(data)
# dynamic_programming
In this File directory there exist a python file named "label_correcting_alg.py" you can either:  
1. Open the file and scroll to the buttom of the code and call the "label_corecting_alg" function with its arguments. e.g: 

```python
label_corecting_alg(file_location="your data file.csv ", origin=234986, destination=148685 , policy="SLF_LLL")
```

The arguments of this function are the data file directory, the origin node as a number, the destination index as a number, and finally, the policy either BFS, DFS, Dijkstra, or SLF_LLL.  

2. import the function from the python script and run it with your arbitrary arguments. e.g (calling function from command prompt)

```console
foo@bar:~$ cd /to/the/file/directory
foo@bar:~$ pip install -r requirements.txt
foo@bar:~$ python 
>>> import label_corecting_alg form label_corecting_alg.py 
>>> label_corecting_alg(file_location="your data file.csv", origin=234986, destination=148685 , policy="SLF_LLL")
```

**note the data file should be a CSV file whit three columns. each row should represent an arc. the first column is the origin of the arc, the second column is the destination of the arc, and finally, the third one is the associated cost of that arc.

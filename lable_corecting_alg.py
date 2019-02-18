import pandas as pd
import numpy as np
import timeit
import time


'''the following is a function which gets the file location, origin, destination, and policy as arguments and gives back a text file, in which all desired 
output are printed, such as cost, path, and so on. the policy argument only takes four value: BFS, DFS, Dijkstra, and SLF_LLL. '''



def label_corecting_alg(file_location, origin, destination, policy = "BFS" ):
    start = timeit.default_timer()     # this timer is activated for the purpose of calculating running time
    df = pd.read_csv(file_location, header=None, names=["origin", "destination", "cost"]) #we read data into a pandas dataframe


    # we find all the possible nodes in dataframe
    origin_list = np.sort(df.origin.unique())
    destination_list = np.sort(df.destination.unique())
    all_nodes = list(set().union(origin_list, destination_list))

    # initialization of upper
    upper = float("inf")


    # in the following lines of code we create a class of nodes, each nodes is an object of this class with the following attributes: name,
    # distance from origin, parent, number of visiting, and all the neighbours it has.
    class node:
        # constructor
        def __init__(self, name):
            self.name = name
            self.distance = float("inf")
            self.parent = ""
            self.visited = 0
            self.direct_down_stream_nodes = ""    #df.loc[df.origin == self.name, ["destination", "cost"]].reset_index(drop=True).to_dict('records')

        def find_path(self, dest, org):
            path = [dest.name]
            while dest != org:
                path.append(dest.parent.name)
                dest = dest.parent
            return path



    # for each node we create an object and store them all in the folloing list.
    all_nodes_objects = [node(i) for i in all_nodes]

    origin_index = all_nodes.index(origin)
    origin = all_nodes_objects[origin_index]
    origin.distance = 0
    OPEN_SET = [all_nodes_objects[origin_index]]
    destination = all_nodes_objects[all_nodes.index(destination)]

    # the following function determine the policy based on the policy input that you call the whole label correcting function with it.
    def Policy_indicatior():
        # the bsf policy always gets the fist element of open set.
        if policy == "BFS":
            return OPEN_SET[0]
        # DFS always get the last one.
        elif policy == "DFS":
            return OPEN_SET[-1]
        # for dijkstra we look into the open set and find the minimum distance
        elif policy == "Dijkstra":
            min_dist = min(OPEN_SET, key=lambda x: x.distance)
            return min_dist
        # the following snippet of code find the node that its distance is lower than the avarage distance of all the nodes in open set
        elif policy == "SLF_LLL":
            avarage = (sum(i.distance for i in OPEN_SET))/len(OPEN_SET)
            while OPEN_SET[0].distance > avarage:
                OPEN_SET.append(OPEN_SET.pop(0))
            return OPEN_SET[0]
        else:
            raise Exception("There is No policy calling {}".format(policy) + ". The policy can be BFS, DFS, Dijkstra, or SLF_LLL ")


    # the following snippet of code is the implementation of label correcting algorithem, based on the policy we remove nodes from the open set
    # and we add the nodes to open set if they meet the conditions.
    # the while loops goes on untill either time runs out or the solution is found.
    # at each iteration of the while loop we look at all the neighbours of the leaving node, and add them to the open set if they meet the conditions.
    t_end = time.time() + (60*60*2)
    total_iterations = 0
    while len(OPEN_SET) > 0 and time.time() < t_end:

        leaving_node = Policy_indicatior()
        if leaving_node.direct_down_stream_nodes == "":
            leaving_node.direct_down_stream_nodes = df.loc[df.origin == leaving_node.name, ["destination", "cost"]].reset_index(drop=True).to_dict('records')

        for i in leaving_node.direct_down_stream_nodes:
            pros_entering_node = i["destination"]
            total_iterations += 1
            #pros_entering_node = all_nodes_objects[all_nodes.index(pros_entering_node)]
            pros_entering_node = all_nodes_objects[pros_entering_node -1 ]
            if leaving_node.distance + i["cost"] < min(pros_entering_node.distance , upper):
                pros_entering_node.distance = leaving_node.distance + i["cost"]
                pros_entering_node.parent = leaving_node
                pros_entering_node.visited += 1
                if destination != pros_entering_node:
                    if policy =="SLF_LLL" and len(OPEN_SET) > 1:
                        if OPEN_SET[1].distance > pros_entering_node.distance:
                            OPEN_SET.insert(0,pros_entering_node)
                        else:
                            OPEN_SET.append(pros_entering_node)

                    else:
                        OPEN_SET.append(pros_entering_node)
                else:
                    upper = pros_entering_node.distance
        OPEN_SET.remove(leaving_node)


    stop = timeit.default_timer()
    execution_time = stop - start


    #the following lines of code show the percentage of nodes that have been visited at least once, that might be helpfull for the analysis purpose.
    visited_number = 0
    for i in all_nodes_objects:
        if i.visited > 0:
            visited_number += 1
    visited_percentage = 100 * visited_number/len(all_nodes_objects)


    # after the process is finished the results will be stored in a text file in the code file directory.
    if destination.distance < float("inf"):
        print (destination.distance, destination.find_path(destination, origin), len(destination.find_path(destination, origin)))
        output_name = "sol_" + file_location + "_" + str(origin.name) + "_"+ str(destination.name) + "_" + policy + ".txt"
        f = open(output_name, "w+")
        f.write("Armin Khayyer \n")
        f.write("Data File: {}\n".format(file_location))
        f.write("Algorithem: {}\n".format(policy))
        f.write("Origin: {}\n".format(origin.name))
        f.write("Destination: {}\n".format(destination.name))
        f.write("cost: {}\n".format(destination.distance))
        f.write("Path: {}\n".format(destination.find_path(destination, origin)))
        f.write("running time: {}\n".format(execution_time))
        f.write("total iterations : {}\n".format(total_iterations))
        f.write("number of nodes: {}\n".format(len(destination.find_path(destination, origin))))
        f.write("visited percentge: %{}".format(visited_percentage))



#instances = [[94998, 255479], [85, 34373], [234986, 148685], [14113, 260935],[103085, 219305], [2122, 142669], [703, 109758], [224011, 1585],[5641, 151854], [263213, 180097]]
#algs = ["SLF_LLL", "BFS", "Dijkstra", "DFS" ]


#for i in instances:
label_corecting_alg(file_location="NewYorkData.csv", origin=234986, destination=148685 , policy="SLF_LLL")






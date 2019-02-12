import pandas as pd
import numpy as np
import timeit


#ALL THE PROGRAM STATEMETNS




def label_corecting_alg(file_location, origin, destination, policy = "BFS" ):
    start = timeit.default_timer()
    df = pd.read_csv(file_location, header=None, names=["origin", "destination", "cost"])

    origin_list = np.sort(df.origin.unique())
    destination_list = np.sort(df.destination.unique())
    all_nodes = list(set().union(origin_list, destination_list))
    upper = float("inf")



    class node:
        # constructor
        def __init__(self, name):
            self.name = name
            self.distance = float("inf")
            self.parent = ""
            self.visited = 0
            self.direct_down_stream_nodes = ""#df.loc[df.origin == self.name, ["destination", "cost"]].reset_index(drop=True).to_dict('records')

        def find_path(self, dest, org):
            path = [dest.name]
            while dest != org:
                path.append(dest.parent.name)
                dest = dest.parent
            return path




    all_nodes_objects = [node(i) for i in all_nodes]

    origin_index = all_nodes.index(origin)
    origin = all_nodes_objects[origin_index]
    origin.distance = 0
    OPEN_SET = [all_nodes_objects[origin_index]]
    destination = all_nodes_objects[all_nodes.index(destination)]


    def Policy_indicatior():
        if policy == "BFS":
            return OPEN_SET[0]

        elif policy == "DFS":
            return OPEN_SET[-1]

        elif policy == "Dijkstra":
            min_dist = min(OPEN_SET, key=lambda x: x.distance)
            return min_dist

        elif policy == "SLF_LLL":
            avarage = (sum(i.distance for i in OPEN_SET))/len(OPEN_SET)
            while OPEN_SET[0].distance > avarage:
                OPEN_SET.append(OPEN_SET.pop(0))
            return OPEN_SET[0]
        else:
            raise Exception("There is No policy calling {}".format(policy) + ". The policy can be BFS, DFS, Dijkstra, or SLF_LLL ")




    while len(OPEN_SET) > 0:

        leaving_node = Policy_indicatior()
        leaving_node.direct_down_stream_nodes = df.loc[df.origin == leaving_node.name, ["destination", "cost"]].reset_index(drop=True).to_dict('records')
        print(leaving_node.name)
        for i in leaving_node.direct_down_stream_nodes:
            pros_entering_node = i["destination"]
            pros_entering_node = all_nodes_objects[all_nodes.index(pros_entering_node)]
            if leaving_node.distance + i["cost"] < min(pros_entering_node.distance , upper):
                pros_entering_node.distance = leaving_node.distance + i["cost"]
                pros_entering_node.parent = leaving_node
                pros_entering_node.visited += 1
                if destination.name != pros_entering_node.name:
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
    visited_number = 0
    for i in all_nodes_objects:
        if i.visited > 0:
            visited_number += 1
    visited_percentage = 100 * visited_number/len(all_nodes_objects)


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
    f.write("number of nodes: {}\n".format(len(destination.find_path(destination, origin))))
    f.write("visited percentge: %{}".format(visited_percentage))



instances = [[94998, 255479], [85, 34373], [234986, 148685], [14113, 260935],[103085, 219305], [2122, 142669], [703, 109758], [224011, 1585],[5641, 151854], [263213, 180097]]
algs = ["SLF_LLL", "BFS", "Dijkstra", "DFS" ]


#for i in instances:
label_corecting_alg(file_location="RomeData.csv", origin=1, destination=400, policy="BFS")






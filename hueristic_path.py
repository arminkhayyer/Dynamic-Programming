import pandas as pd
import numpy as np
import timeit


#ALL THE PROGRAM STATEMETNS




def find_path(file_location, origin, destination ):
    start = timeit.default_timer()
    df = pd.read_csv(file_location, header=None, names=["origin", "destination", "cost"])
    origin_list = np.sort(df.origin.unique())
    destination_list = np.sort(df.destination.unique())
    all_nodes = list(set().union(origin_list, destination_list))



    class node:
        # constructor
        def __init__(self, name):
            self.name = name
            self.distance = float("inf")
            self.parent = ""
            self.visited = False
            self.direct_down_stream_nodes = df.loc[df.origin == self.name, ["destination", "cost"]].reset_index(drop=True).to_dict('records')

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

    while len(OPEN_SET) >0 :
        leaving_node = OPEN_SET[0]
        for i in leaving_node.direct_down_stream_nodes:
            pros_entering_node = i["destination"]
            pros_entering_node = all_nodes_objects[all_nodes.index(pros_entering_node)]
            pros_entering_node.parent = leaving_node
            if pros_entering_node.visited == False:
                OPEN_SET.append(pros_entering_node)
                pros_entering_node.visited = True
            else:
                pass
            print([i.name for i in OPEN_SET])
            if destination.name == pros_entering_node.name:
                break
        OPEN_SET.remove(leaving_node)

    print(destination.find_path(destination, origin))

find_path(file_location="RomeData.csv", origin=2204, destination=90)

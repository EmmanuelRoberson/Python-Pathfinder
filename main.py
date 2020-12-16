class WayPoint:
    
    def __init__(self, xVal, yVal):
        self.x = xVal #x positional value
        self.y = yVal #y positional value
        self.neighbors = [] #list of neighbor waypoints
        self.parent = None #parent waypoint

    def get_neighbors(self): #return neighbor waypoints
        return self.neighbors

#Finds a target by searching through every possible node in the vicinity. Also known as Breadth First Search
def find_path(starting_waypoint, target_waypoint):
    open_list = []
    open_list.append( starting_waypoint ) #add the start to the open list. open list is the list of waypoints that need to be checked
    visited_list = [] #list of already visited waypoints

    loop = 0
    for w_p in open_list: #iterate through all the waypoints in the open list
        #print(w_p)
        for v_w in visited_list: #if we already visited this waypoint, move to the next one
            if w_p is v_w:
                continue

        visited_list.append(w_p) #add the current neightbor to the visited list

        if (w_p is target_waypoint): #check if the current waypoint is the target
            if (w_p is target_waypoint):
                return w_p #return the waypoint if true

        current_waypoint = w_p
        current_neighbors = current_waypoint.get_neighbors() #get the neighbors of the current waypoint
        
        for c_n in current_neighbors: #set each neighbors' parent to the current waypoint
            c_n.parent = w_p

        for n_b in current_neighbors:
            open_list.append(n_b) #add the neighbors to the open list
        loop += 1
        #print(type(w_p) is list, loop)


    return None #return none if the target isnt found


def main():

    #implementation goes here

    start = WayPoint(0,0)
    wp1 = WayPoint(1,0)
    wp2 = WayPoint(0,1)
    wp3 = WayPoint(2,2)

    start.neighbors.append(wp1)
    start.neighbors.append(wp2)


    the_target = find_path(start, wp1)
    not_the_target = find_path(start, wp3)

    print(the_target is wp1)
    print(not_the_target is wp3)
    
    return None


main()



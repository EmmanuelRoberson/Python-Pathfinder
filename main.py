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
    open_list = [starting_waypoint] #add the start to the open list. open list is the list of waypoints that need to be checked
    visited_list = [] #list of already visited waypoints

    for cw in open_list: #iterate through all the waypoints in the open list

        if (visited_list.__contains__(cw)): #if we already visited this waypoint, move to the next one
            continue

        visited_list.append(cw) #add the current neightbor to the visited list

        if (cw.x is target_waypoint.x and cw.y is target_waypoint.y): #check if the current waypoint is the target
            return cw #return the waypoint if true

        current_neighbors = cw.get_neighbors() #get the neighbors of the current waypoint
        
        for cn in current_neighbors: #set each neighbors' parent to the current waypoint
            cn.parent = cw

        open_list.append(current_neighbors) #add the neighbors to the open list


    return None #return none if the target isnt found


def main():

    #implementation goes here

    start = WayPoint(0,0)

    start.neighbors = [WayPoint(1,0), WayPoint(0,1)]

    the_target = find_path(start, WayPoint(0,1))

    not_the_target = find_path(start, WayPoint(2,2))
    
    return None


main()



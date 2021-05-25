from typing import List
import itertools


# first parameter is the 
def maximum_unit_truck(*, box_types: List[List[int]], truck_size: int) -> int:
    """Find the Maximum unit of boxes that can be put on the trucks
    Solution: Greedy Algorithm
    
    Parameters
    ----------
    box_types:  List of Item where the Item: first item is the number of boxes, 
                second items is the number of unit in each box
    truck_size: the maximum number of boxes that can be put on the truck
    """
    
    # Flattern the Item from [[1,3],[2,2],[3,1]] -> [3, 2, 2, 1, 1, 1]
    flatten = sorted(itertools.chain(
        *map(lambda x: [x[1]] * x[0], box_types)), reverse=True)
    
    return sum(itertools.islice(flatten, truck_size))
    
assert maximum_unit_truck(box_types=[[1,3],[2,2],[3,1]], truck_size=4) == 8
assert maximum_unit_truck(box_types=[[5,10],[2,5],[4,7],[3,9]], truck_size=10) == 91

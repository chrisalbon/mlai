Title: Priority Queues  
Slug: priority_queues  
Summary: Priority Queues Using Python.  
Date: 2017-02-02 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon  

## Preliminaries


```python
import heapq
```

## Create A Priority Queue Object


```python
# Create a priority queue abstract base class
class priority_queue:
    # Initialize the instance
    def __init__(self):
        # Create a list to use as the queue
        self._queue = []
        # Create an index to use as ordering
        self._index = 0

    # Create a function to add a task to the queue
    def add_task(self, item, priority):
        # Push the arguments to the _queue using a heap
        heapq.heappush(self._queue, (-priority, self._index, item))
        # Add one to the index
        self._index += 1

    # Create a function to get the next item from the queue
    def next_task(self):
        # Return the next item in the queue
        return heapq.heappop(self._queue)[-1]
```


```python
# Create a priority queue called task_list
task_list = priority_queue()
```

## Add Items To Queue


```python
# Add an item to the queue
task_list.add_task('Clean Dishes', 1)

# Add an item to the queue
task_list.add_task('Wash Car', 2)

# Add an item to the queue
task_list.add_task('Walk Dog', 3)
```

## Retrieve Items From Queue By Priority


```python
# Retrieve items from the queue
task_list.next_task()
```




    'Walk Dog'




```python
# Retrieve items from the queue
task_list.next_task()
```




    'Wash Car'




```python
# Retrieve items from the queue
task_list.next_task()
```




    'Clean Dishes'



Title: Scheduling Jobs In The Future  
Slug: schedule_run_in_the_future  
Summary: Scheduling Jobs In The Future  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon  


```python
# Import required modules
import sched
import time

# setup the scheduler with our time settings
s = sched.scheduler(time.time, time.sleep)
```


```python
# Create a function we want to run in the future.
def print_time():
    print("Executive Order 66")
```


```python
# Create a function for the delay
def print_some_times():
    # Create a scheduled job that will run
    # the function called 'print_time'
    # after 10 seconds, and with priority 1.
    s.enter(10, 1, print_time)
    
    # Run the scheduler
    s.run()
```


```python
# Run the function for the delay
print_some_times()
```

    Executive Order 66


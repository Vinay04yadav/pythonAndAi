from multiprocessing import Process
import time

def brew_chai(name):
    print(f"start of {name} chai brewing")
    time.sleep(3)
    print(f"end of {name} chai brewing")

if __name__ == "__main__":
    chai_makers = [
        Process(target=brew_chai, args=(f"Chai maker #{i+1}", )) # target: The function that the process should execute. args: The arguments that should be passed to that function.
        # brew_chai not brew_chai()
        for i in range(3)
    ]

    # Start all process
    for p in chai_makers:
        p.start()

    # wait for all to complete
    for p in chai_makers:
        p.join()

    print(f"All chai served")




# Other ways to make that list
# chai_makers = []

# for i in range(3):
#     p = Process(
#         target=brew_chai,
#         args=(f"Chai maker #{i+1}",)
#     )
#     chai_makers.append(p)






# ==========================================
# LIST COMPREHENSION WITH MULTIPROCESSING
# ==========================================

# Creating multiple Process objects using list comprehension:

# chai_makers = [
#     Process(target=brew_chai, args=(f"Chai maker #{i+1}",))
#     for i in range(3)
# ]

# How it works:
# 1. range(3) generates: 0, 1, 2
# 2. For each value of i, a new Process object is created.
# 3. target specifies the function to execute.
# 4. args passes arguments to that function as a tuple.
# 5. All three Process objects are stored in a list.

# Equivalent approach using a normal for loop:

# chai_makers = []

# for i in range(3):
#     p = Process(
#         target=brew_chai,
#         args=(f"Chai maker #{i+1}",)
#     )
#     chai_makers.append(p)

# Both approaches create the same list of 3 Process objects.


# ==========================================
# STARTING AND JOINING PROCESSES
# ==========================================

# First loop: Start all processes.
# for p in chai_makers:
#     p.start()

# start() launches the process.
# All processes can now execute independently.

# Second loop: Wait for all processes to finish.
# for p in chai_makers:
#     p.join()

# join() blocks the main process until that particular
# child process completes.

# Once all processes finish, execution continues.
# print("All chai served")
import threading

def main():
    n = int(input("How many times do you want the philosophers to eat? "))

    if n > 60:
        print("Philosophers are not that hungry, please enter a number less than 60.")
        return
    if n < 1:
        print("Philosophers are hungry, please enter a number greater than 0.")
        return
#Makes sure the user input is in the peramaters

    forks = [threading.Lock() for _ in range(5)]
    log = []  
    #Collects peramaters

    threads = [
        threading.Thread(target=philosopher, args=(i, n, forks, log))
        for i in range(5)
    ]
#Makes the threads for the philosophers and then starts them and waits for them to finish before printing the log
    for t in threads:
        t.start()
    for t in threads:
        t.join()
#It will then print the log of the philosophers actions in order of what they did and what they were doing
    print(log)


def philosopher(id, n, forks, log):
    left = id
    right = (id + 1) % 5
#Sets the left and right forks for each philosopher based on their id

    first_fork, second_fork = sorted((left, right))
#Avoids a deadlock by always picking up the lower numbered fork first, then the higher numbered fork second

    for _ in range(n):
#Picks the first fork
        log.append([id, 1 if first_fork == left else 2, 1])
        with forks[first_fork]:

            log.append([id, 1 if second_fork == left else 2, 1])
            with forks[second_fork]:

                log.append([id, 0, 3])

                log.append([id, 1 if second_fork == left else 2, 2])

            log.append([id, 1 if first_fork == left else 2, 2])
#Does the actions of picking up forks, eating, and putting down forks while logging each action with the philosopher's id, fork number, and action type (1 for pick up, 2 for put down, 3 for eat).


if __name__ == "__main__":
    main()
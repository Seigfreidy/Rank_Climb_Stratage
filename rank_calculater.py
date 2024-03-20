import numpy as np
import matplotlib.pyplot as plt
import rival_generator
import strive_to_win
import lose_to_run
import recognize_weakness

def main():
    rivals = rival_generator.generator(1000000)
    step  = 0.1
    range = np.arange(0, 1+step, step)
    averages = []
    averages2 =[]
    for a in range:
        ranks = []
        ranks2 =[]
        for rival in rivals:
            # rank = strive_to_win.random_rank(rival)
            # rank = lose_to_run.random_rank(rival)
            rank = recognize_weakness.random_rank(rival, a)
            rank2 = recognize_weakness.random_rank_one_to_run(rival, a)
            ranks.append(rank)
            ranks2.append(rank2)
        average = np.average(ranks)
        average2 = np.average(ranks2)
        averages.append(average)
        averages2.append(average2)
        # print(average)
    
 
    plt.figure()  
    plt.plot(range, averages, color = 'red')
    plt.plot(range, averages2, color = 'blue')
    plt.title('Simple Plot')  
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.show()

if __name__ == '__main__':
    main()

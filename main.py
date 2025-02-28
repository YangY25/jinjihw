import random

def labor_exploitation_simulator():
    print("Welcome to the Labor Exploitation Simulator! You are a factory owner in the U.S.")
    
    # Initial conditions
    profit = 100000  # Starting company profit
    worker_satisfaction = 50  # Worker happiness (0-100 scale)
    productivity = 100  # Productivity level
    social_stability = 100  # Social stability indicator
    bankruptcy_risk = 0  # Bankruptcy risk percentage
    round_count = 0
    consecutive_twos = 0  # Track consecutive '2' choices
    
    while round_count < 10:
        round_count += 1
        print(f"\nRound {round_count}")
        print(f"Current Profit: ${profit}")
        print(f"Worker Satisfaction: {worker_satisfaction}")
        print(f"Productivity: {productivity}")
        print(f"Social Stability: {social_stability}")
        print(f"Bankruptcy Risk: {bankruptcy_risk}%")
        
        # Check for bankruptcy
        if profit < 0:
            print("You are a good boss, but being too generous has led to your failure. Game Over.")
            print("Thank you for playing!")
            return
        if bankruptcy_risk >= 80 and random.random() < (bankruptcy_risk / 100):
            print("Your company has gone bankrupt due to excessive costs! Game Over.")
            print("Thank you for playing!")
            return
        
        # Check for worker strike
        if worker_satisfaction < 25:
            print("Workers have gone on strike due to poor conditions! Game Over.")
            print("Thank you for playing!")
            return
        
        # Player makes a decision
        print("Choose your labor policy:")
        print("1. Increase wages and improve conditions (+Worker Satisfaction, -Profit, ++Bankruptcy Risk if consecutive)")
        print("2. Maintain current policies (neutral effects, lower profit growth; long-term dissatisfaction risk)")
        print("3. Cut wages and extend work hours (-Worker Satisfaction, ++Profit, -Social Stability)")
        
        choice = input("Enter 1, 2, or 3: ")
        
        if choice == "1":
            if profit < 20000:
                print("You don't have enough funds to increase wages!")
                continue
            profit -= random.randint(20000, 35000)
            worker_satisfaction += random.randint(10, 20)
            productivity += random.randint(5, 10)
            social_stability += random.randint(5, 10)
            bankruptcy_risk += 20  # Increased bankruptcy risk if choosing 1 too often
            consecutive_twos = 0
        elif choice == "2":
            consecutive_twos += 1
            if consecutive_twos >= 3:
                print("Due to inflation, currency devaluation, or better benefits offered by competitors, you should change your policy soon!")
                worker_satisfaction -= random.randint(5, 10)
            profit += random.randint(1000, 5000)
        elif choice == "3":
            profit += random.randint(20000, 40000)
            worker_satisfaction -= random.randint(15, 25)
            productivity -= random.randint(5, 15)
            social_stability -= random.randint(10, 20)
            consecutive_twos = 0
        else:
            print("Invalid choice, please enter 1, 2, or 3.")
            continue
        
        # Random events (1/4 probability per round), only triggered after pressing 1
        if random.random() < 0.5:
            input("Press 1 to continue to the next round: ")
            event_chance = random.random()
            if event_chance < 0.2:
                print("Unexpected major expense! You must pay an additional large cost.")
                expense = random.randint(20000, 50000)
                profit -= expense
            elif event_chance < 0.35:
                print("Workers are striking due to poor conditions!")
                productivity -= random.randint(10, 20)
                social_stability -= random.randint(10, 20)
            elif event_chance < 0.5:
                print("Government intervention! You are forced to improve working conditions.")
                profit -= random.randint(5000, 15000)
                worker_satisfaction += random.randint(5, 10)
            elif event_chance < 0.6:
                print("A competitor has introduced better working conditions, making your company less attractive!")
                worker_satisfaction -= random.randint(5, 10)
            elif event_chance < 0.7:
                print("An economic downturn has decreased consumer demand, reducing your profit margin.")
                profit -= random.randint(5000, 15000)
            elif event_chance < 0.8:
                print("New labor regulations have increased costs, forcing you to adapt!")
                profit -= random.randint(10000, 25000)
            elif event_chance < 0.9:
                print("A worker union has formed, demanding better wages and conditions!")
                worker_satisfaction += random.randint(10, 20)
                profit -= random.randint(5000, 15000)
            else:
                print("A major scandal about your labor policies has hit the media, reducing your reputation!")
                social_stability -= random.randint(10, 20)
                worker_satisfaction -= random.randint(5, 10)
        
        # Bankruptcy risk adjustment
        if choice != "1":
            bankruptcy_risk = max(0, bankruptcy_risk - 10)
        
    # Game over, analyze outcome
    print("\nFinal Results:")
    print(f"Final Profit: ${profit}")
    print(f"Final Worker Satisfaction: {worker_satisfaction}")
    print(f"Final Productivity: {productivity}")
    print(f"Final Social Stability: {social_stability}")
    print(f"Final Bankruptcy Risk: {bankruptcy_risk}%")
    
    if worker_satisfaction < 20 and social_stability < 30:
        print("Your company faces mass protests and collapses due to public pressure!")
    elif profit > 200000 and worker_satisfaction > 60:
        print("You've found a balance between profit and fair labor conditions. Well done!")
    else:
        print("Your company survives, but at what cost? The economy and society bear the burden.")
    
    print("Labor exploitation can indeed increase economic benefits in the short term by reducing workers' rights, but in the long run, this practice will have a profound negative impact on society. In the short term, companies reduce costs by lowering wages, cutting benefits or extending working hours, thereby increasing profits.")
    print("")
    print("For example, according to the Economic Policy Institute (EPI), wage theft costs low-income workers up to $50 billion each year, and these funds flow directly to business owners and shareholders, driving short-term economic growth.")
    print("")
    print("However, in the long run, labor exploitation will weaken consumption capacity, lead to a widening gap between the rich and the poor in society, and trigger deeper economic instability. When the income of most workers is compressed, their consumption capacity decreases, and the long-term market demand of enterprises decreases, which ultimately affects the overall economic vitality. In addition, deteriorating working conditions and low wages often lead to higher employee turnover and health problems, increasing the burden on social security and medical systems.")
    print("")
    print("For example, a large number of workers lack medical insurance and retirement security, which exacerbates social inequality. Therefore, although labor exploitation brings growth to businesses and capital markets in the short term, in the long run it undermines the sustainable development of society as a whole and may ultimately undermine the economic stability of the entire country.")

# Run the simulator
labor_exploitation_simulator()

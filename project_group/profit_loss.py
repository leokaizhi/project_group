import csv

def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)  
        next(reader) 
        data = []
        for row in reader:
            if len(row) >= 5:
                data.append(row)
    return data


def analyse_net_profit(data):
    """
    Analyses net profit data to determine the profit trend 
    and identify the highest surplus or deficit
    """
    differences = []  # create empty list
    previous_net_profit = float(data[0][4])  # initialise data at net profit column (5th column)

    for current_row in data[1:82]:  # limit to the first 81 rows (90 days)
        current_day = current_row[0]
        current_net_profit = float(current_row[4])  # convert net profit to float
        difference = current_net_profit - previous_net_profit  # calculate the difference
        differences.append((current_day, difference)) 
        previous_net_profit = current_net_profit


    # check if net profit is always increasing
    increasing = True
    for _, diff in differences:
        if diff < 0:
            increasing = False
            break


    # check if net profit is always decreasing
    decreasing = True
    for _, diff in differences:
        if diff > 0:
            decreasing = False
            break



    #if net profit is always increasing
    if increasing:
        scenario = "Scenario 1"
        # find day with highest surplus
        max_difference = float('-inf')
        for day, diff in differences:
            if diff > max_difference:
                max_difference = diff
                max_day = day
                max_amount = diff
        output = [
            "[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY",
            f"[HIGHEST NET PROFIT SURPLUS] DAY: {max_day}, AMOUNT: SGD{max_amount}"
        ]

    
    
    #if net profit is always decreasing
    elif decreasing:
        scenario = "Scenario 2"
        # find day with highest deficit
        min_difference = float('inf')
        for day, diff in differences:
            if diff < min_difference:
                min_difference = diff
                max_day = day
                max_amount = -diff
        output = [
            "[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN PREVIOUS DAY",
            f"[HIGHEST NET PROFIT DEFICIT] DAY: {max_day}, AMOUNT: SGD{max_amount}"
        ]



    #if net profit is neither always increasing or always decreasing
    else:
        scenario = "Scenario 3"
        deficits = []  # list to store deficits
        for day, amt in differences:
            if amt < 0:
                deficits.append((day, amt))

        # Initialize variables for top three deficits
        top1_deficit = top2_deficit = top3_deficit = ('', float(1000000))
        
        for day, amt in deficits:
            if amt < top1_deficit[1]:
                top1_deficit, top2_deficit, top3_deficit = (day, amt), top1_deficit, top2_deficit
            elif amt < top2_deficit[1]:
                top2_deficit, top3_deficit = (day, amt), top2_deficit
            elif amt < top3_deficit[1]:
                top3_deficit = (day, amt)

        output = []
        for day, amt in deficits:
            output.append(f"[NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD{-amt}")
            
        output.append(f"[1 HIGHEST NET PROFIT DEFICIT] DAY: {top1_deficit[0]}, AMOUNT: SGD{-top1_deficit[1]}")
        output.append(f"[2 HIGHEST NET PROFIT DEFICIT] DAY: {top2_deficit[0]}, AMOUNT: SGD{-top2_deficit[1]}")
        output.append(f"[3 HIGHEST NET PROFIT DEFICIT] DAY: {top3_deficit[0]}, AMOUNT: SGD{-top3_deficit[1]}")

    return scenario, output
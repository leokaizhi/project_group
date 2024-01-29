import csv

def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)  
        next(reader) 
        data = []
        for row in reader:
            if len(row) >= 2:
                data.append(row)
    return data

def analyse_cash_on_hand(data):
    """
    Analyses cash on hand data to determine the trend
    and identify the highest surplus or deficit
    """
    differences = []  # create empty list
    previous_cash_on_hand = float(data[0][1])  # initialise data at cash on hand column (2nd column)

    for current_row in data[1:82]:  # process all rows
        current_day = current_row[0]
        current_cash_on_hand = float(current_row[1])  # convert cash on hand to float
        difference = current_cash_on_hand - previous_cash_on_hand  # calculate the difference
        differences.append((current_day, difference))
        previous_cash_on_hand = current_cash_on_hand


    # check if cash on hand is always increasing
    increasing = True
    for _, diff in differences:
        if diff < 0:
            increasing = False
            break

    # check if cash on hand is always decreasing 
    decreasing = True
    for _, diff in differences:
        if diff > 0:
            decreasing = False
            break


    # if cash on hand is always increasing
    if increasing:
        scenario = "Scenario 1"
        # find day with highest surplus
        max_difference = float('-inf')
        max_day = ""
        max_amount = 0
        for day, diff in differences:
            if diff > max_difference:
                max_difference = diff
                max_day = day
                max_amount = diff
        output = [
            "[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN PREVIOUS DAY",
            f"[HIGHEST CASH SURPLUS] DAY: {max_day}, AMOUNT: SGD{max_amount}"
        ]


    # if cash on hand is always decreasing
    elif decreasing:
        scenario = "Scenario 2"
        # find day with highest deficit
        min_difference = float('inf')
        min_day = ""
        min_amount = 0
        for day, diff in differences:
            if diff < min_difference:
                min_difference = diff
                min_day = day
                min_amount = -diff
        output = [
            "[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN PREVIOUS DAY",
            f"[HIGHEST CASH DEFICIT] DAY: {min_day}, AMOUNT: SGD{min_amount}"
        ]



    # if cash on hand is neither always increasing or always decreasing
    else:
        scenario = "Scenario 3"
        deficits = []  # list to store deficits
        for day, amt in differences:
            if amt < 0:
                deficits.append((day, amt))

        # Initialize variables for top three deficits
        top1_deficit = top2_deficit = top3_deficit = ('', float(10000))
        
        for day, amt in deficits:
            if amt < top1_deficit[1]:
                top1_deficit, top2_deficit, top3_deficit = (day, amt), top1_deficit, top2_deficit
            elif amt < top2_deficit[1]:
                top2_deficit, top3_deficit = (day, amt), top2_deficit
            elif amt < top3_deficit[1]:
                top3_deficit = (day, amt)

        output = []
        for day, amt in deficits:
            output.append(f"[CASH DEFICIT] DAY: {day}, AMOUNT: SGD{-amt}")

        output.append(f"[1 HIGHEST CASH DEFICIT] DAY: {top1_deficit[0]}, AMOUNT: SGD{-top1_deficit[1]}")
        output.append(f"[2 HIGHEST CASH DEFICIT] DAY: {top2_deficit[0]}, AMOUNT: SGD{-top2_deficit[1]}")
        output.append(f"[3 HIGHEST CASH DEFICIT] DAY: {top3_deficit[0]}, AMOUNT: SGD{-top3_deficit[1]}")

    return scenario, output
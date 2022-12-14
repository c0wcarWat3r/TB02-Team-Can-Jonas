def coh_function(forex): 
    """
    function accepts 1 parameter: forex
    computes the difference in cash on hand each day
    if cash on hand is not consecutively higher, 
    it highlights the day where cash on hand is lower than previous day 
    and value difference
    """
    # Import path method from Pathlib
    from pathlib import Path 
    # Import csv module 
    import csv
    
    # Create 4 empty lists 
    coh=[]
    dd=[]
    d=[]
    results = []

    # Instantiate a file path to the cash on hand csv file 
    file_path = Path.cwd()/"project_group"/"csv_reports"/"cash-on-hand-usd-42.csv"

    # Open file in read mode 
    with file_path.open(mode="r",encoding="UTF-8", newline="") as file: 
        # Create a reader object
        reader = csv.reader(file)
        # Skip the headers
        next(reader)
        for line in reader:
            # Append the cash on hand for each day to the empty list 'coh' and convert them to floats (so difference can be calculated later)
            coh.append(float(line[1]))
            # Append the number of days to the empty list 'd' (stands for days)
            d.append(line[0])
    # Use the total number of days minus 1 so that the for loop would repeat for index 0 to 5.
    day=(len(coh)-1) 
    # i represents index
    # for each index in the range of 0-5,
    for i in range(day):
        # Find the difference between cash on hand for each consecutive day 
        diff=(coh[i+1]-coh[i])
        # Append the list of number of days when there is a cash deficit with the list of the difference in the empty list 'dd' (stands for daily difference)
        dd.append([d[i+1]]+[diff])

    # Convert nested list into a dictionary where the day number is the key and the difference is the value 
    dictionary =dict(dd)
    # set a condition to a new variable 'is_positive' stating that it is true 
    is_positive= True
    # Use a for loop to access the values in the dictionary 
    for cd in dictionary:
        # dictionary[cd] accesses the values (cash on hand difference) and cd is the key 
        # If the cash on hand difference is less than 0,
        if dictionary[cd] < 0: 
            # Append the final message into the empty list 'results'
            # Use dictionary[cd]*forex to convert the difference to SGD 
            # abs() to convert the negative values to a positive value 
            # round() to round the difference to 1 decimal place
            results.append(f"[CASH DEFICIT] DAY: {float(cd)}, AMOUNT: SGD{abs(round(((dictionary[cd])*forex),1))}\n")
            # If this condition is true, is_positive would change to false 
            is_positive= False 
    # After running through the loop above, if is_positive does not change to false and remains true, 
    if is_positive==True:
        # Append this final message into the empty list 'results' instead 
        results.append(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
    # return the list of results 
    return results

    
<<<<<<< HEAD
=======
import cash_on_hand
import profit_loss
import overheads

# Define file paths for each module
cash_csv_file_path = "C:/Users/Admin/OneDrive - Ngee Ann Polytechnic/Programming for Business/P4B FILES/project_group/csv_reports/Cash_on_Hand.csv"
net_profit_csv_file_path = "C:/Users/Admin/OneDrive - Ngee Ann Polytechnic/Programming for Business/P4B FILES/project_group/csv_reports/Profits_and_Loss.csv"
overhead_csv_file_path = "C:/Users/Admin/OneDrive - Ngee Ann Polytechnic/Programming for Business/P4B FILES/project_group/csv_reports/Overheads.csv"

# Analyze cash data
cash_data = cash_on_hand.read_csv(cash_csv_file_path)
cash_result = cash_on_hand.analyse_cash_on_hand(cash_data)

# Analyze net profit data
net_profit_data = profit_loss.read_csv(net_profit_csv_file_path)
net_profit_result = profit_loss.analyse_net_profit(net_profit_data)

# Analyze overhead data
overhead_data = overheads.read_csv(overhead_csv_file_path)
overhead_result = overheads.analyse_overheads(overhead_data)

# Create a summary report file
with open("summary_report.txt", "w") as summary_file:
    summary_file.write(overhead_result + "\n")

    for line in cash_result[1]:
        summary_file.write(line + "\n")

    for line in net_profit_result[1]:
        summary_file.write(line + "\n")


print("Results written to summary_report.txt.")
>>>>>>> f5bf6f541e06e8b312f8b0796761852d2b573229

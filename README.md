
## run in vs code
1. save CSV file (ledger_data.csv) in the same folder as the script (check_balance.py).
2. open a terminal
3. run the script "python check_balance.py"

## output 
1.Prints only the rows where the two values do not match.

## Formula
Current Balance = Previous Balance + Credit - Debit
## working
1. Loads the CSV file using pandas.
2. Calculates the Actual Balance row by row.
3. Compares the Actual Balance with the Recorded Balance.
4. Prints only the rows where the two values do not match.
   

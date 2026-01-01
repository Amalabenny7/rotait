import pandas as pd
def main():
    df=pd.read_csv("ledger_data.csv")
    df["Credit"] = pd.to_numeric(df["Credit"], errors="coerce")
    df["Debit"] = pd.to_numeric(df["Debit"], errors="coerce")
    df["Recorded_Balance"] = pd.to_numeric(df["Recorded_Balance"])
    actual_balances = []
    for i in range(len(df)):
        if i == 0:
            actual_balances.append(df.loc[i,"Recorded_Balance"])
        else:
            previous_balance = actual_balances[i-1]
            current_balance = previous_balance + df.loc[i, "Credit"] - df.loc[i, "Debit"]
            actual_balances.append(current_balance)
    df["Actual_Balance"] = actual_balances
    mismatched = df[df["Actual_Balance"] != df["Recorded_Balance"]]
    if mismatched.empty:
        print(" All balances are correct.")
    else:
        print("Rows with incorrect Recorded Balance:")
        print(mismatched[["Date", "Description", "Credit", "Debit", "Recorded_Balance", "Actual_Balance"]])
    print("Script finished running.")
if __name__ == "__main__":
    main()

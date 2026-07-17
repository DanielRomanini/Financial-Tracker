import sys
import csv
import sqlite3
from flask import Flask, jsonify, render_template


categories = {
    "groceries": {"keywords": ["Publix", "Walmart", "Target", "Kroger", "Aldi", "Whole Foods", "Trader Joe"], "amount": 0},
    "gas": {"keywords": ["RaceTrac", "Marathon", "Chevron", "Shell", "BP", "Sunoco", "Circle K", "Exxon", "Mobil", "Citgo", "Valero"], "amount": 0},
    "restaurants": {"keywords": ["McDonald", "Panda Express", "Chipotle", "Taco Bell", "Bar Louie", "Raising Cane", "Gumbo", "Camila", "La Perla", "Kingdom Sushi", "Panna", "Oakberry", "Butter Smash", "Jaws Hot Chicken", "Insomnia Cookies", "Catalina Cafe", "Florida Fresh"], "amount": 0},
    "food_delivery": {"keywords": ["Uber Eats", "UBER * EATS", "DoorDash", "Grubhub"], "amount": 0},
    "transportation": {"keywords": ["Uber Technologies", "Lyft", "MTA", "PATH TAPP", "NJTRANSIT", "EVOLVE ST"], "amount": 0},
    "subscriptions": {"keywords": ["Spotify", "OPENAI", "ChatGPT", "Apple.com", "Riot"], "amount": 0},
    "entertainment": {"keywords": ["Steam", "STEAMGAMES", "WL *STEAM", "AMNH"], "amount": 0},
    "income": {"keywords": ["THE UNIVERSITY O", "ZELLE FROM", "WELLS FARGO REWARDS", "ONLINE TRANSFER FROM"], "amount": 0},
    "health_personal": {"keywords": ["Walgreens", "GNC", "ALLIANZ"], "amount": 0},
    "travel": {"keywords": ["DELTA AIR", "Airbnb", "UCF CASHIERS"], "amount": 0},
    "transfers": {"keywords": ["ZELLE TO", "ONLINE TRANSFER REF", "ATM WITHDRAWAL"], "amount": 0},
    "other":  {"keywords": ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'], "amount": 0}
    #Other has every letter as a keyword so that any description that doesn't match the other categories will go into other
}


file = open("Checking.csv", 'r')

transactions = []

reader = csv.DictReader(file)

checker = False

for row in reader:           #row is list: description, amount, etc
    for cat in categories:   #cat is list: groceries, gas, etc)
        for keyword in categories[cat]["keywords"]:      #keyword is word: Publix, Target, etc
            if keyword.lower() in row["DESCRIPTION"].lower():
                transactions.append({"Type": f"{cat}", "Amount": float(row["AMOUNT"]), "Date": f"{row["DATE"].replace("/","-")}", "Description": row["DESCRIPTION"]})
                categories[cat]["amount"] += float(row["AMOUNT"])
                checker = True
                break

        if checker:
            checker = False
            break


            
file.close()  
   
#for amt in categories: #Debugging purposes
 #  print(f"Amount for {amt}:  {round(categories[amt]['amount'],2)}")

#ALL OF CODE ABOVE WAS TO SORT TRANSACTIONS INTO CATEGORIES AND LIST DIFFERENT TRANSACTIONS INTO DICS




#BELOW IS INCORPORATION OF SQLITE3

connection = sqlite3.connect("Transactions.db")   #Creates database
cursor = connection.cursor()                      #Gives me a way of sending commands to database

cursor.execute("CREATE TABLE IF NOT EXISTS transactions(id INTEGER PRIMARY KEY AUTOINCREMENT, Type TEXT, Amount REAL, Description TEXT, Date TEXT)")

cursor.execute("DELETE FROM transactions") #Deletes all transactions so new CSV file can be uploaded
cursor.execute("DELETE FROM sqlite_sequence WHERE name='transactions'") #Restarts the count for id

for trans in transactions: #Adds each individual transaction into transactions table in the database
    cursor.execute("INSERT INTO transactions(Type, Amount, Description, Date) VALUES (?, ?, ?, ?)", (trans["Type"], trans["Amount"], trans["Description"], trans["Date"]))

connection.commit() #Without this, no actual changes are being permanently ran in the database.


#INCORPORATION OF FLASK STARTS BELOW

app = Flask(__name__)



@app.route("/api/transactions") #GETS A LIST OF ALL TRANSACTIONS
def transactions():
    connection = sqlite3.connect("Transactions.db")   #Creates connection to database
    cursor = connection.cursor()                      #Gives me a way of sending commands to database
    cursor.execute("SELECT * FROM transactions")
    transact = cursor.fetchall()
    transactions_list = []
    for tup in transact:
        i = 0
        temp = {"id": "", "Type": "","Amount": "", "Description": "", "Date": ""}
        for key in temp:
            temp[key] = tup[i]
            i+=1
        transactions_list.append(temp)
    return jsonify(transactions_list)

@app.route("/transactions")
def trans():
    return render_template('transactions.html')


@app.route("/api/transactions/<type>") #GETS A LIST OF TRANSACTIONS ACCORDING TO SPECIFIC TYPE OF TRANSACTION
def transaction_per_type(type):
    connection = sqlite3.connect("Transactions.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM transactions WHERE type = ?", (type,))
    tuple_list = cursor.fetchall()
    transactions_list = []
    for tup in tuple_list:
        i = 0
        temp = {"id": "", "Type": "","Amount": "", "Description": "", "Date": ""}
        for key in temp:
            temp[key] = tup[i]
            i+=1
        transactions_list.append(temp)
    return jsonify(transactions_list)

@app.route("/transactions/<type>")
def transac_per_type(type):
    return render_template('transactions.html')



@app.route("/api/transactions/<type>/total") #GETS TOTAL OF TRANSACTIONS FOR WHICHEVER TYPE YOU WANT
def total_per_type(type):
    connection = sqlite3.connect("Transactions.db")
    cursor = connection.cursor()
    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type = ?",(type,))
    total = cursor.fetchall()
    return jsonify(total[0][0])

@app.route("/transactions/<type>/total")
def tot_per_type(type):
    return render_template("transactions.html")


@app.route("/api/transactions/date/<date>") #RETURNS TRANSACTIONS ON A SPECIFIC DATE
def transactions_date(date):
    connection = sqlite3.connect("Transactions.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM transactions WHERE Date = ?",(date,))
    tuple_list = cursor.fetchall()
    transactions_list = []
    for tup in tuple_list:
        i = 0
        temp = {"id": "", "Type": "","Amount": "", "Description": "", "Date": ""}
        for key in temp:
            temp[key] = tup[i]
            i+=1
        transactions_list.append(temp)
    return jsonify(transactions_list)

@app.route("/transactions/date/<date>")
def trans_date(date):
    return render_template("transactions.html")

@app.route("/api/totals") #RETURNS TOTALS OF ALL TRANSACTIONS GROUPED BY TYPE
def totals():
    connection = sqlite3.connect("Transactions.db")
    cursor = connection.cursor()
    cursor.execute("SELECT SUM(Amount), Type FROM transactions GROUP BY Type")
    tuple_list = cursor.fetchall()
    totals_list = []
    total = 0
    for tup in tuple_list:
        totals = {"Type": "", "Total": ""}
        totals["Type"] = tup[1]
        totals["Total"] = tup[0]
        totals_list.append(totals)
        total += tup[0]
    temp = {"Type": "Total", "Total": total}
    totals_list.append(temp)
    return jsonify(totals_list)

@app.route("/totals")
def tots():
    return render_template("transactions.html")


@app.route("/api/summary") #Shows how much you've spent, how much you've gained, and the difference between those
def summary():
    connection = sqlite3.connect("Transactions.db")
    cursor = connection.cursor()
    cursor.execute("SELECT SUM(Amount) FROM transactions WHERE Amount > 0")
    tuples = cursor.fetchall()
    transactions = []
    net = tuples[0][0]
    temp = {"Income": tuples[0][0]}
    transactions.append(temp)
    cursor.execute("SELECT SUM(Amount) FROM transactions WHERE Amount < 0")
    tuples = cursor.fetchall()
    net += tuples[0][0]
    temp = {"Spent": tuples[0][0]}
    transactions.append(temp)
    temp = {"Net": net}
    transactions.append(temp)
    return jsonify(transactions)

@app.route("/summary")
def sum():
    return render_template('transactions.html')



@app.route('/') #Initial dashboard where you're launched to
def home():
    return render_template('index.html')


if __name__ == "__main__": #Checks that the file was run directly
    app.run(debug=True)    #app.run() starts a local server, debug=True has some conveniences
    
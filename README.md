## Bank Test

[Specification](#specification) |[Acceptance criteria](#acceptance criteria) |[Design](#design) | [Installation](#installation) | [Resources](#resources)

## Specification

* Be able to interact with code via IRB.  (You don't need to implement a command line interface that takes input from STDIN.)
* Deposits, withdrawal.
* Account statement (date, amount, balance) printing.
* Data can be kept in memory (it doesn't need to be stored to a database or anything).

### Acceptance criteria

**Given** a client makes a deposit of 1000 on 10-01-2012
**And** a deposit of 2000 on 13-01-2012
**And** a withdrawal of 500 on 14-01-2012
**When** she prints her bank statement
**Then** she would see

```
date       || credit || debit   || balance
14/01/2012 ||        || 500.00  || 2500.00
13/01/2012 || 2000.00||         || 3000.00
10/01/2012 || 1000.00||         || 1000.00
```

## Design

Variable name    | Type  		| Comment
------------------ | -------------------	| ---------------------------
Deposit | Number(float) | Amount added to balance  
Withdrawal | Number(float) | Amount deducted from balance
Statement | Number(float), Date | Stores date, amount and balance

Class    | Functions  	    	| Comment 
------------------ | -------------------	| ---------------------------
Account *changes the balance*  | deposit(*amount, date*)  | adds amount to balance on given date 
                               | withdrawal(*amount, date*)  | deducts amount from balance on given date
Bank *displays the statement*  | history(*balance, deposit, withdrawal*)  | stores deposit and withdrawal history
                               | statement(*account, history*)            | displays account statement 
 
## Installation

## Resources

- Official Python docs https://docs.python.org/3/
- Python Program Design https://youtu.be/bbVkQ0evqzw


# Bank account example
# class BankAccount:
#     def __init__(self, account_number, account_holder, balance):
#         self.account_number = account_number        # Public attribute
#         self._account_holder = account_holder       # Protected attribute
#         self.__balance = balance                    # Private attribute

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f" Deposited ₹{amount}. New Balance: ₹{self.__balance}")
#         else:
#             print(" Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if amount <= 0:
#             print(" Withdrawal amount must be positive.")
#         elif amount > self.__balance:
#             print("Insufficient balance.")
#         else:
#             self.__balance -= amount
#             print(f" Withdrawn ₹{amount}. Remaining Balance: ₹{self.__balance}")

#     def check_balance(self):
#         print(f" Current Balance: ₹{self.__balance}")

#     def profile(self):
#         print("\n------ Bank Account Profile ------")
#         print(f"Account Holder : {self._account_holder}")
#         print(f"Account Number : {self.account_number}")
#         print("----------------------------------")


# class Loan:
#     def __init__(self, applicant_name, loan_amount, cibil_score):
#         self._applicant_name = applicant_name       # Protected attribute
#         self.__loan_amount = loan_amount            # Private attribute
#         self.__cibil_score = cibil_score            # Private attribute
#         self.__approved = False                     # Private attribute

#     def check_eligibility(self):
#         print(f"\nChecking loan eligibility for {self._applicant_name}...")
#         if self.__cibil_score >= 750:
#             self.__approved = True
#             print("Loan Approved")
#         elif self.__cibil_score >= 650:
#             print(" CIBIL score is average. Needs manual review.")
#         else:
#             print(" Loan Rejected due to low CIBIL score.")

#     def profile(self):
#         print("\n-------- Loan Profile --------")
#         print(f"Applicant Name : {self._applicant_name}")
#         print(f"Loan Amount    : ₹{self.__loan_amount}")
#         print(f"CIBIL Score    : {self.__cibil_score}")
#         print(f"Loan Status    : {'Approved' if self.__approved else 'Not Approved'}")
#         print("------------------------------")

#     def is_approved(self):
#         return self.__approve

# # Bank account example
# dev_account = BankAccount(11312, "Dev", 97)
# dev_account.profile()
# dev_account.check_balance()
# dev_account.deposit(10000)
# dev_account.withdraw(97)
# dev_account.check_balance()

# # Loan example
# dev_loan = Loan("Dev", 500000, 745)
# dev_loan.profile()
# dev_loan.check_eligibility()
# dev_loan.profile()





#Example 3..
class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number        # Public attribute
        self._account_holder = account_holder       # Protected attribute
        self.__balance = balance                    # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"✅ Deposited ₹{amount}. New Balance: ₹{self.__balance}")
        else:
            print("❌ Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("❌ Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"✅ Withdrawn ₹{amount}. Remaining Balance: ₹{self.__balance}")

    def check_balance(self):
        print(f"💰 Current Balance: ₹{self.__balance}")

    def profile(self):
        print("\n------ Bank Account Profile ------")
        print(f"Account Holder : {self._account_holder}")
        print(f"Account Number : {self.account_number}")
        print("----------------------------------")


class Loan:
    def __init__(self, applicant_name, loan_amount, cibil_score):
        self._applicant_name = applicant_name       # Protected attribute
        self.__loan_amount = loan_amount            # Private attribute
        self.__cibil_score = cibil_score            # Private attribute
        self.__approved = False                     # Private attribute

    def get_cibil_score(self):
        return self.__cibil_score

    def get_loan_amount(self):
        return self.__loan_amount

    def approve(self):
        self.__approved = True

    def is_approved(self):
        return self.__approved

    def profile(self):
        print("\n-------- Loan Profile --------")
        print(f"Applicant Name : {self._applicant_name}")
        print(f"Loan Amount    : ₹{self.__loan_amount}")
        print(f"CIBIL Score    : {self.__cibil_score}")
        print(f"Loan Status    : {'Approved' if self.__approved else 'Not Approved'}")
        print("------------------------------")


class LoanApproval:
    def __init__(self, loan: Loan):
        self.loan = loan

    def process(self):
        print(f"\n🔎 Processing loan for {self.loan._applicant_name}...")
        cibil = self.loan.get_cibil_score()

        if cibil >= 750:
            self.loan.approve()
            print("✅ Loan Approved Automatically.")
        elif cibil >= 650:
            print("⚠️  CIBIL score is average. Manual verification required.")
        else:
            print("❌ Loan Rejected due to low CIBIL score.")


# === Example Usage ===

# Create bank account
account = BankAccount(11312, "Dev", 5000)
account.profile()
account.check_balance()

# Create loan
loan = Loan("Dev", 200000, 710)
loan.profile()

# Process loan approval
approval = LoanApproval(loan)
approval.process()

# Check final loan profile
loan.profile()

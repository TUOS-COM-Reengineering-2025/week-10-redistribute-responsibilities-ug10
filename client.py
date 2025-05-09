from Account import Account
from Bank import Bank
from Branch import Branch
from Staff import Staff
from Customer import Customer
from Payroll import Payroll


def client():
    # This mimics the behaviour of a "client" of the Banking system "server" APIs. 
    
    bank = Bank()

    branch_london = Branch(location="London", opening_time="9:00")
    bank.setup_branch(branch_london)
    assert branch_london in bank.branches
    assert branch_london.get_opening_times() == "9:00"

    branch_london.change_opening_time(time="8:00")
    assert branch_london.get_opening_times() == "8:00"

    staff_john = Staff(name="John")
    branch_london.add_staff_member(staff=staff_john)
    assert staff_john in branch_london.get_staff()

    branch_sheffield = Branch(location="Sheffield", opening_time="9:00")
    bank.setup_branch(branch_sheffield)
    assert branch_sheffield in bank.branches
    assert branch_sheffield.get_opening_times() == "9:00"

    bank.close_branch(branch=branch_london, transfer_branch=branch_sheffield)
    assert branch_london not in bank.branches
    assert branch_sheffield in bank.branches
    assert staff_john in branch_sheffield.get_staff()

    customer_alice = Customer(name="Alice")
    account_alice = Account()
    bank.setup_new_account(account=account_alice, customer=customer_alice)
    assert account_alice in bank.accounts
    assert customer_alice in bank.customers
    assert bank.customer_addresses[customer_alice] == "NO ADDRESS"
    assert bank.customer_phone_numbers[customer_alice] == "NO PHONE NUMBER"

    account_alice_new = Account()
    bank.setup_new_account(account=account_alice_new, customer=customer_alice)
    assert account_alice_new in bank.accounts
    assert len(bank.customers) == 1

    bank.add_funds(account=account_alice, amount=1000)
    assert account_alice.get_balance() == 1000.0

    bank.add_interest(account=account_alice)
    assert account_alice.get_balance() == 1000.0 + 0.05 * 1000.0

    bank.close_account(account=account_alice)
    assert account_alice.get_balance() == 0
    assert account_alice.get_customer() is None
    assert account_alice not in bank.accounts

    payroll = Payroll()
    bank.change_payroll_date(payroll=payroll, date="31", staff_category="Manager")
    assert payroll.get_staff_category_pay_day("Manager") == "31"

    return True

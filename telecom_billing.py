from datetime import datetime

# Class representing a Customer
class Customer:
    def __init__(self, customer_id, first_name, last_name, phone, subscription_plan):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.subscription_plan = subscription_plan

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

# Class representing a Subscription Plan
class SubscriptionPlan:
    def __init__(self, name, monthly_fee):
        self.name = name
        self.monthly_fee = monthly_fee

# Class representing a Bill
class Bill:
    def __init__(self, customer, amount):
        self.customer = customer
        self.amount = amount
        self.billing_date = datetime.now()

    def print_bill(self):
        print("----- Telecom Bill -----")
        print(f"Customer: {self.customer.full_name()}")
        print(f"Plan: {self.customer.subscription_plan}")
        print(f"Amount: ${self.amount:.2f}")
        print(f"Billing Date: {self.billing_date.strftime('%Y-%m-%d')}")
        print("-----------------------\n")

# Main simulation
def main():
    # Create subscription plans
    basic_plan = SubscriptionPlan("Basic", 10.0)
    premium_plan = SubscriptionPlan("Premium", 25.0)

    # Create customers
    c1 = Customer(1, "Ali", "Rezaei", "+989123456789", basic_plan.name)
    c2 = Customer(2, "Sara", "Ahmadi", "+989876543210", premium_plan.name)

    customers = [c1, c2]

    # Generate and print bills for each customer
    for customer in customers:
        if customer.subscription_plan == "Basic":
            bill_amount = basic_plan.monthly_fee
        elif customer.subscription_plan == "Premium":
            bill_amount = premium_plan.monthly_fee
        else:
            bill_amount = 0  # Default or unknown plan

        bill = Bill(customer, bill_amount)
        bill.print_bill()

if __name__ == "__main__":
    main()

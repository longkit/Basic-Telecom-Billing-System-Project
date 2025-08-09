import tkinter as tk
from tkinter import messagebox
from telecom_billing import Customer, Bill

def update_price(event=None):
    selected_plan = plan_var.get()
    if selected_plan == "Basic":
        price_var.set("$10.00")
    elif selected_plan == "Premium":
        price_var.set("$25.00")
    else:
        price_var.set("$0.00")

def generate_bill():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    phone = entry_phone.get()
    plan = plan_var.get()

    if plan == "Basic":
        amount = 10
    elif plan == "Premium":
        amount = 25
    else:
        amount = 0

    customer = Customer(1, first_name, last_name, phone, plan)
    bill = Bill(customer, amount)

    bill_text = (
        f"Customer: {customer.full_name()}\n"
        f"Plan: {plan}\n"
        f"Amount: ${amount:.2f}\n"
        f"Billing Date: {bill.billing_date.strftime('%Y-%m-%d')}"
    )

    messagebox.showinfo("Generated Bill", bill_text)

root = tk.Tk()
root.title("Telecom Billing System")

tk.Label(root, text="First Name:").grid(row=0, column=0, sticky="e")
entry_first_name = tk.Entry(root)
entry_first_name.grid(row=0, column=1)

tk.Label(root, text="Last Name:").grid(row=1, column=0, sticky="e")
entry_last_name = tk.Entry(root)
entry_last_name.grid(row=1, column=1)

tk.Label(root, text="Phone:").grid(row=2, column=0, sticky="e")
entry_phone = tk.Entry(root)
entry_phone.grid(row=2, column=1)

tk.Label(root, text="Plan:").grid(row=3, column=0, sticky="e")

plan_var = tk.StringVar()
plan_dropdown = tk.OptionMenu(root, plan_var, "Basic", "Premium", command=update_price)
plan_dropdown.grid(row=3, column=1)
plan_var.set("Basic")  # default value

tk.Label(root, text="Price:").grid(row=4, column=0, sticky="e")
price_var = tk.StringVar(value="$10.00")
price_label = tk.Label(root, textvariable=price_var)
price_label.grid(row=4, column=1, sticky="w")

tk.Button(root, text="Generate Bill", command=generate_bill).grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()

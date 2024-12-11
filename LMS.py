import tkinter as tk
from tkinter import messagebox

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1500x800+0+0")
        self.root.config(bg="#f0f0f0")

        self.create_login_screen()

    def create_login_screen(self):
        self.clear_screen()
        title = tk.Label(self.root, text="Library Management System", bg="powder blue", fg="green", bd=20, relief=tk.RIDGE, font=("times new roman", 30, "bold"), padx=2, pady=6)
        title.pack(pady=20)

        admin_button = tk.Button(self.root, text="Admin Login", command=self.create_admin_login, font=("Arial", 12), bg="#007BFF", fg="white", width=20, height=2)
        admin_button.pack(pady=10)

        user_button = tk.Button(self.root, text="User Login", command=self.create_user_login, font=("Arial", 12), bg="#28A745", fg="white", width=20, height=2)
        user_button.pack(pady=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_admin_login(self):
        self.clear_screen()
        title = tk.Label(self.root, text="Admin Login", font=("Arial", 18, "bold"), bg="#f0f0f0")
        title.pack(pady=20)

        tk.Label(self.root, text="Admin ID", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        self.admin_id_entry = tk.Entry(self.root, font=("Arial", 12))
        self.admin_id_entry.pack(pady=5)

        tk.Label(self.root, text="Password", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        self.admin_password_entry = tk.Entry(self.root, show="*", font=("Arial", 12))
        self.admin_password_entry.pack(pady=5)

        login_button = tk.Button(self.root, text="Login", command=self.admin_login, font=("Arial", 12), bg="#007BFF", fg="white", width=10)
        login_button.pack(pady=10)

        back_button = tk.Button(self.root, text="Back", command=self.create_login_screen, font=("Arial", 12), bg="#6c757d", fg="white", width=10)
        back_button.pack(pady=10)

    def create_user_login(self):
        self.clear_screen()
        title = tk.Label(self.root, text="User Login", font=("Arial", 18, "bold"), bg="#f0f0f0")
        title.pack(pady=20)

        tk.Label(self.root, text="User ID", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        self.user_id_entry = tk.Entry(self.root, font=("Arial", 12))
        self.user_id_entry.pack(pady=5)

        tk.Label(self.root, text="Password", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        self.user_password_entry = tk.Entry(self.root, show="*", font=("Arial", 12))
        self.user_password_entry.pack(pady=5)

        login_button = tk.Button(self.root, text="Login", command=self.user_login, font=("Arial", 12), bg="#28A745", fg="white", width=10)
        login_button.pack(pady=10)

        back_button = tk.Button(self.root, text="Back", command=self.create_login_screen, font=("Arial", 12), bg="#6c757d", fg="white", width=10)
        back_button.pack(pady=10)

    def admin_login(self):
        admin_id = self.admin_id_entry.get()
        password = self.admin_password_entry.get()
        if admin_id == "admin" and password == "admin123":
            self.create_admin_home_page()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")

    def user_login(self):
        user_id = self.user_id_entry.get()
        password = self.user_password_entry.get()
        if user_id == "user" and password == "user123":
            self.create_user_home_page()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")


    def create_admin_home_page(self):
        self.clear_screen()
        title = tk.Label(self.root, text="Admin Home Page", font=("times new roman", 40, "bold"), bg="powder blue", fg="green", bd=10, relief=tk.RIDGE)
        title.pack(side=tk.TOP, fill=tk.X)
        
        navigation_frame = tk.Frame(self.root, bd=10, relief=tk.RIDGE, bg="powder blue")
        navigation_frame.place(x=0, y=70, width=1550, height=70)
        
        maintenance_button = tk.Button(navigation_frame, text="Book Management", font=("Arial", 12), bg="#007BFF", fg="white", width=15, command=self.maintenance)
        maintenance_button.grid(row=0, column=0, padx=10, pady=10)
        
        reports_button = tk.Button(navigation_frame, text="Reports", font=("Arial", 12), bg="#007BFF", fg="white", width=15, command=self.reports)
        reports_button.grid(row=0, column=1, padx=10, pady=10)
        
        transactions_button = tk.Button(navigation_frame, text="Transactions", font=("Arial", 12), bg="#007BFF", fg="white", width=15, command=self.transactions)
        transactions_button.grid(row=0, column=2, padx=10, pady=10)
        
        back_button = tk.Button(navigation_frame, text="Back", font=("Arial", 12), bg="#6c757d", fg="white", width=10, command=self.create_login_screen)
        back_button.grid(row=0, column=3, padx=10, pady=10)
        
        logout_button = tk.Button(navigation_frame, text="Log Out", font=("Arial", 12), bg="#dc3545", fg="white", width=10, command=self.create_login_screen)
        logout_button.grid(row=0, column=4, padx=10, pady=10)
        
    def maintenance(self):
        self.clear_screen()
        title = tk.Label(self.root, text="Book Management", font=("times new roman", 40, "bold"), bg="powder blue", fg="green", bd=10, relief=tk.RIDGE)
        title.pack(side=tk.TOP, fill=tk.X)
        
        back_button = tk.Button(self.root, text="Back", font=("Arial", 12), bg="#6c757d", fg="white", width=10, command=self.create_admin_home_page)
        back_button.pack(pady=10)
    def reports(self):
        self.clear_screen()
        title = tk.Label(self.root, text="Reports", font=("times new roman", 40, "bold"), bg="powder blue", fg="green", bd=10, relief=tk.RIDGE)
        title.pack(side=tk.TOP, fill=tk.X)
        
        back_button = tk.Button(self.root, text="Back", font=("Arial", 12), bg="#6c757d", fg="white", width=10, command=self.create_admin_home_page)
        back_button.pack(pady=10)
    def transactions(self):
        self.clear_screen()
        title = tk.Label(self.root, text="Transactions", font=("times new roman", 40, "bold"), bg="powder blue", fg="green", bd=10, relief=tk.RIDGE)
        title.pack(side=tk.TOP, fill=tk.X)
        
        back_button = tk.Button(self.root, text="Back", font=("Arial", 12), bg="#6c757d", fg="white", width=10, command=self.create_admin_home_page)
        back_button.pack(pady=10)



    def create_user_home_page(self):
        self.clear_screen()
        title = tk.Label(self.root, text="User Home Page", font=("times new roman", 40, "bold"), bg="powder blue", fg="green", bd=10, relief=tk.RIDGE)
        title.pack(side=tk.TOP, fill=tk.X)
        
        navigation_frame = tk.Frame(self.root, bd=10, relief=tk.RIDGE, bg="powder blue")
        navigation_frame.place(x=0, y=70, width=1550, height=70)
        
        reports_button = tk.Button(navigation_frame, text="Reports", font=("Arial", 12), bg="#007BFF", fg="white", width=15, command=self.reports)
        reports_button.grid(row=0, column=0, padx=10, pady=10)
        
        transactions_button = tk.Button(navigation_frame, text="Transactions", font=("Arial", 12), bg="#007BFF", fg="white", width=15, command=self.transactions)
        transactions_button.grid(row=0, column=1, padx=10, pady=10)
        
        back_button = tk.Button(navigation_frame, text="Back", font=("Arial", 12), bg="#6c757d", fg="white", width=10, command=self.create_login_screen)
        back_button.grid(row=0, column=2, padx=10, pady=10)

        logout_button = tk.Button(navigation_frame, text="Log Out", font=("Arial", 12), bg="#dc3545", fg="white", width=10, command=self.create_login_screen)
        logout_button.grid(row=0, column=4, padx=10, pady=10)

    def reports(self):
        self.clear_screen()
        title = tk.Label(self.root, text="Reports", font=("times new roman", 40, "bold"), bg="powder blue", fg="green", bd=10, relief=tk.RIDGE)
        title.pack(side=tk.TOP, fill=tk.X)
        
        back_button = tk.Button(self.root, text="Back", font=("Arial", 12), bg="#6c757d", fg="white", width=10, command=self.create_admin_home_page)
        back_button.pack(pady=10)
    def transactions(self):
        self.clear_screen()
        title = tk.Label(self.root, text="Transactions", font=("times new roman", 40, "bold"), bg="powder blue", fg="green", bd=10, relief=tk.RIDGE)
        title.pack(side=tk.TOP, fill=tk.X)
        
        back_button = tk.Button(self.root, text="Back", font=("Arial", 12), bg="#6c757d", fg="white", width=10, command=self.create_admin_home_page)
        back_button.pack(pady=10)

    def maintenance(self):
        self.clear_screen()
        title = tk.Label(self.root, text="Book Management", font=("times new roman", 40, "bold"), bg="powder blue", fg="green", bd=10, relief=tk.RIDGE)
        title.pack(side=tk.TOP, fill=tk.X)

        navigation_frame = tk.Frame(self.root, bd=10, relief=tk.RIDGE, bg="powder blue")
        navigation_frame.place(x=0, y=70, width=1550, height=70)

        add_membership_button = tk.Button(navigation_frame, text="Add Membership", font=("Arial", 12), bg="#007BFF", fg="white", width=15, command=self.add_membership)
        add_membership_button.grid(row=0, column=0, padx=10, pady=10)

        update_membership_button = tk.Button(navigation_frame, text="Update Membership", font=("Arial", 12), bg="#007BFF", fg="white", width=15, command=self.update_membership)
        update_membership_button.grid(row=0, column=1, padx=10, pady=10)

        add_book_button = tk.Button(navigation_frame, text="Add Book", font=("Arial", 12), bg="#007BFF", fg="white", width=15, command=self.add_book)
        add_book_button.grid(row=0, column=2, padx=10, pady=10)

        update_book_button = tk.Button(navigation_frame, text="Update Book", font=("Arial", 12), bg="#007BFF", fg="white", width=15, command=self.update_book)
        update_book_button.grid(row=0, column=3, padx=10, pady=10)

        user_management_button = tk.Button(navigation_frame, text="User Management", font=("Arial", 12), bg="#007BFF", fg="white", width=15, command=self.user_management)
        user_management_button.grid(row=0, column=4, padx=10, pady=10)

        back_button = tk.Button(navigation_frame, text="Back", font=("Arial", 12), bg="#6c757d", fg="white", width=10, command=self.create_admin_home_page)
        back_button.grid(row=0, column=5, padx=10, pady=10)

        back_button = tk.Button(navigation_frame, text="Back", font=("Arial", 12), bg="#6c757d", fg="white", width=10, command=self.create_admin_home_page)
        back_button.grid(row=0, column=5, padx=10, pady=10)

# Add Membership Function
    def add_membership(self):
        self.clear_screen()
        title = tk.Label(self.root, text="Add Membership", font=("times new roman", 40, "bold"), bg="powder blue", fg="green", bd=10, relief=tk.RIDGE)
        title.pack(side=tk.TOP, fill=tk.X)

        form_frame = tk.Frame(self.root, bg="#f0f0f0")
        form_frame.place(x=400, y=150, width=750, height=400)

        tk.Label(form_frame, text="User ID", font=("Arial", 14), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.user_id_entry = tk.Entry(form_frame, font=("Arial", 14))
        self.user_id_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        tk.Label(form_frame, text="Membership Duration", font=("Arial", 14), bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.membership_duration = tk.StringVar(value="6 months")
        duration_dropdown = tk.OptionMenu(form_frame, self.membership_duration, "6 months", "1 year", "2 years")
        duration_dropdown.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        submit_button = tk.Button(form_frame, text="Add Membership", font=("Arial", 14), bg="#007BFF", fg="white", width=15, command=self.submit_add_membership)
        submit_button.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        back_button = tk.Button(form_frame, text="Back", font=("Arial", 12), bg="#6c757d", fg="white", width=10, command=self.maintenance)
        back_button.grid(row=3, column=1, padx=10, pady=10, sticky='w')

    def submit_add_membership(self):
        user_id = self.user_id_entry.get()
        duration = self.membership_duration.get()
        messagebox.showinfo("Success", f"Membership added for User ID: {user_id} for duration: {duration}")
        self.maintenance()

# Update Membership Function
    def update_membership(self):
        self.clear_screen()
        title = tk.Label(self.root, text="Update Membership", font=("times new roman", 40, "bold"), bg="powder blue", fg="green", bd=10, relief=tk.RIDGE)
        title.pack(side=tk.TOP, fill=tk.X)

        form_frame = tk.Frame(self.root, bg="#f0f0f0")
        form_frame.place(x=400, y=150, width=750, height=400)

        tk.Label(form_frame, text="Membership Number", font=("Arial", 14), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.membership_no_entry = tk.Entry(form_frame, font=("Arial", 14))
        self.membership_no_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        tk.Label(form_frame, text="Update Duration", font=("Arial", 14), bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.update_duration = tk.StringVar(value="6 months")
        duration_dropdown = tk.OptionMenu(form_frame, self.update_duration, "6 months", "1 year", "2 years")
        duration_dropdown.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        submit_button = tk.Button(form_frame, text="Update Membership", font=("Arial", 14), bg="#007BFF", fg="white", width=20, command=self.submit_update_membership)
        submit_button.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        back_button = tk.Button(form_frame, text="Back", font=("Arial", 12), bg="#6c757d", fg="white", width=10, command=self.maintenance)
        back_button.grid(row=3, column=1, padx=10, pady=10, sticky='w')

    def submit_update_membership(self):
    # Code to handle membership update
        membership_no = self.membership_no_entry.get()
        duration = self.update_duration.get()
        messagebox.showinfo("Success", f"Membership No: {membership_no} updated with duration: {duration}")
        self.maintenance

    def reports(self):
        self.clear_screen()
        title = tk.Label(self.root, text="Reports", font=("times new roman", 40, "bold"), bg="powder blue", fg="green", bd=10, relief=tk.RIDGE)
        title.pack(side=tk.TOP, fill=tk.X)

        navigation_frame = tk.Frame(self.root, bd=10, relief=tk.RIDGE, bg="powder blue")
        navigation_frame.place(x=0, y=70, width=1550, height=70)

        active_issues_button = tk.Button(navigation_frame, text="Active Issues", font=("Arial", 12), bg="#007BFF", fg="white", width=15, command=self.active_issues_report)
        active_issues_button.grid(row=0, column=0, padx=10, pady=10)

        membership_list_button = tk.Button(navigation_frame, text="Master List of Memberships", font=("Arial", 12), bg="#007BFF", fg="white", width=25, command=self.membership_list_report)
        membership_list_button.grid(row=0, column=1, padx=10, pady=10)

        movies_list_button = tk.Button(navigation_frame, text="Master List of Movies", font=("Arial", 12), bg="#007BFF", fg="white", width=20, command=self.movies_list_report)
        movies_list_button.grid(row=0, column=2, padx=10, pady=10)

        books_list_button = tk.Button(navigation_frame, text="Master List of Books", font=("Arial", 12), bg="#007BFF", fg="white", width=20, command=self.books_list_report)
        books_list_button.grid(row=0, column=3, padx=10, pady=10)

        overdue_returns_button = tk.Button(navigation_frame, text="Overdue Returns", font=("Arial", 12), bg="#007BFF", fg="white", width=20, command=self.overdue_returns_report)
        overdue_returns_button.grid(row=0, column=4, padx=10, pady=10)

        pending_issues_button = tk.Button(navigation_frame, text="Pending Issues Requests", font=("Arial", 12), bg="#007BFF", fg="white", width=20, command=self.pending_issues_report)
        pending_issues_button.grid(row=0, column=5, padx=10, pady=10)

        back_button = tk.Button(navigation_frame, text="Back", font=("Arial", 12), bg="#6c757d", fg="white", width=10, command=self.create_admin_home_page)
        back_button.grid(row=0, column=6, padx=10, pady=10)

    def active_issues_report(self):
    # Add your logic to display the active issues report here
        pass

    def membership_list_report(self):
    # Add your logic to display the master list of memberships here
        pass

    def movies_list_report(self):
    # Add your logic to display the master list of movies here
        pass

    def books_list_report(self):
    # Add your logic to display the master list of books here
        pass

    def overdue_returns_report(self):
    # Add your logic to display the overdue returns report here
        pass

    def pending_issues_report(self):
    # Add your logic to display the pending issues requests report here
        pass


    def transactions(self):
        self.clear_screen()
        title = tk.Label(self.root, text="Transactions", font=("times new roman", 40, "bold"), bg="powder blue", fg="green", bd=10, relief=tk.RIDGE)
        title.pack(side=tk.TOP, fill=tk.X)

        navigation_frame = tk.Frame(self.root, bd=10, relief=tk.RIDGE, bg="powder blue")
        navigation_frame.place(x=0, y=70, width=1550, height=70)

        check_availability_button = tk.Button(navigation_frame, text="Check Book Availability", font=("Arial", 12), bg="#007BFF", fg="white", width=20, command=self.check_book_availability)
        check_availability_button.grid(row=0, column=0, padx=10, pady=10)

        issue_book_button = tk.Button(navigation_frame, text="Issue a Book", font=("Arial", 12), bg="#007BFF", fg="white", width=20, command=self.issue_book)
        issue_book_button.grid(row=0, column=1, padx=10, pady=10)

        return_book_button = tk.Button(navigation_frame, text="Return a Book", font=("Arial", 12), bg="#007BFF", fg="white", width=20, command=self.return_book)
        return_book_button.grid(row=0, column=2, padx=10, pady=10)

        back_button = tk.Button(navigation_frame, text="Back", font=("Arial", 12), bg="#6c757d", fg="white", width=10, command=self.create_user_home_page)
        back_button.grid(row=0, column=3, padx=10, pady=10)

    def check_book_availability(self):
        self.clear_screen()
        title = tk.Label(self.root, text="Check Book Availability", font=("times new roman", 40, "bold"), bg="powder blue", fg="green", bd=10, relief=tk.RIDGE)
        title.pack(side=tk.TOP, fill=tk.X)
    
        tk.Label(self.root, text="Enter Book Name or Serial Number:", font=("Arial", 12)).pack(pady=5)
        self.book_search_entry = tk.Entry(self.root, font=("Arial", 12))
        self.book_search_entry.pack(pady=5)
    
        search_button = tk.Button(self.root, text="Search", font=("Arial", 12), bg="#28A745", fg="white", width=10, command=self.perform_book_search)
        search_button.pack(pady=10)
    
        back_button = tk.Button(self.root, text="Back", font=("Arial", 12), bg="#6c757d", fg="white", width=10, command=self.transactions)
        back_button.pack(pady=10)

    def perform_book_search(self):
    # Add logic to search for the book here
        book_search_query = self.book_search_entry.get()
        messagebox.showinfo("Search Result", f"Searching for: {book_search_query}")

    def issue_book(self):
        self.clear_screen()
        title = tk.Label(self.root, text="Issue a Book", font=("times new roman", 40, "bold"), bg="powder blue", fg="green", bd=10, relief=tk.RIDGE)
        title.pack(side=tk.TOP, fill=tk.X)
    
        tk.Label(self.root, text="Enter Book Serial Number:", font=("Arial", 12)).pack(pady=5)
        self.book_serial_entry = tk.Entry(self.root, font=("Arial", 12))
        self.book_serial_entry.pack(pady=5)
    
        tk.Label(self.root, text="Enter User ID:", font=("Arial", 12)).pack(pady=5)
        self.user_id_entry = tk.Entry(self.root, font=("Arial", 12))
        self.user_id_entry.pack(pady=5)
    
        issue_button = tk.Button(self.root, text="Issue", font=("Arial", 12), bg="#28A745", fg="white", width=10, command=self.perform_issue_book)
        issue_button.pack(pady=10)
    
        back_button = tk.Button(self.root, text="Back", font=("Arial", 12), bg="#6c757d", fg="white", width=10, command=self.transactions)
        back_button.pack(pady=10)

    def perform_issue_book(self):
    # Add logic to issue the book here
        book_serial = self.book_serial_entry.get()
        user_id = self.user_id_entry.get()
        messagebox.showinfo("Issue Result", f"Issuing book with Serial Number: {book_serial} to User ID: {user_id}")

    def return_book(self):
        self.clear_screen()
        title = tk.Label(self.root, text="Return a Book", font=("times new roman", 40, "bold"), bg="powder blue", fg="green", bd=10, relief=tk.RIDGE)
        title.pack(side=tk.TOP, fill=tk.X)
    
        tk.Label(self.root, text="Enter Book Serial Number:", font=("Arial", 12)).pack(pady=5)
        self.book_return_serial_entry = tk.Entry(self.root, font=("Arial", 12))
        self.book_return_serial_entry.pack(pady=5)
    
        return_button = tk.Button(self.root, text="Return", font=("Arial", 12), bg="#28A745", fg="white", width=10, command=self.perform_return_book)
        return_button.pack(pady=10)
    
        back_button = tk.Button(self.root, text="Back", font=("Arial", 12), bg="#6c757d", fg="white", width=10, command=self.transactions)
        back_button.pack(pady=10)

    def perform_return_book(self):
    # Add logic to return the book here
        book_return_serial = self.book_return_serial_entry.get()
        messagebox.showinfo("Return Result", f"Returning book with Serial Number: {book_return_serial}")


    def return_book(self):
        self.clear_screen()
        title = tk.Label(self.root, text="Return a Book", font=("times new roman", 40, "bold"), bg="powder blue", fg="green", bd=10, relief=tk.RIDGE)
        title.pack(side=tk.TOP, fill=tk.X)
    
        tk.Label(self.root, text="Enter Book Serial Number:", font=("Arial", 12)).pack(pady=5)
        self.book_return_serial_entry = tk.Entry(self.root, font=("Arial", 12))
        self.book_return_serial_entry.pack(pady=5)
    
        return_button = tk.Button(self.root, text="Return", font=("Arial", 12), bg="#28A745", fg="white", width=10, command=self.check_fine_payment)
        return_button.pack(pady=10)
    
        back_button = tk.Button(self.root, text="Back", font=("Arial", 12), bg="#6c757d", fg="white", width=10, command=self.transactions)
        back_button.pack(pady=10)

    def check_fine_payment(self):
        book_return_serial = self.book_return_serial_entry.get()
    # Placeholder logic to determine if there is an overdue fine
        overdue_fine = 50  # Let's say the fine is 50 units for the sake of this example

        if overdue_fine > 0:
            self.display_fine_payment(overdue_fine)
        else:
            self.complete_return(book_return_serial)

    def display_fine_payment(self, fine_amount):
        self.clear_screen()
        title = tk.Label(self.root, text="Fine Payment", font=("times new roman", 40, "bold"), bg="powder blue", fg="green", bd=10, relief=tk.RIDGE)
        title.pack(side=tk.TOP, fill=tk.X)

        tk.Label(self.root, text=f"Overdue Fine: {fine_amount}", font=("Arial", 12)).pack(pady=5)
    
        tk.Label(self.root, text="Fine Paid (Yes/No):", font=("Arial", 12)).pack(pady=5)
        self.fine_paid_var = tk.StringVar(value="No")
        tk.Radiobutton(self.root, text="Yes", variable=self.fine_paid_var, value="Yes", font=("Arial", 12)).pack(pady=2)
        tk.Radiobutton(self.root, text="No", variable=self.fine_paid_var, value="No", font=("Arial", 12)).pack(pady=2)
    
        pay_fine_button = tk.Button(self.root, text="Confirm Payment", font=("Arial", 12), bg="#28A745", fg="white", width=15, command=self.confirm_fine_payment)
        pay_fine_button.pack(pady=10)
    
        back_button = tk.Button(self.root, text="Back", font=("Arial", 12), bg="#6c757d", fg="white", width=10, command=self.return_book)
        back_button.pack(pady=10)

    def confirm_fine_payment(self):
        fine_paid = self.fine_paid_var.get()
        book_return_serial = self.book_return_serial_entry.get()
    
        if fine_paid == "Yes":
            self.complete_return(book_return_serial)
        else:
            messagebox.showwarning("Payment Pending", "Please pay the overdue fine to complete the return process.")

    def complete_return(self, book_return_serial):
    # Add logic to complete the return process
        messagebox.showinfo("Return Complete", f"Book with Serial Number {book_return_serial} has been successfully returned.")
        self.transactions()


if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()

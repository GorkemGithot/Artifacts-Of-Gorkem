"""author: ACER Gorkem"""
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog
import pyodbc  

conn_str = r'Driver={SQL Server};Server=DESKTOP-UA39NGG;Database=master;Trusted_Connection=yes;'
try:
    conn = pyodbc.connect(conn_str)
    print("connected!")
    
except Exception as e:
    print("connection error:", str(e))

def add_new_customer(p_CUSTOMER_ID, p_CUSTOMER_NAME, p_ADDRESS_O, p_PHONE_NUMBER):
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO Customer (CUSTOMER_ID, CUSTOMER_NAME, ADDRESS_O, PHONE_NUMBER)
            VALUES (?, ?, ?, ?)
        """, (p_CUSTOMER_ID, p_CUSTOMER_NAME, p_ADDRESS_O, p_PHONE_NUMBER))
        conn.commit()
        messagebox.showinfo("Successful!", "Customer added...")
    except Exception as e:
        messagebox.showerror(f"Error {str(e)}")
    finally:
        cursor.close()



def open_add_customer_window():
    def submit_customer():
        
        customer_id = entry_customer_id.get()
        customer_name = entry_customer_name.get()
        address = entry_address.get()
        phone_number = entry_phone_number.get()
        
        
        if not customer_id or not customer_name or not phone_number:
            messagebox.showerror("Error", "Please enter required datas!")
            return
        
        
        if not customer_id.isdigit():
            messagebox.showerror("Error", "Customer ID must valid!")
            return

        
        add_new_customer(int(customer_id), customer_name, address, phone_number)
        add_customer_window.destroy()

    
    add_customer_window = tk.Toplevel(root)
    add_customer_window.title("Add New Customer")

    
    tk.Label(add_customer_window, text="Customer ID:").grid(row=0, column=0, padx=10, pady=5)
    entry_customer_id = tk.Entry(add_customer_window)
    entry_customer_id.grid(row=0, column=1, padx=10, pady=5)

    
    tk.Label(add_customer_window, text="Customer Name:").grid(row=1, column=0, padx=10, pady=5)
    entry_customer_name = tk.Entry(add_customer_window)
    entry_customer_name.grid(row=1, column=1, padx=10, pady=5)

    
    tk.Label(add_customer_window, text="Address:").grid(row=2, column=0, padx=10, pady=5)
    entry_address = tk.Entry(add_customer_window)
    entry_address.grid(row=2, column=1, padx=10, pady=5)

    
    tk.Label(add_customer_window, text="Phone Number:").grid(row=3, column=0, padx=10, pady=5)
    entry_phone_number = tk.Entry(add_customer_window)
    entry_phone_number.grid(row=3, column=1, padx=10, pady=5)

    
    submit_button = tk.Button(add_customer_window, text="Apply", command=submit_customer)
    submit_button.grid(row=4, column=0, columnspan=2, pady=10)

    
    back_button = tk.Button(add_customer_window, text="Return Main Menu", command=add_customer_window.destroy)
    back_button.grid(row=5, column=0, columnspan=2, pady=10)

def add_new_payment(Payment_ID, p_PAYMENT_METHOD, p_PAYMENT_CHECK, ORDER_ID):
    cursor = conn.cursor()
    try:
        
        cursor.execute("""
            INSERT INTO Payment (PAYMENT_ID, PAYMENT_METHOD, PAYMENT_CHECK, ORDER_ID)
            VALUES (?, ?, ?, ?)
        """, (Payment_ID, p_PAYMENT_METHOD, p_PAYMENT_CHECK, ORDER_ID))
        conn.commit()

        
        if p_PAYMENT_CHECK == '1':  
            
            cursor.execute("""
                SELECT oi.PRODUCT_ID, oi.QUANTITY
                FROM OrderInfo oi
                WHERE oi.ORDER_ID = ?
            """, (ORDER_ID,))
            product = cursor.fetchone()

            if product:
                product_id = product[0]
                quantity_ordered = product[1]

                
                cursor.execute("""
                    SELECT CURRENT_STOCK_QUANTITY 
                    FROM Product 
                    WHERE PRODUCT_ID = ?
                """, (product_id,))
                current_stock = cursor.fetchone()

                if current_stock:
                    new_stock = current_stock[0] - quantity_ordered
                    if current_stock[0]==0:
                        messagebox.showerror("Error", f"You can not pay your order because there is no quantity!!")
                    elif new_stock >= 0:
                        cursor.execute("""
                            UPDATE Product 
                            SET CURRENT_STOCK_QUANTITY = ?
                            WHERE PRODUCT_ID = ?
                        """, (new_stock,product_id))
                        conn.commit()
                        messagebox.showinfo("Process Done...", "Payment processed successfully, stock updated.")            
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def open_add_payment_window():
    def submit_payment():
        
        payment_id = entry_payment_ID.get()
        payment_method = entry_payment_method.get()
        payment_check = entry_payment_check.get()  
        order_check = entry_ORDER_ID.get()
        
        
        if not payment_id or not payment_method or not payment_check or not order_check:
            messagebox.showerror("Error", "Please enter all required fields!")
            return

        
        add_new_payment(payment_id, payment_method, payment_check, order_check)
        add_payment_window.destroy()
    
    add_payment_window = tk.Toplevel(root)
    add_payment_window.title("Add Payment Window")

    
    tk.Label(add_payment_window, text="Payment ID:").grid(row=0, column=0, padx=10, pady=5)
    entry_payment_ID = tk.Entry(add_payment_window)
    entry_payment_ID.grid(row=0, column=1, padx=10, pady=5) 

    
    tk.Label(add_payment_window, text="Payment Method (CASH/CREDIT):").grid(row=1, column=0, padx=10, pady=5)
    entry_payment_method = tk.Entry(add_payment_window)
    entry_payment_method.grid(row=1, column=1, padx=10, pady=5)

    
    tk.Label(add_payment_window, text="Payment Check (1/0):").grid(row=2, column=0, padx=10, pady=5)
    entry_payment_check = tk.Entry(add_payment_window)
    entry_payment_check.grid(row=2, column=1, padx=10, pady=5)

    
    tk.Label(add_payment_window, text="Order ID:").grid(row=3, column=0, padx=10, pady=5)
    entry_ORDER_ID = tk.Entry(add_payment_window)
    entry_ORDER_ID.grid(row=3, column=1, padx=10, pady=5)
    
    
    submit_button = tk.Button(add_payment_window, text="Apply", command=submit_payment)
    submit_button.grid(row=5, column=0, columnspan=2, pady=10)

    
    back_button = tk.Button(add_payment_window, text="Return Main Menu", command=add_payment_window.destroy)
    back_button.grid(row=6, column=0, columnspan=2, pady=10)


def open_add_supplier_window():
    def browse_image():
        
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if file_path:
            image_path.set(file_path)
    
    def add_supplier():
        
        supplier_id = int(entry_supplier_id.get())  
        company_name = entry_company_name.get()
        contact_info = entry_contact_info.get()
        
        
        
        if image_path.get():
            with open(image_path.get(), 'rb') as file:
                image_data = file.read()
        else:
            image_data = None  
        
        
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO Supplier (SUPPLIER_ID, COMPANY_NAME, CONTACT_INFO, PICTURE)
                VALUES (?, ?, ?, ?)
            """, (supplier_id, company_name, contact_info, image_data))
            conn.commit()
            messagebox.showinfo("Success", "Supplier added successfully!")
            add_supplier_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    
    add_supplier_window = tk.Toplevel(root)
    add_supplier_window.title("Add New Supplier")

    
    tk.Label(add_supplier_window, text="Supplier ID:").grid(row=0, column=0, padx=10, pady=5)
    entry_supplier_id = tk.Entry(add_supplier_window)
    entry_supplier_id.grid(row=0, column=1, padx=10, pady=5)

    
    tk.Label(add_supplier_window, text="Company Name:").grid(row=1, column=0, padx=10, pady=5)
    entry_company_name = tk.Entry(add_supplier_window)
    entry_company_name.grid(row=1, column=1, padx=10, pady=5)

    
    tk.Label(add_supplier_window, text="Contact Info:").grid(row=2, column=0, padx=10, pady=5)
    entry_contact_info = tk.Entry(add_supplier_window)
    entry_contact_info.grid(row=2, column=1, padx=10, pady=5)

    

    
    tk.Label(add_supplier_window, text="Supplier Image:").grid(row=3, column=0, padx=10, pady=5)
    image_path = tk.StringVar()
    entry_image_path = tk.Entry(add_supplier_window, textvariable=image_path, state='readonly')
    entry_image_path.grid(row=3, column=1, padx=10, pady=5)
    
    browse_button = tk.Button(add_supplier_window, text="Browse", command=browse_image)
    browse_button.grid(row=3, column=2, padx=10, pady=5)

    
    add_button = tk.Button(add_supplier_window, text="Add Supplier", command=add_supplier)
    add_button.grid(row=4, column=0, columnspan=3, pady=10)


def add_new_order(p_ORDER_ID, p_ORDER_DATE, p_TOTAL_PRICE, p_QUANTITY, p_CUSTOMER_ID, p_PRODUCT_ID):
    cursor = conn.cursor()
    try:
        
        cursor.execute("""
            INSERT INTO OrderInfo (ORDER_ID, ORDER_DATE, TOTAL_PRICE, QUANTITY, CUSTOMER_ID, PRODUCT_ID)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (p_ORDER_ID, p_ORDER_DATE, p_TOTAL_PRICE, p_QUANTITY, p_CUSTOMER_ID, p_PRODUCT_ID))
        conn.commit()
        messagebox.showinfo("Done...", "Order added succesfully!")
    except Exception as e:
        messagebox.showerror(f"Error {str(e)}")
    finally:
        cursor.close()

def open_add_order_window():
    def submit_order():
        
        order_id = entry_order_id.get()
        order_date = entry_order_date.get()
        total_price = entry_total_price.get()
        quantity = entry_quantity.get()
        customer_id = entry_customer_id.get()
        product_id = entry_product_id.get()
        
        
        if not order_id or not order_date or not total_price or not quantity or not customer_id or not product_id:
            messagebox.showerror("Error", "Please enter required datas!")
            return

        
        if not total_price.replace('.', '', 1).isdigit() or not quantity.isdigit():
            messagebox.showerror("Error", "Total price and quantity must be valid!")
            return

        def check_product_availability(product_id, requested_quantity):
            cursor = conn.cursor()
            try:
                cursor.execute("""
                    SELECT CURRENT_STOCK_QUANTITY FROM Product WHERE PRODUCT_ID = ?
                """, (product_id,))
                result = cursor.fetchone()
                
                if result is None:
                    messagebox.showerror("Error", "Invalid Product ID!")
                    return False
                
                
                available_quantity = result[0]
                print(available_quantity)
                
                if available_quantity < requested_quantity:
                    messagebox.showerror("Error", f"There are no sufficient quantity for creating order:{available_quantity}")
                    return False
                
                return True
            except Exception as e:
                messagebox.showerror(f"Error {str(e)}")
                return False
            finally:
                cursor.close()
        if(False==check_product_availability(int(product_id),int(quantity))):
            messagebox.showerror("Error",f"Process is cancelled!")
        else:
            add_new_order(order_id, order_date, float(total_price), int(quantity), int(customer_id), int(product_id))
            add_order_window.destroy()
    
    add_order_window = tk.Toplevel(root)
    add_order_window.title("Add New Order")

    
    tk.Label(add_order_window, text="Order ID:").grid(row=0, column=0, padx=10, pady=5)
    entry_order_id = tk.Entry(add_order_window)
    entry_order_id.grid(row=0, column=1, padx=10, pady=5)

    
    tk.Label(add_order_window, text="Order Date (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=5)
    entry_order_date = tk.Entry(add_order_window)
    entry_order_date.grid(row=1, column=1, padx=10, pady=5)

    
    tk.Label(add_order_window, text="Sold Price:").grid(row=2, column=0, padx=10, pady=5)
    entry_total_price = tk.Entry(add_order_window)
    entry_total_price.grid(row=2, column=1, padx=10, pady=5)

    
    tk.Label(add_order_window, text="Quantity:").grid(row=3, column=0, padx=10, pady=5)
    entry_quantity = tk.Entry(add_order_window)
    entry_quantity.grid(row=3, column=1, padx=10, pady=5)

    
    tk.Label(add_order_window, text="Customer ID:").grid(row=4, column=0, padx=10, pady=5)
    entry_customer_id = tk.Entry(add_order_window)
    entry_customer_id.grid(row=4, column=1, padx=10, pady=5)

    
    tk.Label(add_order_window, text="Product ID:").grid(row=5, column=0, padx=10, pady=5)
    entry_product_id = tk.Entry(add_order_window)
    entry_product_id.grid(row=5, column=1, padx=10, pady=5)

    
    submit_button = tk.Button(add_order_window, text="Apply", command=submit_order)
    submit_button.grid(row=6, column=0, columnspan=2, pady=10)

    
    back_button = tk.Button(add_order_window, text="Return Main Menu", command=add_order_window.destroy)
    back_button.grid(row=7, column=0, columnspan=2, pady=10)






def open_add_product_window():
    def browse_image():
        
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if file_path:
            image_path.set(file_path)
    
    def add_product():
        
        product_id = int(entry_product_id.get())  
        product_name = entry_product_name.get()
        price_bought = float(entry_price_bought.get())
        stock_quantity = int(entry_stock_quantity.get())
        category_name = entry_category_name.get()
        supplier_id = int(entry_supplier_id.get())
        
        
        if image_path.get():
            with open(image_path.get(), 'rb') as file:
                image_data = file.read()
        else:
            image_data = None  
        
        
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO Product (PRODUCT_ID, PRODUCT_NAME, PRICE_BOUGHT, CURRENT_STOCK_QUANTITY, PICTURE, CATEGORY_NAME, SUPPLIER_ID)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (product_id, product_name, price_bought, stock_quantity, image_data, category_name, supplier_id))
            conn.commit()
            messagebox.showinfo("Success", "Product added successfully!")
            add_product_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    
    add_product_window = tk.Toplevel(root)
    add_product_window.title("Add New Product")

    
    tk.Label(add_product_window, text="Product ID:").grid(row=0, column=0, padx=10, pady=5)
    entry_product_id = tk.Entry(add_product_window)
    entry_product_id.grid(row=0, column=1, padx=10, pady=5)

    
    tk.Label(add_product_window, text="Product Name:").grid(row=1, column=0, padx=10, pady=5)
    entry_product_name = tk.Entry(add_product_window)
    entry_product_name.grid(row=1, column=1, padx=10, pady=5)

    
    tk.Label(add_product_window, text="Price Bought:").grid(row=2, column=0, padx=10, pady=5)
    entry_price_bought = tk.Entry(add_product_window)
    entry_price_bought.grid(row=2, column=1, padx=10, pady=5)
    
    tk.Label(add_product_window, text="Stock Quantity:").grid(row=3, column=0, padx=10, pady=5)
    entry_stock_quantity = tk.Entry(add_product_window)
    entry_stock_quantity.grid(row=3, column=1, padx=10, pady=5)

    
    tk.Label(add_product_window, text="Category Name:").grid(row=4, column=0, padx=10, pady=5)
    entry_category_name = tk.Entry(add_product_window)
    entry_category_name.grid(row=4, column=1, padx=10, pady=5)

    
    tk.Label(add_product_window, text="Supplier ID:").grid(row=5, column=0, padx=10, pady=5)
    entry_supplier_id = tk.Entry(add_product_window)
    entry_supplier_id.grid(row=5, column=1, padx=10, pady=5)

    
    tk.Label(add_product_window, text="Product Image:").grid(row=6, column=0, padx=10, pady=5)
    image_path = tk.StringVar()
    entry_image_path = tk.Entry(add_product_window, textvariable=image_path, state='readonly')
    entry_image_path.grid(row=6, column=1, padx=10, pady=5)
    
    browse_button = tk.Button(add_product_window, text="Browse", command=browse_image)
    browse_button.grid(row=6, column=2, padx=10, pady=5)

    
    add_button = tk.Button(add_product_window, text="Add Product", command=add_product)
    add_button.grid(row=7, column=0, columnspan=3, pady=10)
    
   
def update_supplier_info(p_SUPPLIER_ID, p_COMPANY_NAME, p_CONTACT_INFO):
    cursor = conn.cursor()
    try:
        
        cursor.execute("""
            UPDATE Supplier
            SET COMPANY_NAME = ?, CONTACT_INFO = ?
            WHERE SUPPLIER_ID = ?
        """, (p_COMPANY_NAME, p_CONTACT_INFO, p_SUPPLIER_ID))
        conn.commit()  
        messagebox.showinfo("Done...", "Supplier infos updated!")
    except Exception as e:
        messagebox.showerror("Error", f"The Error: {str(e)}")

def update_customer_info(p_CUSTOMER_ID, p_CUSTOMER_NAME, p_ADDRESS_O, p_PHONE_NUMBER):
    cursor = conn.cursor()
    try:
        
        cursor.execute("""
            UPDATE Customer
            SET CUSTOMER_NAME = ?, ADDRESS_O = ?, PHONE_NUMBER = ?
            WHERE CUSTOMER_ID = ?
        """, (p_CUSTOMER_NAME, p_ADDRESS_O, p_PHONE_NUMBER, p_CUSTOMER_ID))
        conn.commit()  
        messagebox.showinfo("Done...", "Customer infos updated!")
    except Exception as e:
        messagebox.showerror("Error", f"The Error: {str(e)}")



def update_product_quantity(p_PRODUCT_ID, p_NEW_QUANTITY):
    cursor = conn.cursor()
    try:
        
        cursor.execute("""
            UPDATE Product
            SET CURRENT_STOCK_QUANTITY = ?
            WHERE PRODUCT_ID = ?
        """, (p_NEW_QUANTITY, p_PRODUCT_ID))
        conn.commit()  
        messagebox.showinfo("Done...", "Quantity of product updated!")
    except Exception as e:
        messagebox.showerror("Error", f"The Error: {str(e)}")

def update_product_selling_price(p_PRODUCT_ID, p_NEW_PRICE_SOLD):
    cursor = conn.cursor()
    try:
        
        cursor.execute("""
            UPDATE Product
            SET PRICE_BOUGHT = ?
            WHERE PRODUCT_ID = ?
        """, (p_NEW_PRICE_SOLD, p_PRODUCT_ID))
        conn.commit()  
        messagebox.showinfo("Done...", "Sale Price Of Product Updated!")
    except Exception as e:
        messagebox.showerror("Error", f"The Error: {str(e)}")



def  update_payment_info(Payment_ID, p_PAYMENT_METHOD, p_PAYMENT_CHECK, ORDER_ID):
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE Payment
            SET PAYMENT_ID=?, PAYMENT_METHOD=?, PAYMENT_CHECK=?, ORDER_ID=?
            WHERE PAYMENT_ID=?
        """, (Payment_ID, p_PAYMENT_METHOD, p_PAYMENT_CHECK, ORDER_ID,Payment_ID))
        conn.commit()

        
        if p_PAYMENT_CHECK == '1':  
            
            cursor.execute("""
                SELECT oi.PRODUCT_ID, oi.QUANTITY
                FROM OrderInfo oi
                WHERE oi.ORDER_ID = ?
            """, (ORDER_ID,))
            product = cursor.fetchone()

            if product:
                product_id = product[0]
                quantity_ordered = product[1]

                
                cursor.execute("""
                    SELECT CURRENT_STOCK_QUANTITY 
                    FROM Product 
                    WHERE PRODUCT_ID = ?
                """, (product_id,))
                current_stock = cursor.fetchone()

                if current_stock:
                    new_stock = current_stock[0] - quantity_ordered
                    if current_stock[0]==0:
                       messagebox.showerror("Error", f"You can not create an order bcs there is no quantity!!")
                    elif new_stock >= 0:
                        cursor.execute("""
                            UPDATE Product 
                            SET CURRENT_STOCK_QUANTITY = ?
                            WHERE PRODUCT_ID = ?
                        """, (new_stock,product_id))
                        conn.commit()
                        
        messagebox.showinfo("Process Done...", "Payment processed successfully, stock updated.")            
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")




def open_update_payment_window():
    def submit_update():
        payment_id = entry_payment_id.get()
        payment_method = entry_payment_method.get()
        payment_check = entry_payment_check.get()
        order_id = entry_order_id.get()

        if not payment_method or not payment_check or not payment_id or not order_id:
            messagebox.showerror("Error", "Please enter required data!")
            return
        try:
            payment_id = payment_id
            payment_check = payment_check
            order_id = order_id
        except ValueError:
            messagebox.showerror("Error", "Please enter valid data!")
            return      
        update_payment_info(payment_id, payment_method, payment_check, order_id)
        update_payment_window.destroy()

    update_payment_window = tk.Toplevel(root)
    update_payment_window.title("Update Payment Information")

    tk.Label(update_payment_window, text="Payment ID:").grid(row=0, column=0, padx=10, pady=5)
    entry_payment_id = tk.Entry(update_payment_window)
    entry_payment_id.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(update_payment_window, text="Payment Method (CASH/CREDIT):").grid(row=1, column=0, padx=10, pady=5)
    entry_payment_method = tk.Entry(update_payment_window)
    entry_payment_method.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(update_payment_window, text="Payment Check (1/0):").grid(row=2, column=0, padx=10, pady=5)
    entry_payment_check = tk.Entry(update_payment_window)
    entry_payment_check.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(update_payment_window, text="Order ID:").grid(row=3, column=0, padx=10, pady=5)
    entry_order_id = tk.Entry(update_payment_window)
    entry_order_id.grid(row=3, column=1, padx=10, pady=5)

    submit_button = tk.Button(update_payment_window, text="Update Payment Information", command=submit_update)
    submit_button.grid(row=4, column=0, columnspan=2, pady=10)

    back_button = tk.Button(update_payment_window, text="Return to Main Menu", command=update_payment_window.destroy)
    back_button.grid(row=5, column=0, columnspan=2, pady=10)

def open_update_supplier_window():
    def submit_update():
        
        supplier_id = entry_supplier_id.get()
        company_name = entry_company_name.get()
        contact_info = entry_contact_info.get()

        if not company_name or not contact_info  or not supplier_id:
            messagebox.showerror("Error", "Please enter required datas!")
            return
        try:
            supplier_id = int(supplier_id)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid data!")
            return

        
        update_supplier_info(supplier_id, company_name, contact_info)
        update_supplier_window.destroy()
    
    update_supplier_window = tk.Toplevel(root)
    update_supplier_window.title("Update Supplier Information")

    
    tk.Label(update_supplier_window, text="Supplier ID:").grid(row=0, column=0, padx=10, pady=5)
    entry_supplier_id = tk.Entry(update_supplier_window)
    entry_supplier_id.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(update_supplier_window, text="Company Name:").grid(row=1, column=0, padx=10, pady=5)
    entry_company_name = tk.Entry(update_supplier_window)
    entry_company_name.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(update_supplier_window, text="Contact Information:").grid(row=2, column=0, padx=10, pady=5)
    entry_contact_info = tk.Entry(update_supplier_window)
    entry_contact_info.grid(row=2, column=1, padx=10, pady=5)

    

    
    submit_button = tk.Button(update_supplier_window, text="Update Supplier Information", command=submit_update)
    submit_button.grid(row=3, column=0, columnspan=2, pady=10)

    
    back_button = tk.Button(update_supplier_window, text="Main Menu", command=update_supplier_window.destroy)
    back_button.grid(row=4, column=0, columnspan=2, pady=10)
def open_update_customer_window():
    def submit_update():
        
        customer_id = entry_customer_id.get()
        customer_name = entry_customer_name.get()
        address = entry_address.get()
        phone_number = entry_phone_number.get()

        
        if not customer_name or not address or not phone_number or not customer_id:
            messagebox.showerror("Error", "Please fill in all the fields!")
            return

        
        try:
            customer_id = int(customer_id)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid customer ID!")
            return

        
        update_customer_info(customer_id, customer_name, address, phone_number)
        update_customer_window.destroy()
    update_customer_window = tk.Toplevel(root)
    update_customer_window.title("Update Customer Information")

    tk.Label(update_customer_window, text="Customer ID:").grid(row=0, column=0, padx=10, pady=5)
    entry_customer_id = tk.Entry(update_customer_window)
    entry_customer_id.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(update_customer_window, text="Customer Name:").grid(row=1, column=0, padx=10, pady=5)
    entry_customer_name = tk.Entry(update_customer_window)
    entry_customer_name.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(update_customer_window, text="Adress:").grid(row=2, column=0, padx=10, pady=5)
    entry_address = tk.Entry(update_customer_window)
    entry_address.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(update_customer_window, text="Phone Number:").grid(row=3, column=0, padx=10, pady=5)
    entry_phone_number = tk.Entry(update_customer_window)
    entry_phone_number.grid(row=3, column=1, padx=10, pady=5)

    
    submit_button = tk.Button(update_customer_window, text="Update Customer Information", command=submit_update)
    submit_button.grid(row=4, column=0, columnspan=2, pady=10)

    
    back_button = tk.Button(update_customer_window, text="Main Menu", command=update_customer_window.destroy)
    back_button.grid(row=5, column=0, columnspan=2, pady=10)
def open_update_product_quantity_window():
    def submit_update(): 
        product_id = entry_product_id.get()
        new_quantity = entry_new_quantity.get()
        try:
            product_id = int(product_id)  
            new_quantity = int(new_quantity) 
             
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid product ID and stock quantity!")
            return
        if new_quantity<0:
            messagebox.showerror("Error", "Please enter a valid product ID and stock quantity!")
        else:
            update_product_quantity(product_id, new_quantity)
            update_quantity_window.destroy()
    
    update_quantity_window = tk.Toplevel(root)
    update_quantity_window.title("Update Product Quantity")

    
    tk.Label(update_quantity_window, text="Product ID:").grid(row=0, column=0, padx=10, pady=5)
    entry_product_id = tk.Entry(update_quantity_window)
    entry_product_id.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(update_quantity_window, text="New Stock Quantity:").grid(row=1, column=0, padx=10, pady=5)
    entry_new_quantity = tk.Entry(update_quantity_window)
    entry_new_quantity.grid(row=1, column=1, padx=10, pady=5)

    
    submit_button = tk.Button(update_quantity_window, text="Update Stock Quantity", command=submit_update)
    submit_button.grid(row=2, column=0, columnspan=2, pady=10)

    
    back_button = tk.Button(update_quantity_window, text="Main Menu", command=update_quantity_window.destroy)
    back_button.grid(row=3, column=0, columnspan=2, pady=10)

def open_update_product_price_window():
    def submit_update():     
        product_id = entry_product_id.get()
        new_price = entry_new_price.get()
        try:
            product_id = int(product_id)  
            new_price = float(new_price)  
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid product ID and price!")
            return
        if(new_price<0):
            messagebox.showerror("Error", "Please enter a valid product ID and price!")
        else:
            update_product_selling_price(product_id, new_price)
            update_price_window.destroy()
    
    update_price_window = tk.Toplevel(root)
    update_price_window.title("Update Product Selling Price")

    
    tk.Label(update_price_window, text="Product ID:").grid(row=0, column=0, padx=10, pady=5)
    entry_product_id = tk.Entry(update_price_window)
    entry_product_id.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(update_price_window, text="New Price:").grid(row=1, column=0, padx=10, pady=5)
    entry_new_price = tk.Entry(update_price_window)
    entry_new_price.grid(row=1, column=1, padx=10, pady=5)

    
    submit_button = tk.Button(update_price_window, text="Update Sale Price", command=submit_update)
    submit_button.grid(row=2, column=0, columnspan=2, pady=10)

    
    back_button = tk.Button(update_price_window, text="Main Menu", command=update_price_window.destroy)
    back_button.grid(row=3, column=0, columnspan=2, pady=10)


def fetch_query_1():
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT 
                s.SUPPLIER_ID,
                p.PRODUCT_ID,
                p.PRODUCT_NAME,
                p.CATEGORY_NAME,
                s.COMPANY_NAME AS SUPPLIER_NAME,
                p.CURRENT_STOCK_QUANTITY,
                p.PRICE_BOUGHT
            FROM 
                Product p
            JOIN 
                Supplier s ON p.SUPPLIER_ID = s.SUPPLIER_ID
            ORDER BY 
                p.CURRENT_STOCK_QUANTITY DESC;
        """)
        rows = cursor.fetchall()
        open_result_window("Product Stock", ["Supplier Id","Product Id","Product Name","Category Name", "Supplier Name", "Current Stock","Price Bought"], rows)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
  
def fetch_query_2():
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT 
                o.ORDER_ID,
                o.CUSTOMER_ID,
                o.PRODUCT_ID,
                s.SUPPLIER_ID,
                o.ORDER_DATE,
                p.PRODUCT_NAME,
                p.CATEGORY_NAME,
                s.COMPANY_NAME AS SUPPLIER_NAME
            FROM 
                OrderInfo o
            JOIN 
                Product p ON o.PRODUCT_ID = p.PRODUCT_ID
            JOIN 
                Supplier s ON p.SUPPLIER_ID = s.SUPPLIER_ID
            ORDER BY 
                o.ORDER_DATE;
        """)

        rows = cursor.fetchall()
        open_result_window("Order Information", ["Order ID", "Customer ID", "Product ID","SUPPLIER_ID" ,"Order Date", "Product Name", "Category", "Supplier Name"], rows)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")



def fetch_query_3():
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT 
                o.ORDER_ID,
                s.SUPPLIER_ID,
                p.PRODUCT_ID,
                p.PRODUCT_NAME,
                SUM(o.QUANTITY) AS TOTAL_UNITS_SOLD,
                p.CATEGORY_NAME,
                p.PRICE_BOUGHT,
                o.TOTAL_PRICE,
                pa.PAYMENT_CHECK
            FROM 
                OrderInfo o
            JOIN 
                Product p ON o.PRODUCT_ID = p.PRODUCT_ID  
            JOIN 
                Supplier s ON p.SUPPLIER_ID = s.SUPPLIER_ID
            JOIN 
                Payment pa ON o.ORDER_ID = pa.ORDER_ID
            GROUP BY 
                o.ORDER_ID, s.SUPPLIER_ID,p.PRODUCT_ID, p.PRODUCT_NAME, p.CATEGORY_NAME, p.PRICE_BOUGHT, o.TOTAL_PRICE,pa.PAYMENT_CHECK
            ORDER BY 
                TOTAL_UNITS_SOLD DESC;
        """)
        rows = cursor.fetchall()
        open_result_window("Sales Data", ["Order Id", "Supplier Id","Product Id", "Product Name", "Total Units Sold", "Category", "Price Bought", "Price Sold","Payment Check"], rows)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def fetch_query_6():
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT 
                c.CUSTOMER_ID,
                c.CUSTOMER_NAME,
                c.ADDRESS_O,
                c.PHONE_NUMBER
            FROM 
                Customer c
            ORDER BY 
                c.CUSTOMER_ID DESC;
        """)
        rows = cursor.fetchall()
        open_result_window("Customer Information", ["CUSTOMER_ID", "CUSTOMER_NAME", "ADDRESS_O", "PHONE_NUMBER"], rows)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def fetch_query_4(start_date, end_date):
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT 
                c.CUSTOMER_ID,
                p.PRODUCT_ID,
                s.SUPPLIER_ID,
                o.ORDER_DATE,
                c.CUSTOMER_NAME,
                c.PHONE_NUMBER AS CUSTOMER_CONTACT,
                s.COMPANY_NAME AS SUPPLIER_NAME,
                o.TOTAL_PRICE
            FROM 
                OrderInfo o
            JOIN 
                Customer c ON o.CUSTOMER_ID = c.CUSTOMER_ID
            JOIN 
                Product p ON o.PRODUCT_ID = p.PRODUCT_ID
            JOIN 
                Supplier s ON p.SUPPLIER_ID = s.SUPPLIER_ID
            WHERE 
                o.ORDER_DATE BETWEEN ? AND ?
            ORDER BY 
                o.ORDER_DATE;
        """, (start_date, end_date))
        rows = cursor.fetchall()
        open_result_window("Customer Orders", ["Customer Id","PRODUCT_ID","SUPPLIER_ID","Order Date", "Customer Name", "Customer Contact", "Supplier Name", "Total Price"], rows)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def open_date_input_window():
    
    date_window = tk.Toplevel(root)
    date_window.title("Enter Date Range")
    
    
    tk.Label(date_window, text="Start Date (YYYY-MM-DD):").grid(row=0, column=0, padx=10, pady=5)
    start_date_entry = tk.Entry(date_window)
    start_date_entry.grid(row=0, column=1, padx=10, pady=5)
    
    
    tk.Label(date_window, text="End Date (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=5)
    end_date_entry = tk.Entry(date_window)
    end_date_entry.grid(row=1, column=1, padx=10, pady=5)
    
    
    def apply_dates():
        start_date = start_date_entry.get()
        end_date = end_date_entry.get()
        
        
        if not start_date or not end_date:
            messagebox.showwarning("Input Error", "Please enter both start and end dates.")
        else:
            try:
                
                fetch_query_4(start_date, end_date)
                date_window.destroy()  
            except Exception as e:
                messagebox.showerror("Invalid Date", f"Please enter valid date format.\nError: {str(e)}")
    
    
    apply_button = tk.Button(date_window, text="Apply", command=apply_dates)
    apply_button.grid(row=2, column=0, columnspan=2, pady=10)
  




def fetch_query_5():
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT 
                s.COMPANY_NAME AS SUPPLIER_NAME,
                SUM(p.CURRENT_STOCK_QUANTITY) AS NUMBER_OF_ITEMS_SOLD
            FROM 
                Product p
            JOIN 
                Supplier s ON p.SUPPLIER_ID = s.SUPPLIER_ID
            GROUP BY 
                s.COMPANY_NAME
            ORDER BY 
                NUMBER_OF_ITEMS_SOLD DESC;
        """)
        rows = cursor.fetchall()
        open_result_window("Supplier Orders", ["Supplier Name", "Items Bought"], rows)
    except Exception as e:
        messagebox.showerror("Error", f"Some error occured: {str(e)}")

def fetch_7():
    cursor = conn.cursor()
    try:
        
        cursor.execute("""
            SELECT 
                p.PAYMENT_ID,
                oi.ORDER_ID,
                oi.PRODUCT_ID,
                oi.ORDER_DATE,
                oi.TOTAL_PRICE,
                oi.QUANTITY,
                p.PAYMENT_METHOD,
                p.PAYMENT_CHECK
            FROM 
                OrderInfo oi
            JOIN 
                Payment p ON oi.ORDER_ID = p.ORDER_ID
            
        """)
        
        rows = cursor.fetchall()
        
        
        if rows:
            open_result_window("Order & Payment Details", ["Payment ID","Order ID","Product ID", "Order Date", "Total Price", "Quantity", "Payment Method", "Payment Check"], rows)
        else:
            messagebox.showerror("Error", "No data found for the given Order ID.")
    except Exception as e:
        messagebox.showerror("Error", f"Some error occurred: {str(e)}")

def fetch_8():
    cursor = conn.cursor()
    try:
        
        cursor.execute("""
            SELECT 
                s.SUPPLIER_ID,
                s.COMPANY_NAME,
                s.CONTACT_INFO
            FROM 
                Supplier s
        """)
        
        rows = cursor.fetchall()
        
        
        if rows:
            open_result_window("Supplier Information", ["Supplier ID","Company Name","Contact Info"], rows)
        else:
            messagebox.showerror("Error", "No data found for the given Supplier ID.")
    except Exception as e:
        messagebox.showerror("Error", f"Some error occurred: {str(e)}")




def open_result_window(title, columns, rows):
    result_window = tk.Toplevel(root)
    result_window.title(title)

    tree = ttk.Treeview(result_window, columns=columns, show="headings")
 
    for col in columns:
        tree.heading(col, text=col)
  
    for row in rows:
        
        cleaned_row = tuple(str(item).replace("(", "").replace(")", "").replace(",", "") for item in row)
        tree.insert("", "end", values=cleaned_row)
 
    tree.pack(padx=20, pady=20)

    for i, col in enumerate(columns):
        tree.column(col, width=100)  






root = tk.Tk()
root.title("WHOLESALE MANAGEMENT")

button_width = 30  
button_height = 2  

query_1_button = tk.Button(root, text="Inventory Stock Observation", command=fetch_query_1, width=button_width, height=button_height)
query_1_button.grid(row=0, column=0, padx=20, pady=10)

query_2_button = tk.Button(root, text="Order Fulfillment", command=fetch_query_2, width=button_width, height=button_height)
query_2_button.grid(row=1, column=0, padx=20, pady=10)

query_3_button = tk.Button(root, text="Product Sales", command=fetch_query_3, width=button_width, height=button_height)
query_3_button.grid(row=2, column=0, padx=20, pady=10)

query_4_button = tk.Button(root, text="Sales Report For A Specific Period", command=open_date_input_window, width=button_width, height=button_height)
query_4_button.grid(row=3, column=0, padx=20, pady=10)

query_5_button = tk.Button(root, text=" Supplier Performance", command=fetch_query_5, width=button_width, height=button_height)
query_5_button.grid(row=4, column=0, padx=20, pady=10)

query_6_button = tk.Button(root, text="Customer Informations", command=fetch_query_6, width=button_width, height=button_height)
query_6_button.grid(row=5, column=0, padx=20, pady=10)

query_7_button = tk.Button(root, text="Payment Informations", command=fetch_7, width=button_width, height=button_height)
query_7_button.grid(row=6, column=0, padx=20, pady=10)

query_8_button = tk.Button(root, text="Supplier Informations", command=fetch_8, width=button_width, height=button_height)
query_8_button.grid(row=7, column=0, padx=20, pady=10)

add_product_button = tk.Button(root, text="Add New Product", command=open_add_product_window, width=button_width, height=button_height)
add_product_button.grid(row=0, column=2, padx=20, pady=10)

add_customer_button = tk.Button(root, text="Add New Customer", command=open_add_customer_window, width=button_width, height=button_height)
add_customer_button.grid(row=1, column=2, padx=20, pady=10)


create_order_button = tk.Button(root, text="Add New Order", command=open_add_order_window, width=button_width, height=button_height)
create_order_button.grid(row=2, column=2, padx=20, pady=10)

add_payment_button = tk.Button(root, text="Add New Payment", command=open_add_payment_window, width=button_width, height=button_height)
add_payment_button.grid(row=3, column=2, padx=20, pady=10)


add_supplier_button = tk.Button(root, text="Add New Supplier", command=open_add_supplier_window, width=button_width, height=button_height)
add_supplier_button.grid(row=4, column=2, padx=20, pady=10)

update_product_quantity_button = tk.Button(root, text="Update Product Quantity", command=open_update_product_quantity_window, width=button_width, height=button_height)
update_product_quantity_button.grid(row=0, column=1, padx=20, pady=10)


update_customer_button = tk.Button(root, text="Update Customer Information", command=open_update_customer_window, width=button_width, height=button_height)
update_customer_button.grid(row=1, column=1, padx=20, pady=10)


update_supplier_button = tk.Button(root, text="Update Supplier Information", command=open_update_supplier_window, width=button_width, height=button_height)
update_supplier_button.grid(row=2, column=1, padx=20, pady=10)

update_product_price_button = tk.Button(root, text="Update Product Price", command=open_update_product_price_window, width=button_width, height=button_height)
update_product_price_button.grid(row=3, column=1, padx=20, pady=10)

update_payment_button = tk.Button(root, text="Update Payment", command=open_update_payment_window, width=button_width, height=button_height)
update_payment_button.grid(row=4, column=1, padx=20, pady=10)


root.mainloop()

from fastapi import FastAPI
from queries import get_all,get_tot_rev,get_num_customers,get_num_sales,get_avg_val
app=FastAPI(title="Sales Analytics API")



@app.get("/home")
def health():
    return {"sales_platform_running":"True"}

@app.get("/db")
def get_table():
    return get_all()

@app.get("/total_revenue")
def get_total_revenue():
    return get_tot_rev()

@app.get("/number_of_customer")
def get_number_of_customers():
    return get_num_customers()

@app.get("/number_of_sales")
def get_number_of_sales():
    return get_num_sales()

@app.get("/avg_value")
def get_average_order_value():
    return get_avg_val()

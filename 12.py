import fastapi
import mysql.connector
app = fastapi.FastAPI()
class Managerdb:
    def __init__(self,host,user,password,database):
        self.mydb = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        self.mycursor = self.mydb.cursor( )
    
    def selectdb (self,table):
        sql = f"SELECT * FROM {table}"
        self.mycursor.execute(sql)
        show = self.mycursor.fetchall()
        return show
db={
    "shop_db" : Managerdb("localhost","root","1234","yumyum")
}
@app.get('/selectdb/{database}/{table}')
async def select_db(database,table):
    all_db = db[database]
    result = all_db.selectdb(table)
    return {"select_data" : result}
# http://127.0.0.1:8000/selectdb/shop_db/products

@app.get('/addcategories/{database}/{category_name}')
async def add_categories(database, category_name):
    all_db = db[database]
    sql = "INSERT INTO categories VALUES (%s, %s)"
    val_sql = (None, category_name)
    
    all_db.mycursor.execute(sql, val_sql)
    all_db.mydb.commit()
    
    if all_db.mycursor.rowcount > 0:
        return {"status": "success"}
    else:
        return {"status": "failed"}
    
@app.get('/addproduct/{database}/{product_name}/{description}/{price}/{stock}')
async def add_product(database, product_name, description, price, stock):
    all_db = db[database]
    sql = "INSERT INTO products VALUES (%s, %s, %s, %s, %s)"
    val_sql = (None, product_name, description, price, stock)
    
    all_db.mycursor.execute(sql, val_sql)
    all_db.mydb.commit()
    
    if all_db.mycursor.rowcount > 0:
        return {"status": "success"}
    else:
        return {"status": "failed"}
    
@app.get('/addorder/{database}/{order_date}/{total_amount}/{status}')
async def add_order(database,order_date,total_amount,status):
    all_db = db[database]
    sql = "INSERT INTO orders VALUES (%s, %s, %s, %s)"
    val_sql = (None,order_date,total_amount,status)
    
    all_db.mycursor.execute(sql, val_sql)
    all_db.mydb.commit()
    
    if all_db.mycursor.rowcount > 0:
        return {"status": "success"}
    else:
        return {"status": "failed"}
    
@app.get('/adduser/{database}/{username}/{password}/{email}/{user_role}')
async def add_order(database,username,password,email,user_role):
    all_db = db[database]
    sql = "INSERT INTO users VALUES (%s, %s, %s, %s, %s)"
    val_sql = (None,username,password,email,user_role)
    
    all_db.mycursor.execute(sql, val_sql)
    all_db.mydb.commit()
    
    if all_db.mycursor.rowcount > 0:
        return {"status": "success"}
    else:
        return {"status": "failed"}
    
@app.get('/delete/{database}/{table}/{column}/{id}')
async def delete(database, table, column, id):
    all_db = db[database]
    sql = f"DELETE FROM {table} WHERE {column} = %s"
    val_sql = (id,)

    all_db.mycursor.execute(sql, val_sql)
    all_db.mydb.commit()

    if all_db.mycursor.rowcount > 0:
        return {"status": "success"}
    else:
        return {"status": "failed"}
    
@app.get('/edit/{database}/{table}/{columname}/{val}/{columid}/{id}')
async def edit(database,table,columname,val,columid,id):
    all_db = db[database]
    sql = f"UPDATE {table} SET {columname} = %s WHERE {columid} = %s"
    val_sql = (val,id)

    all_db.mycursor.execute(sql,val_sql)
    all_db.mydb.commit()

    if all_db.mycursor.rowcount > 0:
        return {"status": "success"}
    else:
        return {"status": "failed"}
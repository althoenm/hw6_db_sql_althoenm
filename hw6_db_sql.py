'''
Name: Matteo Althoen
Uniqname: althoenm
'''

import sqlite3 

def question0():
    ''' Constructs and executes SQL query to retrieve
    all fields from the Region table
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT * FROM Region"
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question1():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT * FROM Territory"
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question2():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT COUNT(*) FROM Employee"
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question3():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT * From Product order by Id desc limit 10"
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question4():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "Select ProductName, UnitPrice from Product order by UnitPrice desc limit 3"
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question5():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "Select ProductName, UnitPrice, UnitsInStock from Product where UnitsInStock between 60 AND 100"
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question6():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "Select ProductName from Product where UnitsInStock < ReorderLevel"
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question7():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "Select Id from [Order] where (ShipCountry = 'France') AND (ShipPostalCode LIKE '%04')"
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question8():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "Select CompanyName, ContactName from Customer where Country = 'UK' and Fax is not null"
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question9():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "Select Product.ProductName, Product.UnitPrice from Product join Category on Product.CategoryId=Category.Id where Category.CategoryName = 'Beverages'"
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question10():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "Select Product.ProductName from Product join Category on Product.CategoryId=Category.Id where Category.CategoryName = 'Meat/Poultry' and Product.Discontinued=1"
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question11():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT [Order].Id, Employee.FirstName, Employee.LastName from [Order] Join Employee ON [Order].EmployeeId=Employee.Id WHERE [Order].ShipCountry = 'Germany'"
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question12():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT [Order].Id, [Order].OrderDate, Customer.CompanyName from [Order] Join Customer ON [Order].CustomerId=Customer.Id WHERE [Order].OrderDate <= '2012-07-10'"
    result = cursor.execute(query).fetchall()
    connection.close()
    return result



#################################################################
########################  ECs start here  #######################
#################################################################

#########
## EC1 ##
#########

def print_query_result(raw_query_result):
    ''' Pretty prints raw query result
    
    Parameters
    ----------
    list 
        a list of tuples that represent raw query result
    
    Returns
    -------
    None
    '''
    #TODO Implement function
    pass


if __name__ == "__main__":
    '''WHEN SUBMIT, UNCOMMENT THE TWO LINES OF CODE
    BELOW IF YOU COMPLETED EC1'''
    # result = question9()
    # print_query_result(result)
  
#########
## EC2 ##
#########
    
    #TODO Implement interactive program here
    pass


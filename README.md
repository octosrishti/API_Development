# Market Analysis system

The Market Analysis system is a backend API returns a analytical data from server using 4 api's

The system provides four APIs:

1 Api 1:
End point : /api/total_items ,
```
API Use Cases :
1. Total item (total seats) sold in Marketting for last in q3 of the year?
Expected O/P: returns integer
Parameters: {start_date: DATE, end_date: DATE, department: string}
```
2. Api 2:
End point : /api/nth_most_total_item ,
```
API Use Cases:
1.What is the 2nd most sold item in terms of quantity sold in q4,
2.What is the fourth most sold item in terms of Total price in q2?
Expected O/P: returns string name
Parameters: { item_by: ("quantity" | | "price"), start_date: DATE, end_date:
DATE, n:integer }
```
3. Api 3:
End point : /api/percentage_of_department_wise_sold_items
```
API Use Cases:
1.What is the percentage of sold items (seats) department wise?
Expected O/P: {dept_name: x%,……. }
Parameters: {start_date: Date, end_date: Date}
```
4. Api 4:
End point : /api/monthly_sales
```
API Use Cases:
1.How does the monthly sales for any product look like?
Expected O/P: [1908.0, … 1952.0] for all 12 months
Parameters: {product: String, year:Number}
```

## Data Sources 

The system has the following three sources of data:

A CSV file with three columns (id, department, software seats, amount, date, user)
    
**_NOTE:_**  Data files cannot be pushed due to lfs issue 
     
         #### Files structure 
         
         ```
            config/
            api/
            data.csv
            
            ```

## Installation 

To install the required packages, run the following command in the project directory:
```
    pipenv shell
    pip install -r requirements.txt

```



To install postgresql docker

```

    docker run -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -v /postgresql/data:/var/lib/postgresql/data -d postgres:15

```

## Usage

Start postgres docker container in interactive mode

```

    docker exec -it 0c847b8babad -U postgres -p mysecretpassword

```

Create database and User in the container terminal
```

    psql
    CREATE DATABASE restaurant_poll
    CREATE USER poll_user WITH PASSWORD 'poll_password'
    ALTER USER poll_user WITH SUPERUSER
    GRANT ALL PRIVILEGES ON restaurant_poll TO 'poll_user'

```

Start rabbitmq:management server if container not running 

```

    docker ps -a
    docker run 'container ID'

```

Make migrations in the Database

```

    python manage.py makemigrations 
    python manage.py migrate

```

To start the server, run the following command in the project directory:
```

    python manage.py runserver
    
```

The server will start running on http://localhost:8000

Note: Remember to add url prefix in the api like http://localhost:8000/api

## API Documentation

- ### /api/total_items 

    This endpoint triggers the generation of a report from the data provided (stored in the database).

    * Request
    ```
    POST /api/total_items  HTTP/1.1

    ```
    * Response
    ```
        HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "total" : "total items : Number"
    }

    ```
- ### /api/nth_most_total_item 

    This endpoint triggers the generation of a report from the data provided (stored in the database).

    * Request
    ```
    POST /api/nth_most_total_item  HTTP/1.1

    ```
    * Response
    ```
        HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "department" : "string"
    }

    ```
- ### /api/percentage_of_department_wise_sold_items 

    This endpoint triggers the generation of a report from the data provided (stored in the database).

    * Request
    ```
    POST /api/percentage_of_department_wise_sold_items  HTTP/1.1

    ```
    * Response
    ```
        HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "data" : [department : total sales]
    }

    ```
- ### /api/monthly_sales

    This endpoint triggers the generation of a report from the data provided (stored in the database).

    * Request
    ```
    POST /api/monthly_sales HTTP/1.1

    ```
    * Response
    ```
        HTTP/1.1 200 OK
    Content-Type: application/json

    {
        'departments': [month : total sales], 
    }

    ```
## Functionalities 

Used advance python features like -
 - docker for postgres db
 - dango rest framework


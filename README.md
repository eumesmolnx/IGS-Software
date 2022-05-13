# IGS Software Manager

This is Python-Django test project and your main go is to create a API to manage Human Recourses data.

**Technologies**:

 - Python 3.10.1
 - Django 4.0.4
 - PostgreSQL 13.5
 - Docker Compose 3.3

## How to Run
1. Build Docker Image
`docker-compose build`
2. Run Docker Container
`docker-compose up`

## Usage
1. List Employees

**Request**

> [GET] /employee

**Response**
`[  
    {  "name":  "Felipe Morais",
      "email":  "felipe.morais@igs-software.com.br",
      "departament":  "Tester"  
    },  
    {  "name":  "Tatiane Laura", 
        "email":  "tatiane.laura@igs-software.com.br", 
        "departament":  "Developer"
    },  
    {  "name":  "Mauricio Alegretti",
        "email":  "mauricio.alegretti@igs-software.com.br",
        "departament":  "RH" 
    }
]`

2. List Departaments

**Request Body**

> [GET] /departament
 
**Response**
`[  {  "name":  "RH"  },  {  "name":  "Tester"  },  {  "name":  "Developer"  }  ]`

3. Create New Employee

**Request Body**

> [POST] /employee
    
    Header: application/json
    
    {
    "name": "John Doe",
    "email": "john@mail.com",
    "departament": "RH"
    }

**Response**
`{ "name": "John Doe", "email": "john@mail.com", "departament": "RH" }`

4. Create New Departament

**Request Body**

> [POST] /departament
    
    Header: application/json
    
    {
    "name": "IT"
    }

**Response**
`{ "name": "IT" }`

5. Update Employee

**Request Body**

> [PUT] /employee/[id]

**Parameters**
>**id** - Departament Id    
    
    Header: application/json
    
    {
    "name": "John Doe",
    "email": "john@mail.com",
    "departament": "RH"
    }

**Response**
`{ "name": "John Doe", "email": "john@mail.com", "departament": "RH" }`

6. Update Departament

**Request Body**

> [PUT] /departament/[id]

**Parameters**
>**id** - Departament Id    

    
    Header: application/json
    {
    "name": "IT"
    }

**Response**
`{ "name": "IT" }`

7. Delete Employee

**Request Body**

> [DELETE] /employee/[id]
>     
**Parameters**
>**id** - Departament Id

**Response**
`200 OK`

8. Delete Departament

**Request Body**

> [DELETE] /departament/[id]

**Parameters**
>**id** - Departament Id    

**Response**
`200 OK`

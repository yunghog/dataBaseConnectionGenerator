#dbGen.py : Easy way to generate Database connection file for your project
#author : Samartha

format = input('Input extension of DBConnect file (js/php/java) : ')
platform = input('Input Database provider (mysql/oracle) :  ')
dbServer = input('Enter the Database Server URL : ')
dbName = input('Enter the Database Name : ')
dbUser = input('Enter the Username : ')
dbPswd = input('Enter the Database Password : ')
if format=='js':
    dbCon = open(r'dbConnect.js','w')
    dbCon.write("var mysql = require('mysql')\n")
    dbCon.write("var con = mysql.createConnection({\n")
    host="host: " + dbServer + ",\n"
    dbCon.write(host)
    dbUser="user: " + dbName + ",\n"
    dbCon.write(dbUser)
    dbPswd="passsword: " + dbPswd + ",\n"
    dbCon.write(dbPswd)
    dbCon.write("})")
    dbCon.write("con.connect(function(err)){\n")
    dbCon.write("if(err) throw err;\n")
    dbCon.write("console.log('Connected')\n")
    dbCon.write("});")

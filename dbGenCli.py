#dbGen.py : Easy way to generate Database connection file for your project
#author : Samartha
import dbGen as d
format = input('Input extension of DBConnect file (js/php) : ')
platform = input('Input Database provider (mysql/oracle) :  ')
dbServer = input('Enter the Database Server URL : ')
dbName = input('Enter the Database Name : ')
dbUser = input('Enter the Username : ')
dbPswd = input('Enter the Database Password : ')
print(d.gen(format,dbServer,dbName,dbPswd,dbName))

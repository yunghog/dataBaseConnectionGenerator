#dbGen.py : Easy way to generate Database connection file for your project
#author : Samartha

def gen(format,dbServer,dbUser,dbPswd,dbName):
    flag=0
    if format=='js':
        dbCon = open(r'dbConnect.js','w')
        dbCon.write("var mysql = require('mysql')\n")
        dbCon.write("var con = mysql.createConnection({\n")
        host="host: " + dbServer + ",\n"
        dbCon.write(host)
        dbUser="user: " + dbUser + ",\n"
        dbCon.write(dbUser)
        dbPswd="passsword: " + dbPswd + ",\n"
        dbCon.write(dbPswd)
        dbCon.write("})")
        dbCon.write("con.connect(function(err)){\n")
        dbCon.write("if(err) throw err;\n")
        dbCon.write("console.log('Connected')\n")
        dbCon.write("});")
        flag=1
    elif format=='php':
        dbCon = open(r'dbConnect.php','w')
        dbCon.write("<?php\n")
        host="$servername = '" + dbServer + "';\n"
        dbCon.write(host)
        dbUser="$username = '" + dbUser + "';\n"
        dbCon.write(dbUser)
        dbName="$dbname = '" + dbName + "';\n"
        dbCon.write(dbName)
        dbPswd="$passsword = '" + dbPswd + "';\n"
        dbCon.write(dbPswd)
        dbCon.write("$conn = new mysqli($servername,$username,$passsword,$dbname);\n")
        dbCon.write("if ($conn->connect_error) {\n")
        dbCon.write(" die('Connection failed: ' . $conn->connect_error);\n")
        dbCon.write("}\n")
        dbCon.write("echo 'Connected Successfully';\n?>")
        flag=1
    if flag==1:
        return 'Success'
    else:
        return 'Failed'

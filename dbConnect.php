<?php
$servername = 'localhost';
$username = 'testDB';
$dbname = 'testDB';
$passsword = 'pswd';
$conn = new mysqli($servername,$username,$passsword,$dbname);
if ($conn->connect_error) {
 die('Connection failed: ' . $conn->connect_error);
}
echo 'Connected Successfully';
?>
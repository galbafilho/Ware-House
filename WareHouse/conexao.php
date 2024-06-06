<?php
$hostname = 'localhost';
$username = 'root';
$password = '';
$database = 'gwarehouse';

$conexao = mysqli_connect($hostname, $username, $password, $database);
if(!$conexao){
die("Houve um erro: ".mysqli_connect_error());
}
?>
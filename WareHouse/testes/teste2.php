<?php
include_once("teste.php");
$nome=$_POST['nome'];
$email=$_GET['email'];
$senha=$_GET['senha'];
$sql="INSERT INTO cadastro(nome, email, senha) VALUES ('$nome', '$email', '$senha' )";
$resultado = mysqli_query($conexao,$sql);
mysqli_close($conexao);
?>
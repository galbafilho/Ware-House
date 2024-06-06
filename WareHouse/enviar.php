<?php
include_once("conexao.php");
$nome=$_POST['nome'];
$email=$_POST['email'];
$dt_nasc=$_POST['dt_nasc'];
$senha=$_POST['senha'];
$sql="INSERT INTO cadastro(nome, email, dt_nasc, senha) VALUES ('$nome', '$email', '$dt_nasc', '$senha' )";
$resultado = mysqli_query($conexao,$sql);
mysqli_close($conexao);
?>
<script>
    setTimeout(function(){
        window.location.href="index.html";
    }, 1000)
</script>
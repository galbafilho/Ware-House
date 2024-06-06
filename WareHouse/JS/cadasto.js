function checkPassword() {
    var password = document.getElementById('senha').value;
    var confirmPassword = document.getElementById('confirmPassword').value;

    if (password === confirmPassword) {
        document.getElementById('passwordMatch').textContent = 'As senhas coincidem!';
    } else {
        document.getElementById('passwordMatch').textContent = 'As senhas não coincidem.';
    }
}

function abrirPagina() {
  window.location.href = 'index.html';
}

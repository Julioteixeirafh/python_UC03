from conta import ContaCorrente

contas = {
    '123': ContaCorrente('Julio', '123', 'jui666', 50000),
    '456': ContaCorrente('Cezar', '456', 'Cez333', 100000) 
}


#Login

ContaCorrente.mostrar_saldo(contas['123'])
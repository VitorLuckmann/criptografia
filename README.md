# Projeto de Criptografia em Python

Implementação de algoritmos de criptografia:
- **Simétrica (Fernet - AES)**
- **Assimétrica (RSA)**

## Requisitos
- Python 3.8+
- Biblioteca `cryptography`

Instalação:
```bash
pip install cryptography
```

## Estrutura
```
criptografia/
│
├── simetrica.py       # Algoritmo de criptografia simétrica
├── assimetrica.py     # Algoritmo de criptografia assimétrica
└── README.md          # Documentação do projeto
```

## Execução

### Criptografia Simétrica
```bash
python simetrica.py
```

### Criptografia Assimétrica
```bash
python assimetrica.py
```

## Saída esperada
Os programas exibem:
- Texto original
- Texto cifrado
- Texto decifrado
- (Para simétrica) chave gerada

## Observações
- A chave simétrica é gerada automaticamente a cada execução.  
- As chaves RSA são criadas dinamicamente para fins didáticos.  
- Para uso real, recomenda-se salvar as chaves em arquivos seguros.

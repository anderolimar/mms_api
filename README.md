# Crypto Moving Average Service

Este serviço gerencia e expõe dados de Média Móvel Simples (MMS) para pares de criptomoedas BRL/BTC e BRL/ETH. O sistema consiste em uma API REST, um job agendado para atualização de dados diária e um script de carga inicial.

## Visão Geral

O sistema é composto por três componentes principais:

1. **API REST**: Fornece um endpoint para consulta de dados de MMS
2. **Job Diário**: Atualiza automaticamente os dados de MMS todos os dias
3. **Script de Carga Inicial**: Popula o banco de dados com dados históricos de MMS

## API

A API expõe o seguinte endpoint:

### GET /:pair/mms

Retorna os dados de Média Móvel Simples (MMS) para um par de moedas específico.

#### Parâmetros do Path

- `pair` (obrigatório): Par de moedas (valores aceitos: `BRLBTC` ou `BRLETH`)

#### Parâmetros de Query

- `from` (obrigatório): Timestamp inicial para filtrar os dados
- `to` (opcional): Timestamp final para filtrar os dados (padrão: dia anterior)
- `range` (obrigatório): Período da média móvel (valores aceitos: `20`, `50` ou `200` dias)

#### Exemplo de Requisição

```
GET http://localhost:8080/BRLBTC/mms?from=1680307200&to=1683072000&range=20
```

#### Exemplo de Resposta

```json
[
  {
    "timestamp": 1680307200,
    "mms": 142567.89
  },
  {
    "timestamp": 1680393600,
    "mms": 143210.45
  },
  ...
]
```

## Estrutura do Banco de Dados

Os dados são armazenados em uma tabela única com a seguinte estrutura:

> pair_mms

| Campo    | Tipo      | Descrição                           |
|----------|-----------|-------------------------------------|
| pair     | string    | Par de moedas (BRLBTC ou BRLETH)    |
| timestamp| integer   | Timestamp do dia (época Unix)       |
| mms_20   | float     | Média Móvel Simples de 20 dias      |
| mms_50   | float     | Média Móvel Simples de 50 dias      |
| mms_200  | float     | Média Móvel Simples de 200 dias     |

Para a execução do job temos a tabela a seguir:

> jobs

| Campo    | Tipo      | Descrição                           |
|----------|-----------|-------------------------------------|
| pair     | string    | Par de moedas (BRLBTC ou BRLETH)    |
| timestamp| integer   | Timestamp do dia (época Unix)       |
| finished | boolean   | Indicação de finalizaçãodo job      |


## Componentes do Sistema

### Job de Atualização Diária

Um job automatizado que atualiza a tabela de dados de MMS todos os dias.

**Estratégia:**
- Controle de excução do job via entrada na tabela `jobs` no banco de dados
- Obtém os dados dos últimos 200 dias para cada par (BRLBTC, BRLETH)
- Calcula a média móvel para os períodos de 20, 50 e 200 dias
- Persiste os resultados no banco de dados
- Execução diária (via scheduler)

### Script de Carga Inicial

Script que realiza o carregamento inicial da tabela com dados históricos.

**Estratégia:**
- Obtém os dados dos últimos 565 dias para cada par (BRLBTC, BRLETH)
- Calcula as médias móveis para os períodos de 20, 50 e 200 dias
- Persiste os resultados no banco de dados
- Execução única (manual)

## Documentação da API

A documentação completa da API está disponível via Swagger:

**URL**: http://localhost:8080/docs

## Instalação e Execução


Para iniciar o ambiente via docker-compose

```ssh
make env-up
```

Rodar script para carga inicial de dados

```ssh
make load
```

### Local

Crie ambiente virtual executando o comando:

```sh
make virtual
source .venv/bin/activate	
```

Instale as dependecias com o comando:

```sh
make install
```

Para rodar a api localmente execute o comando:

```sh
make start
```

Para rodar a job localmente execute o comando:

```sh
make job
```

### Testes

Para rodar os tests execute o comando:

```sh
make test
```

## Debitos Técnicos

- Implementar um alarme que deveria ser disparado quando falte o registro de algum dia dentre
  os registros dos últimos 365 dias

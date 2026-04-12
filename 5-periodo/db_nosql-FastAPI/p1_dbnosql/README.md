
# Passo a passo realizado

1. Para iniciar a infraestrutura e deixar os contêineres rodando em segundo plano, na raiz do projeto:

```bash
sudo docker-compose up -d --build
```
2. Acessando o MongoDB

```bash
sudo docker exec -it p1_dbnosql_mongodb_1 mongosh
```

## CRUD - Alunos

3. Criar e acessar o banco de dados
```bash
use escola
```

4. Inserir 5 alunos na coleção alunos
```
db.alunos.insertMany([
  { "nome": "João Silva", "idade": 20, "curso": "ADS", "notas": [7, 8, 9], "endereco": { "cidade": "Maricá", "estado": "RJ" } },
  { "nome": "Mariana Costa", "idade": 22, "curso": "Sistemas de Informação", "notas": [8, 9, 10], "endereco": { "cidade": "Niterói", "estado": "RJ" } },
  { "nome": "Carlos Eduardo", "idade": 19, "curso": "ADS", "notas": [6, 7, 8], "endereco": { "cidade": "Maricá", "estado": "RJ" } },
  { "nome": "Ana Beatriz", "idade": 23, "curso": "Engenharia de Software", "notas": [9, 9, 8], "endereco": { "cidade": "Rio de Janeiro", "estado": "RJ" } },
  { "nome": "Jonathan Almeida", "idade": 18, "curso": "Engenharia de Software", "notas": [9, 8, 10], "endereco": { "cidade": "Maricá", "estado": "RJ" } }
])
```

## Consultas Realizadas
1. Buscar todos os alunos

```
db.alunos.find()
```

2. Buscar alunos do curso "ADS"

```
db.alunos.find({ "curso": "ADS" })
```

3. Buscar alunos com idade maior que 21

```
db.alunos.find({ "idade": { $gt: 21 } })
```

4. Atualizar a idade de um aluno (Ex: Atualizando o João Silva para 21 anos)

```
db.alunos.updateOne(
  { "nome": "João Silva" },
  { $set: { "idade": 21 } }
)
```

5. Adicionar uma nova nota a um aluno (Ex: Adicionando a nota 10 para o João Silva)

```
db.alunos.updateOne(
  { "nome": "João Silva" },
  { $push: { "notas": 10 } }
)
```

6. Remover um aluno (Ex: Removendo a Ana Beatriz)

```
db.alunos.deleteOne({ "nome": "Ana Beatriz" })
```

7. Média de notas por aluno

```
db.alunos.aggregate([
  {
    $project: {
      nome: 1,
      media: { $avg: "$notas" }
    }
  }
])
```

8. Quantidade de alunos por curso

```bash
db.alunos.aggregate([
  {
    $group: {
      _id: "$curso",
      quantidade: { $sum: 1 }
    }
  }
])
```
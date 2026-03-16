const express = require("express")
const Database = require("better-sqlite3")
const fs = require("fs")

const app = express()
const banco = new Database("banco.db")

banco.prepare("CREATE TABLE IF NOT EXISTS pessoas (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)").run()

app.get("/", (req, res) => {
  const pessoas = banco.prepare("SELECT * FROM pessoas").all()

  let itens = ""

  for (let i = 0; i < pessoas.length; i++) {
    let pessoa = pessoas[i]
    itens = itens + "<li>" + pessoa.id + " - " + pessoa.nome + ' <a href="/delete?id=' + pessoa.id + '">Excluir</a></li>'
  }

  let pagina = fs.readFileSync("index.html", "utf8")
  pagina = pagina.replace("__LISTA__", itens)

  res.send(pagina)
})

app.get("/salvar", (req, res) => {
  console.log(req)
  const nome = req.query.nome

  if (nome) {
    banco.prepare("INSERT INTO pessoas (nome) VALUES (?)").run(nome)
  }

  res.redirect("/")
})

app.get("/delete", (req, res) => {
  const id = req.query.id

  if (id) {
    banco.prepare("DELETE FROM pessoas WHERE id = ?").run(id)
  }

  res.redirect("/")
})

app.listen(3000, () => {
  console.log("Servidor rodando na porta 3000")
})
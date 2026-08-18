---
tipo: moc
titulo: 00-INBOX
tags: [moc]
---

# 📥 Inbox

Lugar de **capturar sem pensar**. Ideia, foto de campo, print de WhatsApp do cliente,
dúvida de norma, número que ouvi numa reunião — joga aqui e segue.

Processar é outra tarefa, e ela tem hora marcada: **sexta-feira, 30 minutos**.

## Como processar

Para cada item, uma das cinco saídas:

1. **É cliente novo?** → [[T - Cliente]] em `03-CLIENTES/`
2. **É trabalho contratado?** → [[T - Projeto]] em `04-PROJETOS/`
3. **É conhecimento?** → nota em `02-NORMAS/` ou `05-BIBLIOTECA/`
4. **É ação com prazo?** → [[T - Ação]], com `prazo:` no frontmatter
5. **Não é nada disso** → apagar. Sem cerimônia.

Item que fica no Inbox por mais de duas semanas quase sempre pertence à saída 5.

## O que está aqui agora

```dataview
LIST
FROM "00-INBOX"
WHERE file.name != "00-INBOX" AND !contains(file.folder, "diario")
SORT file.mtime ASC
```

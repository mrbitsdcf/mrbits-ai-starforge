# Política de segurança

## Versões suportadas

Este repositório distribui artefatos versionados por tags e releases do GitHub. A versão suportada é a release pública mais recente.

## Como relatar uma vulnerabilidade

Não abra uma issue pública para:

- Segredos ou credenciais expostos.
- Vulnerabilidades exploráveis.
- MCPs com permissões excessivas ou vazamento de dados.
- Prompts ou skills que induzam execução insegura.

Use o recurso de private vulnerability reporting do GitHub, quando disponível, ou entre em contato de forma privada com os mantenedores.

Inclua:

- Artefato afetado.
- Versão, commit ou branch.
- Passos para reproduzir.
- Impacto esperado.
- Mitigação sugerida, se houver.

## Escopo

Estão no escopo:

- Scripts e templates incluídos no repositório.
- Instruções de agentes que possam executar ações perigosas.
- Configurações de MCP que acessem dados, rede, arquivos ou credenciais.
- Exemplos que possam vazar dados sensíveis.

Fora do escopo:

- Vulnerabilidades em serviços de terceiros não configurados por este repositório.
- Uso indevido causado por alteração local fora dos artefatos publicados.

## Princípios de segurança

- Nenhum artefato deve exigir credenciais reais no repositório.
- Exemplos devem usar valores fictícios.
- MCPs devem documentar permissões e variáveis de ambiente.
- Scripts devem evitar ações destrutivas por padrão.
- Templates devem privilegiar configurações seguras.

# Aula 09

**Sumário**

- [Aula 09](#aula-09)
  - [Docker](#docker)
    - [`Dockerfile`](#dockerfile)
    - [`Docker CLI`](#docker-cli)
    - [`Docker compose`](#docker-compose)
  - [Mais informações](#mais-informações)


## Docker

O `Docker` é uma plataforma aberta para **desenvolver**, **distribuir** e **executar** aplicações. O `Docker` permite **separar** suas aplicações da sua infraestrutura, possibilitando a entrega rápida de software. Ele permite empacotar e executar uma aplicação em um ambiente **parcialmente isolado**, chamado `contêiner`. O isolamento e a segurança permitem executar vários `contêineres` simultaneamente em um mesmo *host*.

Um `contêiner` é uma unidade padrão de software que **empacota** o código e todas as suas dependências, permitindo que o aplicativo seja executado de forma rápida e confiável em **diferentes ambientes computacionais**.

<figure style="text-align:center;">
  <img src="imagens/docker-what-is-container.png">
</figure>

Em outras palavras, `contêineres` são **processos isolados para cada componente** de uma aplicação. Cada componente (por exemplo, uma aplicação *front-end* com React, *back-end* API com Python, e um banco de dados) é executado em seu próprio ambiente isolado, e completamente isolado do restante de sua máquina.

<figure style="text-align:center;">
  <img src="imagens/docker-containerized-and-vm-transparent-bg-1110x454.png">
  <figcaption>Diferença entre contêneres e Máquinas Virtuais</figcaption>
</figure>

Uma **imagem de contêiner** Docker é um pacote de software leve, **independente** e **executável**, que **inclui tudo o que é necessário para executar um aplicativo**: código, ambiente de execução, ferramentas de sistema, bibliotecas de sistema e configurações.

**Imagens de contêiner** podem ser encontradas no [`Docker Hub`](https://hub.docker.com/), o qual consiste em um `registro` público de imagens, ou seja, uma localização central de armazenamento e compartilhamento de imagens de contâiner. Os registros podem também ser locais e privados e, quando públicos, não serem o [`Docker Hub`](https://hub.docker.com/). Exemplo:

- [Amazon Elastic Container Registry](https://aws.amazon.com/pt/ecr/) (ECR);
- [Azure Container Registry](https://azure.microsoft.com/en-in/products/container-registry) (ACR);
- [Google Container Registry](https://docs.cloud.google.com/artifact-registry/docs?hl=pt-br) (GCR).

### `Dockerfile`

Um `Dockerfile` é um arquivo/documento que é usado para criar um contêiner a partir de uma imagem. [Exemplo](https://docs.docker.com/get-started/docker-concepts/building-images/writing-a-dockerfile/):

```Dockerfile
FROM python:3.13
WORKDIR /usr/local/app

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY src ./src
EXPOSE 8080

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
```

Onde:

- `FROM <image>` especifica a imagem base.
- `WORKDIR <path>` especifica o "diretório de trabalho", ou o caminho na imagem onde os arquivos serão copiados e os comandos executados.
- `COPY <host-path> <image-path>` informa ao *builder* (o software que vai construir o contêiner a partir da imagem) para copiar arquivos do *host* e colar no contêiner da imagem.
- `RUN <command>` diz para *builder* executar o comando especificado.
- `ENV <name> <value>` define a variável de ambiente que um contêiner em execução usará.
- `EXPOSE <port-number>` define a configuração da imagem, indicando a porta que a imagem deseja expor.
- `USER <user-or-uid>` define o usuário padrão para todas as instruções subsequentes.
- `CMD ["<command>", "<arg1>"]` define o comando padrão que o contêiner dessa imagem executará.

Para uma lista completa de instruções que podem ser utilizadas no `Dockerfile`, e sua documentação: [Dockerfile reference](https://docs.docker.com/reference/dockerfile/).

### `Docker CLI`

O `Docker CLI` (*Command Line Interface*) é a forma “padrão” de uso do Docker. Sua referência pode ser encontrada [aqui](docs.docker.com/reference/cli/docker/). Alguns dos principais comandos são:

- [`docker build`](https://docs.docker.com/reference/cli/docker/buildx/build/)
- [`docker [container] run`](https://docs.docker.com/reference/cli/docker/container/run/)
- [`docker [image] pull`](https://docs.docker.com/reference/cli/docker/image/pull/)
- [`docker init`](https://docs.docker.com/reference/cli/docker/init/)

### `Docker compose`

Projetos maiores e mais complexos possuem mais componentes. Todos esses componentes podem estar inclusos em um único contêiner. Entretanto, essa não é uma boa prática. Além de deixar o projeto como um todo mais complexo, podemos ter como consequência vulnerabilidades de segurança e também de *runtime*. Solução: `Docker compose`, o qual consiste em um arquivo `yaml` contendo todos os contêineres e suas configurações.

Exemplo:

```yaml
services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/code
    environment:
      - FLASK_ENV=development
      - DATABASE_URL=postgresql://postgres:secret_pass@db:5432/mydb
    depends_on:
      - db

  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: secret_pass
      POSTGRES_DB: mydb
    volumes:
      - postgres_data: /var/lib/postgresql/data
    ports:
      - "5432:5432"
  
volumes:
  postgres_data:
```

## Mais informações

- [Roadmap Docker](https://roadmap.sh/docker)
- [Docker docs](https://docs.docker.com/)
  - [Get started](https://docs.docker.com/get-started/)
  - [Guides](https://docs.docker.com/guides/)
  - [Manuals](https://docs.docker.com/manuals/)
  - [Reference](https://docs.docker.com/reference/)
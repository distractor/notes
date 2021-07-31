# Docker containers

You can think of dockers like extremely lightweight virtual environment.

This is not entirely true but it is a good representation. The right way of using a docker container is to first create a virtual environment (as light as possible) and then install the docker there. **Why?** Mainly for the security reasons. In case of security breach the hackers can only see and mess with the files within the virtual environment, and not the whole server computer.

## Dockerfile

Creating a docker file is not that difficult. There are many examples online. Here is one I used for registration app backend written in .NET

```docker
FROM mcr.microsoft.com/dotnet/aspnet:5.0-buster-slim AS base
RUN sed -i'.bak' 's/$/ contrib/' /etc/apt/sources.list
RUN apt-get update; apt-get install -y ttf-mscorefonts-installer fontconfig
WORKDIR /app

FROM mcr.microsoft.com/dotnet/sdk:5.0-buster-slim AS build
WORKDIR /src
COPY ["MetuljmaniaDatabase.csproj", "."]
RUN dotnet restore "./MetuljmaniaDatabase.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "MetuljmaniaDatabase.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "MetuljmaniaDatabase.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
EXPOSE 80
COPY --from=publish /app/publish .
ENV ASPNETCORE_ENVIRONMENT="Development"
ENTRYPOINT ["dotnet", "MetuljmaniaDatabase.dll"]
```

## Building docker image

First go to project's root and run

```sh
docker build -t metuljmania/dockerapi .
```

## Running docker image

After the image is build, run it with

```sh
docker run --name backend --mount type=bind,source=/home/mjancic/Documents/Data,target=/Data -p 8081:80 metuljmania/dockerapi
```

Now this is a but more complex.

- The _name_ flag is not that important, it does however simplify things.
- The _mount_ flag mounts volume of local (server) files with docker filesystem.
- The _p_ flag is about the ports.

> Note that the order of the flags is important!
>
> ```sh
> docker run [OPTIONS] IMAGE[:TAG|@DIGEST] [COMMAND] [ARG...]
> ```
>
> Or check official documentation for more details.

## How to enter Docker when running

You can enter Docker just as any other server. Similar to ssh but not really.

To connect to Docker, use

```sh
docker exec -it CONTAINER_ID bash
```

or

```sh
docker exec -it CONTAINER_ID /bin/sh
```

depending on the lightness of the docker OS used.

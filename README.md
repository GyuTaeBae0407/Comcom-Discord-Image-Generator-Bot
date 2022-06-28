# comcom

## 사용법

```shell
git clone git@github.com:GyuTaeBae0407/comcom.git
cd comcom
docker build -t <DOCKER_IMAGE_NAME> .
docker run -d -e DISCORD_TOKEN=<DISCORD_TOKEN> -e DISCORD_GUILD_ID=<DISCORD_GUILD_ID> -e FIREBASE_FUNCS_URL=<FIREBASE_FUNCS_URL> <DOCKER_IMAGE_NAME>
```

## 참고자료

- https://guide.pycord.dev/getting-started/creating-your-first-bot/

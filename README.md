# Weather Talk
Templates para o projeto do Processo Seletivo da GoBots. Escolha o template
nas pastas do repositório pela linguagem de sua preferência. Nós recomendamos
explicitamente o uso de IDEs como **IntelliJ**, **PyCharm** ou **VSCode**.


# API de Processamento de Linguagem Natural
O *parsing* de texto em intenções e entidades pode ser feito com um **POST**:
```bash
curl -XPOST -s https://weathertalk.gobots.com.br/model/parse -d '{"text":"qual a temperatura no próximo domingo em Campinas?"}'
```

A resposta retornada pela API é um JSON da forma:
```json
{
  "text": "qual a temperatura no próximo domingo em Campinas?",
  "intent": {
    "name": "clima",
    "confidence": 0.9249110221862793
  },
  "entities": [
    {
      "start": 19,
      "end": 37,
      "text": "no próximo domingo",
      "value": "2021-12-05T00:00:00.000-03:00",
      "entity": "time",
      ...
    },
    {
      "entity": "city",
      "start": 41,
      "end": 49,
      "value": "Campinas",
      ...
    }
  ],
  ...
}
```

# API de Previsão do Tempo
Recomendamos o uso do [OpenWeather](https://openweathermap.org/) para saber informações climáticas.
Para requisitar informações sobre o clima de **agora** em uma cidade:
```bash
curl -XGET -s 'https://api.openweathermap.org/data/2.5/weather?q=$CITY_NAME&units=metric&lang=pt_br&appid=$APP_ID'
```
Veja o objeto JSON retornado na [Documentação](https://openweathermap.org/current#current_JSON). 

Você precisa de uma chave `APP_ID` para ter acesso à API. 
Solicite a um dos examinadores ou crie sua conta no [OpenWeather](https://home.openweathermap.org/users/sign_in).

Para requisitar informações detalhadas sobre o clima nas próximas horas ou nos próximos dias em um local, use a API
de *one-call* com a **latitude** e **longitude** da cidade em que se deseja conhecer a informação climática:
```bash
curl -XGET -s 'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&lang=pt_br&appid=$APP_ID'
```

As **latitude** e **longitude** podem ser obtidas a partir da cidade com a API *weather* do OpenWeather. Veja o objeto JSON retornado na [Documentação](https://openweathermap.org/api/one-call-api#example).

# Templates e Dependências

## Java
O projeto em Java usa *Maven*.
Para instalar as dependências, execute dentro da pasta **java/**:
```bash
$ ./mvnw package
```

## Kotlin
O projeto em Kotlin usa *Gradle*.
Para instalar as dependências, execute dentro da pasta **kotlin/**:
```bash
$ ./gradlew build
```

## Python
O projeto em python usa *virtual environments* com o `pipenv`. 
Para instalar as dependências, execute dentro da pasta **python/**:
```bash
$ pipenv install --dev
```

Para rodar a aplicação:
```bash
$ pipenv run app
```

Para executar testes:
```bash
$ pipenv run test
```

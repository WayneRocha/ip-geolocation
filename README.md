# IP Geolocation &#127758;

Aplicação Web que obtem a localização geografica aproximada de um ip

 * [Sobre](#sobre)
 * [Instalações e requisitos](#requisitos)
 * [Como iniciar a API](#como-usar)
 * [Tecnologias](#tecnologias)
 * [Contribuição](#contribuição)

<a href="#sobre">
  
## Sobre

</a>

No site se pede um IP ao usuario, e ao coloca-lo, são mostradas as informações geograficas dele como:

* Pais e cidade
* coordenas
* Precisão
* Mapa com o local aproximado do IP

### Exemplo de uso

![_Projetos_Localizador_de_IP_index html](https://user-images.githubusercontent.com/62760711/118326183-02a2e700-b4db-11eb-92c7-bb135dbdab8b.png)

![_C__Users_olawa_OneDrive_%C3%81rea%20de%20Trabalho_Projetos_Localizador_de_IP_index html](https://user-images.githubusercontent.com/62760711/118326393-4f86bd80-b4db-11eb-9733-3501c2ecd37c.png)


### Funcionamento

![IP-Geolocation-diagram](https://user-images.githubusercontent.com/62760711/117606597-987ff000-b130-11eb-967d-2032e8b37901.png)

<a href="#requisitos">
  
## Requisitos

</a>

Para o site funcionar é necessario que a API no arquivo [getLocationAPI](https://github.com/WayneRocha/Localizador_de_IP/blob/main/getLocationAPI.py) esteja executando

para que essa API funcione, as bibliotecas no arquivo [requirements.txt](https://github.com/WayneRocha/Localizador_de_IP/blob/main/requirements.txt) precisa estar instaladas na maquina.

basta digitar esse comando dentro da pasta do projeto para que as dependencias sejam instaladas:

```
pip install -r requirements.txt
```

<a href="#como-usar">
  
### Como iniciar a API

</a>

Abra o arquivo [getLocationAPI](https://github.com/WayneRocha/Localizador_de_IP/blob/main/getLocationAPI.py) com PyCharm ou outro programa que tenha suporte ao Flask

Ao iniciar será dado o endereço da API(caso você esteja rodando localmente). A url da API deve ser substituida no arquivo [api.js](https://github.com/WayneRocha/Localizador_de_IP/blob/main/js/api.js#L4)

![image](https://user-images.githubusercontent.com/62760711/117604728-87cd7b00-b12c-11eb-965a-de9b2d9eaa00.png)


<a href="#tecnologias">
  
### 🛠 Tecnologias

</a>

As seguintes ferramentas foram usadas na construção do projeto:

<img alt="HTML5" src="https://img.shields.io/badge/html5-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white"/>
<img alt="CSS3" src="https://img.shields.io/badge/css3-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white"/>
<img alt="JavaScript" src="https://img.shields.io/badge/javascript-%23323330.svg?&style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"/>
<img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/>
<img alt="Flask" src="https://img.shields.io/badge/flask-%23000.svg?&style=for-the-badge&logo=flask&logoColor=white"/>

<a href="contribuição">
  
  ### contribuição
  
</a>

<table>
<tr><td align="center"><a href="https://github.com/ArthurRoque"><img src="https://avatars.githubusercontent.com/u/66979434?v=4" width="200px;" alt=""/><br /><sub><b>Arthur Carvalho Roque</b></sub></a><br /><a href="https://github.com/ArthurRoque/Localizador_de_IP" title="Code">💻</a></td>
  <td align="center"><a href="https://github.com/WayneRocha"><img src="https://avatars.githubusercontent.com/u/62760711?v=4" width="200px;" alt=""/><br /><sub><b>Wayne Rocha</b></sub></a><br /><a href="https://github.com/WayneRocha/ip-geolocation" title="Code">💻</a></td>
</tr>
</table>

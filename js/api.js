let ip;
let ipInfos;
async function getIpInformations(ip){
    const apiDomain = 'http://127.0.0.1:5000/';
    fetch(`${apiDomain}geolocation?ip=${ip}`).then(Response => Response.json()).then(data => {
        if (data.isValid){
            ipInfos = data;
            insertIpInformation();
            createNewMap(ipInfos);
            showIpinfosScreen();
        } else {
            alert('invalid IP');
        }
    }).catch(e => {
        console.log(`api communication error: ${e}`);
        alert('ocorreu um erro, verifique o ip e tente novamente');
    });
}
async function getClientIp(){
    fetch('https://api.ipify.org?format=json').then(response => response.json())
    .then(data => input.value = data.ip)
    .catch(e => {
        console.log(`api communication error: ${e}`);
        alert('não foi possivel obter seu IP');
    });
}
function insertIpInformation(){
    const ipTable = document.querySelectorAll('.value');
    ipTable[0].innerHTML = ipInfos.ip;
    ipTable[1].innerHTML = ipInfos.city;
    ipTable[2].innerHTML = ipInfos.country;
    ipTable[3].innerHTML = ipInfos.latitude;
    ipTable[4].innerHTML = ipInfos.longitude;
    ipTable[5].innerHTML = `${Math.round(ipInfos.reliability)}%`;
}

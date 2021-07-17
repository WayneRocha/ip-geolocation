const seachButton = document.getElementById('go-button');
const returnButton = document.getElementById('return');
const myIpButton = document.getElementById('find-my-ip__button');
const input = document.getElementById('find-ip__input');
const ipScreen = document.getElementById('enter-ip__screen');
const ipInformationsScreen = document.getElementById('ip-informations__screen');

seachButton.addEventListener('click' , () => {
    if (input.value){
        getIpInformations(input.value);
    }
});
returnButton.addEventListener('click' , () => {
    showHomeScreen();
});
myIpButton.addEventListener('click', () => {
    console.log('set client IP on input');
});
myIpButton.addEventListener('click', () => {
    getClientIp();
});
function showIpinfosScreen(){
    ipScreen.style.display = 'none';
    ipInformationsScreen.style.display = 'flex';
}
function showHomeScreen(){
    ipScreen.style.display = 'flex';
    ipInformationsScreen.style.display = 'none';
}
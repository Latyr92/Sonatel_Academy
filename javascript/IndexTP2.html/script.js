const leftContainer = document.querySelector('.left-column .items-container');
const rightContainer = document.querySelector('.right-column .items-container');
const moveRightButton = document.querySelector('.move-right');
const moveLeftButton = document.querySelector('.move-left');
const notificationContainer = document.getElementById('notification-container');

// Tableau de données
const data = ['Mon Premier', 'Mon Deuxieme', 'Mon Troisieme', 'Mon Quatrieme'];

// Génération dynamique des éléments
data.forEach(item => {
  const element = document.createElement('p');
  element.textContent = item;
  element.classList.add('item');
  leftContainer.appendChild(element);
});

// Sélection d'un élément
leftContainer.addEventListener('mouseover', event => {
  const item = event.target;
  if (item.classList.contains('item')) {
    item.style.background='blue';
    const items = leftContainer.querySelectorAll('.item');
    items.forEach(element => element.classList.remove('selected'));
    item.classList.add('selected');
    moveRightButton.disabled = false;

  }
});

// Déplacement d'un élément vers la droite
moveRightButton.addEventListener('mouseover', () => {
  const selectedItem = leftContainer.querySelector('.selected');
  if (selectedItem) {
    const newItem = selectedItem.cloneNode(true);
    rightContainer.appendChild(newItem);
    selectedItem.remove();
    moveRightButton.disabled = false;
    moveLeftButton.disabled = false;
    showNotification('success', `${newItem.textContent} a été déplacé vers la droite`);
  }
});

// Déplacement d'un élément vers la gauche
moveLeftButton.addEventListener('click', () => {
  const selectedItem = rightContainer.querySelector('.selected');
  if (selectedItem) {
    const newItem = selectedItem.cloneNode(true);
    leftContainer.appendChild(newItem);
    selectedItem.remove();
    moveRightButton.disabled = false;
    moveLeftButton.disabled = false;
    showNotification('success', `${newItem.textContent} a été déplacé vers la droite`);
  }
});
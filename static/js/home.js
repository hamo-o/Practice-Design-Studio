const homeBtn = document.querySelector('.home-button');
const modalBtn = document.querySelector('.modal-btn');
const modal = document.querySelector('.modal-wrapper');
const form = document.getElementById('home-form');

const show = () => {
  modal.style.display = 'flex';
};

homeBtn.addEventListener('click', show);

modalBtn.addEventListener('click', () => {
  form.submit();
});

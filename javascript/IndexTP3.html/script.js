const rectangles = document.querySelectorAll('.rectangle');
      const petitRectangleVert = document.querySelector('#petit-rectangle-vert');
      let timeoutID
      rectangles.forEach(rectangle => {
        rectangle.addEventListener('click', () => {
          clearTimeout(timeoutID);
    petitRectangleVert.style.backgroundColor = rectangle.dataset.color;
    timeoutID = setTimeout(() => {
      petitRectangleVert.style.backgroundColor = '';
    }, 1000);
  });

        });
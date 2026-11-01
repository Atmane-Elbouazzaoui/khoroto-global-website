// Native scrolling does the work; buttons run only when the visitor clicks.
const track = document.getElementById('featured-games');
const controls = document.querySelector('[data-carousel-controls]');

if (track && controls) {
  const slides = [...track.children];
  controls.addEventListener('click', event => {
    const button = event.target.closest?.('button[data-carousel-slide]');
    if (!button || !controls.contains(button)) return;
    const slide = slides[Number(button.dataset.carouselSlide)];
    if (slide) {
      track.scrollTo({ left: slide.offsetLeft - slides[0].offsetLeft, behavior: 'auto' });
    }
  });
  controls.hidden = false;
}

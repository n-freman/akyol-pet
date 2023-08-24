let header = document.getElementById('banner');
let banners = header.getAttribute('data-banners').split(',')
let counter = 0;

if (banners.length > 1) {
    setInterval(() => {
        header.style.backgroundImage = `url(${banners[counter++]})`;
        if (counter == banners.length) {
            counter = 0;
        }
    }, 2000);
}
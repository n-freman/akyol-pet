const open = document.querySelector('.nav-toggle');
const close = document.querySelector('.close');
var tl = gsap.timeline({ defaults: { duration: 0.3, ease: 'expo.inOut' } });
open.addEventListener('click', () => {
	if (tl.reversed()) {
		tl.play();
	} else {
		tl.to('nav', { top: 0, background: 'rgba(0, 0, 0, 0.95)', height: '20vh' })
			.to('.language-bar', { display: 'block'})
			.to('nav', { height: '100vh' }, '-=.1')
			.to('.language-bar', { opacity: 0.5})
			.to('.bars', { opacity: 0})
			.to('.language-bar', { opacity: 1})
			.to('nav ul li a', { opacity: 1, pointerEvents: 'all', stagger: .2 }, '-=.8')
			.to('.close', { opacity: 1, pointerEvents: 'all' }, "-=.8")
			.to('nav .nav__logo', { opacity: 1 }, '-=1');
	}
});

close.addEventListener('click', () => {
	tl.reverse();
});

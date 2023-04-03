 const sr = ScrollReveal ({
     distance: '70px',
     duration: 1500,
     reset: true,
 });
 
sr.reveal('h1',{delay:350, origin:'left'})
sr.reveal('.home, .about, .blog,.Testimonials,.contact,.copyright',{delay:50, orgin:'bottom'})


var swiper = new swiper(".mySwiper", {
    slidesPerView: 3,
    spaceBetween: 30,
    slidesPerGroup: 3,
    loop: true,
    loopFillGroupWithBlank: true,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    navigation: {
        nextE1: ".swiper-button-next",
        prevE1: ".swiper-button-prev",
    },
})
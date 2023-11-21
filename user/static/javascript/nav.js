window.onscroll = function() {
    var navBar = document.querySelector('.nav-links');
    if (window.scrollY > 0) {
        navBar.classList.add('scrolled');
    } else {
        navBar.classList.remove('scrolled');
    }
};


    var swiper = new Swiper(".mySwiper", {
      slidesPerView: 4,
      spaceBetween: 20,
      slidesPerGroup: 1,
      loop: true,
      loopFillGroupWithBlank: true,
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
      },
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
   
    });
  
    window.onload = function(){
       document.getElementById('manueClick').click();// manue link button click on page load
        var button = document.getElementById('desk_next');
        setInterval(function(){
            button.click();
        },3000);  // this will make it click again every 1000 miliseconds

    };
    function show(){
      document.getElementById("agentNo").className="";
    }
//new code for mobile 
var swiper = new Swiper(".mySwiper2", {
  slidesPerView: 1,
  spaceBetween: 20,
  slidesPerGroup: 1,
  loop: true,
  loopFillGroupWithBlank: true,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});
//ended new code

//try to make it auto slide
window.onload = function(){
  document.getElementById('manueClick').click();// manue link button click on page load
    var button = document.getElementById('mobile_next');
    setInterval(function(){
        button.click();
    },3000);  // this will make it click again every 1000 miliseconds
};

//try code end

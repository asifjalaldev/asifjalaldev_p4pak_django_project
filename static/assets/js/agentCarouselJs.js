
    var swiper = new Swiper(".mySwiper", {
        slidesPerView: 4,
        spaceBetween: 22,
        slidesPerGroup: 4,
        loop: true,
        loopFillGroupWithBlank: false,
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
       
          var button = document.getElementById('desk_next');
          var button2 = document.getElementsByClassName('arrow-container')[0].click();

          setInterval(function(){
              button.click();

             document.getElementById('rightArrow').addEventListener('click', function (event) {
              
             }, false);
             document.getElementById('arrow-container').addEventListener('click', function (event) {

             }, true);
          },7000);  // this will make it click again every 1000 miliseconds
  
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
    // document.getElementById('manueClick').click();// manue link button click on page load
      var button = document.getElementById('mobile_next');
      var button2=document.getElementById('btn').onclick = function () {
      btn.click();
      };
    var btn= document.getElementsByClassName("carousel-next-item next arrow-container");
      setInterval(function(){
          button.click();
          button2.click();
         btn.click();
      },5000);  // this will make it click again every 1000 miliseconds
  };
  
  //try code end
  
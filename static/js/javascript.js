$(".buttons").mouseover(function(){
    $(this).addClass("animated jello");
  });
  
  $(".buttons").mouseout(function(){
    $(this).removeClass("animated jello");
  });
  
  $(".close").click(function() {
    close.play();
  })
  
  var loaded = anime({
    targets: '.name',
    scale: [{
      value: 3,
      duration: 100,
      elasticity: 100
    }, {
      value: 1,
      duration: 500,
      elasticity: 100
    }],
    duration: 4000,
    autoplay: false,
  
  });
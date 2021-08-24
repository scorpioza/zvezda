(function () {
  'use strict';

    $('a[href="#"]').click(function (event) {
      event.preventDefault();
    })
    $(".to_anchor").click(function(e){
      e.preventDefault();
      $('html,body').animate({scrollTop: $('body').offset().top},'slow');
    });
    $("#zvezdaShowToast").click(function(){
      if($("#zvezdaToast").hasClass("show")){
        $("#zvezdaToast").toast('hide');
      }else{
        $("#zvezdaToast").toast('show');
      }
    });
    $('body').on('click','.close',function(){
      $(this).closest('.toast').toast('hide')
    })

})();

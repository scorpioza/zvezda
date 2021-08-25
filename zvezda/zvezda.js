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
    $("#zvezda-btn-groups .btn-cat-group, .zvezda-cat-select").click(function(){
      var lbl = $(this).attr("role");
      $(".zvezda-cat").hide();      
      $(".zvezda-cat-"+lbl).show();
      $("#zvezdaFilter").attr("class", "card mb-3 border-"+lbl).show();
      $("#zvezdaFilterLabel").attr("class", "badge rounded-pill bg-"+lbl).text($(this).text());
      $('html,body').animate({scrollTop: $('#zvezdaFilter').offset().top},'fast');
    });      

    $("#zvezdaFilterClean").click(function(){
      $("#zvezdaFilter").hide();
      $(".zvezda-cat").show();
    });
})();



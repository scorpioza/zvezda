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

    $(".zvezda-share").click(function(){
      var zvShare = $(this).closest(".zvezda-cat").find(".zv-share")[0];
      var link = $(this).closest(".zvezda-cat").
                    find('.zvezda-img-link').attr("href").
                    replace("./", "https://scorpioza.github.io/zvezda/");
      var title = "ПАК Звезда: "+
        $(this).closest(".zvezda-cat").find('.card-text').text();

      var cat = $(this).closest(".zvezda-cat").find('.zvezda-cat-select').text();
      var img = $(this).closest(".zvezda-cat").find('.card-img-top')
      .attr("src").replace("./", "https://scorpioza.github.io/zvezda/");

      var share = Ya.share2(zvShare, {
          content: {
            title: title,
            description: cat,
            url: link,
            image: img       
          },
            theme: {
              services: 'vkontakte,facebook,odnoklassniki,telegram,whatsapp,twitter,pinterest,pocket'
          }/*,
          hooks: {
            onready: function () {
                alert('блок инициализирован');
            },
    
            onshare: function (name) {
                alert('нажата кнопка' + name);
            }
        }*/
      });
    });
})();



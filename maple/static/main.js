$(function(){
  $("#hwSettingImg").click(function(){
      $('#offcanvasRight').offcanvas('show');
  });
});

$(function(){
  $("#hwDeleteImg").click(function(){
      var nickname = $('#homework_header_nickname').text();
      var check = CharacterData.deleteCharacter(nickname);
      if (check){
        $('#mainBtn').find('button').each(function(i, e){
          var tabName = $(this).text();
          if (tabName==nickname){
            $(this).remove();
          }
        });
       }
  });
});


$( document ).ready(function(){
  var id_list = JSON.parse(JSON.parse($("#idDataTmpSave").attr('data-geocode')));
  
  console.log(id_list.length);
  for (var i = 0; i < id_list.length; i++) {
    var cnt = $('#mainBtn').children().length;
    console.log(id_list[i]);
    CharacterData.createNewCharacter(id_list[i]);
    var new_tab = $('<button class="tablink" onclick="openCity(this)" id="' + cnt+'">'+ id_list[i].nickname +'</button>');
    var new_tab = $("#1").clone();
    var new_tabcont = $("#content_2").clone();

    new_tab.attr('id', cnt);
    new_tab.text(id_list[i].nickname);
    new_tabcont.attr('id', "content_"+cnt);
    new_tabcont.text(id_list[i].nickname);
    new_tab.attr("style","display:block");
    new_tabcont.attr("style","display:none");
    $('#container').append(new_tabcont);
    
    new_tab.insertBefore($("#nicknamePlusTab"));
  }
});

$( document ).ready(function(){
  var allOffcanvas = document.querySelectorAll('.offcanvas');
  for (var i = 0; i < allOffcanvas.length; i++) {
      allOffcanvas[i].addEventListener('show.bs.offcanvas', function () {
        $('.offcanvas-body').find('input').each(function(index, item){
          $(this).prop('checked', true);
        });

        charactor_info = CharacterData.getNowCharacterInfo();
        for (let key in charactor_info.visible_boss){
          const val = charactor_info.visible_boss[key];
          const id = 'offcanvas_boss_' + key;
          if (val){
              $("#"+id).prop('checked',true);
          }
          else{
              $("#"+id).prop('checked',false);
          }
        }
        for (let key in charactor_info.visible_basic){
          const val = charactor_info.visible_basic[key];
          const id = 'offcanvas_basic_' + key;
          if (val){
              $("#"+id).prop('checked',true);
          }
          else{
              $("#"+id).prop('checked',false);
          }
        }
        for (let key in charactor_info.visible_symbol){
          const val = charactor_info.visible_symbol[key];
          const id = 'offcanvas_symbol_' + key;
          if (val){
              $("#"+id).prop('checked',true);
          }
          else{
              $("#"+id).prop('checked',false);
          }
        }
        for (let key in charactor_info.visible_event){
          const val = charactor_info.visible_event[key];
          const id = 'offcanvas_event_' + key;
          if (val){
              $("#"+id).prop('checked',true);
          }
          else{
              $("#"+id).prop('checked',false);
          }
        }
      });
      allOffcanvas[i].addEventListener('hide.bs.offcanvas', function () {
          boss = {};
          symbol = {};
          basic = {};
          _event = {};
          $('#offcanvas_boss_group').find('input').each(function(i, e){
              var opt = $(this).is(':checked');
              boss_name = e.id.split('_')[2];
              boss[boss_name] = opt;
          });
          $('#offcanvas_symbol_group').find('input').each(function(i, e){
              var opt = $(this).is(':checked');
              symbol_name = e.id.split('_')[2];
              symbol[symbol_name] = opt;
          });
          $('#offcanvas_basic_group').find('input').each(function(i, e){
              var opt = $(this).is(':checked');
              basic_name = e.id.split('_')[2];
              basic[basic_name] = opt;
          });
          $('#offcanvas_event_group').find('input').each(function(i, e){
              var opt = $(this).is(':checked');
              event_name = e.id.split('_')[2];
              _event[event_name] = opt;
          });
          CharacterData.visibleDataUpdate(boss, symbol, basic, _event);
          charactor_info = CharacterData.getNowCharacterInfo();
          initHomeworkVisible(charactor_info);
      });
  };
});
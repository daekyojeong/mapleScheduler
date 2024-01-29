function hw_page_load(){
    
}

$(function(){
    $(".bossCheckBoxLabel").click(function(e){
        isReal = e.originalEvent.isTrusted;
        e = $(this).children('input')[0];
        var checkBoxID = e.id;
        var checked = e.checked;
        var disableVal = e.disabled;
        console.log('disableVal', disableVal);
        if (!disableVal){
            
            if (isReal){
                CharacterData.checkedDataUpdate('boss', checkBoxID, checked);
            }
            var splitStr = e.id.split('_');
            var siblingsMember = $('#'+checkBoxID).parents(".bossDifficultyCol").siblings('.bossDifficultyCol')//.children('.bossCheckboxClass');
            var period = splitStr[1];
            for (var i=0; i< siblingsMember.length; i++){
                var sibling_id = $(siblingsMember[i]).find('.bossCheckboxClass')[0].id;
                if (sibling_id.split('_')[1] == period){
                    console.log(sibling_id, checked);
                    $('#'+sibling_id).attr('disabled', checked);
                }
            }
        }
    });
    $(".symbolCheckBoxLabel").click(function(e){
        isReal = e.originalEvent.isTrusted;
        e = $(this).children('input')[0];
        var checkBoxID = e.id;
        var checked = e.checked;
        if (isReal){
            CharacterData.checkedDataUpdate('symbol', checkBoxID, checked);
        }
    });

    
    $(".basicCheckBoxLabel").click(function(e){
        isReal = e.originalEvent.isTrusted;
        e = $(this).children('input')[0];
        var checkBoxID = e.id;
        var checked = e.checked;
        if (isReal){
            CharacterData.checkedDataUpdate('basic', checkBoxID, checked);
        }
    });

    
    $(".eventCheckBoxLabel").click(function(e){
        isReal = e.originalEvent.isTrusted;
        e = $(this).children('input')[0];
        var checkBoxID = e.id;
        var checked = e.checked;
        if (isReal){
            CharacterData.checkedDataUpdate('event', checkBoxID, checked);
        }
    });
});


function callNewCharacter(nickname){
    const newCharacterURL = 'http://' + window.location.host + '/new_char';
    suc = false;
    if (!CharacterData.checkCharacterName(nickname)){
        $.ajax({
            type:'POST',
            url:newCharacterURL,
            data:JSON.stringify({'nickname':nickname}),
            dataType:'json',
            contentType: 'application/json',
            async:false,
            success: function(response){
            var verification = response['suc'];
            var data = response['data'];
            if (verification){
                data = JSON.parse(data);
                CharacterData.createNewCharacter(data);
                suc= true;
            }
            else{
                alert('없는 ID 입니다.');
                suc=false;
            }
            }
        });
    }
    else{
        alert('이미 존재하는 ID 입니다.');
    }
    return suc
}

function charactorPlusClick(e){
    var cnt = $('#mainBtn').children().length;
    var userName = prompt("ID를 입력하세요", "");
    if (userName == null){
        return;
    }
    var verification = callNewCharacter(userName);
    if (verification){
        var new_tab = $('<button class="tablink" onclick="openCity(this)" id="' + cnt+'">'+ userName +'</button>');
        var new_tab = $("#1").clone();
        var new_tabcont = $("#content_2").clone();

        new_tab.attr('id', cnt);
        new_tab.text(userName);
        new_tabcont.attr('id', "content_"+cnt);
        new_tabcont.text(userName);
        new_tab.attr("style","display:block");
        new_tabcont.attr("style","display:none");
        $('#container').append(new_tabcont);
        
        new_tab.insertBefore($("#nicknamePlusTab"));
    }

}

function clickHomeworkNickname(e){
    // header change
    charactor_info = CharacterData.getCharacterInfo(e.innerText);
    console.log(charactor_info);
    CharacterData.setNowSelectedCharartersName(charactor_info.nickname);
    initHomeworkContents(charactor_info);
    initHomeworkVisible(charactor_info);
    $('#header_img').attr("src", charactor_info.imgUrl);
    $('#homework_header_level').text('Lv. '+ charactor_info.lvl);
    $('#homework_header_job').text(charactor_info.job);
    $('#homework_header_nickname').html('<b>' + charactor_info.nickname + '</b>');
    
    $('#hwDeleteImg').attr("style","display:inline-flex");
    $('#hwSettingImg').attr("style","display:inline-flex");
    $('#hwRefreshImg').attr("style","display:inline-flex");

    // tab color change
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].style.backgroundColor = "";
    }

    e.style.backgroundColor = '#111';
    // contents change
}


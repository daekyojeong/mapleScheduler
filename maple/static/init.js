function initHomeworkContents(charactor_info){
    $('#homeWorkMainDIV').find('input').each(function(index, item){
        if ($(this).is(':checked')){
            $(this).trigger("click", {"foo":"1234", "bar":"이순신"});
        }
    });
    for (let key in charactor_info.boss){
        const val = charactor_info.boss[key];
        if (val){
            console.log(key, val);
            $("#"+key).trigger("click");
        }
    }
    for (let key in charactor_info.symbol){
        const val = charactor_info.symbol[key];
        if (val){
            $("#"+key).trigger("click");
        }
    }
    for (let key in charactor_info.basic){
        const val = charactor_info.basic[key];
        if (val){
            $("#"+key).trigger("click");
        }
    }
    for (let key in charactor_info.event){
        const val = charactor_info.event[key];
        if (val){
            $("#"+key).trigger("click");
        }
    }
}

function initHomeworkVisible(charactor_info){
    for (let key in charactor_info.visible_boss){
        const val = charactor_info.visible_boss[key];
        const id = 'boss' + key + 'Wrapper';
        if (val){
            $('#'+id).attr("style","display:block");
        }
        else{
            $('#'+id).attr("style","display:none");
        }
    }
    for (let key in charactor_info.visible_symbol){
        const val = charactor_info.visible_symbol[key];
        const id = key + '_Wrapper';
        if (val){
            $('#'+id).attr("style","display:block");
        }
        else{
            $('#'+id).attr("style","display:none");
        }
    }
    for (let key in charactor_info.visible_basic){
        const val = charactor_info.visible_basic[key];
        const id = 'basic' + key + 'Wrapper';
        if (val){
            $('#'+id).attr("style","display:block");
        }
        else{
            $('#'+id).attr("style","display:none");
        }
    }
    for (let key in charactor_info.visible_event){
        const val = charactor_info.visible_event[key];
        const id = 'event' + key + 'Wrapper';
        if (val){
            $('#'+id).attr("style","display:block");
        }
        else{
            $('#'+id).attr("style","display:none");
        }
    }
}
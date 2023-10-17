const CharacterData = (function() {
    // 현재 counter 값을 저장하기 위한 변수
    let characters = [];
    let nowSelectedCharartersName = '';
    return {
        setNowSelectedCharartersName: function(nickname){
            nowSelectedCharartersName = nickname;
        },

        createNewCharacter: function (data){
            characters.push(data);
            console.log(characters);
        },
        getCharacterInfo: function (nickname){
            var findCharacter;
            characters.forEach(function(character){
                if (character.nickname == nickname){
                    findCharacter = character;
                }
            });
            return findCharacter
        },
        getNowCharacterInfo: function (){
            var findCharacter;
            characters.forEach(function(character){
                if (character.nickname == nowSelectedCharartersName){
                    findCharacter = character;
                }
            });
            return findCharacter
        },
        checkCharacterName: function (newNickname){
            var isExist = false;
            characters.forEach(function(character){
                if (character.nickname == newNickname){
                    isExist = true;
                }
            });
            return isExist
        },
        deleteCharacter: function (nickname){
            const findIdx = characters.findIndex(function(data){ return data.nickname === nickname});
            if (findIdx != -1){
                characters.splice(findIdx, 1);
                return true
            }
            return false
        },
        visibleDataUpdate: function(boss, symbol, basic, _event){
            var nowCharacter;
            characters.forEach(function(character, index){
                if (character.nickname == nowSelectedCharartersName){
                    characters[index].visible_boss = boss;
                    characters[index].visible_symbol = symbol;
                    characters[index].visible_basic = basic;
                    characters[index].visible_event = _event;
                    nowCharacter = characters[index];
                }
            });

            const newCharacterURL = 'http://' + window.location.host + '/hw_visible_update';
            $.ajax({
                type:'POST',
                url:newCharacterURL,
                data:JSON.stringify({'char':nowCharacter}),
                dataType:'json',
                contentType: 'application/json',
                async:true,
                success: function(response){
                    console.log('visible_update_success');
                }
            });
            
        },
        checkedDataUpdate: function(group, key, value){
            var userID = -1;
            characters.forEach(function(character, index){
                if (character.nickname == nowSelectedCharartersName){
                    if (group in characters[index] == false){
                        characters[index][group] = {};
                    }
                    characters[index][group][key] = value;
                    userID = characters[index].userid;
                }
            });
            console.log(nowSelectedCharartersName, key, value);
            console.log(characters);
            const newCharacterURL = 'http://' + window.location.host + '/hw_checkbox_update';
            $.ajax({
                type:'POST',
                url:newCharacterURL,
                data:JSON.stringify({'id': userID, 'nickname': nowSelectedCharartersName, 'key':key, 'value':value}),
                dataType:'json',
                contentType: 'application/json',
                async:true,
                success: function(response){
                    console.log('visible_update_success');
                }
            });
        }
    };
})();

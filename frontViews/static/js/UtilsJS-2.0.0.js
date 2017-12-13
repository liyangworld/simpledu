
function _joinParams(obj,isSkipEmpty) {
    var str = [];
    for (var key in obj) {
        if (isSkipEmpty) {
            if (obj[key] === null || obj[key] === '') continue;
        }
        str.push(key + "=" + obj[key]);
    }
    return str.join("&");
};
//---------------------------1. 对Ajax请求的封装--------------------
var sendToServer = {

    get: function(url, params,successFn,errorFn) {
        var serverURL = url;
        var paramsStr = _joinParams(params,true);

        if (paramsStr) { 
            if (serverURL.indexOf('?') > 0) {
                serverURL += '&' + paramsStr;
            }else{
                serverURL += '?' + paramsStr;
            }
        }
        $.ajax({
            url: serverURL,
            method: 'GET',
            dataType: 'json',
            data: null,
            cache: false,
            crossDomain: true,
            complete: function (jqXHR, textStatus) {
            },
            success: function (responseData, textStatus, jqXHR) {
                successFn && successFn(responseData);
            },
            error: function (jqXHR, textStatus, errorThrown) {
                errorFn && errorFn();
            }
        });
    },
    post: function (url, data, successFn, errorFn) {
        //contentType: "application/json;charset=utf-8",
        //contentType: "text/xml",
        //contentType:"application/x-www-form-urlencoded",//默认值
        $.ajax({
            url: url,
            method: 'POST',
            dataType: 'json',
            contentType: "application/json;charset=utf-8",
            data: JSON.stringify(data),
            cache: false,
            crossDomain: true,
            complete: function (jqXHR, textStatus) {

            },
            success: function (responseData, textStatus, jqXHR) {
                successFn && successFn(responseData);
            },
            error: function (jqXHR, textStatus, errorThrown) {
                errorFn && errorFn();
            }
        });
    },
    getJsonp: function (url, params, successFn, errorFn) {
        var serverURL = url;
        var paramsStr = _joinParams(params, true);


        if (paramsStr) {
            paramsStr = paramsStr + "&callback=?";

        } else {
            paramsStr = "callback=?";
        }

        if (serverURL.indexOf('?') > 0) {
            serverURL += '&' + paramsStr;
        } else {
            serverURL += '?' + paramsStr;
        }

        //jsonpCallback 选项用于指定调用的函数，暂不使用
        $.ajax({
            url: serverURL,
            method: 'GET',
            dataType: 'jsonp',
            jsonp: 'callback',
            data: null,
            cache: false,
            crossDomain: true,
            complete: function (jqXHR, textStatus) {
            },
            success: function (responseData, textStatus, jqXHR) {
                successFn && successFn(responseData);
            },
            error: function (jqXHR, textStatus, errorThrown) {
                errorFn && errorFn();
            }
        });
    }
};



//---------------------------_Object 方法-------------开始------
var _Object = {
    assign : function(){
        var resultObj = arguments.length ? arguments[0] : {};
        for (var i = 1; i < arguments.length; i++) {
            var curObj =  arguments[i];
            for(var key in curObj){
                resultObj[key] = curObj[key] ;
            }
        }
        return resultObj;
    }
};


//---------------------------apis-------------开始------


var _APIs = {
    Base: 'http://localhost:5001/api/v1.0',

    courseList: '/courses/',
    userList: '/users/',
    liveList: '/lives/'
};

var _getApiUrl = function(route){
    return _APIs.Base + _APIs[route];
};
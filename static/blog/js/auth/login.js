//
// function success(data) {
//
//     if (data['status'] == 0){
//         window.location.href = host + '/index';
//     }
//
//     else {
//         window.location.href = host
//     }
// }
//
// function fail(response) {
//
// }
//
// function get_params() {
//
//     var data = {
//         'username': '',
//         'password': '',
//         'is_remember': false
//     };
//
//     var username_value = $('#inputEmail').val();
//     var password_value = $('#inputPassword').val();
//
//     if($('#ck_remember').attr('checked')){
//         data['is_remember'] = true
//     }
//
//     data['username'] = username_value;
//     data['password'] = password_value;
//
// }
//
// function send_login_request(){
//     var url = host + '/api/v1/login';
//     console.log(url);
//     var data = get_params();
//     http(url, data, 'POST', success, fail)
// }

//提交ajax表单
function ajaxForm(){
        //提交表单，可以通过serialize（）方法获取form表单数据
        // var datas = {};
        // var username = $('#username').val();
        // var password = $('#inputPassword').val();
        // var is_remember = false;
        // datas['username'] = username;
        // datas['password'] = password;
        // datas['is_remember'] = is_remember;

        var form = $('#login_form').serialize();
        $.ajax({
            url:host + "/auth/api/v1/login",
            type:"post",
            data:form,
            dataType: 'json',
            processData:false,
            contentType:false,
            success:function(data){
                console.log(data);
                console.log(data['status']);

                if (data['status'] == 0){
                    console.log(data['status']);
                    window.location.href = host + '/index';

                } else if (data['status'] == 400){
                    console.log(data['status']);
                    window.location.href = host + '/index';
                    alert('用户名或密码错误，请联系管理员！');

                } else {
                    console.log(data['status']);
                    window.location.href = host + '/index';
                    alert('系统错误请联系管理员！');
                }

            },
            error:function(e){
                console.log(form);
                    alert("error");
            }
        })
}

//提交POST表单数据，以json格式提交
function ajaxPost(){

        var datas = {};
        var username = $('#username').val();
        var password = $('#inputPassword').val();
        var is_remember = false;
        datas['username'] = username;// 用户名
        datas['password'] = password;// 密码
        datas['is_remember'] = is_remember;// 是否记住密码

        // 检查是否记住密码
        if($('#ck_remember').is(':checked')){
            datas['is_remember'] = true
        }

        $.ajax({
            url:host + "/auth/api/v1/login",
            type:"post",
            data:JSON.stringify(datas),// 转化为json格式数据
            dataType: 'json',
            processData:false,
            contentType:"application/json; charset=utf-8",
            // 成功回调
            success:function(data){
                console.log(data);
                console.log(data['status']);

                // 请求成功，跳转至首页
                if (data['status'] == 0){
                    window.location.href = host + '/index';

                // 用户名或密码错误，停留当前页面
                } else if (data['status'] == 400){
                    alert('用户名或密码错误，请联系管理员！');

                } else {
                    alert('系统错误请联系管理员！');
                }

            },
            // 失败回调
            error:function(e){
                console.log(form);
                    alert("error");
            }
        })
}


$(function () {

    $('#lg_submit').click(ajaxPost);

});
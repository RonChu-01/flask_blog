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
            url:host + "/auth/api/v1/register",
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
                    window.location.href = host;

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

    $('#rg_submit').click(ajaxPost);

});
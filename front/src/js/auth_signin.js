function Auth() {

}

Auth.prototype.ListenSigninBtnEvent = function(){
    var signinBtn =$('#signin-btn');
    var usernameInput = $("input[name='username']");
    var passwordInput = $("input[name='password']");
    var imgcapthaInput = $("input[name='captcha']");

    signinBtn.click(function (event) {
        event.preventDefault();
        var username = usernameInput.val();
        var password = passwordInput.val();
        var imgcaptcha = imgcapthaInput.val();
        if(!username || !password){
            window.messageBox.showError('输入完整信息');
            console.log('输入完整信息');
            return;
        }
        if(!imgcaptcha){
            window.messageBox.showError('请输入验证码！');
            return;
        }
        xfzajax.post({
            'url':'/signin/',
            'data':{
                'username':username,
                'password':password,
                'imgcaptcha':imgcaptcha
            },
            'success':function (result) {
                if (result['code'] == 200){
                    window.location = '/';
                }else {
                    // 根据需求，forms中已经将get_errors的返回值处理为字典格式
                    var messageObject = result['message'];
                    if (typeof messageObject == 'string' || messageObject.constructor == String) {
                        window.messageBox.showError(messageObject);
                    } else {
                        // {'username':['xxxxxxxxxxxxxxx','xxx'],'telephone':['xxxxxxx','xxxxxx']}
                        for (var key in messageObject) {
                            var messages = messageObject[key];
                            var message = messages[0];
                            window.messageBox.showError(message)
                        }
                    }
                }
            },
            'fail':function (error) {
                window.messageBox.showError(error)
            }

        })
    })
};

// 图片验证码切换
Auth.prototype.ListenimgcaptchaClick = function(){
    var imgCaptcha = $('.img-captcha');
    imgCaptcha.click(function () {
        imgCaptcha.attr('src','/img_captcha/'+'?random='+Math.random())
    })
};

Auth.prototype.run = function () {
    var self = this;
    self.ListenSigninBtnEvent();
    self.ListenimgcaptchaClick();
};

$(function () {
   var auth = new Auth();
   auth.run();
});
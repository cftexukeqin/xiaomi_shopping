function Auth() {

}


// 图片验证码切换
Auth.prototype.ListenimgcaptchaClick = function(){
    var imgCaptcha = $('.img-captcha-btn');
    imgCaptcha.click(function () {
        imgCaptcha.attr('src','/img_captcha/'+'?random='+Math.random())
    })
};
Auth.prototype.ListenSignupBtnEvent = function(){

    var signupBtn = $('#signup-btn');
    var usernameInput = $("input[name='username']");
    var passwordInput = $("input[name='password']");
    var repasswordInput = $("input[name='repassword']");
    var imgcaptchaInput = $("input[name='imgcaptcha']");
    var telephoneInput = $("input[name='telephone']");
    signupBtn.click(function (event) {
        event.preventDefault();
        var username = usernameInput.val();
        var password = passwordInput.val();
        var repassword = repasswordInput.val();
        var telephone = telephoneInput.val();
        var imgCaptcha = imgcaptchaInput.val();
        console.log(username,password,repassword,telephone,imgCaptcha);
        if(!username || !password || !repassword || !telephone){
            window.messageBox.showError('请输入完整信息')
        }
        if(!imgCaptcha){
            window.messageBox.showError('请输入验证码');
        }
        xfzajax.post({
            'url':'/signup/',
            'data':{
                'username':username,
                'password':password,
                'repassword':repassword,
                'imgcaptcha':imgCaptcha,
                'telephone':telephone
            },
            'success':function (result) {
                if(result['code'] == 200){
                    window.messageBox.showSuccess('注册成功！');
                    setTimeout(function () {
                        window.location ='/'
                    },1500);

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
Auth.prototype.run = function () {
    var self = this;
    self.ListenSignupBtnEvent();
    self.ListenimgcaptchaClick();
};

$(function () {
   var auth = new Auth();
   auth.run();
});
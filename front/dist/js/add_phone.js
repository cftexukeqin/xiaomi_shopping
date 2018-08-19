function Phone() {

}
Phone.prototype.listenAddPhone = function(){
    var commitBtn = $('#commitBtn');
    var nameInput = $('input[name="name"]');
    var thumbnailInput = $('input[name="thumbnail"]');
    var priceInput = $('input[name="price"]');
    var colorInput = $('input[name="color"]');
    var descInput = $('input[name="desc"]');
    var romInput = $('input[name="rom"]');
    var ramInput = $('input[name="ram"]');
    commitBtn.click(function (event) {
        event.preventDefault();
        var name = nameInput.val();
        var thumbnail = thumbnailInput.val();
        var price = priceInput.val();
        var color = colorInput.val();
        var desc = descInput.val();
        var rom = romInput.val();
        var ram = ramInput.val();
        if(!name){
            messageBox.showInfo('请输入手机名称！')
        }
        xfzajax.post({
            'url':'/cms/add_phone/',
            'data':{
                'name':name,
                'thumbnail':thumbnail,
                'price':price,
                'color':color,
                'desc':desc,
                'rom':rom,
                'ram':ram
            },
            'success':function (result) {
                if(result['code'] === 200){
                    messageBox.showSuccess('添加手机成功！')
                }else {
                    messageBox.showInfo(result['message'])
                }
            },
            'fail':function (err) {
                console.log(err)
            }
        })
    })
};
Phone.prototype.run = function () {
    this.listenAddPhone();
};
$(function () {
   var addphone = new Phone();
   addphone.run()
});
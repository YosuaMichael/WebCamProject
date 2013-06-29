$(function() {
    function update() { 
        var d = new Date();
        $('img#WebCam').attr("src",$SCRIPT_ROOT + "_get_pictures?"+d.getTime());         
    }
    setInterval(update, 150);
    });


/**
 * Created by Administrator on 2017/6/1.
 */
$(function(){
    var becomeLeaderURL = "http://localhost:9000/boat.html";
    var getTop3BoatURL = "http://localhost:9000/gettop3"
    console.log("hello world");

    function getTop3Boat()
    {
        console.log("getTop3Boat");
        $.ajax({
            url:getTop3BoatURL,
            method:"POST",
            data:{
                key:"hello",
                value:"world"
            },
            success:function(){
                console.log("ajax success");
            },
            error:function(){
                console.warn("ajax error");
            }
        })
    };

    function disableButton(){
        $(".btn").css("background","gray");
        $(".action-text").css("color","gray");
        $(".btn").unbind();
    };

    function enableButton(){
        $(".btn#jumpBoat").click(function(){
            console.log("call jumpBoat");
            disableButton();
        });
        $(".btn#becomeLeader").click(function(){
            console.log("call becomeleader");
            //location.href=becomeLeaderURL;
            getTop3Boat()
        });
    }
    enableButton();
});

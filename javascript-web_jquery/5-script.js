$(document).ready(function(){
    $("#add_item").click(function(){
        var newitem = $("<li>Item<li>");
        $(".my_list").append(newitem);
    });
});

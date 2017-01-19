$('#myTabs a').click(function (e) {
  e.preventDefault()
  $(this).tab('show')
})

$(document).ready(function(){
    // Activate Carousel
    $("#myCarousel").carousel();
    
    // Enable Carousel Indicators
    $(".item1").click(function(){
        $("#myCarousel").carousel(0);
    });
    $(".item2").click(function(){
        $("#myCarousel").carousel(1);
    });
    $(".item3").click(function(){
        $("#myCarousel").carousel(2);
    });
    $(".item4").click(function(){
        $("#myCarousel").carousel(3);
    });
    
    // Enable Carousel Controls
    $(".left").click(function(){
        $("#myCarousel").carousel("prev");
    });
    $(".right").click(function(){
        $("#myCarousel").carousel("next");
    });
});


var addReward = function(e){
    var li = document.createElement("li");
    //var name = prompt("Reward Name:");
    /var cost = prompt("Reward Value:");
    //var button = "<button id=\"obtain\">purchase</button>";
    //button.addEventListener("click", purchase(cost));
    //button.addEventListener("click", deleteItem);
    li.innerHTML = "Reward: " //+ name + ", Costs: " + cost + button
    li.addEventListener("mouseover", headerChange);
    li.addEventListener("mouseout", restoreHead);
    var ol = document.getElementById("rewards");
    ol.appendChild(li);
}

var deleteReward = function(e){
    var li.reward =this;
    this.remove();
}


var listItems = document.getElementsByTagName("li");

for (i = 0; i < listItems.length; i++){
    listItems[i].addEventListener("click", deleteItem);
}

var reward_button = document.getElementById("add_reward");
reward_button.addEventListener("click", addReward);

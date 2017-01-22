$('#myTabs a').click(function (e) {
  e.preventDefault();
  $(this).tab('show');
})


var addReward = function(e){
    var li = document.createElement("li");
    li.setAttribute("id", "reward")
    var name = document.getElementById("reward_name");
    name = name.value;
    var price = document.getElementById("reward_cost");
    price = price.value;
    li.innerHTML = "Reward: " + name + " Price: " + price + "<button id='purchase'>hello</button>";
    var ol = document.getElementById("rewards");
    ol.appendChild(li);
}


var reward_button = document.getElementById("add_reward");
reward_button.addEventListener("click", addReward);

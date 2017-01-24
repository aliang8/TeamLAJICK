$('#myTabs a').click(function (e) {
  e.preventDefault();
  $(this).tab('show');
})

var purchase = function(e){
    var price = this.parentNode.childNode["reward_cost"].innerHTML;
    var balance = document.getElementById("balance").innerHTML;
    price = parseInt(price);
    balance = parseInt(balance);
    alert(balance);
    if(balance >= price){
  	var transaction = balance - price;
	balance.innerHTML = transaction.toString();
	this.parentNode.remove();
    }
}

var addReward = function(e){
    var li = document.createElement("li");
    li.setAttribute("id", "reward")
    var name = document.getElementById("reward_name");
    name = name.value;
    var price = document.getElementById("reward_cost");
    price = price.value;
    li.innerHTML = "Reward: " + name + " Price: " + price + "<button class='purchase'>Purchase</button>";
    var ol = document.getElementById("rewards");
    ol.appendChild(li);
    var reward_list = document.getElementById("rewards");
    var rewards = reward_list.getElementsByClassName("purchase");
    for(i=0; i < rewards.length; i++){
	rewards[i].addEventListener("click", purchase);

    }
}

var reward_button = document.getElementById("add_reward");
reward_button.addEventListener("click", addReward);

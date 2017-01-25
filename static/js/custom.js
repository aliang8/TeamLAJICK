$('#myTabs a').click(function (e) {
  e.preventDefault();
  $(this).tab('show');
})

var purchase = function(e){
    var balance = document.getElementById("balance");
    var initial = parseInt(balance.innerHTML);
    var price = this.parentNode.childNodes;
    price = parseInt(price[1].innerHTML);
    if(price > balance){
	alert("This Reward Is Too Expensive");
    }
    else{
	var transaction = initial - price;
	balance.innerHTML = transaction.toString();
	this.parentNode.remove();
    }
}

var addReward = function(e){
    var name = document.getElementById("reward_name");
    name = name.value;
    var price = document.getElementById("reward_cost");
<<<<<<< HEAD
    price = price.value;
    li.innerHTML = "Reward: " + name + " Price: " + price + "<button class='purchase'>Purchase</button>";
    var ol = document.getElementById("rewards");
    ol.appendChild(li);
    var reward_list = document.getElementById("rewards");
    var rewards = reward_list.getElementsByClassName("purchase");
    for(var i=0; i < rewards.length; i++){
    	rewards[i].addEventListener("click", purchase);
=======
    price = parseInt(price.value);
    if(name.length == 0){
	alert("Reward Must Have Name");
    }
    if(isNaN(price)){
	alert("Price Must Be A Number");
    }
    if(name.length > 0 && !isNaN(price)){
	var li = document.createElement("li");
	li.setAttribute("id", "reward")
	li.innerHTML = "<p id='reward'>Reward: " + name + "</p><p id='price'>" + price + "</p><button class='purchase'>Purchase</button>";
	var ol = document.getElementById("rewards");
	ol.appendChild(li);
	var reward_list = document.getElementById("rewards");
	var rewards = reward_list.getElementsByClassName("purchase");
	for(i=0; i < rewards.length; i++){
	    rewards[i].addEventListener("click", purchase);
>>>>>>> d254e3f0195940e3d315a13f5172803c21f471f4

	}
    }
}

var reward_button = document.getElementById("add_reward");
reward_button.addEventListener("click", addReward);


var addToDo = function(e){
  
  //var item = document.createElement("li");
  //var.class = "todoitem";
  
  
  
}

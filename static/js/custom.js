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
	for(var i=0; i < rewards.length; i++){
	    rewards[i].addEventListener("click", purchase);

	}
    }
}

var reward_button = document.getElementById("add_reward");
reward_button.addEventListener("click", addReward);


$.fn.serializeObject = function(e)
{
   var o = {};
   var a = this.serializeArray();
   $.each(a, function() {
       if (o[this.name]) {
           if (!o[this.name].push) {
               o[this.name] = [o[this.name]];
           }
           o[this.name].push(this.value || '');
       } else {
           o[this.name] = this.value || '';
       }
   });
   return o;
};

var newToDo = function(e) {
  var item = document.createElement("li");
  item.class = "todoitem";

  $.ajax({
      url: "/home",
      type: 'POST',
      data: $("todoform").serializeObject()
  }).done(function(result) {
            item.innerHTML = result;
            console.log(result);
          }).fail(function() {
                    console.log("Ooops");
              });
              

  var list = document.getElementById("todolist");
  list.insertBefore(item, list.childNodes[0]);
}

var newHabit = function(e) {
  var item = document.createElement("li");
  item.class = "habititem";

  $.ajax({
      url: "/home",
      type: 'POST',
      data: $("habitform").serializeObject()
  }).done(function(result) {
            item.innerHTML = result;
          }).fail(function() {
                    console.log("Oops");
                  });

  var list = document.getElementById("habitlist");
  list.insertBefore(item, list.childNodes[0]);
}

var newGoal = function(e) {
  var item = document.createElement("li");
  item.class = "goalitem";
  
  $.ajax({
      url: "/home",
      type: 'POST',
      data: $("goalform").serializeObject()
  }).done(function(result) {
            item.innerHTML = result;
          }).fail(function() {
                    console.log("oops");
              });

  var list = document.getElementById("goallist");
  list.insertBefore(item, list.childNodes[0]);
}

var todo = document.getElementById("newtodo");
todo.addEventListener("click", newToDo);

var habit = document.getElementById("newhabit");
habit.addEventListener("click", newHabit);

var goal = document.getElementById("newgoal");
goal.addEventListener("click", newGoal);
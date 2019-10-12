NUM_PLAYERS = 6
import sys
if len(sys.argv) >1:
    NUM_PLAYERS = int(sys.argv[1])

rounds = ["Each trick 5 points", "Each heart 5 points", "Each Queen 20 points", "King of Spades 80 points", "First and last trick 40 points","All of the above","7 up and 7 down<br/>(-100 first out, +100 last out)"]

header = """
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="width=device-width, height=device-height, user-scalable=no, initial-scale=1.0">
    <style>
        body {margin: 5% auto; background: #f2f2f2; color: #444444; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; font-size: 16px; line-height: 1.8; text-shadow: 0 1px 0 #ffffff; max-width: 85%;} 
        code {background: white;}
        a {border-bottom: 1px solid #444444; color: #444444; text-decoration: none;}
        a:hover {border-bottom: 0;}
		tr:nth-child(even) {background: #BADEBC}
		tr:nth-child(odd) {background: #FFF}
		button {margin-right:250px}
    </style>
</head>
	<title>Ronald Andres Salad Scoreboard</title>
	<body>
	<h1>The Ronald Andres Salad Scoreboard</h1>
	<table id="scores" border="0">"""
footer = """
	</table>
        <button onclick="window.location.href = 'index.html';">Return to main page</button>
	<button onclick="new_game()">New game, same players</button>
	<script>

		function update_score(valNum){
			num_players = scores.rows[0].cells.length
			for (p=1; p<num_players;p++){
				var sum_elements = document.getElementsByClassName("pl"+p);
				sumVal = 0;
				for (i=0; i<sum_elements.length;i++){
					sumVal = sumVal + Number(sum_elements[i].value);
				}
				document.getElementById("pl"+p+"-total").innerHTML=sumVal;
			}
		}

		function new_game(){
			num_players = scores.rows[0].cells.length
			for (p=1; p<num_players;p++){
				var sum_elements = document.getElementsByClassName("pl"+p);
				for (i=0; i<sum_elements.length;i++){
					sum_elements[i].value = sum_elements[i].defaultValue;
				}
				document.getElementById("pl"+p+"-total").innerHTML=0;
			}
		}
	</script>
	</body>
</html>"""

line1 = "<tr><th>Round</th>"+"".join(map(lambda x: '<th><input type="text" size="8" placeholder="Player'+str(x)+'"></th>', range(1,NUM_PLAYERS+1)))+"</tr>"
bulk = ""
for r in rounds:
    bulk = bulk+ "\n<tr><td>"+r+"</td>"+"".join(map(lambda x: '<td><input type="tel"class="pl'+str(x)+'" pattern="[0-9]*" style="width: 6em" placeholder="0" oninput="update_score(this.value)" onchange="update_score(this.value)"></td>', range(1,NUM_PLAYERS+1)))+"</td>"
last_line = '<tr><td>Total</td>'+"".join(map(lambda x: '<td><span id="pl'+str(x)+'-total"></span></td>',range(1,NUM_PLAYERS+1)))+"</td>"
print(header+line1+bulk+last_line+footer)

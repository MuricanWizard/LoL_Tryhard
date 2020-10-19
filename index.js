var { PythonShell } = require('python-shell');

let region = "";
let summonerName = "";
let filePath = "";
let x = "";
let y = "";
function switchToChampSelect(){
  region = document.getElementById('region').value;
  summonerName = document.getElementById('sName').value;
  filePath = document.getElementById('filePath').value;
  if(summonerName == ""){
    alert("Please enter a Summoner Name");
    return;
  }
  else if(region == ""){
    alert("Please select a Region");
    return;
  }
  else if(filePath == ""){
    alert("Please enter a valid File Path");
    return;
  }
  else{
    document.getElementById('homePage').style.display = "none";
    document.getElementById('champSelect').style.display = "block";
    sendToPython();
  }
}

function getLeagueData(){
  const url = 'https://127.0.0.1:2999/liveclientdata/playerlist';
  fetch(url).then(response => response.json()).then(data => console.log(data));
}

function sendToPython() {
  let options = {
    mode: 'text',
    args: [filePath]
  };

  PythonShell.run('./test.py', options, function (err, results) {
    if (err){
      document.getElementById('text').innerHTML += err.toString();
    }
    else{
      // results is an array consisting of messages collected during execution
      console.log('results: ', results.toString());
      x = results.toString();
      document.getElementById('text').innerHTML += x;
      return results.toString();
    }});

  }

  function initialize(){
    let options = {
      mode: 'text',
      args: [0]
    };
    document.getElementById('homePage').display = "none";
    PythonShell.run('./initialize.py', options, function (err, results) {
      if (err) throw err;
      // results is an array consisting of messages collected during execution
      console.log('results: ', results.toString());
      y = results.toString();
      document.getElementById('initialize').innerHTML += y;
      document.getElementById('homePage').display = "block";
      return results.toString();
    });
  }

  initialize();

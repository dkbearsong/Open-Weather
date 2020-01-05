// This script will take input from owweb.html and then send it to main.py to retrieve from the SQL database file the weather and forecast information to return back to the html file

// #3 Javascript pulling form information
forms = ['city', 'state', 'county', 'country', 'latitude', 'longitude'];
input = {};

for (i in forms) {
  if ($('#' + i) != null) {
    input[i] = $('#' + i);
  }
  else {
    input[i] = 'null'
  }
};

// determines which of the fields are filled out and feeds information to main.py
// #4 Javascript feeds information to main.py 
function getData(input) {
  this.today = function (input) {
    $.ajax({
      type: "POST",
      url: "/main.py",
      data: { param: this.input }
    });
    return jqXHR.responseText
  }
}
// may need some work on the this.input parts

dData = new getData(input);

$('#submit').click(function(){
  result = dData.today(input)})
}

// returns data to the fields on the html web page
function returnData() {
  var resultIds = ['Today', 'TempToday', 'HighToday', 'LowToday', 'HumidityToday', 'WindToday', 'WeatherToday']
  for (i in this.resultIDs) {
    $('#' + i).empty().append(data)
  }
}
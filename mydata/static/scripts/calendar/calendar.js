
$(document).ready(function() {
// var manth = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}
// var date = new Date();


  $.get("/api/user_daily_mobility_summary/",function(data,status){
    alert(data[0]['body']['walking_distance_in_km'])
    // meals = []

    for (i = 0; i < data.length; i++) {
    date = data[i]['body']['date'].split("-")
    // alert(date[2])
     var source = {
        title: "walking_distance_in_km:"+"\n" + data[i]['body']['walking_distance_in_km'].toString() +"\n" +
        "active_time_in_seconds:"+"\n" + data[i]['body']['active_time_in_seconds'].toString(),//"{0}{1}".format("walking_distance_in_km",data[i]['body']['walking_distance_in_km'].toString()),
        // start: new Date(date[0].toString(),data[1].toString(),data[2].toString()),
        // title:"TEST",
        start: new Date(date[0].toString(),date[1].toString()-1,date[2].toString()),
        allDay: true,
        // id: i,
     }
    //  alert(new Date(date[0].toString(),data[2].toString(),data[1].toString()))
    //  alert(date[0].toString())
     alert(source.start)
    //  alert(date[2].toString())

     $('#calendar').fullCalendar( 'addEventSource', [source] )
    }
    alert("Done")

  });

    //   var saveInLocalStorage = function(time){
    //     if(typeof(Storage) !== "undefined") {
    //           localStorage.setItem("type", "meal");
    //           timeArray = time.split(' ')
    //           localStorage.setItem("type", "meal");
    //           localStorage.setItem("day", timeArray[0]);
    //           localStorage.setItem("mm", manth[timeArray[1]]);
    //           localStorage.setItem("dd", timeArray[2]);
    //           localStorage.setItem("yyyy",timeArray[3]);
    //           localStorage.setItem("hh", timeArray[4]);
    //
    //           localStorage.setItem("actionType","Save")
    //     } else {
    //         alert("Sorry! No Web Storage support..")
    //     }
    // }

var calendar = $('#calendar').fullCalendar({
    header: {
        left: 'prev,next today',
        center: 'title',
        right: 'month,agendaWeek,agendaDay'
    },
    editable: true,
    weekMode: 'liquid',
    url:'#',
    // events: meals,
    dayClick: function(date, allDay, jsEvent, view) {
        //#######
        saveInLocalStorage(date.toString())
        //#######
				// window.location.replace("/foodJournal/mealplanning/");
			},
    eventDrop: function(event, delta, revertFunc) {
        if (!confirm("Are you sure about this change?")) {
            revertFunc();
        }

    },
    eventClick: function(calEvent, jsEvent, view) {
        $(this).css('border-color', 'red');
        // window.location.replace("/foodJournal/meal/"+calEvent.id+"/");
    }
    });
});

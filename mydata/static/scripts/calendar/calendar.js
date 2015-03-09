
$(document).ready(function() {
  $.get("/api/user_daily_mobility_summary/",function(data,status){
    // alert(data[0]['body']['walking_distance_in_km'])
    for (i = 0; i < data.length; i++) {
    date = data[i]['body']['date'].split("-")
     var source = {
        title: "walking_distance_in_km:"+"\n" + data[i]['body']['walking_distance_in_km'].toString() +"\n" +
        "active_time_in_seconds:"+"\n" + data[i]['body']['active_time_in_seconds'].toString(),
        start: new Date(date[0].toString(),date[1].toString()-1,date[2].toString()),
        allDay: true,
        // id: i,
     }
    //  alert(source.start)
     $('#calendar').fullCalendar( 'addEventSource', [source] )
    }
    // alert("Done")

  });

var calendar = $('#calendar').fullCalendar({
    header: {
        left: 'prev,next today',
        center: 'title',
        right: 'month,agendaWeek,agendaDay'
    },
    editable: true,
    weekMode: 'liquid',
    url:'#',
    dayClick: function(date, allDay, jsEvent, view) {
        saveInLocalStorage(date.toString())
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

$.ajax({
    url: 'https://data.gov.gr/api/v1/query/admie_dailyenergybalanceanalysis',
    dataType: 'jsonp',
    headers: {
        "Authorization": "39cfd83f0388cc86536960a2eebc748761d1accc"
    },
    success: function(data) {
      alert('Total results found: ' + data.length)
    }
  });
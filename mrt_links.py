
  
mrt_links = {
   'Changi Airport': set(['Expo']),
  'Expo': set(['Changi Airport', 'Tanah Merah']),
  'Tanah Merah': set(['Expo', 'Bedok']),
  'Bedok': set(['Tanah Merah', 'Kembangan']),
  'Kembangan': set(['Bedok', 'Eunos']),
  'Eunos': set(['Kembangan', 'Paya Lebar']),
  'Paya Lebar': set(['Eunos', 'Aljunied','Dakota', 'MacPherson']),
  'Aljunied': set(['Paya Lebar', 'Kallang']),
  'Kallang': set(['Aljunied', 'Lavender']),
  'Lavender': set(['Kallang', 'Bugis']),
  'Bugis': set(['Lavender', 'City Hall','Rochor', 'Promenade']),
  'City Hall': set(['Bugis', 'Raffles Place', 'Dhoby Ghaut']),
  'Raffles Place': set(['City Hall', 'Tanjong Pagar', 'Marina Bay']),
  'Tanjong Pagar': set(['Raffles Place', 'Outram Park']),
  'Outram Park': set(['Tanjong Pagar', 'Tiong Bahru','HarbourFront', 'Chinatown']),
  'Tiong Bahru': set(['Outram Park', 'Redhill']),
  'Redhill': set(['Tiong Bahru', 'Queenstown']),
  'Queenstown': set(['Redhill', 'Commonwealth']),
  'Commonwealth': set(['Queenstown', 'Buona Vista']),
  'Buona Vista': set(['Commonwealth', 'Dover','Holland VIllage', 'one-north']),
  'Dover': set(['Buona Vista', 'Clementi']),
  'Clementi': set(['Dover', 'Jurong East']),
  'Jurong East': set(['Clementi', 'Chinese Garden', 'Bukit Batok']),
  'Chinese Garden': set(['Jurong East', 'Lakeside']),
  'Lakeside': set(['Chinese Garden', 'Boon Lay']),
  'Boon Lay': set(['Lakeside', 'Pioneer']),
  'Pioneer': set(['Boon Lay', 'Joo Koon']),
  'Joo Koon': set(['Pioneer']),
  'Bukit Batok': set(['Jurong East', 'Bukit Gombak']),
  'Bukit Gombak': set(['Bukit Batok', 'Choa Chu Kang']),
  'Choa Chu Kang': set(['Bukit Gombak', 'Yew Tee']),
  'Yew Tee': set(['Choa Chu Kang', 'Kranji']),
  'Kranji': set(['Yew Tee', 'Marsiling']),
  'Marsiling': set(['Kranji', 'Woodlands']),
  'Woodlands': set(['Marsiling', 'Admiralty']),
  'Admiralty': set(['Woodlands', 'Sembawang']),
  'Sembawang': set(['Admiralty', 'Canberra']),
  'Canberra': set(['Sembawang', 'Yishun']),
  'Yishun': set(['Canberra', 'Khatib']),
  'Khatib': set(['Yishun', 'Yio Chu Kang']),
  'Yio Chu Kang': set(['Khatib', 'Ang Mo Kio']),
  'Ang Mo Kio': set(['Yio Chu Kang', 'Bishan']),
  'Bishan': set(['Ang Mo Kio', 'Braddell', 'Lorong Chuan', "Marymount"]),
  'Braddell': set(['Bishan', 'Toa Payoh']),
  'Toa Payoh': set(['Braddell', 'Novena']),
  'Novena': set(['Toa Payoh', 'Newton']),
  'Newton': set(['Novena', 'Orchard', 'Stevens', 'Little India']),
  'Orchard': set(['Newton', 'Somerset']),
  'Somerset': set(['Orchard', 'Dhoby Ghaut']),
  'Dhoby Ghaut': set(['Somerset', 'City Hall','Clarke Quay', 'Little India', 'Bras Basah']),
  'Marina Bay': set(['Raffles Place']),
  'Botanic Gardens': set(['Stevens','Caldecott', 'Farrer Road']),
  'Stevens': set(['Botanic Gardens', 'Newton']),
  'Little India': set(['Newton', 'Rochor','Dhoby Ghaut', 'Farrer Park']),
  'Rochor': set(['Little India', 'Bugis']),
  'Promenade': set(['Bugis', 'Esplanade', 'Nicoll Highway', 'Bayfront']),
  'Bayfront': set(['Promenade', 'Downtown', 'Marina Bay']),
  'Downtown': set(['Bayfront', 'Telok Ayer']),
  'Telok Ayer': set(['Downtown', 'Chinatown']),
  'Chinatown': set(['Telok Ayer', 'Fort Canning','Outram Park', 'Clarke Quay']),
  'Fort Canning': set(['Chinatown', 'Bencoolen']),
  'Bencoolen': set(['Fort Canning', 'Jalan Besar']),
  'Jalan Besar': set(['Bencoolen', 'Bendemeer']),
  'Bendemeer': set(['Jalan Besar', 'Geylang Bahru']),
  'Geylang Bahru': set(['Bendemeer', 'Mattar']),
  'Mattar': set(['Geylang Bahru', 'MacPherson']),
  'MacPherson': set(['Mattar', 'Paya Lebar', 'Tai Seng']),
  'Bras Basah': set(['Dhoby Ghaut', 'Esplanade']),
  'Esplanade': set(['Bras Basah', 'Promenade']),
  'Nicoll Highway': set(['Promenade', 'Stadium']),
  'Stadium': set(['Nicoll Highway', 'Mountbatten']),
  'Mountbatten': set(['Stadium', 'Dakota']),
  'Dakota': set(['Mountbatten', 'Paya Lebar']),
  'Tai Seng': set(['MacPherson', 'Bartley']),
  'Bartley': set(['Tai Seng', 'Serangoon']),
  'Serangoon': set(['Bartley', 'Lorong Chuan', 'Woodleigh']),
  'Lorong Chuan': set(['Serangoon', 'Bishan']),
  'Marymount': set(['Bishan', 'Caldecott']),
  'Caldecott': set(['Marymount', 'Botanic Gardens']),
  'Farrer Road': set(['Botanic Gardens', 'Holland VIllage']),
  'Holland VIllage': set(['Farrer Road', 'Buona Vista']),
  'one-north': set(['Buona Vista', 'Kent Ridge']),
  'Kent Ridge': set(['one-north', 'Haw Par Villa']),
  'Haw Par Villa': set(['Kent Ridge', 'Pasir Panjang']),
  'Pasir Panjang': set(['Haw Par Villa', 'Labrador Park']),
  'Labrador Park': set(['Pasir Panjang', 'Telok Blangah']),
  'Telok Blangah': set(['Labrador Park', 'HarbourFront']),
  'HarbourFront': set(['Telok Blangah', 'Outram Park']),
  'Clarke Quay': set(['Chinatown', 'Dhoby Ghaut']),
  'Farrer Park': set(['Little India', 'Boon Keng']),
  'Boon Keng': set(['Farrer Park', 'Potong Pasir']),
  'Potong Pasir': set(['Boon Keng', 'Woodleigh']),
  'Woodleigh': set(['Potong Pasir', 'Serangoon'])

}



  
# Metro stations
stations = [
    "Akademmistechko", "Zhytomyrska", "Sviatoshyn", "Nyvky", "Beresteiska", "Shuliavska", "Politekhnichnyi Instytut",
    "Vokzalna", "Universytet", "Teatralna", "Khreshchatyk", "Arsenalna", "Dnipro", "Hidropark", "Livoberezhna", "Darnytsia",
    "Chernihivska", "Lisova", "Heroiv Dnipra", "Minska", "Obolon", "Pochaina", "Tarasa Shevchenka", "Kontraktova Ploshcha",
    "Poshtova Ploshcha", "Maidan Nezalezhnosti", "Ploshcha Ukrayinskykh heroyiv", "Olimpiiska", "Palats Ukraina", "Lybidska", 
    "Demiivska", "Holosiivska", "Vasylkivska", "Vystavkovyi Tsentr", "Ipodrom", "Teremky", "Syrets", "Dorohozhychi", "Lukianivska",
    "Zoloti Vorota", "Palats Sportu", "Klovska", "Pecherska", "Zvirinetska", "Vydubychi", "Slavutych", "Osokorky", 
    "Pozniaky", "Kharkivska", "Vyrlytsia", "Boryspilska", "Chervony Khutir"
]

# Edges with lines and weights
edges_with_lines = [
    ("Akademmistechko", "Zhytomyrska", 4, "red"), ("Zhytomyrska", "Sviatoshyn", 3, "red"), ("Sviatoshyn", "Nyvky", 2, "red"), 
    ("Nyvky", "Beresteiska", 3, "red"), ("Beresteiska", "Shuliavska", 2, "red"), ("Shuliavska", "Politekhnichnyi Instytut", 2, "red"), 
    ("Politekhnichnyi Instytut", "Vokzalna", 2, "red"), ("Vokzalna", "Universytet", 1, "red"), ("Universytet", "Teatralna", 1, "red"), 
    ("Teatralna", "Khreshchatyk", 1, "red"), ("Khreshchatyk", "Arsenalna", 1, "red"), ("Arsenalna", "Dnipro", 1, "red"), 
    ("Dnipro", "Hidropark", 2, "red"), ("Hidropark", "Livoberezhna", 2, "red"), ("Livoberezhna", "Darnytsia", 2, "red"), 
    ("Darnytsia", "Chernihivska", 2, "red"), ("Chernihivska", "Lisova", 3, "red"), 

    ("Heroiv Dnipra", "Minska", 4, "blue"), ("Minska", "Obolon", 2, "blue"), ("Obolon", "Pochaina", 3, "blue"), 
    ("Pochaina", "Tarasa Shevchenka", 3, "blue"), ("Tarasa Shevchenka", "Kontraktova Ploshcha", 2, "blue"), 
    ("Kontraktova Ploshcha", "Poshtova Ploshcha", 1, "blue"), ("Poshtova Ploshcha", "Maidan Nezalezhnosti", 1, "blue"), 
    ("Maidan Nezalezhnosti", "Ploshcha Ukrayinskykh heroyiv", 1, "blue"), ("Ploshcha Ukrayinskykh heroyiv", "Olimpiiska", 1, "blue"), 
    ("Olimpiiska", "Palats Ukraina", 1, "blue"), ("Palats Ukraina", "Lybidska", 1, "blue"), ("Lybidska", "Demiivska", 2, "blue"), 
    ("Demiivska", "Holosiivska", 2, "blue"), ("Holosiivska", "Vasylkivska", 2, "blue"), ("Vasylkivska", "Vystavkovyi Tsentr", 3, "blue"), 
    ("Vystavkovyi Tsentr", "Ipodrom", 3, "blue"), ("Ipodrom", "Teremky", 2, "blue"), 

    ("Syrets", "Dorohozhychi", 3, "green"), ("Dorohozhychi", "Lukianivska", 2, "green"), ("Lukianivska", "Zoloti Vorota", 2, "green"), 
    ("Zoloti Vorota", "Palats Sportu", 1, "green"), ("Palats Sportu", "Klovska", 1, "green"), ("Klovska", "Pecherska", 2, "green"), 
    ("Pecherska", "Zvirinetska", 2, "green"), ("Zvirinetska", "Vydubychi", 2, "green"), ("Vydubychi", "Slavutych", 2, "green"), 
    ("Slavutych", "Osokorky", 3, "green"), ("Osokorky", "Pozniaky", 2, "green"), ("Pozniaky", "Kharkivska", 2, "green"), 
    ("Kharkivska", "Vyrlytsia", 2, "green"), ("Vyrlytsia", "Boryspilska", 4, "green"), ("Boryspilska", "Chervony Khutir", 2, "green"), 
    ("Zoloti Vorota", "Teatralna", 1, "green"), ("Khreshchatyk", "Maidan Nezalezhnosti", 1, "red"), 
    ("Ploshcha Ukrayinskykh heroyiv", "Palats Sportu", 1, "blue")
]

# Positions for each station
positions = {
    # Red line (x-axis)
    "Akademmistechko": (-46, 28), "Zhytomyrska": (-42, 24), "Sviatoshyn": (-38, 20), 
    "Nyvky": (-34, 16), "Beresteiska": (-32, 12), "Shuliavska": (-28, 8), 
    "Politekhnichnyi Instytut": (-24, 4), "Vokzalna":(-20, 0), "Universytet": (-14, 0), 
    "Teatralna": (-8, 2), "Khreshchatyk": (4, 2), "Arsenalna": (12, -4), 
    "Dnipro": (16, -8), "Hidropark":(24, -14), "Livoberezhna": (28, -10), 
    "Darnytsia": (32, -6), "Chernihivska": (36, -4), "Lisova": (40, -2), 

    # Blue line (y-axis)
    "Heroiv Dnipra": (2, 32), "Minska": (2, 28), "Obolon": (2, 24), 
    "Pochaina": (2, 20), "Tarasa Shevchenka": (2, 16), "Kontraktova Ploshcha": (2, 12), 
    "Poshtova Ploshcha": (2, 8), "Maidan Nezalezhnosti": (4, 0), 
    "Ploshcha Ukrayinskykh heroyiv": (-4, -12), "Olimpiiska": (-14,-18), 
    "Palats Ukraina": (-14, -22), "Lybidska": (-14, -26), "Demiivska": (-18, -30), 
    "Holosiivska": (-22, -26), "Vasylkivska": (-26, -22), "Vystavkovyi Tsentr": (-30, -18), 
    "Ipodrom": (-34, -14), "Teremky": (-38, -10),

    # Green line (diagonal)
    "Syrets": (-24, 16), "Dorohozhychi": (-20, 10), "Lukianivska": (-14, 6), 
    "Zoloti Vorota": (-8, -0.5), "Palats Sportu": (-4, -14), "Klovska": (4, -18), 
    "Pecherska": (4, -22), "Zvirinetska": (8, -24), "Vydubychi": (12, -28), 
    "Slavutych": (18, -32), "Osokorky": (24, -36), "Pozniaky": (30, -32), 
    "Kharkivska": (34, -28), "Vyrlytsia": (38, -24), "Boryspilska": (42, -20), 
    "Chervony Khutir": (46, -16)
}

# Projekts_CO2

## Programmas nosaukums
CO2 Monitoringa Sistēma - tīmekļa lietotne gaisa kvalitātes kontrolei Daugavpils Tehnoloģiju vidusskolā - licejā.

## Uzstādīšana
1. Instalē Python (3.8 vai jaunāku versiju) no python.org
2. Instalē Flask bibliotēku, atverot komandu rindu (CMD) un ierakstot: pip install flask
3. Lejupielādē visus projekta failus vienā mapē (app.py, CO2.csv, un templates mapi ar index.html, chart.html, data.html)
4. Atver komandu rindu mapē ar failiem un ieraksti: python app.py
5. Atver pārlūkprogrammu un ievadi adresi: http://127.0.0.1:5000

## Kā izmantot programmu
Dati atrodas failā CO2.csv ar kolonnām: id, CO2 vērtība (ppm), diena, kabinets, lokācija, temperatūra, mitrums. Piemērs: 1,587,1,10.kab,Daugavpils Tehnoloģiju vidusskola - licejs,17.6,46. Sākuma lapā izvēlies "Grafiks" vai "Dati". Grafika lapā izvēlies kabinetu un nospied "Atjaunināt grafiku". Datu lapā nospied "Parādīt visus datus" vai izmanto filtrus pēc kabineta/dienas.

## Sagaidāmā izvade
Programma parāda CO2 līmeni ppm. Krāsu kodējums: zaļš (420-1000 ppm - labs), dzeltens (1000-2000 ppm - pasliktinās), oranžs (2000-3000 ppm - būtiski pasliktinājusies), sarkans (3000-4000 ppm - bīstams), tumši sarkans (4000-5000 ppm - ļoti bīstams), melns (>5000 ppm - kritisks). Datu lapā redzama tabula ar visiem mērījumiem un statistikas kartes. Grafikā redzams līniju grafiks pa dienām.

## Galvenie faili
app.py - galvenais Flask fails ar API un datu apstrādi. CO2.csv - datu fails ar visiem mērījumiem (125 ieraksti, 25 telpas, 5 dienas). templates/index.html - izvēlnes lapa. templates/chart.html - grafika lapa ar Chart.js. templates/data.html - datu un statistikas lapa.

## Piemēri
Pievienojot jaunu rindu CO2.csv: "126,4500,6,101.kab,Daugavpils Tehnoloģiju vidusskola - licejs,23.5,45", programma rādīs šo mērījumu ar tumši sarkanu krāsu (ļoti bīstams). Izvēloties kabinetu "101.kab" grafikā, var redzēt tā CO2 līmeni pa visām dienām. Izmantojot filtrus datu lapā, var atlasīt tikai "115.kab" datus par dienu 3.

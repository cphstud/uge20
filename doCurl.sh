myfile=$1
#point_Type=0&pool=2&lob=3&gender=2&date_from=01%2F01%2F2019&date_to=&group=1&age_from=&age_to=&club=
#curl -d "@${myfile}" -H  "Content-Type: application/json" -X POST https://xn--svmmetider-1cb.dk/ranglister/
curl -d "@datax" -H  "Content-Type:application/x-www-form-urlencoded" -X POST https://xn--svmmetider-1cb.dk/ranglister/

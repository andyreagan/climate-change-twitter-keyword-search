for YEAR in 200{8..9} 20{10..14}
do
  echo "catting days in ${YEAR}"
  for MONTH in 0{1..9} {10..12}
  do
    echo "catting days in ${MONTH}"
    for DAY in 0{1..9} {10..31}
    do
      cat rawtweets/${YEAR}-${MONTH}-${DAY}-* > daytweets/${YEAR}-${MONTH}-${DAY}.txt
    done
  done
done
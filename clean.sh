cat currdate.txt
# echo "grepping"
# grep -l "delete me" emilyKeywordScrape.o* | xargs rm
echo "catting..."
for YEAR in 200{8..9} 20{10..14}
do
  echo "catting ${YEAR}"
  cat rawtweets/${YEAR}-* > ${YEAR}.txt
done
# too many files for this:
# cat rawtweets/* > alltweets 
echo "counting"
wc 20*

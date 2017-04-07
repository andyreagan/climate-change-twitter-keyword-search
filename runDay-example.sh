DATE=2014-04-14
for HOUR in 0{0..9} {10..23}
do
  echo "${DATE}-${HOUR}"
  qsub -qshortq -V runHour.qsub
done
